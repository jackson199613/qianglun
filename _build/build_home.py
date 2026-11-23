# -*- coding: utf-8 -*-
"""首页（2026.11.23 客户反馈改版）：改由脚本生成，页头页脚与内页完全一致"""
import json
from common import w
from layout import head, header, footer, SITE, TEL, TEL_RAW, ADDR, LOGO
from divisions import DIVS
from news_data import NEWS

ARW = '<svg class="i"><use href="#i-arrow"/></svg>'

INDS = [
    ("a-filtration.html", "img/en-filtration.webp", "过滤分离", "化纤熔体 · 石油化工 · 高温烟气 · 湿法冶金",
     "熔体、料液与烟气的精密过滤，以及萃取料液的除油与油份回收。", "叶片滤盘 · 烧结滤芯 · 烧结毡 · 收油系统"),
    ("a-glass.html", "img/en-glass.webp", "玻璃深加工", "钢化炉辊道 · 热弯成型 · 夹具与吸盘包覆",
     "高温成型与输送时保护玻璃表面，不划伤、不留痕。", "金属纤维织带 · 编织套管 · 金属纤维布"),
    ("a-emi.html", "img/en-emi.webp", "电磁屏蔽与防静电", "防静电工作服 · 屏蔽面料 · 设备接地",
     "释放静电、屏蔽电磁干扰，耐水洗、效果持久。", "金属纤维纱 · 混纺纱 · 缝纫用线"),
    ("a-aero.html", "img/en-sh-pad.webp", "航空航天与特种材料", "航空航天领域 · 特种耐温材料",
     "强纶金属纤维材料已应用于航空航天领域，满足耐温、减震与可靠性要求。", "金属纤维毡制品 · 金属纤维烧结毡"),
    ("a-auto.html", "img/en-automotive.webp", "汽车", "座椅加热 · 汽车玻璃热弯成型",
     "柔软均匀的发热线材，以及耐高温、不划伤的玻璃成型包覆材料。", "强纶金属纤维线 · 耐高温套管"),
    ("a-textile.html", "img/en-textiles.webp", "功能纺织与智能穿戴", "发热服饰 · 电子标签 · 智能穿戴",
     "导电、发热又柔软耐弯折，能直接织进、缝进衣物。", "强纶金属纤维线 · 包胶线 · 导电纱"),
    ("a-other.html", "img/en-micro-burner.webp", "其他应用", "燃气燃烧器 · 制氢扩散层 · 吸声降噪",
     "兼具导电、耐高温与多孔结构，服务氢能、燃烧与降噪等新方向。", "燃烧器用毡 · 气体扩散层用毡"),
]

FAQ = [
    ("强纶主要做哪些产品？", "强纶专注金属纤维及其制品，产品由净化、机加工、滤材、纱线、热动五大事业部提供：收油系统等净化装备、滤芯与滤盘、金属纤维与烧结毡、金属纤维纱线，以及耐高温金属纤维织物。"),
    ("烧结毡和滤布怎么选？", "高温、高粘度或有腐蚀性的场合选金属纤维烧结毡：耐温耐腐蚀、可清洗再生；常温、要求不高的场合可用滤布。"),
    ("金属纤维滤芯能清洗再用吗？", "可以。金属纤维滤材耐高温、耐腐蚀，可反复清洗再生，使用寿命长。"),
    ("强纶收油系统适合什么场合？", "适合镍钴湿法冶金、化工萃取等溶液的预除油：纯物理分离不加药剂，分离出的油可回收复用。"),
    ("金属纤维纱线洗涤后还导电吗？", "导电。导电性来自金属纤维本身而不是涂层，可正常水洗、机洗。"),
    ("是否支持定制与打样？", "支持。按应用场景、尺寸与接口定制，并可提供样品试用；场景复杂的项目可安排技术人员到现场。"),
]


def news_cards():
    picks = [n for n in NEWS if n["img"] not in ("img/news/news16-0.webp", "img/news/news13-0.webp")][:3]
    out = ""
    for n in picks:
        out += f'''<a class="nc3 rv" href="{n['slug']}.html"><div class="im"><img loading="lazy" src="{n['img']}" alt="{n['title']}"></div>
<div class="bd"><div class="meta num">{n['date'].replace('-', '.')} · {n['cat']}</div><h3>{n['title']}</h3></div></a>'''
    return out


def inds_html():
    tabs = "".join(f'<a href="{u}">{t}</a>' for u, _, t, *_ in INDS)
    pans = ""
    for i, (u, im, t, sc, val, rec) in enumerate(INDS):
        pans += f'''<div class="pan2{' on' if i == 0 else ''}" tabindex="0" data-go="{u}"><i class="bg" style="background-image:url('{im}')"></i>
<div class="vt"><b>{i+1:02d}</b>{t}</div>
<div class="full"><div class="n">{i+1:02d} / {len(INDS):02d}</div><h3>{t}</h3>
<p><b>应用场景</b>{sc}</p><p>{val}</p><p><b>推荐产品</b>{rec}</p>
<a class="go" href="{u}">查看{t}方案{ARW}</a></div></div>'''
    return tabs, pans


def tree_html():
    out = ""
    for d in DIVS:
        cls = " contain" if d.get("cover_fit") == "contain" else ""
        lis = "".join(f'<li><a href="{d["file"]}#{p["id"]}">{p["name"]}</a></li>' for p in d["products"][:5])
        out += f'''<div class="br rv"><div class="bcard">
<a class="im{cls}" href="{d['file']}"><img loading="lazy" src="{d['cover']}" alt="{d['name']}"></a>
<div class="bd"><span class="no num">{d['no']} · {d['en']}</span><h3><a href="{d['file']}">{d['name']}</a></h3><p class="what">{d['what']}</p>
<ul>{lis}</ul><a class="go" href="{d['file']}">进入{d['name']}{ARW}</a></div></div></div>'''
    return out


schema = json.dumps({"@context": "https://schema.org", "@graph": [
    {"@type": "Organization", "@id": f"{SITE}/#org", "name": "福建强纶新材料股份有限公司",
     "alternateName": ["强纶新材", "FUJIAN QL METAL FIBER CO., LTD"], "url": f"{SITE}/", "logo": f"{SITE}/img/logo.png",
     "foundingDate": "2002-12", "tickerSymbol": "872336",
     "address": {"@type": "PostalAddress", "streetAddress": "龙岩市东肖镇经济技术开发区黄邦路11号", "addressLocality": "龙岩市", "addressRegion": "福建省", "addressCountry": "CN"},
     "telephone": "+86-15359927344", "email": "hcq@jl-jiber.com",
     "description": "专注金属纤维及其制品、过滤成套装备研发生产的国家级专精特新“小巨人”企业，设净化、机加工、滤材、纱线、热动五大事业部，证券代码872336。"},
    {"@type": "WebSite", "@id": f"{SITE}/#site", "url": f"{SITE}/", "name": "强纶新材中文官网", "publisher": {"@id": f"{SITE}/#org"},
     "potentialAction": {"@type": "SearchAction", "target": {"@type": "EntryPoint", "urlTemplate": f"{SITE}/search.html?q={{search_term_string}}"}, "query-input": "required name=search_term_string"}},
    {"@type": "ItemList", "name": "强纶五大事业部", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": d["name"], "url": f"{SITE}/{d['file']}"} for i, d in enumerate(DIVS)]},
    {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]},
]}, ensure_ascii=False)

tabs, pans = inds_html()
faq = "".join(f'<details class="rv"><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ)
cats = "".join(f"<option>{d['name']} · {d['tag']}</option>" for d in DIVS)

html = head(
    "福建强纶新材料股份有限公司 | 金属纤维制品领跑者",
    "福建强纶新材料股份有限公司（证券代码 872336）创立于2002年，专注金属纤维及其制品、过滤成套装备，设净化、机加工、滤材、纱线、热动五大事业部，产品用于过滤分离、玻璃深加工、电磁屏蔽、汽车、智能穿戴与航空航天等领域。",
    "金属纤维,金属纤维制品,收油系统,烧结滤芯,叶片滤盘,金属纤维烧结毡,金属纤维线,耐高温套管,强纶新材",
    "", extra_css='<link rel="stylesheet" href="home.css">', schema=schema, og_img="img/campus-gate-bright.webp"
) + header("index.html") + f"""
<main id="top" class="hm">

<section class="hhero" aria-label="首屏">
  <div class="wrap">
    <div>
      <div class="kick">Leading Metal Fiber Products · Since 2002</div>
      <h1><em>金属纤维制品</em><br>领跑者</h1>
      <p class="sub">以微米之纤，成就精密过滤</p>
      <p class="lead">二十余年专注金属纤维及其制品。从一根金属纤维，到烧结毡、滤芯滤盘、纱线织物与成套净化装备，强纶以五大事业部服务过滤分离、玻璃深加工、新能源与航空航天等领域。</p>
      <div class="ctas">
        <a class="pill pill-gold" href="#industry">按行业找产品{ARW}</a>
        <a class="pill pill-line" href="products.html">产品中心</a>
        <a class="pill pill-line" href="contact.html#inq">在线询价</a>
      </div>
      <div class="facts">
        <div><b class="num">2002</b><span>公司创立</span></div>
        <div><b class="num">872336</b><span>新三板挂牌</span></div>
        <div><b class="cn">专精特新</b><span>国家级“小巨人”</span></div>
        <div><b class="num">5</b><span>大事业部</span></div>
      </div>
    </div>
    <div class="mosaic">
      <figure><img src="img/en-hero.webp" alt="金属纤维烧结毡"><figcaption>金属纤维烧结毡</figcaption></figure>
      <figure><img src="img/en-filtration.webp" alt="过滤分离"><figcaption>过滤分离</figcaption></figure>
      <figure><img src="img/en-sh-yarn.webp" alt="金属纤维纱线"><figcaption>金属纤维纱线</figcaption></figure>
    </div>
  </div>
</section>

<div class="trust" aria-label="资质荣誉"><div class="wrap">
  <div><i><svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="6"/><path d="M15.5 13 17 22l-5-3-5 3 1.5-9"/></svg></i>国家级专精特新“小巨人”企业</div>
  <div><i><svg viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg></i>国家高新技术企业</div>
  <div><i><svg viewBox="0 0 24 24"><path d="M9 18h6M10 22h4M12 2a7 7 0 0 0-4 12.7c.6.5 1 1.3 1 2.3h6c0-1 .4-1.8 1-2.3A7 7 0 0 0 12 2z"/></svg></i>国家知识产权优势企业</div>
  <div><i><svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/></svg></i>参与制修订国家标准</div>
  <div><i><svg viewBox="0 0 24 24"><path d="M3 3v18h18"/><path d="m7 15 4-4 3 3 5-6"/></svg></i>新三板挂牌 · 872336</div>
</div></div>

<section class="sec" id="industry">
  <div class="wrap">
    <div class="head rv"><div><span class="eb">INDUSTRY · 按行业找产品</span><h2 class="t">您在哪个行业？<br><em>从这里直接找到适合的产品</em></h2>
      <p class="lead2">选择您所在的行业，查看应用场景与推荐产品；点击进入行业方案页。</p></div></div>
    <div class="ind-tabs rv">{tabs}</div>
    <div class="acc2 rv" id="acc">{pans}</div>
  </div>
</section>

<section class="sec soft" id="products">
  <div class="wrap">
    <div class="head rv"><div><span class="eb">PRODUCTS · 产品中心</span><h2 class="t">一棵树，<em>五大事业部</em></h2>
      <p class="lead2">每个事业部讲清三件事：产品是什么、有什么特点、用在哪些场景。点击进入事业部查看全部产品。</p></div>
      <a class="pill pill-line" href="products.html">进入产品中心{ARW}</a></div>
    <div class="tree">
      <div class="root rv"><a href="products.html"><img src="{LOGO}" alt="">强纶新材 · 产品中心</a></div>
      <div class="stem"></div>
      <div class="bar"></div>
      <div class="branches">{tree_html()}</div>
    </div>
  </div>
</section>

<section class="sec" id="rd">
  <div class="wrap rdg">
    <div class="rv">
      <span class="eb">R&amp;D · 科研创新</span>
      <h2 class="t">研发源于车间实践，<br><em>创新用于高端领域</em></h2>
      <p class="lead2">依托强纶新材料创新研究院，设流体净化、氢能源、金属橡胶等研究室，配备完善的实验室与检测设备，并与厦门大学、同济大学等高校院所开展产学研合作，持续把新材料从实验室带进产线。</p>
      <div class="rdk">
        <a href="patents.html"><b class="num">57<sup>项</sup></b><span>授权专利</span></a>
        <a href="lab.html"><b class="num">6<sup>个</sup></b><span>研究室</span></a>
        <a href="patents.html"><b class="num">5<sup>+1</sup></b><span>参与制修订国家 / 行业标准</span></a>
        <a href="coop.html"><b class="num">13<sup>项</sup></b><span>产学研合作</span></a>
      </div>
      <div style="margin-top:26px;display:flex;gap:12px;flex-wrap:wrap"><a class="pill pill-gold" href="rd.html">进入科研创新{ARW}</a><a class="pill pill-line" href="lab.html">研发中心与实验室</a></div>
    </div>
    <div class="labwall rv">
      <figure class="w"><img loading="lazy" src="img/lab-wide-01.webp" alt="理化实验室"><figcaption>理化实验室</figcaption></figure>
      <figure class="t"><img loading="lazy" src="img/news/news14-2.webp" alt="强纶新材展厅"><figcaption>展厅</figcaption></figure>
      <figure><img loading="lazy" src="img/lab-chem-03.webp" alt="化学分析"><figcaption>化学分析</figcaption></figure>
      <figure><img loading="lazy" src="img/lab-op-01.webp" alt="检测分析"><figcaption>检测分析</figcaption></figure>
      <figure><img loading="lazy" src="img/eq-sem.webp" alt="扫描电镜"><figcaption>扫描电镜</figcaption></figure>
      <figure class="w"><img loading="lazy" src="img/news/news03-3.webp" alt="研究院展厅"><figcaption>研究院展厅</figcaption></figure>
    </div>
  </div>
</section>

<section class="sec wash" id="about">
  <div class="wrap abt">
    <div class="pic rv"><img loading="lazy" src="img/campus-gate-bright.webp" alt="福建强纶新材料股份有限公司 · 强纶新材料创新研究院"></div>
    <div class="rv">
      <span class="eb">ABOUT · 关于强纶</span>
      <h2 class="t">二十余年，<br><em>专注把金属做成纤维</em></h2>
      <p class="lead2">福建强纶新材料股份有限公司创立于 2002 年，坐落于福建龙岩，2017 年在新三板挂牌（872336）。公司自主研发复合拉拔工艺，打通从金属纤维、纱线织物、烧结毡到过滤元器件与净化装备的完整产业链。</p>
      <ul class="pts">
        <li>国家级专精特新“小巨人”企业、国家高新技术企业</li>
        <li>五大事业部：净化、机加工、滤材、纱线、热动</li>
        <li>产品服务化纤、石化、玻璃、新能源、汽车与航空航天等领域</li>
      </ul>
      <div class="btns"><a class="pill pill-gold" href="about.html">企业简介{ARW}</a><a class="pill pill-line" href="history.html">发展历程</a><a class="pill pill-line" href="#film">观看宣传片</a></div>
    </div>
  </div>
</section>

<section class="sec" id="film">
  <div class="wrap">
    <div class="head rv"><div><span class="eb">FILM · 企业宣传片</span><h2 class="t">一部片子，<em>看懂强纶</em></h2></div></div>
    <div class="hfilm rv"><figure class="player" data-player>
      <video playsinline controls preload="none" poster="img/film-poster-2026.webp" aria-label="福建强纶新材料企业宣传片">
        <source src="video/qlfiber-film-2026-1080p.mp4" type="video/mp4">
        您的浏览器不支持视频播放，请<a href="video/qlfiber-film-2026-1080p.mp4">下载观看</a>。
      </video>
      <button type="button" class="cover" aria-label="播放企业宣传片">
        <img src="img/film-poster-2026.webp" alt="强纶新材企业宣传片封面" loading="lazy">
        <span class="pbtn"><svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg></span>
      </button>
    </figure></div>
  </div>
</section>

<section class="sec soft" id="cases">
  <div class="wrap">
    <div class="head rv"><div><span class="eb">CASES · 应用案例</span><h2 class="t">用在哪里，<em>效果如何</em></h2>
      <p class="lead2">按“应用场景 · 方案 · 效果”呈现，客户名称按保密约定脱敏。</p></div>
      <a class="pill pill-line" href="applications.html">全部应用领域{ARW}</a></div>
    <div class="cases2">
      <article class="case2 rv"><span class="tag">湿法冶金</span><h3>某新能源材料企业 · 萃取料液预除油</h3>
        <dl><dt>应用场景</dt><dd>镍钴萃取料液中含有非溶解油，影响后端树脂与膜系统</dd><dt>方案</dt><dd>槽式收油系统</dd><dt>效果</dt><dd>纯物理除油、不加药剂，分离出的油回收复用</dd></dl></article>
      <article class="case2 rv"><span class="tag">资源再生</span><h3>某钴新材料企业 · 溶液除油</h3>
        <dl><dt>应用场景</dt><dd>硫酸钴溶液除油，要求长期稳定、运行成本可控</dd><dt>方案</dt><dd>罐式收油系统，核心为表面改性金属纤维</dd><dt>效果</dt><dd>除油效果稳定，已连续运行多年，核心组件无需更换</dd></dl></article>
      <article class="case2 rv"><span class="tag">航空航天</span><h3>航空航天领域 · 金属纤维毡制品</h3>
        <dl><dt>应用场景</dt><dd>航空航天领域对材料耐温性与批次一致性要求高</dd><dt>方案</dt><dd>自主研发的金属纤维毡制品</dd><dt>效果</dt><dd>产品已应用于航空航天领域</dd></dl></article>
    </div>
  </div>
</section>

<section class="sec" id="news">
  <div class="wrap">
    <div class="head rv"><div><span class="eb">NEWS · 新闻动态</span><h2 class="t">强纶<em>最新动态</em></h2></div>
      <a class="pill pill-line" href="news.html">全部新闻{ARW}</a></div>
    <div class="news3">{news_cards()}</div>
  </div>
</section>

<section class="sec soft" id="faq">
  <div class="wrap">
    <div class="head rv"><div><span class="eb">FAQ · 常见问题</span><h2 class="t">采购前，<em>先读懂这几点</em></h2></div>
      <a class="pill pill-line" href="faq.html">更多问题{ARW}</a></div>
    <div class="faq2">{faq}</div>
  </div>
</section>

<section class="sec ask" id="contact">
  <div class="wrap">
    <div class="rv">
      <span class="eb" style="color:#4a3d00">CONTACT · 在线询价</span>
      <h2 class="t">告诉我们<br><em>您的应用场景</em></h2>
      <p class="lead2">留下需求，工程师会结合您的行业与使用场景，给出产品建议、样品与报价。</p>
      <div class="ct">
        <div><small>销售热线</small><a class="num" href="tel:{TEL_RAW}">{TEL}</a></div>
        <div><small>公司总机</small><a class="num" href="tel:05972799968">0597-2799968</a></div>
        <div><small>企业邮箱</small><a href="mailto:hcq@jl-jiber.com">hcq@jl-jiber.com</a></div>
        <div><small>公司地址</small><span>{ADDR}</span></div>
      </div>
    </div>
    <form class="rv" id="homeInq" name="inquiry" method="POST" action="contact.html?sent=1" data-netlify="true" netlify-honeypot="bot-field">
      <input type="hidden" name="form-name" value="inquiry">
      <p hidden><label>请勿填写：<input name="bot-field"></label></p>
      <h3>快速询价</h3>
      <label>姓名 *<input name="name" required autocomplete="name"></label>
      <label>手机 *<input name="tel" type="tel" required autocomplete="tel"></label>
      <label>公司<input name="company" autocomplete="organization"></label>
      <label>感兴趣的产品<select name="cat">{cats}<option>不确定 / 请工程师推荐</option></select></label>
      <label class="full">您的行业与应用场景<textarea name="msg" placeholder="例如：化纤熔体过滤，想替换现用滤芯；或玻璃钢化炉辊道包覆"></textarea></label>
      <button class="pill" type="submit">提交询价{ARW}</button>
    </form>
  </div>
</section>
</main>
""" + footer().replace('<script src="site.js"></script>', '''<script src="site.js"></script>
<script>
(function(){
  /* 行业入口：悬停展开，点击进入 */
  var pans=[].slice.call(document.querySelectorAll('#acc .pan2'));
  pans.forEach(function(p){
    function act(){pans.forEach(function(x){x.classList.toggle('on',x===p)})}
    p.addEventListener('mouseenter',function(){if(innerWidth>980)act()});
    p.addEventListener('focus',act);
    p.addEventListener('click',function(e){if(e.target.closest('a'))return;if(p.classList.contains('on'))location.href=p.getAttribute('data-go');else act()});
    p.addEventListener('keydown',function(e){if(e.key==='Enter'){p.classList.contains('on')?location.href=p.getAttribute('data-go'):act()}});
  });
})();
</script>''')

w("index.html", html)
