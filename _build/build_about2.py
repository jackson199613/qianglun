# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from layout import head, header, crumb, page_hero, footer
from common import w, anav, ENDCTA

# ───────────────────────────── 4. 质量体系
w('quality.html', head(
    "质量体系 | 强纶新材",
    "通过 GB/T 19001-2016 / ISO 9001:2015 质量管理体系认证（证书号 00224Q21982R1M），覆盖金属纤维及金属线、耐高温金属膜滤料、多层金属烧结网、金属过滤元件的设计、生产和售后服务。",
    "强纶质量体系,ISO9001,质量管理体系认证,检验流程,质量控制",
    "quality.html", og_img="img/cert-iso9001.webp")
 + header('about.html')
 + crumb([("关于强纶", "about.html"), ("质量体系", None)])
 + page_hero("04", "QUALITY", "质量体系",
             "过滤产品的质量，<em>最终体现在客户的产线上</em>",
             "公司已建立覆盖来料检验、过程控制、出厂检验的完整质量控制流程，并通过 ISO 9001 质量管理体系认证；同时建立环境、职业健康安全管理体系，形成三体系运行。")
 + f"""<section class="sec"><div class="wrap">{anav(3)}
  <div class="g2 wide">
    <div class="prose rv">
      <h3 style="margin-top:0">三道检验关口</h3>
      <p><strong>来料检验</strong>：原材料入厂按牌号、丝径、化学成分与力学性能抽检，合金材质留样备查。</p>
      <p><strong>过程控制</strong>：拉拔、成条、铺网、烧结、折波、焊接等关键工序设置控制点，按《产品监视与测量控制程序》（QL-CP-25-D1）执行，工序记录可追溯。</p>
      <p><strong>出厂检验</strong>：按型号逐项检测过滤精度、气泡点压力、透气值、厚度与外观；过滤元件另做压力与密封试验。检验合格后出具检验报告随货交付。</p>
      <h3>可出具的检测项目</h3>
      <p>绝对过滤等级、过滤效率、孔隙率、第一起泡压强与平均起泡压强、透气度（200Pa）、厚度、面密度等；另可按订单约定提供 ROHS 等第三方检测报告。</p>
      <div class="note" style="margin-top:28px"><b>追溯</b>：每批产品对应独立批次号，工艺参数、检验数据与出厂报告一一对应，便于客户在产线异常时快速定位。</div>
    </div>
    <div class="rv d1">
      <h3 style="font-family:'Noto Serif SC',serif;font-size:21px;font-weight:700;margin-bottom:20px">管理体系认证</h3>
      <div class="certs" style="grid-template-columns:1fr 1fr">
        <figure><img src="img/cert-iso9001.webp" alt="质量管理体系认证证书" loading="lazy"><figcaption>ISO 9001 质量管理体系<br><small style="color:var(--muted)">证书号 00224Q21982R1M<br>有效期至 2027.04.11</small></figcaption></figure>
        <figure><img src="img/cert-iso14001.webp" alt="环境管理体系认证证书" loading="lazy"><figcaption>环境管理体系认证</figcaption></figure>
        <figure><img src="img/cert-iso45001.webp" alt="职业健康安全管理体系认证证书" loading="lazy"><figcaption>职业健康安全管理体系</figcaption></figure>
      </div>
      <p class="tnote">认证范围：金属纤维及金属线、耐高温金属膜滤料、多层金属烧结网、金属过滤元件（滤芯、过滤器）产品的设计、生产和售后服务。</p>
    </div>
  </div>

  <div class="sec-h" style="margin:92px 0 32px"><h2>参与制修订的<em>国家与行业标准</em></h2><p>公司是全国颗粒表征与分检及筛网标准化技术委员会委员单位，主要起草人均含公司董事长兼总工黄朝强。</p></div>
  <div class="tbl-wrap"><table class="tbl">
    <thead><tr><th>标准编号</th><th>标准名称</th><th>类型</th><th>状态</th><th>公开时间</th></tr></thead>
    <tbody>
      <tr><td class="num">GB/T 20100—2016</td><td>不锈钢纤维烧结滤毡</td><td>国家标准</td><td>现行有效</td><td class="num">2016-02-24</td></tr>
      <tr><td class="num">GB/T 17492—2019</td><td>工业用金属丝编织网 技术要求和检验</td><td>国家标准</td><td>现行有效</td><td class="num">2019-12-10</td></tr>
      <tr><td class="num">GB/T 21648—2023</td><td>金属丝编织密纹网</td><td>国家标准</td><td>现行有效</td><td class="num">2023-09-07</td></tr>
      <tr><td class="num">GB/T 45969—2025</td><td>颗粒表征 术语</td><td>国家标准</td><td>现行有效</td><td class="num">2025-08-01</td></tr>
      <tr><td class="num">GB/T 5330—2025</td><td>工业用金属丝编织方孔筛网</td><td>国家标准</td><td>现行有效</td><td class="num">2025-10-31</td></tr>
      <tr><td class="num">JB/T 13511—2018</td><td>分离机械用柔性非织造过滤介质过滤性能测试方法</td><td>行业标准</td><td>现行有效</td><td class="num">2018-04-30</td></tr>
    </tbody>
  </table></div>
  <p class="tnote">合计参与制修订国家标准 5 项、行业标准 1 项。完整专利与标准清单见<a href="patents.html" style="border-bottom:2px solid var(--gold)">专利与标准</a>。</p>
</div></section>"""
 + ENDCTA + footer())

# ───────────────────────────── 5. 资质荣誉
HON = {
 "国家级": ["国家级专精特新“小巨人”企业","国家高新技术企业","国家知识产权优势企业",
            "全国过滤与分离产业技术创新常务理事单位（2016—2020）","第八届全国分离机械标准化技术委员单位（2021—2026.8）",
            "第五届全国颗粒表征与分检及筛网标准化技术委员会先进集体单位","第六届全国颗粒表征与分检及筛网标准化技术委员会委员单位（2019—2024）",
            "入围第十一届中国创新创业大赛全国赛"],
 "省级": ["福建省科技型企业证书（2018—2022）","福建省科技小巨人领军企业证书（2018—2020）","福建省第五批省级新型研发机构",
          "福建省知识产权优势企业","省高新技术企业证书（2024—2027）","2022 年省级企业技术中心","省级博士后创新实践基地",
          "2023 年省专精特新中小企业（第一批）","2022 年福建省百万职工“五小”创新大赛一等奖","2019 年福建省百万职工“五小”创新大赛三等奖",
          "2022 年第十一届中国创新创业大赛（福建赛区）暨第十届福建创新创业大赛优胜奖","第一批省“创业之星”人才"],
 "市级": ["龙岩市军民融合企业","龙岩市科技小巨人领军企业","2019 年市级工业设计中心","市级企业技术中心","龙岩市专利奖三等奖",
          "第八届龙岩市科技创新创业大赛三等奖","龙岩市军民融合发展第二届监事会监事长单位","龙岩市军民两用重点企业",
          "龙岩市军民两用协同创新中心","市科技创新人才飞地","2016—2017 年度龙岩市守合同重信企业","2018—2019 年度龙岩市守合同重信企业",
          "2025 年度龙岩市第一批“产业银发人才”","2025 年龙岩市企业创新英才"],
 "区级": ["2017 年度区潜力成长企业","2018 年度“重点税源企业”称号","先进基层党组织"],
}
hon_html = ""
for lv, items in HON.items():
    lis = "".join(f'<div class="row-i" data-tag="{lv}"><span class="dt">{lv}</span><h4>{t}</h4><span class="tg">{lv}</span></div>' for t in items)
    hon_html += f'<div class="rv"><h3 style="font-family:\'Noto Serif SC\',serif;font-size:22px;font-weight:700;margin:52px 0 6px">{lv} <span style="font-family:\'Barlow Condensed\',sans-serif;color:var(--champ);font-size:18px">{len(items)}</span></h3><div class="rows">{lis}</div></div>'

w('honors.html', head(
    "资质荣誉 | 强纶新材",
    "国家级专精特新“小巨人”、国家高新技术企业、国家知识产权优势企业；省级新型研发机构、省级企业技术中心、博士后创新实践基地等 35 项以上资质荣誉。",
    "强纶资质,专精特新小巨人,高新技术企业,知识产权优势企业,荣誉证书",
    "honors.html")
 + header('about.html')
 + crumb([("关于强纶", "about.html"), ("资质荣誉", None)])
 + page_hero("05", "HONORS", "资质荣誉",
             "资质不是墙上的纸，<em>是工况里的底气</em>",
             "从国家级专精特新“小巨人”到标准化技术委员单位，公司在技术、知识产权与行业话语权上持续积累。")
 + f"""<section class="sec"><div class="wrap">{anav(4)}
  <div class="g4" style="margin-bottom:10px">
    <div class="card rv"><span class="n">8</span><h3>国家级</h3><p>含专精特新“小巨人”、高新技术企业、知识产权优势企业及标委会单位</p></div>
    <div class="card rv d1"><span class="n">12</span><h3>省级</h3><p>新型研发机构、企业技术中心、博士后创新实践基地等</p></div>
    <div class="card rv d2"><span class="n">14</span><h3>市级</h3><p>军民融合、科技小巨人领军、工业设计中心、人才类荣誉等</p></div>
    <div class="card rv d3"><span class="n">3</span><h3>区级</h3><p>潜力成长企业、重点税源企业、先进基层党组织</p></div>
  </div>
  {hon_html}
  <div class="note" style="margin-top:44px"><b>证书扫描件</b>：完整资质证书与认证文件可在<a href="downloads.html" style="border-bottom:2px solid var(--gold)">资料下载中心</a>获取，或联系我们索取。</div>
</div></section>"""
 + ENDCTA + footer())

# ───────────────────────────── 6. 企业文化与社会责任
w('culture.html', head(
    "企业文化与社会责任 | 强纶新材",
    "“工业报国、科技强国”的价值观，“协调创新、联合创业、利益共享”的经营理念；近三年研发投入占企业收入 12% 以上。",
    "强纶企业文化,工业报国,社会责任,员工风采",
    "culture.html", og_img="img/team-build2021.webp")
 + header('about.html')
 + crumb([("关于强纶", "about.html"), ("企业文化与社会责任", None)])
 + page_hero("06", "CULTURE", "企业文化与社会责任",
             "工业报国，<em>科技强国</em>",
             "在不断自我突破的过程中，强纶把价值观凝练为“工业报国、科技强国”；经营上坚持“协调创新、联合创业、利益共享”。",
             bg="img/team-build2021.webp")
 + f"""<section class="sec"><div class="wrap">{anav(5)}
  <div class="g3">
    <article class="card rv"><h3>价值观</h3><p>工业报国、科技强国。把关键材料的国产化，当成企业存在的理由。</p></article>
    <article class="card rv d1"><h3>经营理念</h3><p>协调创新、联合创业、利益共享。与客户、院校、入驻企业共同成长。</p></article>
    <article class="card rv d2"><h3>质量观</h3><p>客户至上、产品为王、标准为冠；管理保证、技术支撑、人才为本。</p></article>
  </div>

  <div class="g2 wide" style="margin-top:88px">
    <div class="prose rv">
      <h3 style="margin-top:0">把研发投入花在刀刃上</h3>
      <p>近三年研发投入占企业收入 <strong>12% 以上</strong>。公司建有省级新型研发机构、省级企业技术中心与博士后创新实践基地，并以创新研究院为平台，整合金纶新材料、金山粉末、柔银新材料、龙象机械等资源，为新材料创业园提供“研发平台 + 专家指导 + 经营服务”的拎包入驻模式。</p>
      <h3>社会责任</h3>
      <p>公司承担关键材料国产化任务，产品应用于航天、能源与高端装备等国家重点领域；在地方上带动产业链配套与人才集聚，获评先进基层党组织、龙岩市守合同重信企业等。</p>
      <h3>员工发展</h3>
      <p>设立忠诚奖、优秀员工与优秀干部评选，各事业部定期组织团建与文体活动，形成稳定的技术骨干队伍。</p>
    </div>
    <div class="rv d1">
      <div class="gal" style="grid-template-columns:1fr 1fr">
        <figure><img src="img/team-star2024.webp" alt="2024 年优秀员工表彰" loading="lazy"><figcaption>优秀员工表彰</figcaption></figure>
        <figure><img src="img/team-loyalty2025.webp" alt="2025 年年终会忠诚奖" loading="lazy"><figcaption>年终会 · 忠诚奖</figcaption></figure>
        <figure><img src="img/team-build2021.webp" alt="公司团建活动" loading="lazy"><figcaption>公司团建</figcaption></figure>
        <figure><img src="img/team-yarn2026.webp" alt="纱线事业部团建活动" loading="lazy"><figcaption>事业部活动</figcaption></figure>
        <figure><img src="img/team-cadre2024.webp" alt="2024 年优秀干部表彰" loading="lazy"><figcaption>优秀干部表彰</figcaption></figure>
        <figure><img src="img/team-purify.webp" alt="净化事业部团建活动" loading="lazy"><figcaption>净化事业部活动</figcaption></figure>
        <figure><img src="img/team-thermo.webp" alt="热动事业部团建活动" loading="lazy"><figcaption>热动事业部活动</figcaption></figure>
        <figure><img src="img/team-dragon2025.webp" alt="2025 年端午节员工慰问" loading="lazy"><figcaption>端午节慰问</figcaption></figure>
      </div>
    </div>
  </div>
</div></section>"""
 + ENDCTA + footer())

# ───────────────────────────── 7. 投资者关系
w('investor.html', head(
    "投资者关系 | 强纶新材（872336）",
    "福建强纶新材料股份有限公司，全国中小企业股份转让系统挂牌，证券代码 872336，2017 年 11 月挂牌，2026 年完成定向增发，注册资本增至 4275 万元。",
    "强纶新材股票,872336,新三板,投资者关系,定向增发",
    "investor.html")
 + header('about.html')
 + crumb([("关于强纶", "about.html"), ("投资者关系", None)])
 + page_hero("07", "INVESTOR", "投资者关系",
             "证券代码 <em>872336</em>",
             "公司于 2017 年 11 月在全国中小企业股份转让系统（新三板）挂牌，持续以规范治理与信息披露回应投资者关切。",
             [("872336", "", "证券代码"), ("2017", ".11", "挂牌时间"), ("4275", "万", "注册资本（元）")])
 + f"""<section class="sec"><div class="wrap">{anav(6)}
  <div class="g2 wide">
    <div class="prose rv">
      <h3 style="margin-top:0">基本信息</h3>
      <dl class="spec" style="margin-top:0">
        <dt>公司全称</dt><dd>福建强纶新材料股份有限公司</dd>
        <dt>英文名称</dt><dd>FUJIAN QL METAL FIBER CO., LTD</dd>
        <dt>证券简称</dt><dd>强纶新材</dd>
        <dt>证券代码</dt><dd>872336</dd>
        <dt>挂牌板块</dt><dd>全国中小企业股份转让系统（新三板）</dd>
        <dt>挂牌时间</dt><dd>2017 年 11 月</dd>
        <dt>股改时间</dt><dd>2017 年 6 月</dd>
        <dt>注册资本</dt><dd>4275 万元（2026 年定增后；设立时 3800 万元）</dd>
        <dt>统一社会信用代码</dt><dd>91350800753119639E</dd>
        <dt>注册地址</dt><dd>福建省龙岩市龙岩经济技术开发区黄邦路 11 号</dd>
      </dl>
      <h3>公告与披露</h3>
      <p>公司定期报告、临时公告以全国中小企业股份转让系统指定信息披露平台发布的内容为准，请投资者以官方披露信息为准，谨慎决策。</p>
      <p><a class="pill pill-ink" href="https://www.neeq.com.cn/" target="_blank" rel="noopener" style="margin-top:10px">前往全国股转系统查询<svg class="i"><use href="#i-arrow"/></svg></a></p>
    </div>
    <aside class="rv d1">
      <div class="note"><b>投资者关系联络</b><br>电话：0597-2799968<br>地址：福建省龙岩市龙岩经济技术开发区黄邦路 11 号<br><br>媒体与投资者问询，亦可通过<a href="contact.html" style="border-bottom:2px solid var(--gold)">联系我们</a>页面留言，公司将安排专人回复。</div>
      <div class="note warn" style="margin-top:20px"><b>风险提示</b><br>本页信息仅供了解公司基本情况，不构成任何投资建议。公司经营数据与财务信息以正式披露的定期报告为准。</div>
    </aside>
  </div>
</div></section>"""
 + ENDCTA + footer())

print('关于强纶：7/7 完成')
