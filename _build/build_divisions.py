# -*- coding: utf-8 -*-
"""产品中心：总览（五大事业部产品树）+ 5 个事业部页（2026.11.23 客户反馈改版）

每个事业部页按客户给的核心逻辑：
  我的产品是什么？ → 我的特点是哪些？ → 我的应用场景是什么？
不放规格参数表与细数据；不放交付 / 发运实拍。
"""
import json
from common import w, ENDCTA
from layout import head, header, footer, crumb, page_hero, SITE
from divisions import DIVS
from contacts import BY_KEY, dept_block

ARW = '<svg class="i"><use href="#i-arrow"/></svg>'


def divbar(cur):
    return '<nav class="pillbar dvbar" aria-label="产品类别">' + "".join(
        f'<a class="pb {"on" if d["file"] == cur else ""}" href="{d["file"]}">{d["cat"]}</a>' for d in DIVS) + "</nav>"


def faq_html(items):
    return '<div class="qa-list">' + "".join(
        f'<div class="qa"><button type="button" aria-expanded="false"><span class="n num">{i+1:02d}</span><span>{q}</span>'
        f'<span class="pm"><svg class="i"><use href="#i-x"/></svg></span></button><div class="ans"><div><p>{a}</p></div></div></div>'
        for i, (q, a) in enumerate(items)) + "</div>"


def product_cards(d):
    out = ""
    n = len(d["products"])
    for k, p in enumerate(d["products"]):
        fit = ""
        # 3.0 第 6 条：竖卡三列；余 2 时末两张各占半行，余 1 时末张整行横排，不留空位
        if n % 3 == 2 and k >= n - 2:
            fit = " half"
        elif n % 3 == 1 and k == n - 1:
            fit = " full"
        feats = "".join(f"<li>{x}</li>" for x in p["feats"])
        scenes = "".join(f"<span>{x}</span>" for x in p["scenes"])
        out += f'''<article class="dvp rv{fit}" id="{p['id']}">
  <div class="im"><img loading="lazy" src="{p['img']}" alt="{p['name']}"></div>
  <div class="bd">
    <h3>{p['name']}</h3>
    <div class="row"><b>是什么</b><p>{p['what']}</p></div>
    {f'<div class="row"><b>特点</b><ul>{feats}</ul></div>' if feats else ''}
    {f'<div class="row"><b>应用场景</b><div class="tags">{scenes}</div></div>' if scenes else ''}
    <a class="tlink" href="#dvcontact">咨询 · {p['name']}{ARW}</a>
  </div>
</article>'''
    return out


FTS_EXTRA = '''<section class="sec alt"><div class="wrap">
  <div class="sh rv"><h2>系统组成与<em>工作原理</em></h2>
  <p>前置过滤器先去除液体中的杂质，保证后续分离装置不被堵塞；油水分离器内的改性金属纤维捕捉油珠，油珠在纤维表面不断聚结长大后快速上浮，进入上部储油腔定期排出。</p></div>
  <div class="dvdiag rv">
    <figure><img loading="lazy" src="img/fts-principle.webp" alt="油水分离工作原理示意"><figcaption>工作原理示意</figcaption></figure>
    <figure><img loading="lazy" src="img/fts-layout.webp" alt="收油系统组成"><figcaption>系统组成</figcaption></figure>
  </div>
</div></section>
<section class="sec"><div class="wrap">
  <div class="sh rv"><h2>部分<em>合作客户</em></h2><p>已为新能源与有色冶炼行业 20 余家企业提供收油系统及过滤服务。</p></div>
  <div class="clients rv">''' + "".join(f"<span>{c}</span>" for c in [
    "广东芳源环保", "福建常青新能源", "衢州华友钴新材料", "衢州华友资源再生", "烟台凯实工业", "江苏天能新材料",
    "江西铜业集团", "福建紫金铜业", "广西巴莫科技", "广西华友新材料", "汉中锌业", "中国恩菲工程技术",
    "格林美", "青海超频三新材料", "湖北睿派新能源", "郑州天一萃取", "河南荣佳钪钒", "湖南邦普循环",
    "江苏凯实金桥新材料", "攀枝花山青钒业", "金昌神泥科技", "江西佳纳能源"]) + '''</div>
</div></section>
'''


def cases_html(d):
    if not d.get("cases"):
        return ""
    cs = "".join(f'''<article class="case2 rv"><span class="tag">客户案例</span><h3>{t}</h3><dl><dt>需求</dt><dd>{a}</dd><dt>方案</dt><dd>{b}</dd><dt>效果</dt><dd>{c}</dd></dl></article>'''
                 for t, a, b, c in d["cases"])
    return f'''<section class="sec"><div class="wrap"><div class="sh rv"><h2>客户<em>合作案例</em></h2></div><div class="cases2 c2">{cs}</div></div></section>'''


def division_page(d):
    feats = "".join(f'<div class="dvf rv"><i class="num">{i+1:02d}</i><h4>{t}</h4><p>{x}</p></div>' for i, (t, x) in enumerate(d["feats"]))
    scenes = "".join(f"<span>{x}</span>" for x in d["scenes"])
    gal = "".join(f'<figure><img loading="lazy" src="{s}" alt="{c}"><figcaption>{c}</figcaption></figure>' for s, c in d["gallery"])
    toc = "".join(f'<a href="#{p["id"]}">{p["name"]}</a>' for p in d["products"])
    fit = " contain" if d.get("cover_fit") == "contain" else ""
    schema = json.dumps({"@context": "https://schema.org", "@type": "ItemList", "name": f"强纶新材 · {d['name']}",
                         "itemListElement": [{"@type": "ListItem", "position": i + 1,
                                              "item": {"@type": "Product", "name": p["name"], "description": p["what"],
                                                       "image": f"{SITE}/{p['img']}", "brand": {"@type": "Brand", "name": "强纶新材"},
                                                       "manufacturer": {"@type": "Organization", "name": "福建强纶新材料股份有限公司"}}}
                                             for i, p in enumerate(d["products"])]}, ensure_ascii=False)
    faq_schema = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in d["faq"]]}, ensure_ascii=False)
    html = head(
        f"{d['cat']} | {'、'.join(p['name'] for p in d['products'][:4])} — 强纶新材",
        f"强纶新材{d['cat']}（{d['name']}）：{d['what']}主要产品：{'、'.join(p['name'] for p in d['products'])}。",
        ",".join([d["name"]] + [p["name"] for p in d["products"]] + ["强纶新材"]),
        d["file"], extra_css='<link rel="stylesheet" href="home.css">', schema=schema + '</script><script type="application/ld+json">' + faq_schema, og_img=d["cover"]
    ) + header(d["file"]) + crumb([("产品中心", "products.html"), (d["name"], None)]) + f'''
<main>
<section class="ph dvhero dvh-c"><div class="wrap">
  <div class="dvh-t">
    <div class="idx">{d['name']} · 产品中心</div>
    <h1>{d['cat']}</h1>
    <p class="ph-lead">{d['what']}</p>
  </div>
  <div class="dvh-a"><a class="pill pill-gold" href="#dvcontact">联系{d['name']}{ARW}</a><a class="pill pill-line" href="sample.html">申请样品</a></div>
</div></section>

<section class="sec dvp-sec"><div class="wrap">
  {divbar(d['file'])}
  <div class="dvps">{product_cards(d)}</div>
</div></section>

<section class="sec alt"><div class="wrap">
  <div class="sh rv"><h2>产品<em>特点</em></h2></div>
  <div class="dvfs">{feats}</div>
</div></section>

<section class="sec wash2"><div class="wrap">
  <div class="sh rv"><h2>{d.get('scenes_title','应用场景')[:2]}<em>{d.get('scenes_title','应用场景')[2:]}</em></h2><p>不确定是否适用？把您的应用场景告诉我们，工程师会给出建议。</p></div>
  <div class="dvscenes rv">{scenes}</div>
</div></section>

{FTS_EXTRA if d.get('extra') == 'fts' else ''}
{cases_html(d)}

{f'''<section class="sec alt"><div class="wrap">
  <div class="sh rv"><h2>产品与<em>现场实拍</em></h2></div>
  <div class="gal rv">{gal}</div>
</div></section>''' if gal else ''}

<section class="sec"><div class="wrap">
  <div class="sh rv"><h2>常见<em>问题</em></h2></div>
  {faq_html(d['faq'])}
</div></section>

<section class="sec alt" id="dvcontact"><div class="wrap">
  <div class="sh rv"><h2>联系<em>{d['name']}</em></h2><p>直接联系负责该类产品的同事，获取选型建议、样品与报价。</p></div>
  <div class="cdepts one rv">{dept_block(BY_KEY[d['key']])}{dept_block(BY_KEY['sales'], '销售管理部（综合咨询）')}</div>
</div></section>
{ENDCTA}
</main>
''' + footer()
    w(d["file"], html)


def products_page():
    branches = ""
    for d in DIVS:
        fit = " contain" if d.get("cover_fit") == "contain" else ""
        lis = "".join(f'<li><a href="{d["file"]}#{p["id"]}">{p["name"]}</a></li>' for p in d["products"])
        branches += f'''<div class="br rv"><div class="bcard">
<a class="im{fit}" href="{d['file']}"><img loading="lazy" src="{d['cover']}" alt="{d['name']}"></a>
<div class="bd"><span class="no">{d['name']}</span><h3><a href="{d['file']}">{d['cat']}</a></h3><p class="what">{d['what']}</p>
<ul>{lis}</ul><a class="go" href="{d['file']}">查看全部产品{ARW}</a></div></div></div>'''
    rows = ""
    for d in DIVS:
        rows += f'''<a class="dvrow rv" href="{d['file']}"><span class="num">{d['no']}</span><b>{d['cat']}</b><em>{d['tag']}</em><i>{'、'.join(d['scenes'][:4])}</i>{ARW}</a>'''
    html = head(
        "产品中心 | 收油净化装备 · 滤芯 · 烧结毡 · 金属纤维纱线 · 耐高温织物 — 强纶新材",
        "强纶新材产品中心：净化事业部（收油系统）、机加工事业部（滤芯、滤盘）、滤材事业部（金属纤维、烧结毡）、纱线事业部（金属纤维纱线）、热动事业部（耐高温金属纤维织物）。",
        "强纶产品中心,金属纤维制品,收油系统,金属滤芯,烧结毡,金属纤维线,耐高温套管",
        "products.html", extra_css='<link rel="stylesheet" href="home.css">', og_img="img/hero-jl-cart.webp"
    ) + header("products.html") + crumb([("产品中心", None)]) + page_hero(
        "PRODUCTS", "PRODUCT CENTER", "产品中心",
        "从一根金属纤维，<em>到成套过滤装备</em>",
        "强纶以自产金属纤维为源头，延伸出烧结毡、滤芯、纱线织物与收油净化装备五类产品。选择产品类别，查看全部产品与应用场景。",
        bg="img/hero-jl-cart.webp") + f'''
<main class="hm">
<section class="sec"><div class="wrap">
  <div class="tree">
    <div class="root rv"><a href="products.html"><img src="img/logo-mark.png" alt="">强纶新材 · 产品中心</a></div>
    <div class="stem"></div><div class="bar"></div>
    <div class="branches">{branches}</div>
  </div>
</div></section>
<section class="sec soft"><div class="wrap">
  <div class="head rv"><div><span class="eb">BY SCENE · 按应用场景找产品</span><h2 class="t">不确定选哪类产品？<br><em>按应用场景对一下</em></h2></div></div>
  <div class="dvrows">{rows}</div>
</div></section>
<section class="sec"><div class="wrap">
  <div class="head rv"><div><span class="eb">CHANNELS · 线上店铺</span><h2 class="t">也可以<em>直接在线下单</em></h2></div></div>
  <div class="chans rv">
    <a href="https://yarn.qlfiber.com/" target="_blank" rel="noopener"><b>纱线事业部官网</b><span>金属纤维纱线、金属纤维线专题站</span></a>
    <a href="https://shop143818143.taobao.com/" target="_blank" rel="noopener"><b>淘宝官方店</b><span>小批量现货与样品</span></a>
    <a href="https://shop68071416lu466.1688.com/" target="_blank" rel="noopener"><b>1688 工厂店</b><span>批量采购与工厂直供</span></a>
    <a href="https://qlfiber.en.alibaba.com/" target="_blank" rel="noopener"><b>阿里巴巴国际站</b><span>海外采购渠道</span></a>
  </div>
</div></section>
</main>
''' + ENDCTA + footer()
    w("products.html", html)


products_page()
for d in DIVS:
    division_page(d)
