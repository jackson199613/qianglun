# -*- coding: utf-8 -*-
"""新闻动态：列表 + 每条独立详情页；人才招聘 2 页"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from layout import head, header, crumb, page_hero, footer, SITE
from common import w, ENDCTA

# slug, 分类, 标题, 日期, 配图, 列表摘要, 来源, 正文段落
NEWS = [
 dict(slug="news-1", cat="企业新闻",
   title="创新驱动 装备向新｜强纶新材入围第十五届中国创新创业大赛新材料全国赛",
   date="2026-11-10", img="img/expo-booth-a57.webp", cap="强纶新材展台产品陈列",
   sum="公司以新材料方向项目入围全国赛，是对强纶持续研发投入与成果转化能力的又一次认可。",
   src="来源：公司官网", link="",
   body=["第十五届中国创新创业大赛新材料行业赛结果公布，福建强纶新材料股份有限公司入围全国赛。",
         "强纶新材创立于 2002 年，是国内规模领先、福建省内唯一专注金属功能纤维及制品研发生产的高新技术企业，2025 年获评国家级专精特新“小巨人”企业。公司自主研发复合拉拔核心工艺，打通金属材料与纺织行业壁垒，牵头开辟“柔性金属纤维及其功能性纺织品”新兴赛道。",
         "近三年，公司研发投入占企业收入 12% 以上，累计授权专利 57 项，参与制修订国家标准 5 项、行业标准 1 项。依托强纶新材料创新研究院的六个研究室与五大制研平台，公司在滤材滤器、流体净化、电热材料、多孔材料、特种纺织五大方向持续攻关。",
         "此前，公司还曾入围第十一届中国创新创业大赛全国赛，并获 2022 年第十一届中国创新创业大赛（福建赛区）暨第十届福建创新创业大赛优胜奖。"]),
 dict(slug="news-2", cat="企业新闻",
   title="从“省内唯一”到“国家级认可”，强纶新材再获殊荣",
   date="2026-10-29", img="img/plant-02.webp", cap="强纶新材生产车间",
   sum="作为福建省内唯一专注金属功能纤维及制品研发生产的企业，公司获评国家级专精特新“小巨人”。",
   src="来源：公司官网", link="",
   body=["福建强纶新材料股份有限公司获评国家级专精特新“小巨人”企业。公司此前已于 2023 年获评福建省专精特新中小企业（第一批）。",
         "公司是国内规模领先、福建省内唯一专注金属功能纤维及制品研发生产的高新技术企业，同时持有国家高新技术企业、国家知识产权优势企业等资质，并建有省级新型研发机构、省级企业技术中心与省级博士后创新实践基地。",
         "在产品层面，公司金属纱线在电热面料领域市占率全国第一，金属烧结毡稳居黏胶行业国内首位；自研针刺毡已成功应用于长征五号 B、长征五号遥五运载火箭发动机，国产化熔体滤芯批量供应国内大型石化、化纤龙头企业。"]),
 dict(slug="news-3", cat="企业新闻",
   title="喜讯｜福建强纶新材料股份有限公司获评中国航发商发合格供应商",
   date="2026-06-18", img="img/media-09.webp", cap="金属纤维烧结滤芯产品",
   sum="公司通过航发商发供应商审核，进一步巩固在航空航天特种材料领域的配套能力。",
   src="来源：公司官网", link="",
   body=["福建强纶新材料股份有限公司通过中国航发商用航空发动机有限责任公司供应商审核，获评合格供应商。",
         "航空航天领域对材料的耐温、耐腐蚀与批次一致性要求极高。公司作为国内最早配套航天工程的金属纤维毡供应商，已建立覆盖来料检验、过程控制、出厂检验的完整质量控制流程，并通过 ISO 9001 质量管理体系认证，认证范围覆盖金属纤维及金属线、耐高温金属膜滤料、多层金属烧结网、金属过滤元件产品的设计、生产和售后服务。",
         "公司在该领域的产品包括金属纤维烧结毡、针刺毡以及燃油过滤、液压系统过滤等元件。"]),
 dict(slug="news-4", cat="行业资讯",
   title="龙岩高新区厚植企业创新沃土，推动行业标准体系建设实现多点突破",
   date="2026-07-14", img="img/media-03.webp", cap="金属纤维烧结毡",
   sum="《闽西日报》报道龙岩高新区（经开区）以科创赋能产业能级跃升，强纶作为国家标准起草单位参与其中。",
   src="来源：《闽西日报》2026 年 07 月 14 日", link="",
   body=["《闽西日报》报道龙岩高新区（经开区）厚植企业创新沃土、推动行业标准体系建设实现多点突破、全域覆盖，以科创赋能产业能级跃升。",
         "强纶新材是全国颗粒表征与分检及筛网标准化技术委员会委员单位、第八届全国分离机械标准化技术委员单位，累计参与制修订国家标准 5 项、行业标准 1 项：GB/T 20100—2016《不锈钢纤维烧结滤毡》、GB/T 17492—2019《工业用金属丝编织网 技术要求和检验》、GB/T 21648—2023《金属丝编织密纹网》、GB/T 45969—2025《颗粒表征 术语》、GB/T 5330—2025《工业用金属丝编织方孔筛网》，以及行业标准 JB/T 13511—2018。",
         "上述标准的主要起草人均包含公司董事长兼总工黄朝强。"]),
 dict(slug="news-5", cat="行业资讯",
   title="产品有活力 工业动能足——龙岩优质工业品调查报道",
   date="2026-08-27", img="img/plant-05.webp", cap="强纶新材机加工车间",
   sum="《闽西日报》走访龙岩优质工业品企业，报道强纶金属纤维产品的市场表现。",
   src="来源：《闽西日报》2026 年 08 月 27 日", link="",
   body=["《闽西日报》开展龙岩优质工业品调查报道，走访本地具有代表性的制造企业。",
         "强纶新材主营金属纤维及其制品，现已形成金属纤维、烧结滤材、金属纱线、编织物、电热服饰等系列产品，兼具导电、耐火、柔性、防切割、减震等性能，广泛服务于航空航天、石油化工、化纤冶金、能源交通等领域。",
         "公司现有员工 200 余人，自有工业用地 40 余亩，产品覆盖化纤、石油化工、玻璃制造、节能环保、新能源与航空航天等行业。"]),
 dict(slug="news-6", cat="行业资讯",
   title="最新一期《海峡通讯》报道：聚焦龙岩专精特新企业发展",
   date="2026-06-30", img="img/lab-01.webp", cap="强纶新材料与应用实验室",
   sum="《海峡通讯》聚焦龙岩专精特新企业发展，强纶新材作为代表企业之一接受报道。",
   src="来源：《海峡通讯》", link="",
   body=["《海峡通讯》刊发专题报道，聚焦龙岩专精特新企业的发展情况。",
         "强纶新材依托强纶新材料创新研究院开展研发，研究院设有流体净化、氢能源、金属橡胶、电化学、金属学、多孔介质燃烧六个研究室，并整合金属复合丝拉拔、压制烧结、纺纱编织、电化学材料加工、精密机械加工五大制研平台。",
         "公司与厦门大学、同济大学、龙岩学院、闽江学院、安徽理工大学等院校及科研院所开展产学研合作，建有省级博士后创新实践基地与研究生专业实践基地。"]),
 dict(slug="news-7", cat="展会活动",
   title="第十四届全国湿法冶金工程技术交流会",
   date="2026-05-20", img="img/expo-hydromet14.webp", cap="第十四届全国湿法冶金工程技术交流会现场",
   sum="强纶收油系统在湿法冶金行业的应用成果受到与会企业关注。",
   src="来源：公司参展记录", link="",
   body=["公司参加第十四届全国湿法冶金工程技术交流会，展示面向镍钴湿法冶金与化工萃取工艺的强纶收油系统（FTS 功能纤维除油系统）。",
         "强纶收油系统以表面改性的亲油疏水金属纤维为聚结材料，通过“前置过滤器 + 油水分离器”实现油水分离。系统采用纯物理方式除油，不添加破乳药剂，不产生化学污泥，分离出的油份可回收复用。",
         "目前公司已为广东芳源、福建常青、衢州华友、江西铜业、格林美、湖南邦普、河南荣佳钪钒等 20 余家新能源与有色冶炼企业提供收油系统及过滤服务，最大单套处理量达 600 m³/h。"]),
 dict(slug="news-8", cat="展会活动",
   title="2024 年德国科隆过滤展 FILTECH",
   date="2024-11-12", img="img/expo-filtech2024.webp", cap="FUJIAN QL METAL FIBER 参展德国科隆 FILTECH",
   sum="公司以 FUJIAN QL METAL FIBER 名义参展国际过滤行业专业展会，对接海外客户。",
   src="来源：公司参展记录", link="",
   body=["公司参加 2024 年德国科隆 FILTECH 过滤展，以 FUJIAN QL METAL FIBER CO., LTD 名义设展，面向国际客户展示金属纤维烧结毡、烧结滤芯与过滤元件产品。",
         "FILTECH 是过滤与分离领域的国际专业展会。公司产品可广泛应用于化工与石油化工、聚合物、合成纤维、冶金、流化、药品、食品饮料、高温空气/气体过滤、水过滤、航空与汽车等行业。",
         "海外客户亦可通过公司阿里国际站了解产品并建立联系。"]),
]

# ───────── 列表页
cards = "".join(f"""<article class="mcard rv" data-tag="{n['cat']}">
  <a href="{n['slug']}.html" class="im"><img src="{n['img']}" alt="{n['title']}" loading="lazy"></a>
  <div class="bd"><div class="cat">{n['cat']} · <span class="num">{n['date']}</span></div><h3>{n['title']}</h3><p>{n['sum']}</p>
  <a class="more" href="{n['slug']}.html">阅读全文<svg class="i"><use href="#i-arrow"/></svg></a></div>
</article>""" for n in NEWS)

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
  <div class="sec-h" style="margin:80px 0 24px"><h2>展会与交流</h2><p>公司每年参加国内外过滤分离、湿法冶金与新材料领域的专业展会与技术交流活动。</p></div>
  <div class="gal c3">
    <figure><img src="img/expo-filtech2024.webp" alt="2024 年德国科隆 FILTECH 过滤展" loading="lazy"><figcaption>FILTECH 科隆 · 2024</figcaption></figure>
    <figure><img src="img/expo-hydromet14.webp" alt="第十四届全国湿法冶金工程技术交流会" loading="lazy"><figcaption>全国湿法冶金交流会</figcaption></figure>
    <figure><img src="img/expo-booth-a57.webp" alt="强纶新材展台产品陈列" loading="lazy"><figcaption>展台产品陈列</figcaption></figure>
    <figure><img src="img/expo-booth-brand.webp" alt="福建品牌展区强纶展位" loading="lazy"><figcaption>福建品牌展区</figcaption></figure>
    <figure><img src="img/expo-forum2026.webp" alt="新材料与技术论坛交流现场" loading="lazy"><figcaption>新材料技术论坛</figcaption></figure>
    <figure><img src="img/expo-booth-fair.webp" alt="国际展会强纶展位" loading="lazy"><figcaption>国际展会展位</figcaption></figure>
  </div>

  <div class="note" style="margin-top:44px"><b>媒体报道</b>：公司相关报道见于龙岩市新罗区人民政府网、《闽西日报》、《海峡通讯》及龙岩高新区（经开区）等平台。</div>
</div></section>"""
 + ENDCTA + footer())

# ───────── 每条独立详情页
for i, n in enumerate(NEWS):
    prev_n = NEWS[i-1] if i > 0 else None
    next_n = NEWS[i+1] if i < len(NEWS)-1 else None
    nav = '<nav class="art-nav">'
    nav += f'<a href="{prev_n["slug"]}.html">← {prev_n["title"][:22]}…</a>' if prev_n else '<a href="news.html">← 返回新闻动态</a>'
    nav += f'<a href="{next_n["slug"]}.html">{next_n["title"][:22]}… →</a>' if next_n else '<a href="news.html">返回新闻动态 →</a>'
    nav += '</nav>'
    paras = "".join(f'<p{" class=\"lede\"" if k==0 else ""}>{t}</p>' for k, t in enumerate(n['body']))
    sc = ('{"@context":"https://schema.org","@type":"NewsArticle","headline":"%s","datePublished":"%s",'
          '"publisher":{"@type":"Organization","name":"福建强纶新材料股份有限公司"},"image":"%s/%s","mainEntityOfPage":"%s/%s.html"}'
          % (n['title'].replace('"', "'"), n['date'], SITE, n['img'], SITE, n['slug']))
    w(f"{n['slug']}.html", head(
        f"{n['title']} | 新闻动态 — 强纶新材",
        n['sum'],
        f"强纶新材,{n['cat']},{n['title'][:14]}",
        f"{n['slug']}.html", schema=sc, og_img=n['img'])
     + header('news.html')
     + crumb([("新闻动态", "news.html"), (n['cat'], "news.html"), (n['title'][:16] + ("…" if len(n['title']) > 16 else ""), None)])
     + f"""<article class="sec" style="padding-top:132px"><div class="wrap art-wrap">
  <div class="art-head rv">
    <div class="idx"><b>{n['cat']}</b>NEWS</div>
    <h1>{n['title']}</h1>
    <div class="art-meta"><span class="num">{n['date']}</span><i>·</i><span>{n['src']}</span></div>
  </div>
  <figure class="art-fig rv"><img src="{n['img']}" alt="{n['cap']}"><figcaption>{n['cap']}</figcaption></figure>
  <div class="prose art-body rv">{paras}</div>
  <div class="art-foot rv">
    <div class="buyrow"><a class="pill pill-ink" href="about.html">了解强纶<svg class="i"><use href="#i-arrow"/></svg></a><a class="pill pill-line" href="contact.html#inq">联系我们</a></div>
    {nav}
  </div>
</div></article>"""
     + ENDCTA + footer())

# ───────── 人才招聘
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
print(f'新闻 {len(NEWS)} 条独立详情页 + 招聘完成')
