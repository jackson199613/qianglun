# -*- coding: utf-8 -*-
"""强纶官网 · 公共页头/页脚/头部模板"""

SITE = "https://qianglun.netlify.app"
TEL_RAW = "18159821773"
TEL = "181 5982 1773"
ADDR = "福建省龙岩市龙岩经济技术开发区黄邦路 11 号"
ICP = "闽ICP备2022016209号-1"
LOGO = "https://www.qlfiber.com/assets/images/logo.png"

# 栏目 → (标题, 链接)   合同附件一（一）栏目与页面清单
NAV = [
    ("科研创新", "rd.html"),
    ("产品中心", "products.html"),
    ("应用方案", "applications.html"),
    ("选型中心", "selector.html"),
    ("技术专栏", "insights.html"),
    ("关于强纶", "about.html"),
    ("新闻动态", "news.html"),
    ("联系我们", "contact.html"),
]

ICONS = """<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<symbol id="i-arrow" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></symbol>
<symbol id="i-phone" viewBox="0 0 24 24"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></symbol>
<symbol id="i-msg" viewBox="0 0 24 24"><path d="M21 11.5a8.4 8.4 0 0 1-9 8.4 8.5 8.5 0 0 1-3.8-.9L3 20.5l1.4-4.2A8.4 8.4 0 0 1 12 3.1a8.4 8.4 0 0 1 9 8.4z"/></symbol>
<symbol id="i-wechat" viewBox="0 0 24 24"><path d="M9 4C5.1 4 2 6.6 2 9.8c0 1.8 1 3.4 2.6 4.5L4 17l3-1.6c.6.2 1.3.3 2 .3h.6M22 15.2c0-2.7-2.6-4.8-5.8-4.8s-5.8 2.1-5.8 4.8S13 20 16.2 20c.6 0 1.2-.1 1.7-.2L21 21l-.7-2.2c1-.9 1.7-2.2 1.7-3.6z"/></symbol>
<symbol id="i-search" viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></symbol>
<symbol id="i-menu" viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h16"/></symbol>
<symbol id="i-x" viewBox="0 0 24 24"><path d="M6 6l12 12M18 6 6 18"/></symbol>
<symbol id="i-up" viewBox="0 0 24 24"><path d="M12 19V5M6 11l6-6 6 6"/></symbol>
<symbol id="i-check" viewBox="0 0 24 24"><path d="m5 13 4 4L19 7"/></symbol>
<symbol id="i-doc" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/></symbol>
<symbol id="i-dl" viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M7 10l5 5 5-5M12 15V3"/></symbol>
</defs></svg>"""


def head(title, desc, keywords="", canonical="", extra_css="", schema="", og_img="img/plant-02.webp"):
    cn = f'<link rel="canonical" href="{SITE}/{canonical}">' if canonical else ""
    kw = f'<meta name="keywords" content="{keywords}">' if keywords else ""
    sc = f'<script type="application/ld+json">{schema}</script>' if schema else ""
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{kw}
{cn}
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/{og_img}">
<meta property="og:site_name" content="福建强纶新材料股份有限公司">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700&family=Noto+Serif+SC:wght@500;700;900&family=Cormorant+Garamond:ital,wght@1,500;1,600&family=Barlow+Condensed:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="site.css">
<link rel="stylesheet" href="page.css">
<link rel="stylesheet" href="theme-v4.css">
{extra_css}
{sc}
</head>
<body class="go">
{ICONS}"""


def header(active=""):
    items = "".join(
        f'<a href="{href}"{" class=\"on\"" if href == active else ""}>{name}</a>'
        for name, href in NAV
    )
    return f"""<header id="hdr" class="solid">
  <div class="util">
    <div class="wrap">
      <span>福建强纶新材料股份有限公司 · 新三板 <b class="num">872336</b></span>
      <nav><a href="https://yarn.qlfiber.com/" target="_blank" rel="noopener">纱线事业部</a><a href="https://shop143818143.taobao.com/" target="_blank" rel="noopener">淘宝官方店</a><a href="https://shop68071416lu466.1688.com/" target="_blank" rel="noopener">1688 工厂店</a><a href="jobs.html">人才招聘</a><a href="https://qlfiber.en.alibaba.com/" target="_blank" rel="noopener" class="en">English</a></nav>
    </div>
  </div>
  <div class="wrap nav">
    <a class="brand" href="index.html" aria-label="强纶新材 首页">
      <img src="{LOGO}" alt="强纶新材 logo" width="42" height="42">
      <span><strong>强纶新材</strong><small>QIANGLUN · SINCE 2002</small></span>
    </a>
    <nav class="menu" id="menu">{items}</nav>
    <div class="nav-r">
      <button class="icon-b" id="searchBtn" aria-label="站内搜索"><svg class="i"><use href="#i-search"/></svg></button>
      <a class="tel" href="tel:{TEL_RAW}"><svg class="i"><use href="#i-phone"/></svg><span class="num">{TEL}</span></a>
      <a class="pill pill-ink" href="contact.html#inq">在线询价<svg class="i"><use href="#i-arrow"/></svg></a>
      <button class="burger" id="burger" aria-label="打开菜单" aria-expanded="false"><svg class="i"><use href="#i-menu"/></svg></button>
    </div>
  </div>
  <div class="search" id="search" hidden>
    <div class="wrap"><svg class="i"><use href="#i-search"/></svg><input id="q" type="search" placeholder="搜索产品、工况或技术问题，例如：化纤熔体过滤精度" aria-label="站内搜索"><button class="icon-b" id="searchX" aria-label="关闭搜索"><svg class="i"><use href="#i-x"/></svg></button></div>
    <div class="wrap hot">热门：<a href="selector.html">按工况选型</a><a href="p-felt.html">烧结毡</a><a href="p-element.html">烧结滤芯</a><a href="p-equipment.html">收油系统</a><a href="rd.html">2μm 超细纤维</a></div>
  </div>
</header>"""


def crumb(trail):
    """trail: [(名称, 链接或None)]，最后一项为当前页"""
    parts, items = [], []
    for i, (name, href) in enumerate([("首页", "index.html")] + trail):
        last = i == len(trail)
        parts.append(f'<span aria-current="page">{name}</span>' if last and href is None
                     else f'<a href="{href}">{name}</a>')
        items.append('{"@type":"ListItem","position":%d,"name":"%s"%s}' % (
            i + 1, name, f',"item":"{SITE}/{href}"' if href else ""))
    schema = '{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[%s]}' % ",".join(items)
    return f"""<nav class="crumb" aria-label="面包屑"><div class="wrap">{'<i>/</i>'.join(parts)}</div></nav>
<script type="application/ld+json">{schema}</script>"""


def page_hero(idx, en, zh, h1, lead, kpis=None, bg=""):
    k = ""
    if kpis:
        k = '<div class="ph-k">' + "".join(
            f'<div><b class="num">{v}<sup>{u}</sup></b><span>{t}</span></div>' for v, u, t in kpis
        ) + "</div>"
    style = f' style="--phbg:url(\'{bg}\')"' if bg else ""
    cls = "ph has-bg" if bg else "ph"
    return f"""<section class="{cls}"{style}><div class="wrap">
  <div class="idx"><b>{idx}</b>{en} · {zh}</div>
  <h1>{h1}</h1>
  <p class="ph-lead">{lead}</p>
  {k}
</div></section>"""


def footer():
    return f"""<footer>
  <div class="wrap ft">
    <div>
      <a class="brand" href="index.html"><img src="{LOGO}" alt="" width="42" height="42"><span><strong>强纶新材</strong><small>QIANGLUN · SINCE 2002</small></span></a>
      <p>福建强纶新材料股份有限公司，专注金属纤维及其制品、过滤成套装备的研发、生产、销售与技术服务。</p>
      <div class="fqr">
        <button type="button" class="sq" aria-label="公众号"><i><svg class="i"><use href="#i-wechat"/></svg></i>公众号<span class="pop"><img src="img/qr-mp.webp" alt="强纶新材微信公众号二维码" loading="lazy"><b>微信公众号</b><em>微信扫一扫关注</em></span></button>
        <button type="button" class="sq" aria-label="视频号"><i><svg class="i"><use href="#i-msg"/></svg></i>视频号<span class="pop"><img src="img/qr-channels.webp" alt="强纶新材视频号二维码" loading="lazy"><b>微信视频号</b><em>微信扫一扫打开</em></span></button>
        <a class="sq" href="https://www.douyin.com/user/MS4wLjABAAAA0PFr_Jq_GxWs3z0qsuOEAX0AYbqEWlcrNGrXj_38tgIQrK6fG3V1MWPy_QD-iqcW" target="_blank" rel="noopener" aria-label="抖音"><i><svg class="i"><use href="#i-play"/></svg></i>抖音<span class="pop"><img src="img/qr-douyin.webp" alt="强纶新材抖音二维码" loading="lazy"><b>抖音号</b><em>点击前往主页，或扫码</em></span></a>
      </div>
    </div>
    <div><h5>产品中心</h5><ul>
      <li><a href="p-yarn.html">金属纤维纱线</a></li>
      <li><a href="p-felt.html">金属纤维烧结毡</a></li>
      <li><a href="p-fabric.html">金属纤维织物</a></li>
      <li><a href="p-element.html">过滤元器件</a></li>
      <li><a href="p-equipment.html">净化设备 · 收油系统</a></li>
    </ul></div>
    <div><h5>应用方案</h5><ul>
      <li><a href="a-filtration.html">过滤分离</a></li>
      <li><a href="a-glass.html">玻璃深加工</a></li>
      <li><a href="a-emi.html">电磁屏蔽与防静电</a></li>
      <li><a href="a-aero.html">航空航天与特种材料</a></li>
      <li><a href="a-auto.html">汽车</a></li>
      <li><a href="a-textile.html">功能纺织与智能穿戴</a></li>
    </ul></div>
    <div><h5>科研与支持</h5><ul>
      <li><a href="rd.html">科研创新</a></li>
      <li><a href="patents.html">专利与标准</a></li>
      <li><a href="selector.html">选型中心</a></li>
      <li><a href="specs.html">参数对照表</a></li>
      <li><a href="downloads.html">资料下载</a></li>
      <li><a href="faq.html">常见问题</a></li>
    </ul></div>
    <div><h5>关于强纶</h5><ul>
      <li><a href="about.html">企业简介</a></li>
      <li><a href="history.html">发展历程</a></li>
      <li><a href="honors.html">资质荣誉</a></li>
      <li><a href="culture.html">企业文化</a></li>
      <li><a href="investor.html">投资者关系</a></li>
      <li><a href="jobs.html">人才招聘</a></li>
    </ul></div>
  </div>
  <div class="wrap fb">
    <span>© 2026 福建强纶新材料股份有限公司 版权所有 · <a href="https://beian.miit.gov.cn/" target="_blank" rel="noopener">{ICP}</a></span>
    <span><a href="sitemap.html">网站地图</a> · <a href="privacy.html">隐私政策</a> · <a href="privacy.html#legal">法律声明</a></span>
  </div>
  <div class="huge" aria-hidden="true">QIANGLUN</div>
</footer>

<div class="float">
  <a href="tel:{TEL_RAW}" aria-label="电话咨询"><svg class="i"><use href="#i-phone"/></svg><span class="tipx">{TEL}</span></a>
  <a href="contact.html#inq" aria-label="在线询价"><svg class="i"><use href="#i-msg"/></svg><span class="tipx">在线询价</span></a>
  <button id="toTop" aria-label="返回顶部"><svg class="i"><use href="#i-up"/></svg></button>
</div>
<nav class="mbar" aria-label="快捷操作">
  <a href="tel:{TEL_RAW}"><svg class="i"><use href="#i-phone"/></svg>电话</a>
  <a href="contact.html#wx"><svg class="i"><use href="#i-wechat"/></svg>微信</a>
  <a href="contact.html#inq" class="hl"><svg class="i"><use href="#i-msg"/></svg>询价</a>
</nav>
<script src="site.js"></script>
</body>
</html>"""
