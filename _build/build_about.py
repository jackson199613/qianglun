# -*- coding: utf-8 -*-
"""关于强纶 栏目（7 页）— 内容全部取自甲方提供资料"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from layout import head, header, crumb, page_hero, footer, SITE
from common import w, anav, ENDCTA, vr_block



# ───────────────────────────── 1. 企业简介
schema_org = '{"@context":"https://schema.org","@type":"Organization","name":"福建强纶新材料股份有限公司","alternateName":["强纶新材","FUJIAN QL METAL FIBER CO., LTD"],"url":"%s/","logo":"https://www.qlfiber.com/assets/images/logo.png","foundingDate":"2002-12","numberOfEmployees":{"@type":"QuantitativeValue","value":200},"tickerSymbol":"872336","address":{"@type":"PostalAddress","streetAddress":"龙岩经济技术开发区黄邦路11号","addressLocality":"龙岩市","addressRegion":"福建省","addressCountry":"CN"},"telephone":"+86-18159821773","description":"国内规模领先、福建省内唯一专注金属功能纤维及制品研发生产的高新技术企业，国家级专精特新“小巨人”企业。"}' % SITE

w('about.html', head(
    "企业简介 | 福建强纶新材料股份有限公司",
    "强纶新材创立于2002年，坐落福建龙岩，2017年股改并新三板挂牌（872336）。国家级专精特新“小巨人”企业，聚焦滤材滤器、流体净化、电热材料、多孔材料、特种纺织五大方向。",
    "强纶新材,福建强纶,金属纤维企业,872336,专精特新小巨人,企业简介",
    "about.html", schema=schema_org, og_img="img/plant-03.webp")
 + header('about.html')
 + crumb([("关于强纶", None)])
 + page_hero("01", "ABOUT", "企业简介",
             "二十余年，<em>只做一件事</em>：<br>把金属做成纤维，再做成产品",
             "福建强纶新材料股份有限公司始创于 2002 年，坐落于福建省龙岩市，2017 年完成股份制改革并登陆新三板（股票代码 872336），是国内规模领先、福建省内唯一专注金属功能纤维及制品研发生产的高新技术企业。",
             [("2002", "", "创立年份"), ("872336", "", "新三板代码"), ("200", "+", "员工人数"), ("40", "亩", "自有工业用地")],
             bg="img/plant-03.webp")
 + f"""<section class="sec"><div class="wrap">{anav(0)}
  <div class="g2 r7-5 wide">
    <div class="prose rv">
      <p class="lede">公司集研发、制造、销售与技术服务于一体，获评国家专精特新“小巨人”企业、国家知识产权优势企业等重要资质。自主研发复合拉拔核心工艺，打通金属材料与纺织行业壁垒，牵头开辟“柔性金属纤维及其功能性纺织品”新兴赛道，填补国家新兴行业目录空白。</p>
      <h3>五大技术方向</h3>
      <p>紧扣国家新材料产业战略布局，公司聚焦<strong>滤材滤器、流体净化、电热材料、多孔材料、特种纺织</strong>五大方向持续攻关，突破多项“卡脖子”技术，实现关键产品进口替代。现已形成金属纤维、烧结滤材、金属纱线、编织物、电热服饰等十大系列产品，兼具导电、耐火、柔性、防切割、减震等性能，广泛服务于航空航天、石油化工、化纤冶金、能源交通等关键领域。</p>
      <h3>核心产品的市场位置</h3>
      <p>金属纱线在电热面料领域市占率全国第一，金属烧结毡稳居黏胶行业国内首位。作为国内最早配套航天工程的金属纤维毡供应商，自研针刺毡成功应用于<strong>长征五号 B、长征五号遥五</strong>运载火箭发动机；国产化熔体滤芯批量供应国内大型石化、化纤龙头企业，先后研制出国内首张 KKF 滤机烧结毡、最大规格 KKF 滤机烧结毡以及首张国产金属纤维针刺毡。</p>
      <h3>创新与标准</h3>
      <p>公司建有省级新型研发机构、省级企业技术中心等科研平台，配备高端精密检测设备，与厦门大学、厦门理工学院等高校深化产学研协同创新。公司是全国颗粒表征与分检及筛网标委会委员单位，参与制修订 <strong>5 项国家标准、1 项行业标准</strong>，累计授权专利 <strong>57 项</strong>（发明 11 项、实用新型 44 项、外观 2 项）。</p>
      <p>展望未来，公司坚持“协调创新、联合创业、利益共享”的经营理念，深耕先进金属功能新材料研发与产业化，着力发展新质生产力、助力区域和行业高质量发展。</p>
    </div>
    <aside class="rv d1">
      <div class="gal c3" style="grid-template-columns:1fr;gap:14px;margin:0">
        <figure style="aspect-ratio:4/3"><img src="img/plant-02.webp" alt="强纶新材激光加工设备" loading="lazy"><figcaption>智能加工设备</figcaption></figure>
        <figure style="aspect-ratio:4/3"><img src="img/lab-01.webp" alt="强纶新材实验室" loading="lazy"><figcaption>材料与应用实验室</figcaption></figure>
      </div>
      <div class="note" style="margin-top:22px"><b>英文名称</b><br>FUJIAN QL METAL FIBER CO., LTD<br><br><b>注册地址</b><br>福建省龙岩市龙岩经济技术开发区黄邦路 11 号<br><br><b>统一社会信用代码</b><br>91350800753119639E</div>
    </aside>
  </div>

  <div class="sec-h" style="margin:96px 0 40px"><h2>覆盖材料到系统的<em>完整链条</em></h2><p>从一根金属纤维出发，向下游延伸到纱线织物、烧结滤材、过滤元件，直到成套净化设备。</p></div>
  <div class="g4">
    <article class="card rv"><span class="n">01</span><h3>金属纤维</h3><p>复合拉拔制备，直径低至 2μm，不锈钢 / 镍 / 钛 / 铁铬铝 / 铜多材质。</p></article>
    <article class="card rv d1"><span class="n">02</span><h3>纱线与织物</h3><p>导电纱、缝纫线、发热线、编织带、套管与机织布，可纺可织。</p></article>
    <article class="card rv d2"><span class="n">03</span><h3>烧结滤材</h3><p>多层梯度孔结构高温烧结，精度 10–60μm，耐温耐腐蚀可再生。</p></article>
    <article class="card rv d3"><span class="n">04</span><h3>元件与设备</h3><p>熔体 / 水 / 除尘滤芯、滤盘，直至收油系统等成套净化装备。</p></article>
  </div>
</div></section>"""
 + vr_block("img/plant-02.webp", "线上走一遍厂区与研究院", "VR 全景支持在电脑与手机上自由漫游车间、实验室与成品区，不便到场时也能先看清生产现场。")
 + ENDCTA + footer())

# ───────────────────────────── 2. 发展历程
TL = [
    ("2002.12", "公司成立", "龙岩强龙金属纤维有限公司成立，注册资本 3800 万元，深耕金属纤维制品及滤材领域。", False),
    ("2017.06", "完成股份制改造", "更名为福建强纶新材料股份有限公司。", False),
    ("2017.11", "新三板挂牌", "强纶新材正式在全国中小企业股份转让系统挂牌，股票代码 872336。", True),
    ("2020", "配套国家航天工程", "公司针刺毡产品成功应用于长征五号 B、长征五号遥五运载火箭发动机。", True),
    ("2021", "获评国家高新技术企业", "持续夯实研发体系，建立省级企业技术中心与新型研发机构。", False),
    ("2023", "省级专精特新“小巨人”", "获评福建省专精特新中小企业（第一批）。", False),
    ("2025", "国家级专精特新“小巨人”", "获评国家级专精特新“小巨人”企业。", True),
    ("2026.09", "拓展新赛道", "完成经营范围升级，拓展储能、先进金属材料方向；完成定向增发，注册资本增至 4275 万元。", True),
]
tl_html = "".join(
    f'<div class="e rv{" gold" if g else ""}"><b class="num">{y}</b><h4>{t}</h4><p>{d}</p></div>'
    for y, t, d, g in TL)

w('history.html', head(
    "发展历程 | 强纶新材",
    "2002 年创立至今：2017 股改并新三板挂牌 872336、2020 产品应用于长征五号 B 火箭发动机、2021 国家高新技术企业、2025 国家级专精特新“小巨人”。",
    "强纶发展历程,强纶大事记,872336挂牌,长征五号",
    "history.html")
 + header('about.html')
 + crumb([("关于强纶", "about.html"), ("发展历程", None)])
 + page_hero("02", "HISTORY", "发展历程",
             "从一台拉拔机，<em>到一条完整产业链</em>",
             "二十余年间，强纶从单一金属纤维制品起步，逐步补齐纱线织物、烧结滤材、过滤元件与成套净化装备，形成自主可控的全链条能力。")
 + f"""<section class="sec"><div class="wrap">{anav(1)}
  <div class="g2 r7-5 wide">
    <div class="tl">{tl_html}</div>
    <aside class="rv d1">
      <div class="gal c3" style="grid-template-columns:1fr">
        <figure><img src="img/team-loyalty2025.webp" alt="强纶新材年会现场" loading="lazy"><figcaption>2025 年度表彰大会</figcaption></figure>
      </div>
      <div class="note" style="margin-top:20px"><b>注册资本变化</b><br>2002 年设立 3800 万元 → 2026 年完成定向增发，增至 4275 万元。</div>
    </aside>
  </div>
</div></section>"""
 + ENDCTA + footer())

# ───────────────────────────── 3. 制造能力
w('manufacturing.html', head(
    "制造能力 | 强纶新材",
    "自有工业用地 40 余亩，覆盖金属复合丝拉拔、压制烧结、纺纱编织、电化学材料加工与精密机械加工五大制研平台，员工 200 余人。",
    "强纶制造能力,金属纤维生产,拉拔工艺,烧结工艺,厂房设备",
    "manufacturing.html", og_img="img/plant-05.webp")
 + header('about.html')
 + crumb([("关于强纶", "about.html"), ("制造能力", None)])
 + page_hero("03", "MANUFACTURING", "制造能力",
             "把金属棒，<em>一路拉到 2 微米</em>",
             "核心工艺是复合拉拔：将金属棒逐级拉拔成金属细丝，再拉拔成金属纤维，最细可至 2μm，比头发丝细约 35 倍；随后通过捻搓、纺纱、编织、烧结等工序制成纱线、织物、烧结毡与过滤元件。",
             [("40", "亩", "自有工业用地"), ("1800", "㎡", "厂房面积"), ("200", "+", "员工人数"), ("5", "大", "制研平台")],
             bg="img/plant-05.webp")
 + f"""<section class="sec"><div class="wrap">{anav(2)}
  <div class="sec-h"><h2>五大制研平台</h2><p>强纶新材料创新研究院整合强纶新材、金纶新材料、金山粉末、柔银新材料、龙象机械等资源，形成互补的制造与中试能力。</p></div>
  <div class="g3">
    <article class="card rv"><span class="n">01</span><h3>金属复合丝拉拔</h3><p>复合拉拔核心工艺，制备 2–100μm 各规格金属纤维，材质覆盖 316L / 304 / 铁铬铝 / 镍 / 钛 / 铜等。</p></article>
    <article class="card rv d1"><span class="n">02</span><h3>压制烧结</h3><p>粉末压制与真空高温烧结，制备多层梯度孔烧结毡、烧结网及传动元件。</p></article>
    <article class="card rv d2"><span class="n">03</span><h3>纺纱编织</h3><p>金属纤维可纺可织，制成纱线、缝纫线、发热线、机织带、套管与机织布。</p></article>
    <article class="card rv"><span class="n">04</span><h3>电化学材料加工</h3><p>面向多孔材料、新能源与氢能方向的材料加工与表面改性。</p></article>
    <article class="card rv d1"><span class="n">05</span><h3>精密机械加工</h3><p>滤芯骨架、过滤器壳体与成套设备的精密加工、焊接与装配。</p></article>
    <article class="card rv d2"><span class="n">06</span><h3>中试与成果转化</h3><p>研发源于车间实践，中试基地与多维测试中心支撑新工艺从实验室到量产。</p></article>
  </div>

  <div class="sec-h" style="margin:90px 0 32px"><h2>厂区与设备</h2><p>激光切割、冲压、数控车、摇臂钻、带锯、焊接与检测装备，支撑从滤材到成套设备的自制能力。</p></div>
  <div class="gal">
    <figure><img src="img/plant-02.webp" alt="激光切割设备" loading="lazy"><figcaption>激光切割</figcaption></figure>
    <figure><img src="img/plant-03.webp" alt="冲压设备" loading="lazy"><figcaption>冲压成型</figcaption></figure>
    <figure><img src="img/plant-05.webp" alt="机加工车间" loading="lazy"><figcaption>机加工车间</figcaption></figure>
    <figure><img src="img/plant-06.webp" alt="数控加工设备" loading="lazy"><figcaption>数控加工</figcaption></figure>
    <figure><img src="img/plant-07.webp" alt="摇臂钻与加工设备" loading="lazy"><figcaption>钻削加工</figcaption></figure>
    <figure><img src="img/plant-08.webp" alt="带锯与下料设备" loading="lazy"><figcaption>下料切割</figcaption></figure>
    <figure><img src="img/plant-09.webp" alt="装配车间" loading="lazy"><figcaption>装配车间</figcaption></figure>
    <figure><img src="img/plant-01.webp" alt="零部件与备件货架" loading="lazy"><figcaption>零部件库</figcaption></figure>
    <figure><img src="img/plant-10.webp" alt="检测与工装设备区" loading="lazy"><figcaption>工装与检测区</figcaption></figure>
    <figure><img src="img/plant-04.webp" alt="物料与备件仓储" loading="lazy"><figcaption>物料仓储</figcaption></figure>
  </div>

  <div class="g2 wide" style="margin-top:90px">
    <div class="prose rv">
      <h3 style="margin-top:0">产品自制范围</h3>
      <p>从纤维到成品的关键工序均在厂内完成：纤维制备、梳理成条、纺纱织造、无纺成毡、真空烧结、折波成型、骨架加工、焊接装配、压力试验与出厂检验。这保证了<strong>精度一致性</strong>与<strong>交期可控</strong>，也使非标定制成为常态能力而非例外。</p>
      <h3>非标定制</h3>
      <p>可按客户的过滤精度、工况温度、介质、尺寸与接口等参数定制；液体工况复杂的客户，公司可<strong>免费提供前期实验设备并派技术人员入厂试验</strong>，用实测数据确定方案后再定型。</p>
    </div>
    <div class="rv d1">
      <div class="gal c3" style="grid-template-columns:1fr 1fr">
        <figure><img src="img/cart-03.webp" alt="金属纤维烧结滤芯批量生产" loading="lazy"><figcaption>滤芯批量生产</figcaption></figure>
        <figure><img src="img/media-05.webp" alt="金属纤维烧结毡" loading="lazy"><figcaption>烧结毡</figcaption></figure>
      </div>
    </div>
  </div>
</div></section>"""
 + ENDCTA + footer())

print('关于强纶：3/7')
