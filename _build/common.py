# -*- coding: utf-8 -*-
"""各栏目构建脚本共用的小工具"""
import os, re
OUT = os.path.join(os.path.dirname(__file__), '..')

# 2026.11.23 客户反馈：重复 / 不要的页面不再生成（netlify.toml 里做 301 跳转）
REMOVED = {"platforms.html", "specs.html", "downloads.html", "encyclopedia.html", "qa.html", "p-detail.html"}


# 图片在 netlify.toml 里是长缓存。内容换了但文件名没变的图（精修产品图、首屏横幅）必须带版本号，
# 否则看过旧图的访客（包括甲方）浏览器里还是旧图。以后再替换这些图，把 IMG_VER 改掉重新生成即可。
IMG_VER = "20261127"
_VER_RE = re.compile(r'(img/(?:pc-|hero-jl-|sleeve-06)[A-Za-z0-9_-]*\.webp)(?!\?)')


def w(name, html):
    if name in REMOVED:
        return
    html = _VER_RE.sub(lambda m: m.group(1) + '?v=' + IMG_VER, html)
    open(os.path.join(OUT, name), 'w', encoding='utf-8').write(html)
    print('  ✓', name)

_ABOUT_NAV = """<nav class="pillbar" style="margin-top:0">
<a class="pb {a0}" href="about.html">企业简介</a><a class="pb {a1}" href="history.html">发展历程</a><a class="pb {a2}" href="manufacturing.html">制造能力</a><a class="pb {a3}" href="quality.html">质量体系</a><a class="pb {a4}" href="honors.html">资质荣誉</a><a class="pb {a5}" href="culture.html">企业文化与社会责任</a><a class="pb {a6}" href="investor.html">投资者关系</a></nav>"""
def anav(i):
    return _ABOUT_NAV.format(**{f'a{k}': ('on' if k == i else '') for k in range(7)})

_RD_NAV = """<nav class="pillbar" style="margin-top:0">
<a class="pb {a0}" href="rd.html">科研总览</a><a class="pb {a2}" href="lab.html">研发中心与实验室</a><a class="pb {a3}" href="testing.html">检测能力</a><a class="pb {a4}" href="patents.html">专利与标准</a><a class="pb {a5}" href="coop.html">产学研合作</a><a class="pb {a6}" href="achievements.html">科研成果</a></nav>"""
def rnav(i):
    return _RD_NAV.format(**{f'a{k}': ('on' if k == i else '') for k in range(7)})

_TS_NAV = """<nav class="pillbar" style="margin-top:0">
<a class="pb {a0}" href="selector.html">选型指南</a><a class="pb {a1}" href="insights.html">技术文章</a><a class="pb {a2}" href="faq.html">常见问题</a><a class="pb {a3}" href="glossary.html">名词解释</a></nav>"""
def _ts(i):
    return _TS_NAV.format(**{f'a{k}': ('on' if k == i else '') for k in range(4)})
def snav(i):
    return _ts({0: 0, 1: -1, 2: 3, 3: -1}.get(i, -1))
def inav(i):
    return _ts({0: 1, 1: 2, 2: 3}.get(i, -1))

ENDCTA = """<section class="endcta"><div class="wrap">
  <div><h2>把<em>应用场景</em>告诉我们，<br>让工程师为您推荐合适的产品</h2>
  <p>说明您的行业、使用场景与需求，强纶工程师会给出产品建议、样品与报价。</p></div>
  <div class="acts"><a class="pill pill-gold" href="contact.html#inq">在线询价<svg class="i"><use href="#i-arrow"/></svg></a><a class="pill pill-line" href="sample.html">申请样品</a></div>
</div></section>"""


def vr_block(poster, title, lead, idx="VR"):
    """2026.11.23 客户要求去掉 VR 板块"""
    return ""


def video_block(poster, title, cap):
    """视频播放模块：后台上传并转码后，把 data-src 换成播放地址即可。"""
    return f'''<figure class="vidbox rv">
  <video controls playsinline preload="none" poster="{poster}" data-src="" aria-label="{title}"></video>
  <span class="vidtip">视频待甲方提供，上传后自动转码多档清晰度，按网络自适应播放</span>
  <figcaption>{cap}</figcaption>
</figure>
'''


FILM_SRC = "video/qlfiber-film-2026-1080p.mp4"
FILM_POSTER = "img/film-poster-2026.webp"

def film_block(h2='三分四十三秒，看完<em>强纶</em>',
               lead='从一根金属纤维出发，到烧结毡、织物、过滤元器件与成套净化装备——这条路公司走了二十余年。',
               prefix=''):
    return f'''<section class="film" id="film"><div class="wrap">
  <div class="idx rv"><b>FILM</b>企业宣传片</div>
  <h2 class="rv">{h2}</h2>
  <p class="flead rv">{lead}</p>
  <figure class="player rv" data-player>
    <video playsinline controls preload="none" poster="{prefix}{FILM_POSTER}" aria-label="福建强纶新材料企业宣传片">
      <source src="{prefix}{FILM_SRC}" type="video/mp4">
      您的浏览器不支持视频播放，请<a href="{prefix}{FILM_SRC}">下载观看</a>。
    </video>
    <button type="button" class="cover" aria-label="播放企业宣传片">
      <img src="{prefix}{FILM_POSTER}" alt="强纶新材企业宣传片封面" loading="lazy">
      <span class="pbtn"><svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg></span>
      <span class="fmeta">
        <b>03:43</b>
        <span class="fchips"><i>中英双语字幕</i><i>1080P</i><i>福建强纶新材料股份有限公司</i></span>
      </span>
    </button>
  </figure>
</div></section>
'''


def faq_block(items):
    qs = "".join(f"""<div class="qa"><button type="button" aria-expanded="false"><span class="n num">{i+1:02d}</span><span>{q}</span><span class="pm"><svg class="i"><use href="#i-x"/></svg></span></button><div class="ans"><div><p>{a}</p></div></div></div>""" for i, (q, a) in enumerate(items))
    sc = '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[%s]}' % ",".join(
        '{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}' % (q.replace('"', "'"), a.replace('"', "'")) for q, a in items)
    return f'<div class="qa-list">{qs}</div><script type="application/ld+json">{sc}</script>'
