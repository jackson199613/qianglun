# -*- coding: utf-8 -*-
"""文章/问答详情模板、新闻、人才招聘"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from layout import head, header, crumb, page_hero, footer, SITE
from common import w, ENDCTA

QA_SCHEMA = '{"@context":"https://schema.org","@type":"QAPage","mainEntity":{"@type":"Question","name":"金属纤维滤芯能清洗再用吗？","acceptedAnswer":{"@type":"Answer","text":"可以。金属纤维烧结滤材耐高温、耐腐蚀，可反复清洗再生。"}}}'


w('qa.html', head(
    "金属纤维滤芯能清洗再用吗？| 常见问题 — 强纶新材",
    "可以。金属纤维烧结滤材耐高温耐腐蚀，可反复清洗再生；本页说明清洗方式、再生次数的影响因素与判断更换的依据。",
    "金属纤维滤芯清洗,滤芯再生,烧结滤材清洗,反洗",
    "qa.html", schema=QA_SCHEMA)
 + header('insights.html')
 + crumb([("技术专栏", "insights.html"), ("常见问题库", "faq.html"), ("滤芯能否清洗再用", None)])
 + """<article class="sec" style="padding-top:132px"><div class="wrap art-wrap">
  <div class="art-head rv">
    <div class="idx"><b>滤芯</b>Q&amp;A</div>
    <h1>金属纤维滤芯能清洗再用吗？</h1>
    <div class="art-meta"><span>常见问题库</span><i>·</i><span>强纶技术团队</span></div>
  </div>
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
