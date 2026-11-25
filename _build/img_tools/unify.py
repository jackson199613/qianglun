# -*- coding: utf-8 -*-
"""产品图统一视觉：抠图 → 亮度校正（压高光、提暗部）→ 统一底色/比例/投影 → 1200x900 webp
甲方 3.0 第 3/5/10 条：同页产品图视觉统一，暗图调亮但不过曝。
"""
import sys, os, json
import numpy as np
from PIL import Image, ImageFilter, ImageDraw, ImageChops

ROOT = '/home/claude/qianglun'
CUT = '/home/claude/cut'
W, H = 1200, 900
BG_TOP, BG_BOT = (250, 250, 249), (240, 240, 238)
_sess = None


def session():
    global _sess
    if _sess is None:
        from rembg import new_session
        _sess = new_session('isnet-general-use')
    return _sess


def rembg_cut(im, key):
    p = f'{CUT}/{key}.png'
    if os.path.exists(p):
        return Image.open(p).convert('RGBA')
    from rembg import remove
    o = remove(im, session=session()).convert('RGBA')
    o.save(p)
    return o


def clean_alpha(o, thr=40):
    a = np.array(o.split()[-1]).astype(np.float32)
    a[a < thr] = 0
    a = np.clip((a - thr) * 255.0 / (255 - thr), 0, 255)
    o.putalpha(Image.fromarray(a.astype(np.uint8)))
    return o


def poly_cut(im, pts, feather=2):
    m = Image.new('L', im.size, 0)
    ImageDraw.Draw(m).polygon(pts, fill=255)
    if feather:
        m = m.filter(ImageFilter.GaussianBlur(feather))
    o = im.convert('RGBA'); o.putalpha(m)
    return o


def thresh_cut(im, box, smin=0, smax=0.22, vmin=0.42):
    im = im.crop(box)
    hsv = np.array(im.convert('HSV')).astype(np.float32) / 255
    m = ((hsv[..., 1] <= smax) & (hsv[..., 2] >= vmin)).astype(np.uint8) * 255
    mi = Image.fromarray(m).filter(ImageFilter.MedianFilter(7)).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.MaxFilter(3))
    mi = mi.filter(ImageFilter.GaussianBlur(1.2))
    o = im.convert('RGBA'); o.putalpha(mi)
    return o


def white_cut(im, thr=14):
    a = np.array(im).astype(np.float32)
    d = 255 - a.min(axis=2)
    m = np.clip((d - thr) * 8, 0, 255).astype(np.uint8)
    mi = Image.fromarray(m).filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.MinFilter(5)).filter(ImageFilter.GaussianBlur(.8))
    o = im.convert('RGBA'); o.putalpha(mi)
    return o


def tubes_cut(im, box, r=10):
    """排列的圆管：先阈值找每根管的上下沿与左右端，再画规整圆角矩形做蒙版"""
    im = im.crop(box)
    hsv = np.array(im.convert('HSV')).astype(np.float32) / 255
    m = (hsv[..., 1] <= .22) & (hsv[..., 2] >= .42)
    rows = m.mean(axis=1)
    band = rows > .55
    mask = Image.new('L', im.size, 0); d = ImageDraw.Draw(mask)
    y = 0; n = len(band)
    while y < n:
        if band[y]:
            y0 = y
            while y < n and band[y]: y += 1
            y1 = y
            if y1 - y0 > 25:
                cols = m[y0:y1].mean(axis=0) > .5
                xs = np.where(cols)[0]
                d.rounded_rectangle((xs.min() + 2, y0 + 1, xs.max() - 2, y1 - 2), r, fill=255)
        y += 1
    mask = mask.filter(ImageFilter.GaussianBlur(1.2))
    o = im.convert('RGBA'); o.putalpha(mask)
    return o


def swatch(im, box, radius=28):
    im = im.crop(box).convert('RGBA')
    m = Image.new('L', im.size, 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, im.width - 1, im.height - 1), radius, fill=255)
    im.putalpha(m)
    return im


def tone(o, lo_target=None, p_hi=238, med_lo=105, med_hi=170, gain=1.0):
    """只看产品像素：高光 98 分位压到 p_hi 以下；中位亮度拉进 [med_lo, med_hi]"""
    rgb = np.array(o.convert('RGB')).astype(np.float32)
    a = np.array(o.split()[-1])
    sel = a > 128
    if sel.sum() < 100:
        return o
    lum = (0.299 * rgb[..., 0] + 0.587 * rgb[..., 1] + 0.114 * rgb[..., 2])[sel]
    med = float(np.median(lum)); hi = float(np.percentile(lum, 98.5))
    x = rgb / 255.0
    # 中位亮度 → gamma
    tgt = min(max(med, med_lo), med_hi)
    if abs(tgt - med) > 2:
        g = np.log(tgt / 255) / np.log(max(med, 1) / 255)
        x = np.power(np.clip(x, 1e-4, 1), g)
    # 压高光：软肩
    y = x * 255
    knee = p_hi - 18
    over = y > knee
    y[over] = knee + (p_hi - knee) * (1 - np.exp(-(y[over] - knee) / (p_hi - knee)))
    y = y * gain
    out = Image.fromarray(np.clip(y, 0, 255).astype(np.uint8)).convert('RGBA')
    out.putalpha(o.split()[-1])
    return out


def sharpen(o):
    rgb = o.convert('RGB').filter(ImageFilter.UnsharpMask(radius=1.4, percent=55, threshold=2))
    rgb = rgb.convert('RGBA'); rgb.putalpha(o.split()[-1])
    return rgb


def background():
    g = np.linspace(0, 1, H)[:, None, None]
    top = np.array(BG_TOP, np.float32); bot = np.array(BG_BOT, np.float32)
    arr = (top * (1 - g) + bot * g) * np.ones((1, W, 1))
    # 中心微亮
    yy, xx = np.mgrid[0:H, 0:W]
    r = np.sqrt(((xx - W / 2) / (W * .6)) ** 2 + ((yy - H * .45) / (H * .6)) ** 2)
    arr += (np.clip(1 - r, 0, 1) ** 2 * 5)[..., None]
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)).convert('RGBA')


def compose(o, fit=(860, 600), cy=0.47, shadow=True, maxscale=3.0):
    o = o.crop(o.getbbox())
    s = min(fit[0] / o.width, fit[1] / o.height, maxscale)
    o = o.resize((max(1, round(o.width * s)), max(1, round(o.height * s))), Image.LANCZOS)
    bg = background()
    x = (W - o.width) // 2; y = int(H * cy - o.height / 2)
    if shadow:
        a = o.split()[-1]
        # 接触阴影：底部椭圆
        sh = Image.new('L', (W, H), 0); d = ImageDraw.Draw(sh)
        cx = W // 2; by = y + o.height
        d.ellipse((cx - o.width * .46, by - 16, cx + o.width * .46, by + 22), fill=70)
        sh = sh.filter(ImageFilter.GaussianBlur(22))
        # 投影：轮廓下移模糊
        sh2 = Image.new('L', (W, H), 0); sh2.paste(a.point(lambda v: v * 0.22), (x + 6, y + 14))
        sh2 = sh2.filter(ImageFilter.GaussianBlur(16))
        shadow_l = ImageChops.lighter(sh, sh2)
        dark = Image.new('RGBA', (W, H), (60, 60, 58, 255)); dark.putalpha(shadow_l)
        bg = Image.alpha_composite(bg, dark)
    bg.alpha_composite(o, (x, y))
    return bg.convert('RGB')


def run(cfg_path):
    cfg = json.load(open(cfg_path))
    for item in cfg:
        src = os.path.join(ROOT, item['src']); out = os.path.join(ROOT, item['out'])
        im = Image.open(src).convert('RGB')
        if item.get('pre_crop'):
            im = im.crop(tuple(item['pre_crop']))
        m = item.get('mode', 'rembg')
        if m == 'rembg':
            o = clean_alpha(rembg_cut(im, item.get('key', os.path.splitext(os.path.basename(src))[0])), item.get('athr', 40))
        elif m == 'poly':
            o = poly_cut(im, [tuple(p) for p in item['pts']])
        elif m == 'thresh':
            o = thresh_cut(im, tuple(item['box']), smax=item.get('smax', .22), vmin=item.get('vmin', .42))
        elif m == 'white':
            o = white_cut(im, item.get('thr', 14))
        elif m == 'tubes':
            o = tubes_cut(im, tuple(item['box']))
        elif m == 'swatch':
            o = swatch(im, tuple(item['box']))
        if item.get('desat'):
            rgb = o.convert('RGB'); g = rgb.convert('L').convert('RGB')
            rgb = Image.blend(rgb, g, item['desat']).convert('RGBA'); rgb.putalpha(o.split()[-1]); o = rgb
        o = tone(o, p_hi=item.get('p_hi', 236), med_lo=item.get('med_lo', 100), med_hi=item.get('med_hi', 168), gain=item.get('gain', 1.0))
        o = sharpen(o)
        fit = tuple(item.get('fit', (860, 600)))
        img = compose(o, fit=fit, cy=item.get('cy', .47))
        img.save(out, 'WEBP', quality=86, method=6)
        print('✓', item['out'], '←', item['src'])


if __name__ == '__main__':
    run(sys.argv[1])
