# -*- coding: utf-8 -*-
"""新闻动态：列表 + 每条独立详情页；人才招聘 2 页"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from layout import head, header, crumb, page_hero, footer, SITE
from common import w, ENDCTA

from news_data import NEWS  # 数据见 news_data.py：以甲方《新闻原链接》表格为准

# ───────── 列表页
cards = "".join(f"""<article class="mcard rv" data-tag="{n['cat']}">
  <a href="{n['slug']}.html" class="im"><img src="{n['img']}" alt="{n['title']}" loading="lazy"></a>
  <div class="bd"><div class="cat">{n['cat']} · <span class="num">{n['date']}</span></div><h3>{n['title']}</h3><p>{n['sum']}</p>
  <a class="more" href="{n['slug']}.html">阅读全文<svg class="i"><use href="#i-arrow"/></svg></a></div>
</article>""" for n in NEWS)

w('news.html', head(
    "新闻动态 | 企业新闻 · 展会活动 · 媒体报道 — 强纶新材",
    "强纶新材企业新闻、展会活动与媒体报道：入围第十五届中国创新创业大赛新材料全国赛、获评国家知识产权示范企业创建对象、中国航发商发合格供应商、FTS-CL600 获省级首台（套）认定等。",
    "强纶新闻,强纶新材动态,展会活动,媒体报道,专精特新小巨人",
    "news.html", og_img=NEWS[0]['img'])
 + header('news.html')
 + crumb([("新闻动态", None)])
 + page_hero("01", "NEWS", "新闻动态",
             "公司在做什么，<em>行业在发生什么</em>",
             "企业新闻、展会活动与媒体报道，内容与配图均取自强纶新材公众号原文。")
 + f"""<section class="sec"><div class="wrap">
  <nav class="pillbar" data-filter=".mcard" aria-label="新闻分类">
    <button class="on" data-v="all">全部</button><button data-v="企业新闻">企业新闻</button><button data-v="展会活动">展会活动</button><button data-v="媒体报道">媒体报道</button>
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

  <div class="note" style="margin-top:44px"><b>媒体报道</b>：公司相关报道见于《科技日报》、《闽西日报》、龙岩发布（龙岩市融媒体中心）等媒体与平台。</div>
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
    paras = "".join(f'<h3>{t[2:]}</h3>' if t.startswith("##") else f'<p{" class=\"lede\"" if k==0 else ""}>{t}</p>'
                    for k, t in enumerate(n['body']))
    if n.get('gal'):
        g = n['gal']
        paras += (f'<div class="gal c3" style="margin-top:36px">' if len(g) >= 3 else
                  f'<div class="gal" style="margin-top:36px;grid-template-columns:repeat({len(g)},1fr)">') + "".join(
            f'<figure><img src="{u}" alt="{c or n["title"]}" loading="lazy">' + (f'<figcaption>{c}</figcaption>' if c else '') + '</figure>'
            for u, c in n['gal']) + '</div>'
    src_html = n['src'] + (f'<i>·</i><a class="tlink" href="{n["link"]}" target="_blank" rel="noopener">查看原文</a>' if n.get('link') else '')
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
    <div class="art-meta"><span class="num">{n['date']}</span><i>·</i><span>{src_html}</span></div>
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
 ("过滤应用工程师","技术中心 · 龙岩","全职","熟悉过滤分离原理与应用场景分析，负责客户选型支持、样品测试与现场试验。"),
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
             "在车间里做研发，<em>在应用场景里找答案</em>",
             "强纶新材料创新研究院不同于其他科研院所，“特”在研发源于车间实践、创新应用于航空航天等高端先进领域。我们需要愿意把材料做到产线上的人。",
             [("200","+","员工人数"),("12","%+","研发投入占收入"),("6","个","研究室"),("5","大","制研平台")], bg="img/en-ph-manufacturing.webp")
 + f"""<section class="sec"><div class="wrap">
  <div class="sec-h row"><div><h2>在招岗位</h2><p>以下岗位长期开放，欢迎投递。</p></div>
    <a class="pill pill-line" href="mailto:hcq@jl-jiber.com">投递简历<svg class="i"><use href="#i-arrow"/></svg></a></div>
  <nav class="pillbar" data-filter=".row-i" aria-label="部门筛选">
    <button class="on" data-v="all">全部</button><button data-v="研发中心">研发中心</button><button data-v="技术中心">技术中心</button><button data-v="净化事业部">净化事业部</button><button data-v="营销中心">营销中心</button><button data-v="质量部">质量部</button>
  </nav>
  <div class="rows">{job_rows}</div>

  <div class="g3" style="margin-top:80px">
    <article class="card rv"><h3>为什么来强纶</h3><p>国家级专精特新“小巨人”，产品服务航空航天领域与大型石化化纤企业，技术问题真实且有分量。</p></article>
    <article class="card rv d1"><h3>成长路径</h3><p>六个研究室与五大制研平台，设有省级企业技术中心与博士后创新实践基地，与厦门大学、同济大学等高校产学研协同。</p></article>
    <article class="card rv d2"><h3>员工关怀</h3><p>设立忠诚奖、优秀员工与优秀干部评选，各事业部定期组织团建与文体活动。</p></article>
  </div>

  <div class="note" style="margin-top:46px"><b>投递方式</b>：简历请发送至 <a href="mailto:hcq@jl-jiber.com" style="border-bottom:2px solid var(--gold)">hcq@jl-jiber.com</a>，或致电 0597-2799968 咨询。公司地址：福建省龙岩市东肖镇经济技术开发区黄邦路 11 号。<br><small style="color:var(--muted)">* 岗位列表由公司后台自主发布与下架，以当前发布为准。</small></div>
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
    <div class="buyrow"><a class="pill pill-ink" href="mailto:hcq@jl-jiber.com">投递简历<svg class="i"><use href="#i-arrow"/></svg></a><a class="pill pill-line" href="tel:05972799968">0597-2799968</a></div>
    <nav class="art-nav"><a href="jobs.html">← 返回岗位列表</a><a href="culture.html">企业文化 →</a></nav>
  </div>
</div></section>"""
 + ENDCTA + footer())
print(f'新闻 {len(NEWS)} 条独立详情页 + 招聘完成')
