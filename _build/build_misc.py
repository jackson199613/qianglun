# -*- coding: utf-8 -*-
"""文章/问答详情模板、新闻、人才招聘"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from layout import head, header, crumb, page_hero, footer, SITE
from common import w, ENDCTA

ART_SCHEMA = '{"@context":"https://schema.org","@type":"TechArticle","headline":"烧结毡和滤布到底怎么选？四个判断条件","datePublished":"2026-10-28","author":{"@type":"Organization","name":"福建强纶新材料股份有限公司"},"publisher":{"@type":"Organization","name":"福建强纶新材料股份有限公司","logo":{"@type":"ImageObject","url":"https://www.qlfiber.com/assets/images/logo.png"}},"image":"%s/img/media-05.webp"}' % SITE

w('article.html', head(
    "烧结毡和滤布到底怎么选？四个判断条件 | 技术专栏 — 强纶新材",
    "从介质温度、腐蚀性、精度要求与再生需求四个维度，给出金属纤维烧结毡与常规滤布的分界线，并附选型速查表。",
    "烧结毡和滤布,滤材选择,金属纤维烧结毡,过滤选型",
    "article.html", schema=ART_SCHEMA, og_img="img/media-05.webp")
 + header('insights.html')
 + crumb([("技术专栏", "insights.html"), ("技术文章", "insights.html"), ("烧结毡和滤布怎么选", None)])
 + """<article class="sec" style="padding-top:132px"><div class="wrap art-wrap">
  <header class="art-head rv">
    <div class="idx"><b>选型</b>TECHNICAL ARTICLE</div>
    <h1>烧结毡和滤布到底怎么选？四个判断条件</h1>
    <div class="art-meta"><span class="num">2026-10-28</span><i>·</i><span>强纶技术团队</span><i>·</i><span>约 6 分钟</span></div>
  </header>
  <figure class="art-fig rv"><img src="img/media-05.webp" alt="金属纤维烧结毡"><figcaption>金属纤维烧结毡：多层梯度孔结构</figcaption></figure>
  <div class="prose art-body rv">
    <p class="lede">这是询盘里最常见的一个问题。答案并不是「烧结毡一定更好」，而是取决于四件事：介质温度、腐蚀性、精度要求，以及你是否需要清洗再生。</p>
    <h3>一、先看温度</h3>
    <p>这是最硬的一条分界线。常规滤纸、滤布在 120–150℃ 以上就会软化、变形甚至碳化；而金属纤维烧结毡可在 <strong>480℃</strong> 环境介质中长期使用，超过这个温度则需改用铁铬铝等耐热合金纤维。</p>
    <p>所以：<strong>工况温度超过 150℃，基本就不用再考虑滤布了。</strong></p>
    <h3>二、再看腐蚀性</h3>
    <p>金属纤维烧结毡以 316L 不锈钢为主，耐酸碱、有机溶剂与药物腐蚀；需要更强耐蚀时可选镍、钛、哈氏合金、蒙乃尔或双相合金。滤布在强溶剂与高温酸碱环境下寿命很难保证。</p>
    <h3>三、精度与纳污量要一起看</h3>
    <p>很多人只盯着精度数字，忽略了纳污量。金属纤维烧结毡的多层梯度孔结构由粗到细逐层拦截，<strong>在相同精度下纳污量远大于单层结构</strong>，表现为升压慢、更换周期长。</p>
    <p>强纶烧结毡的绝对过滤等级覆盖 10–60μm，常用档位见<a href="specs.html">参数对照表</a>。如果下游对杂质要求极严，再结合气泡点压判断最大孔径。</p>
    <h3>四、要不要清洗再生</h3>
    <p>这是成本账。滤布基本是一次性耗材；金属纤维烧结毡耐高温耐腐蚀，<strong>可反复清洗再生</strong>，在换网频繁的工况下总持有成本反而更低。</p>
    <h3>一张速查表</h3>
  </div>
  <div class="tbl-wrap rv"><table class="tbl">
    <thead><tr><th>判断条件</th><th>选金属纤维烧结毡</th><th>可考虑滤布</th></tr></thead>
    <tbody>
      <tr><td>工况温度</td><td>&gt; 150℃，直至 480℃</td><td>≤ 120℃</td></tr>
      <tr><td>腐蚀性</td><td>酸碱、有机溶剂、高温介质</td><td>中性、常温水系</td></tr>
      <tr><td>精度与纳污</td><td>要求升压慢、换网周期长</td><td>精度要求低、更换频率可接受</td></tr>
      <tr><td>再生需求</td><td>需要反复清洗再生</td><td>一次性使用即可</td></tr>
      <tr><td>压力</td><td>中高压、需机械强度</td><td>低压</td></tr>
    </tbody>
  </table></div>
  <div class="prose art-body rv">
    <h3>还是不确定怎么办</h3>
    <p>把介质、温度、压力与精度四个参数提供给我们，用<a href="selector.html">选型指南</a>先得到初步方向，再由工程师复核给出正式选型表。工况复杂的项目可以先做样品测试，用实测数据定型。</p>
  </div>
  <div class="art-foot rv">
    <div class="buyrow"><a class="pill pill-ink" href="selector.html">按工况选型<svg class="i"><use href="#i-arrow"/></svg></a><a class="pill pill-line" href="contact.html#inq">咨询工程师</a></div>
    <nav class="art-nav"><a href="insights.html">← 返回技术专栏</a><a href="faq.html">常见问题库 →</a></nav>
  </div>
</div></article>"""
 + ENDCTA + footer())

QA_SCHEMA = '{"@context":"https://schema.org","@type":"QAPage","mainEntity":{"@type":"Question","name":"金属纤维滤芯能清洗再用吗？","acceptedAnswer":{"@type":"Answer","text":"可以。金属纤维烧结滤材耐高温、耐腐蚀，可反复清洗再生。"}}}'
w('qa.html', head(
    "金属纤维滤芯能清洗再用吗？| 常见问题 — 强纶新材",
    "可以。金属纤维烧结滤材耐高温耐腐蚀，可反复清洗再生；本页说明清洗方式、再生次数的影响因素与判断更换的依据。",
    "金属纤维滤芯清洗,滤芯再生,烧结滤材清洗,反洗",
    "qa.html", schema=QA_SCHEMA)
 + header('insights.html')
 + crumb([("技术专栏", "insights.html"), ("常见问题库", "faq.html"), ("滤芯能否清洗再用", None)])
 + """<article class="sec" style="padding-top:132px"><div class="wrap art-wrap">
  <header class="art-head rv">
    <div class="idx"><b>滤芯</b>Q&amp;A</div>
    <h1>金属纤维滤芯能清洗再用吗？</h1>
    <div class="art-meta"><span>常见问题库</span><i>·</i><span>强纶技术团队</span></div>
  </header>
  <div class="qa-answer rv"><b>可以。</b>金属纤维烧结滤材耐高温、耐腐蚀，可反复清洗再生，这正是它相对滤纸滤布的核心优势之一。</div>
  <div class="prose art-body rv">
    <h3>为什么能再生</h3>
    <p>金属纤维经高温烧结后，纤维交点扩散结合形成整体刚性结构，具备机械强度与尺寸稳定性。清洗时孔隙结构不会像滤纸那样溃散，也不会像金属丝网那样因反复受力而破损。</p>
    <h3>常见清洗方式</h3>
    <ul>
      <li><strong>反冲洗</strong>：在线反向通液/通气，适合污物以表面截留为主的工况；</li>
      <li><strong>超声清洗</strong>：配合清洗液去除深层嵌入的颗粒；</li>
      <li><strong>化学清洗</strong>：针对油污、聚合物残留，按介质选择溶剂或碱洗；</li>
      <li><strong>高温焙烧</strong>：用于聚合物熔体工况，烧除有机残留后再做清洗。</li>
    </ul>
    <h3>能洗多少次</h3>
    <p>没有固定次数。实际再生次数取决于污物性质、嵌入深度与清洗工艺是否得当。判断依据不是次数，而是<strong>清洗后的压差恢复程度</strong>：若清洗后初始压差已明显高于新件且继续上升过快，说明深层孔隙已不可逆堵塞，应考虑更换。</p>
    <h3>怎么判断该换了</h3>
    <ul>
      <li>清洗后初始压差持续走高，恢复不到可接受水平；</li>
      <li>出现下游杂质超标，提示滤材可能已穿透或密封失效；</li>
      <li>外观出现变形、焊缝开裂或明显腐蚀。</li>
    </ul>
  </div>
  <div class="art-foot rv">
    <div class="buyrow"><a class="pill pill-ink" href="p-element.html">查看过滤元器件<svg class="i"><use href="#i-arrow"/></svg></a><a class="pill pill-line" href="contact.html#inq">咨询清洗方案</a></div>
    <nav class="art-nav"><a href="faq.html">← 返回常见问题库</a><a href="insights.html">技术专栏 →</a></nav>
  </div>
</div></article>"""
 + ENDCTA + footer())
print('文章 / 问答模板完成')
