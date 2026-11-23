# -*- coding: utf-8 -*-
"""科研总览 rd.html（2026.11.23 改为脚本生成）
- 技术平台并入本页（原 platforms.html 与本页重复，已撤）
- 发展历程移到“关于强纶 · 发展历程”（第 18 条）
- 不写“已量产”、不写具体型号与发动机名称、不放检测报告（第 2、14、17 条）
- 实验室与展厅图片多放（第 13、26 条）
"""
from common import w, ENDCTA, rnav
from layout import head, header, footer, crumb, page_hero

ARW = '<svg class="i"><use href="#i-arrow"/></svg>'

TECH = [
    ("01", "超细金属纤维制备", "img/en-sh-fiber.webp", "自主研发集束拉拔工艺，把金属拉成微米级纤维：细而均匀，比表面积大，是全部产品的起点。", "p-yarn.html", "纱线事业部"),
    ("02", "金属纤维烧结成型", "img/en-sh-felt.webp", "金属纤维无纺铺制、叠层与真空烧结，形成梯度孔结构，兼顾过滤精度与纳污量。", "p-felt.html", "滤材事业部"),
    ("03", "过滤元器件与净化装备", "img/fts-cover.webp", "从滤芯、滤盘到收油系统，把滤材做成能装上设备的产品与成套装备。", "p-equipment.html", "净化 · 机加工事业部"),
    ("04", "导电与发热应用", "img/en-textiles.webp", "利用金属纤维导电、耐温、柔软可织的特性，开发导电线、包胶线与功能织物。", "p-yarn.html", "纱线 · 热动事业部"),
]
tech = "".join(f'''<a class="tpl rv" href="{u}"><div class="im{' contain' if 'fts' in im else ''}"><img loading="lazy" src="{im}" alt="{t}"></div>
<div class="bd"><span class="num">{n}</span><h3>{t}</h3><p>{d}</p><em>对应：{dv}{ARW}</em></div></a>''' for n, t, im, d, u, dv in TECH)

LAB = [("img/lab-wide-01.webp", "材料与应用实验室", "w"), ("img/news/news14-2.webp", "研究院展厅", "t"),
       ("img/lab-chem-03.webp", "化学分析", ""), ("img/eq-sem.webp", "扫描电子显微镜", ""),
       ("img/lab-op-01.webp", "检测数据采集", ""), ("img/news/news03-3.webp", "展厅入口", "w"),
       ("img/lab-chem-05.webp", "试剂与耗材储备", ""), ("img/news/news08-2.webp", "实验检测", ""),
       ("img/lab-wide-02.webp", "实验室洁净区", "w"), ("img/news/news17-1.webp", "展厅产品展柜", "")]
labwall = "".join(f'<figure class="{c}"><img loading="lazy" src="{s}" alt="{t}"><figcaption>{t}</figcaption></figure>' for s, t, c in LAB)

UNIS = ["厦门大学", "同济大学", "粤港澳大湾区黄埔材料研究院", "中机研标准技术研究院", "安徽理工大学", "厦门理工学院", "集美大学", "闽江学院", "龙岩学院"]

STD = [("GB/T 20100—2016", "不锈钢纤维烧结滤毡"), ("GB/T 17492—2019", "工业用金属丝编织网 技术要求和检验"),
       ("GB/T 21648—2023", "金属丝编织密纹网"), ("GB/T 45969—2025", "颗粒表征 术语"),
       ("GB/T 5330—2025", "工业用金属丝编织方孔筛网"), ("JB/T 13511—2018", "分离机械用柔性非织造过滤介质过滤性能测试方法")]

html = head(
    "科研创新 | 强纶新材料创新研究院 · 实验室 · 专利 · 产学研 — 强纶新材",
    "强纶依托强纶新材料创新研究院开展金属纤维材料研发：超细金属纤维制备、烧结成型、过滤元器件与净化装备、导电发热应用四大方向；授权专利57项，参与制修订国家标准5项、行业标准1项，与厦门大学、同济大学等开展产学研合作。",
    "强纶科研,强纶新材料创新研究院,金属纤维研发,专利,产学研,实验室",
    "rd.html", extra_css='<link rel="stylesheet" href="home.css">', og_img="img/lab-wide-01.webp"
) + header("rd.html") + crumb([("科研创新", None)]) + page_hero(
    "R&amp;D", "RESEARCH &amp; DEVELOPMENT", "科研创新",
    "以研发，<em>驱动金属纤维的每一次进步</em>",
    "强纶依托强纶新材料创新研究院，围绕金属纤维“更细、更均匀、更耐用”持续攻关，打通从纤维、烧结成型到过滤元器件与净化装备的完整技术链。",
    bg="img/en-ph-rd.webp") + f'''
<main>
<section class="sec" style="padding-top:40px"><div class="wrap">
  {rnav(0)}
  <div class="abt hm-abt">
    <div class="pic rv"><img src="img/campus-gate-bright.webp" alt="龙岩高新区新材料创新创业园 · 强纶新材料创新研究院"></div>
    <div class="rv">
      <span class="eb">PLATFORM · 研发平台</span>
      <h2 class="t2">强纶新材料<em>创新研究院</em></h2>
      <p class="lead2">研究院位于龙岩高新区新材料创新创业园，是强纶开展材料研发、工艺攻关与应用验证的核心平台。研究院与生产基地联动，新工艺从实验室走到产线的路径更短，客户现场的反馈也能更快回到研发端。</p>
      <ul class="pts">
        <li>设流体净化、氢能源、金属橡胶、电化学、金属学、多孔介质燃烧 6 个研究室</li>
        <li>省级新型研发机构、省级企业技术中心、省级博士后创新实践基地</li>
        <li>研究成果服务化纤、石化、新能源与航空航天等领域</li>
      </ul>
      <div class="btns"><a class="pill pill-gold" href="lab.html">研发中心与实验室{ARW}</a><a class="pill pill-line" href="testing.html">检测能力</a></div>
    </div>
  </div>
</div></section>

<section class="sec alt"><div class="wrap">
  <div class="sh rv"><h2>四大<em>技术方向</em></h2><p>每个技术方向都对应具体的事业部与产品，研发成果可以快速转化为客户手中的产品。</p></div>
  <div class="tpls">{tech}</div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sh rv"><h2>实验室与<em>研究院展厅</em></h2><p>材料与应用实验室、仪器分析区、电镜室与研究院展厅，以下均为实拍。</p></div>
  <div class="labwall big rv">{labwall}</div>
  <div style="margin-top:24px"><a class="pill pill-line" href="lab.html">查看更多实验室照片{ARW}</a></div>
</div></section>

<section class="sec wash2"><div class="wrap">
  <div class="sh rv"><h2>知识产权与<em>标准</em></h2><p>公司累计获得授权专利 57 项，参与制修订国家标准 5 项、行业标准 1 项，是全国颗粒表征与分检及筛网标准化技术委员会委员单位。</p></div>
  <div class="ipg">
    <a class="cert all rv" href="patents.html"><div class="paper"><b class="big num">57</b><i>项授权专利</i></div><figcaption>查看专利墙 →</figcaption></a>
    <div class="stds rv">{"".join(f'<div><b class="num">{c}</b><span>{n}</span></div>' for c, n in STD)}</div>
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sh rv"><h2>产学研<em>合作</em></h2><p>与多所高校及科研院所保持长期合作，既有联合攻关的课题，也有共建平台与实践基地。</p></div>
  <div class="unis rv">{"".join(f"<span>{u}</span>" for u in UNIS)}</div>
  <div style="margin-top:24px"><a class="pill pill-line" href="coop.html">产学研合作详情{ARW}</a><a class="pill pill-line" style="margin-left:10px" href="achievements.html">科研成果</a></div>
</div></section>

<section class="sec alt"><div class="wrap">
  <div class="sh rv"><h2>合作<em>研发</em></h2><p>面向有特殊需求的客户与科研机构，强纶开放研发合作。</p></div>
  <div class="dvfs">
    <div class="dvf rv"><i class="num">01</i><h4>样品试用</h4><p>按您的应用场景提供样品，验证使用效果。</p></div>
    <div class="dvf rv"><i class="num">02</i><h4>非标定制</h4><p>按尺寸、接口与使用要求定制滤材、元器件与制品。</p></div>
    <div class="dvf rv"><i class="num">03</i><h4>联合开发</h4><p>面向新应用场景，与客户或院校联合开展材料与工艺开发。</p></div>
  </div>
</div></section>
{ENDCTA}
</main>
''' + footer()
w("rd.html", html)
