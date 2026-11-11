# -*- coding: utf-8 -*-
"""全站通用页：搜索结果 / 404 / 隐私政策与法律声明 / 网站地图"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from layout import head, header, crumb, page_hero, footer, NAV, SITE, ADDR, TEL
from common import w, ENDCTA

# 站内搜索索引
INDEX = [
 ("金属纤维烧结毡","p-felt.html","绝对过滤精度 10–60μm，多层梯度孔，纳污量大、升压慢、可清洗再生，耐 480℃","产品"),
 ("金属纤维纱线","p-yarn.html","发热线、缝纫线、混纺纱，米电阻 1–100Ω，耐温 350–850℃，防静电电磁屏蔽","产品"),
 ("金属纤维织物","p-fabric.html","编织套管、针织套管、机织带与机织布，长期耐温 350℃、短时 1100℃，玻璃成型包覆","产品"),
 ("过滤元器件","p-element.html","熔体滤芯、水滤芯、除尘滤芯、叶片滤盘与折波滤芯，整体烧结成型","产品"),
 ("净化设备 · 收油系统","p-equipment.html","FTS 功能纤维除油系统，纯物理聚结除油，最大单套 600 m³/h，除油率 70%","产品"),
 ("25KIA3 产品详情","p-detail.html","25μm 烧结毡，厚度 0.61mm，过滤率 80%，气泡点压 1480Pa，透气值 350","产品"),
 ("选型指南","selector.html","介质 → 温度 → 压力 → 精度 四步选型，即时推荐产品线","选型"),
 ("参数对照表","specs.html","KIA3 / KIA3K / KIC 全系列 15 个型号精度、厚度、过滤率、气泡点与透气值","选型"),
 ("名词解释","glossary.html","过滤精度、孔隙率、透气度、气泡点压、纳污量、聚结、米电阻等术语","选型"),
 ("资料下载中心","downloads.html","产品手册、技术数据表、检测报告与资质证书下载","选型"),
 ("过滤分离方案","a-filtration.html","化纤熔体、黏胶过滤、高温气体除尘与萃取液除油的完整链条","方案"),
 ("玻璃深加工方案","a-glass.html","钢化炉辊道套管、测温探头包覆、模布与吸盘毡，杜绝玻璃划伤","方案"),
 ("电磁屏蔽与防静电","a-emi.html","本体导电不依赖涂层，屏蔽能力不因洗涤衰减，屏蔽率可达 99% 以上","方案"),
 ("航空航天与特种材料","a-aero.html","针刺毡应用于长征五号 B、长征五号遥五运载火箭发动机","方案"),
 ("汽车应用","a-auto.html","座椅加热、SCR 加热系统与尾气微粒过滤","方案"),
 ("功能纺织与智能穿戴","a-textile.html","发热马甲、围脖、鞋袜、手套与 RFID 水洗标，电热面料市占率全国第一","方案"),
 ("科研创新","rd.html","六个研究室、五大制研平台，研发投入占收入 12% 以上","科研"),
 ("专利与标准","patents.html","授权专利 57 项，参与制修订国家标准 5 项、行业标准 1 项","科研"),
 ("研发中心与实验室","lab.html","省级新型研发机构、省级企业技术中心与博士后创新实践基地","科研"),
 ("检测能力","testing.html","过滤精度、气泡点、透气度、孔隙率等检测项目与报告类型","科研"),
 ("产学研合作","coop.html","厦门大学、同济大学、中国兵器 201 所等 13 项合作","科研"),
 ("科研成果","achievements.html","省级科技计划项目 4 项、市级 2 项","科研"),
 ("企业简介","about.html","创立于 2002 年，新三板 872336，国家级专精特新“小巨人”企业","关于"),
 ("发展历程","history.html","2002 创立 → 2017 挂牌 → 2020 配套长征五号 → 2025 国家级小巨人","关于"),
 ("制造能力","manufacturing.html","自有工业用地 40 余亩，五大制研平台，复合拉拔最细至 2μm","关于"),
 ("质量体系","quality.html","ISO 9001 认证，三道检验关口，参与制修订 5 项国标","关于"),
 ("资质荣誉","honors.html","国家级 8 项、省级 12 项、市级 14 项、区级 3 项","关于"),
 ("常见问题库","faq.html","22 条高频问题：精度怎么选、能否清洗再生、耐温上限、除油率","支持"),
 ("术语百科","encyclopedia.html","金属纤维、复合拉拔、烧结网、叶片滤盘、针刺毡等中英文对照","支持"),
 ("技术专栏","insights.html","选型、对比、应用与原理类技术文章","支持"),
 ("新闻动态","news.html","企业新闻、行业资讯与展会活动","关于"),
 ("人才招聘","jobs.html","材料研发、过滤应用、设备设计、海外销售等岗位","关于"),
 ("联系我们","contact.html","电话 181 5982 1773 / 0597-2799968，工况询盘与图纸上传","联系"),
 ("样品申请","sample.html","免费小样，运费到付，现货样品 1–3 天寄出","联系"),
]
import json
idx_json = json.dumps([{"t": t, "u": u, "d": d, "c": c} for t, u, d, c in INDEX], ensure_ascii=False)

w('search.html', head(
    "站内搜索 | 强纶新材",
    "在强纶官网内搜索产品、工况、技术问题与资料，覆盖产品线、选型中心、应用方案、科研创新与常见问题。",
    "强纶站内搜索,产品搜索", "search.html")
 + header('')
 + crumb([("站内搜索", None)])
 + page_hero("", "SEARCH", "站内搜索", "搜索<em>产品、工况或技术问题</em>",
             "例如：化纤熔体过滤精度、烧结毡能否清洗、收油系统处理量、2μm 纤维。")
 + """<section class="sec" style="padding-top:0"><div class="wrap">
  <div class="sbox"><svg class="i"><use href="#i-search"/></svg><input id="sq" type="search" placeholder="输入关键词后按回车" aria-label="站内搜索"></div>
  <p class="shot">热门：<a href="#" data-q="过滤精度">过滤精度</a><a href="#" data-q="烧结毡">烧结毡</a><a href="#" data-q="收油系统">收油系统</a><a href="#" data-q="2μm">2μm 超细纤维</a><a href="#" data-q="清洗">能否清洗再用</a><a href="#" data-q="发热线">发热线</a></p>
  <p class="scount" id="scount"></p>
  <div class="rows" id="sres"></div>
</div></section>
<script>
(function(){
  var DATA=""" + idx_json + """;
  var q=document.getElementById('sq'),res=document.getElementById('sres'),cnt=document.getElementById('scount');
  function esc(s){return s.replace(/[&<>]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;'}[c]})}
  function run(k){
    k=(k||'').trim();
    if(!k){res.innerHTML='';cnt.textContent='';return}
    var low=k.toLowerCase();
    var hit=DATA.filter(function(x){return (x.t+x.d+x.c).toLowerCase().indexOf(low)>-1});
    cnt.textContent='找到 '+hit.length+' 条与「'+k+'」相关的结果';
    res.innerHTML=hit.map(function(x){
      return '<a class="row-i" href="'+x.u+'"><span class="dt">'+x.c+'</span><div><h4>'+esc(x.t)+'</h4><p>'+esc(x.d)+'</p></div><span class="tg">查看</span></a>';
    }).join('') || '<div class="note" style="margin-top:20px">没有找到匹配的内容。可以换个说法，或直接<a href="contact.html#inq" style="border-bottom:2px solid var(--gold)">联系工程师</a>。</div>';
  }
  q.addEventListener('keydown',function(e){if(e.key==='Enter')run(q.value)});
  q.addEventListener('input',function(){if(q.value.length>1)run(q.value)});
  document.querySelectorAll('.shot a').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();q.value=a.getAttribute('data-q');run(q.value)})});
  var p=new URLSearchParams(location.search).get('q');
  if(p){q.value=p;run(p)}
})();
</script>"""
 + footer())

w('404.html', head("页面未找到 | 强纶新材", "抱歉，您访问的页面不存在或已移动。", "", "404.html")
 + header('')
 + """<section class="sec nf"><div class="wrap">
  <div class="idx"><b>404</b>NOT FOUND</div>
  <h1>这个页面<em>没找到</em></h1>
  <p>可能是链接已过期，或者地址输入有误。下面几个入口也许是您要找的。</p>
  <div class="g4" style="margin-top:46px">
    <a class="card" href="index.html"><h3>返回首页</h3><p>从头开始浏览</p><span class="more">前往<svg class="i"><use href="#i-arrow"/></svg></span></a>
    <a class="card" href="products.html"><h3>产品中心</h3><p>五条产品线与参数</p><span class="more">前往<svg class="i"><use href="#i-arrow"/></svg></span></a>
    <a class="card" href="selector.html"><h3>按工况选型</h3><p>四步得到推荐方案</p><span class="more">前往<svg class="i"><use href="#i-arrow"/></svg></span></a>
    <a class="card" href="contact.html#inq"><h3>联系工程师</h3><p>直接说工况</p><span class="more">前往<svg class="i"><use href="#i-arrow"/></svg></span></a>
  </div>
</div></section>"""
 + footer())

w('privacy.html', head(
    "隐私政策与法律声明 | 强纶新材",
    "福建强纶新材料股份有限公司官网隐私政策与法律声明：说明我们收集哪些信息、如何使用与保存，以及网站内容的版权与免责条款。",
    "隐私政策,法律声明,强纶新材", "privacy.html")
 + header('')
 + crumb([("隐私政策与法律声明", None)])
 + page_hero("", "PRIVACY", "隐私政策与法律声明", "我们收集什么，<em>以及怎么用</em>",
             "本页适用于本网站（强纶新材中文官网）的访问与表单提交行为。")
 + f"""<section class="sec"><div class="wrap">
  <div class="prose" style="max-width:62em">
    <h3 style="margin-top:0">一、我们收集的信息</h3>
    <p>当您通过本网站提交<strong>询盘表单</strong>、<strong>样品申请</strong>或<strong>访客留言</strong>时，我们会收集您主动填写的姓名、手机号、公司名称、邮箱、工况参数、收件信息，以及您上传的图纸或参数文件。</p>
    <p>为统计访问情况，我们会通过网站统计工具收集匿名的访问来源、浏览页面、停留时长与 IP 所在地区（省份／城市）等信息。统计数据由统计工具采集，受访客浏览器设置、网络代理等因素影响，仅作经营分析参考。</p>
    <h3>二、信息的使用</h3>
    <p>收集的信息仅用于：回复您的询盘与样品申请、提供选型与技术支持、寄送样品与资料、改进网站内容与服务。<strong>我们不会将您的信息出售、出租或以其他方式提供给与本次业务无关的第三方。</strong></p>
    <h3>三、信息的展示与保存</h3>
    <p>访客留言与询盘内容<strong>仅在网站后台可见，不会在网站前台展示</strong>。新留言会实时推送至公司指定的企业微信或邮箱。相关信息保存于本网站服务器，用于订单追溯与售后服务。</p>
    <h3>四、Cookie</h3>
    <p>本网站可能使用 Cookie 或同类技术记录您的浏览偏好与统计信息。您可以通过浏览器设置拒绝 Cookie，但这可能影响部分功能的使用体验。</p>
    <h3>五、您的权利</h3>
    <p>您可以通过本页下方的联系方式，要求查询、更正或删除我们所保存的您的个人信息。我们会在核实身份后及时处理。</p>
    <h3 id="legal">六、法律声明</h3>
    <p><strong>版权</strong>：本网站所载文字、图片、图表、视频及页面设计，除另有说明外，版权归福建强纶新材料股份有限公司所有。未经书面许可，任何单位或个人不得以任何方式复制、转载、摘编或用于商业用途。</p>
    <p><strong>商标</strong>：本网站使用的「强纶」「强纶新材」及相关标识为本公司的商标或商号，受法律保护。</p>
    <p><strong>内容免责</strong>：本网站所列产品参数、技术数据与应用建议来源于公司产品资料与工程经验，仅供参考。实际选型须结合具体工况由双方工程师确认，<strong>最终以订单与技术协议约定为准</strong>。参数如有调整恕不另行通知。</p>
    <p><strong>外部链接</strong>：本网站包含指向第三方平台（如纱线事业部站点、淘宝、1688、阿里国际站、全国股转系统等）的链接。链接内容由对应平台负责，本公司不对其内容承担责任。</p>
    <p><strong>投资提示</strong>：本网站「投资者关系」栏目的信息仅供了解公司基本情况，不构成任何投资建议；公司经营与财务信息以在全国中小企业股份转让系统正式披露的公告为准。</p>
    <h3>七、联系我们</h3>
    <p>如对本政策有任何疑问，请联系：<br>福建强纶新材料股份有限公司<br>地址：{ADDR}<br>电话：{TEL} / 0597-2799968<br>邮箱：info@qlfiber.com</p>
    <p style="color:var(--muted);font-size:14px;margin-top:30px">本政策最近更新日期：2026 年 11 月。</p>
  </div>
</div></section>"""
 + footer())

# ════════ 网站地图
GROUPS = [
 ("首页", [("首页","index.html")]),
 ("科研创新", [("科研总览","rd.html"),("核心技术平台","platforms.html"),("研发中心与实验室","lab.html"),("检测能力","testing.html"),("专利与标准","patents.html"),("产学研合作","coop.html"),("科研成果","achievements.html")]),
 ("产品中心", [("产品总览","products.html"),("金属纤维纱线","p-yarn.html"),("金属纤维烧结毡","p-felt.html"),("金属纤维织物","p-fabric.html"),("过滤元器件","p-element.html"),("净化设备 · 收油系统","p-equipment.html"),("产品详情（示例 25KIA3）","p-detail.html")]),
 ("应用方案", [("方案总览","applications.html"),("过滤分离","a-filtration.html"),("玻璃深加工","a-glass.html"),("电磁屏蔽与防静电","a-emi.html"),("航空航天与特种材料","a-aero.html"),("汽车","a-auto.html"),("功能纺织与智能穿戴","a-textile.html"),("其他应用","a-other.html")]),
 ("选型中心", [("选型指南","selector.html"),("参数对照表","specs.html"),("名词解释","glossary.html"),("资料下载中心","downloads.html")]),
 ("技术专栏", [("技术文章","insights.html"),("常见问题库","faq.html"),("术语百科","encyclopedia.html"),("文章详情（示例）","article.html"),("问答详情（示例）","qa.html")]),
 ("关于强纶", [("企业简介","about.html"),("发展历程","history.html"),("制造能力","manufacturing.html"),("质量体系","quality.html"),("资质荣誉","honors.html"),("企业文化与社会责任","culture.html"),("投资者关系","investor.html")]),
 ("新闻动态", [("新闻列表","news.html"),("新闻详情（示例）","news-detail.html")]),
 ("人才招聘", [("岗位列表","jobs.html"),("岗位详情（示例）","job-detail.html")]),
 ("联系与询盘", [("联系我们","contact.html"),("样品申请","sample.html")]),
 ("全站通用", [("站内搜索","search.html"),("隐私政策与法律声明","privacy.html"),("网站地图","sitemap.html"),("404 页面","404.html")]),
]
sm = "".join('<div class="sm-g rv"><h3>%s</h3><ul>%s</ul></div>' % (g, "".join(f'<li><a href="{u}">{t}</a></li>' for t, u in items)) for g, items in GROUPS)
total = sum(len(i) for _, i in GROUPS)

w('sitemap.html', head("网站地图 | 强纶新材", f"强纶新材中文官网全站页面索引，共 {total} 个页面，覆盖科研创新、产品中心、应用方案、选型中心、技术专栏、关于强纶、新闻动态、人才招聘与联系询盘。", "网站地图,强纶新材", "sitemap.html")
 + header('')
 + crumb([("网站地图", None)])
 + page_hero("", "SITEMAP", "网站地图", "全站页面，<em>一览</em>", f"当前共 {total} 个页面。也可使用<a href='search.html' style='border-bottom:2px solid var(--gold)'>站内搜索</a>直接查找。")
 + f"""<section class="sec"><div class="wrap"><div class="sm">{sm}</div></div></section>"""
 + footer())
print('全站通用页完成')
