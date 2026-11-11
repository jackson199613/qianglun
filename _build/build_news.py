# -*- coding: utf-8 -*-
"""新闻动态列表 + 新闻详情模板 + 人才招聘 2 页"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from layout import head, header, crumb, page_hero, footer, SITE
from common import w, ENDCTA

NEWS = [
 ("企业新闻","创新驱动 装备向新｜强纶新材入围第十五届中国创新创业大赛新材料全国赛","2026-11-10","img/expo-forum2026.webp",
  "公司以新材料方向项目入围全国赛，是对强纶持续研发投入与成果转化能力的又一次认可。"),
 ("企业新闻","从“省内唯一”到“国家级认可”，强纶新材再获殊荣","2026-10-29","img/plant-02.webp",
  "作为福建省内唯一专注金属功能纤维及制品研发生产的企业，公司获评国家级专精特新“小巨人”。"),
 ("行业资讯","龙岩高新区推动行业标准体系建设实现多点突破——以科创赋能产业能级跃升","2026-07-14","img/media-03.webp",
  "《闽西日报》报道龙岩高新区（经开区）厚植企业创新沃土，强纶作为国家标准起草单位参与其中。"),
 ("企业新闻","喜讯｜福建强纶新材料股份有限公司获评中国航发商发合格供应商","2026-06-18","img/media-09.webp",
  "公司通过航发商发供应商审核，进一步巩固在航空航天特种材料领域的配套能力。"),
 ("展会活动","2026（第七届）军民两用降噪、减振、吸能新材料与技术论坛","2026-06-05","img/expo-forum2026.webp",
  "公司携金属纤维减震与吸能材料参会，与军工及科研院所展开技术交流。"),
 ("展会活动","第十四届全国湿法冶金工程技术交流会","2026-05-20","img/expo-hydromet14.webp",
  "强纶收油系统在湿法冶金行业的应用成果受到与会企业关注。"),
 ("行业资讯","产品有活力 工业动能足——龙岩优质工业品调查报道","2026-08-27","img/plant-05.webp",
  "《闽西日报》走访龙岩优质工业品企业，报道强纶金属纤维产品的市场表现。"),
 ("展会活动","2024 年德国科隆过滤展 FILTECH","2024-11-12","img/expo-filtech2024.webp",
  "公司以 FUJIAN QL METAL FIBER 名义参展国际过滤行业专业展会，对接海外客户。"),
]
cards = "".join(f"""<article class="mcard rv" data-tag="{c}">
  <a href="news-detail.html" class="im"><img src="{img}" alt="{t}" loading="lazy"></a>
  <div class="bd"><div class="cat">{c} · <span class="num">{d}</span></div><h3>{t}</h3><p>{s}</p>
  <a class="more" href="news-detail.html">阅读全文<svg class="i"><use href="#i-arrow"/></svg></a></div>
</article>""" for c, t, d, img, s in NEWS)

w('news.html', head(
    "新闻动态 | 企业新闻 · 行业资讯 · 展会活动 — 强纶新材",
    "强纶新材企业新闻、行业资讯与展会活动：入围中国创新创业大赛全国赛、获评国家级专精特新“小巨人”、中国航发商发合格供应商、德国科隆 FILTECH 过滤展等。",
    "强纶新闻,强纶新材动态,金属纤维行业资讯,展会活动,FILTECH",
    "news.html", og_img="img/expo-filtech2024.webp")
 + header('news.html')
 + crumb([("新闻动态", None)])
 + page_hero("01", "NEWS", "新闻动态",
             "公司在做什么，<em>行业在发生什么</em>",
             "企业新闻、行业资讯与展会活动，由公司后台自主发布与维护。")
 + f"""<section class="sec"><div class="wrap">
  <nav class="pillbar" data-filter=".mcard" aria-label="新闻分类">
    <button class="on" data-v="all">全部</button><button data-v="企业新闻">企业新闻</button><button data-v="行业资讯">行业资讯</button><button data-v="展会活动">展会活动</button>
  </nav>
  <div class="g3">{cards}</div>
  <div class="note" style="margin-top:44px"><b>媒体报道</b>：公司相关报道见于龙岩市新罗区人民政府网、《闽西日报》、《海峡通讯》及龙岩高新区（经开区）等平台。</div>
</div></section>"""
 + ENDCTA + footer())

NEWS_SCHEMA = '{"@context":"https://schema.org","@type":"NewsArticle","headline":"创新驱动 装备向新｜强纶新材入围第十五届中国创新创业大赛新材料全国赛","datePublished":"2026-11-10","publisher":{"@type":"Organization","name":"福建强纶新材料股份有限公司"},"image":"%s/img/expo-forum2026.webp"}' % SITE
w('news-detail.html', head(
    "强纶新材入围第十五届中国创新创业大赛新材料全国赛 | 新闻动态",
    "公司以新材料方向项目入围第十五届中国创新创业大赛全国赛，是对强纶持续研发投入与成果转化能力的又一次认可。",
    "强纶新材,中国创新创业大赛,新材料全国赛,企业新闻",
    "news-detail.html", schema=NEWS_SCHEMA, og_img="img/expo-forum2026.webp")
 + header('news.html')
 + crumb([("新闻动态", "news.html"), ("企业新闻", "news.html"), ("入围中国创新创业大赛全国赛", None)])
 + """<article class="sec" style="padding-top:132px"><div class="wrap art-wrap">
  <div class="art-head rv">
    <div class="idx"><b>企业新闻</b>NEWS</div>
    <h1>创新驱动 装备向新｜强纶新材入围第十五届中国创新创业大赛新材料全国赛</h1>
    <div class="art-meta"><span class="num">2026-11-10</span><i>·</i><span>强纶新材</span></div>
  </div>
  <figure class="art-fig rv"><img src="img/expo-forum2026.webp" alt="强纶新材参加新材料技术论坛"><figcaption>公司技术团队参加新材料与技术论坛</figcaption></figure>
  <div class="prose art-body rv">
    <p class="lede">近日，第十五届中国创新创业大赛新材料行业赛结果公布，福建强纶新材料股份有限公司以新材料方向项目入围全国赛。</p>
    <p>强纶新材创立于 2002 年，是国内规模领先、福建省内唯一专注金属功能纤维及制品研发生产的高新技术企业，2025 年获评国家级专精特新“小巨人”企业。公司自主研发复合拉拔核心工艺，打通金属材料与纺织行业壁垒，牵头开辟“柔性金属纤维及其功能性纺织品”新兴赛道。</p>
    <p>近三年，公司研发投入占企业收入 12% 以上，累计授权专利 57 项，参与制修订国家标准 5 项、行业标准 1 项。依托强纶新材料创新研究院的六个研究室与五大制研平台，公司在滤材滤器、流体净化、电热材料、多孔材料、特种纺织五大方向持续攻关。</p>
    <p>公司表示，将以本次入围为契机，继续推进金属纤维关键材料的国产化与产业化，发展新质生产力，助力区域与行业高质量发展。</p>
  </div>
  <div class="art-foot rv">
    <nav class="art-nav"><a href="news.html">← 返回新闻动态</a><a href="about.html">了解强纶 →</a></nav>
  </div>
</div></article>"""
 + ENDCTA + footer())

# ════════ 人才招聘
JOBS = [
 ("材料研发工程师","研发中心 · 龙岩","全职","金属材料 / 材料加工工程相关专业，硕士及以上优先；负责超细金属纤维制备工艺与多孔材料性能研究。"),
 ("过滤应用工程师","技术中心 · 龙岩","全职","熟悉过滤分离原理与工况分析，负责客户选型支持、样品测试与现场试验。"),
 ("设备设计工程师","净化事业部 · 龙岩","全职","机械设计相关专业，负责收油系统与成套过滤设备的结构设计与工艺包编制。"),
 ("海外销售工程师","营销中心 · 龙岩","全职","英语可作为工作语言，负责阿里国际站与海外客户开发、展会对接。"),
 ("质量工程师","质量部 · 龙岩","全职","熟悉 ISO 9001 体系，负责来料、过程与出厂检验的标准执行与持续改进。"),
 ("纺织工艺技术员","柔银 / 纱线事业部 · 龙岩","全职","熟悉纺纱、编织或针织工艺，负责金属纤维纱线与织物的工艺调试。"),
]
job_rows = "".join(f'<a class="row-i" href="job-detail.html" data-tag="{d.split(" · ")[0]}"><span class="dt">{ty}</span><div><h4>{t}</h4><p>{s}</p></div><span class="tg">{d}</span></a>' for t, d, ty, s in JOBS)

w('jobs.html', head(
    "人才招聘 | 加入强纶新材",
    "强纶新材招聘材料研发工程师、过滤应用工程师、设备设计工程师、海外销售工程师、质量工程师等岗位，工作地福建龙岩。",
    "强纶招聘,金属纤维招聘,龙岩招聘,材料研发工程师,过滤应用工程师",
    "jobs.html", og_img="img/team-build2021.webp")
 + header('')
 + crumb([("人才招聘", None)])
 + page_hero("01", "CAREERS", "人才招聘",
             "在车间里做研发，<em>在工况里找答案</em>",
             "强纶新材料创新研究院不同于其他科研院所，“特”在研发源于车间实践、创新应用于航空航天等高端先进领域。我们需要愿意把材料做到产线上的人。",
             [("200","+","员工人数"),("12","%+","研发投入占收入"),("6","个","研究室"),("5","大","制研平台")],
             bg="img/team-build2021.webp")
 + f"""<section class="sec"><div class="wrap">
  <div class="sec-h row"><div><h2>在招岗位</h2><p>以下岗位长期开放，欢迎投递。</p></div>
    <a class="pill pill-line" href="mailto:hr@qlfiber.com">投递简历<svg class="i"><use href="#i-arrow"/></svg></a></div>
  <nav class="pillbar" data-filter=".row-i" aria-label="部门筛选">
    <button class="on" data-v="all">全部</button><button data-v="研发中心">研发中心</button><button data-v="技术中心">技术中心</button><button data-v="净化事业部">净化事业部</button><button data-v="营销中心">营销中心</button><button data-v="质量部">质量部</button>
  </nav>
  <div class="rows">{job_rows}</div>

  <div class="g3" style="margin-top:80px">
    <article class="card rv"><h3>为什么来强纶</h3><p>国家级专精特新“小巨人”，产品配套长征五号系列火箭与大型石化化纤企业，技术问题真实且有分量。</p></article>
    <article class="card rv d1"><h3>成长路径</h3><p>六个研究室与五大制研平台，设有省级企业技术中心与博士后创新实践基地，与厦门大学、同济大学等高校产学研协同。</p></article>
    <article class="card rv d2"><h3>员工关怀</h3><p>设立忠诚奖、优秀员工与优秀干部评选，各事业部定期组织团建与文体活动。</p></article>
  </div>

  <div class="note" style="margin-top:46px"><b>投递方式</b>：简历请发送至 <a href="mailto:hr@qlfiber.com" style="border-bottom:2px solid var(--gold)">hr@qlfiber.com</a>，或致电 0597-2799968 咨询。公司地址：福建省龙岩市龙岩经济技术开发区黄邦路 11 号。<br><small style="color:var(--muted)">* 岗位列表由公司后台自主发布与下架，以最新发布为准。</small></div>
</div></section>"""
 + ENDCTA + footer())

w('job-detail.html', head(
    "材料研发工程师 | 人才招聘 — 强纶新材",
    "强纶新材招聘材料研发工程师：负责超细金属纤维制备工艺与多孔材料性能研究，工作地福建龙岩，金属材料/材料加工工程相关专业。",
    "材料研发工程师招聘,金属纤维研发,龙岩招聘",
    "job-detail.html")
 + header('')
 + crumb([("人才招聘", "jobs.html"), ("材料研发工程师", None)])
 + """<section class="sec" style="padding-top:132px"><div class="wrap art-wrap">
  <div class="art-head rv">
    <div class="idx"><b>全职</b>研发中心 · 龙岩</div>
    <h1>材料研发工程师</h1>
    <div class="art-meta"><span>研发中心</span><i>·</i><span>福建省龙岩市</span><i>·</i><span>若干名</span></div>
  </div>
  <div class="prose art-body rv">
    <h3>岗位职责</h3>
    <ul>
      <li>参与超细金属纤维制备工艺研究，负责复合拉拔关键参数的试验与优化；</li>
      <li>开展金属微丝强韧化、多孔材料性能等方向的基础与应用研究；</li>
      <li>配合烧结成型、过滤元件等工序进行材料适配与失效分析；</li>
      <li>参与省市级科技项目申报、专利撰写与标准编制工作；</li>
      <li>与厦门大学、同济大学等合作院校对接产学研项目。</li>
    </ul>
    <h3>任职要求</h3>
    <ul>
      <li>金属材料、材料加工工程、冶金工程等相关专业，硕士及以上学历优先；</li>
      <li>熟悉金属材料显微组织分析与力学性能测试方法；</li>
      <li>有多孔材料、过滤材料或金属纤维相关研究经历者优先；</li>
      <li>具备良好的实验设计能力与文字表达能力，能独立撰写技术报告。</li>
    </ul>
    <h3>我们提供</h3>
    <ul>
      <li>省级企业技术中心、省级新型研发机构与博士后创新实践基地平台；</li>
      <li>研发投入占企业收入 12% 以上，项目资源充足；</li>
      <li>五险一金、带薪年假、节日福利、年度体检；</li>
      <li>技术通道与管理通道双轨晋升。</li>
    </ul>
  </div>
  <div class="art-foot rv">
    <div class="buyrow"><a class="pill pill-ink" href="mailto:hr@qlfiber.com">投递简历<svg class="i"><use href="#i-arrow"/></svg></a><a class="pill pill-line" href="tel:05972799968">0597-2799968</a></div>
    <nav class="art-nav"><a href="jobs.html">← 返回岗位列表</a><a href="culture.html">企业文化 →</a></nav>
  </div>
</div></section>"""
 + ENDCTA + footer())
print('新闻 / 招聘完成')
