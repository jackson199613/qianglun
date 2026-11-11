# -*- coding: utf-8 -*-
"""产品线：过滤元器件 / 净化设备（收油系统）"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from layout import head, header, crumb, page_hero, footer
from common import w, ENDCTA
from build_lines import faq_block, cta_row

# ════════════════ 4 过滤元器件
w('p-element.html', head(
    "过滤元器件 | 烧结滤芯 · 叶片滤盘 · 折波滤芯 — 强纶新材",
    "金属纤维烧结滤芯、烧结网滤盘、折波滤芯与耐高温金属滤袋，机械强度高、耐高温耐腐蚀、孔径分布均匀，可清洗再生、可焊接机加工。",
    "金属纤维滤芯,烧结滤芯,叶片滤盘,折波滤芯,熔体滤芯,除尘滤芯,水滤芯",
    "p-element.html", og_img="img/cart-01.webp")
 + header('products.html')
 + crumb([("产品中心", "products.html"), ("过滤元器件", None)])
 + page_hero("04", "FILTER ELEMENTS", "过滤元器件",
             "把滤材做成<em>能装上设备的零件</em>",
             "以金属纤维烧结毡、烧结网或多层丝网为滤材，经折波、卷制、骨架支撑与整体烧结焊接成型，直接匹配客户的过滤器与产线接口。",
             [("10", "μm", "常用名义精度"), ("99.9", "%", "气体过滤效率 @1μm"), ("72", "%", "典型孔隙率"), ("480", "℃", "可用温度")],
             bg="img/cart-03.webp")
 + f"""<section class="sec"><div class="wrap">
  <div class="g2 r7-5 wide">
    <div class="prose rv">
      <p class="lede">一句话定义：由烧结滤材与金属骨架整体成型的过滤零件，强度高、可反洗再生，用来替代滤纸滤布与易碎金属网。</p>
      <h3>主要品类</h3>
      <ul>
        <li><strong>熔体滤芯</strong>：面向化纤与聚合物熔体过滤，可折波、耐压，滤材可选自产或进口；</li>
        <li><strong>水滤芯</strong>：以烧结毡、烧结网或丝网为滤材，用于水处理与料液精滤；</li>
        <li><strong>除尘滤芯</strong>：长纤维毡 / 粉末毡 / 短纤维毡滤材，配法兰盘与骨架，用于高温气体除尘；</li>
        <li><strong>叶片滤盘 / 烧结网滤盘</strong>：由烧结纤维网与编织丝网组成，安装于过滤装置过滤高粘度熔体，可快速去除硬杂质与结块；</li>
        <li><strong>耐高温金属滤袋</strong>：高温烟气工况下替代化纤滤袋。</li>
      </ul>
      <h3>结构与优势</h3>
      <p>多层不锈钢丝网经特殊叠层压制、真空烧结而成，具有较高机械强度与整体刚性；<strong>耐高温、强度大、精度高、可再生、耐磨耐压、高比表面积、可反复冲洗</strong>，加工焊接与组装性能良好。</p>
    </div>
    <aside class="rv d1">
      <div class="gal" style="grid-template-columns:1fr 1fr">
        <figure><img src="img/cart-01.webp" alt="金属纤维折波滤芯" loading="lazy"><figcaption>折波滤芯</figcaption></figure>
        <figure><img src="img/cart-03.webp" alt="滤芯批量生产" loading="lazy"><figcaption>批量供货</figcaption></figure>
        <figure><img src="img/media-06.webp" alt="烧结滤芯组件" loading="lazy"><figcaption>滤芯组件</figcaption></figure>
        <figure><img src="img/media-10.webp" alt="过滤器装置" loading="lazy"><figcaption>过滤器装置</figcaption></figure>
      </div>
      {cta_row('过滤元器件')}
    </aside>
  </div>

  <div class="sec-h" style="margin:88px 0 24px"><h2>典型滤芯规格示例</h2><p>以金属纤维烧结毡滤芯为例，实际按客户设备接口与工况定制。</p></div>
  <div class="g2">
    <div class="tbl-wrap"><table class="tbl">
      <caption>滤芯性能参数</caption>
      <thead><tr><th>项目</th><th>参数</th></tr></thead>
      <tbody>
        <tr><td>滤材</td><td>非对称金属纤维烧结毡（细面朝外）</td></tr>
        <tr><td>名义精度</td><td class="num">10 μm</td></tr>
        <tr><td>过滤效率</td><td class="num">气体过滤 99.9% @ 1μm</td></tr>
        <tr><td>孔隙率</td><td class="num">72%</td></tr>
        <tr><td>平均起泡压强</td><td class="num">3700 Pa（偏差 ±10%）</td></tr>
        <tr><td>第一起泡压强</td><td class="num">不小于 2500 Pa</td></tr>
        <tr><td>平均透气度</td><td class="num">71 L/min/dm² @ 200Pa</td></tr>
      </tbody>
    </table></div>
    <div class="tbl-wrap"><table class="tbl">
      <caption>结构与材料</caption>
      <thead><tr><th>部位</th><th>材料 / 规格</th></tr></thead>
      <tbody>
        <tr><td>冲孔网支撑</td><td>304</td></tr>
        <tr><td>金属纤维烧结毡</td><td>316L · 10μm · 0.4mm</td></tr>
        <tr><td>内部支撑金属丝网</td><td>304 · 丝径 0.125mm · 48 目</td></tr>
        <tr><td>外部保护金属丝网</td><td>304 · 丝径 0.224mm · 40 目</td></tr>
        <tr><td>滤芯接头 / 外部套筒</td><td>304</td></tr>
        <tr><td>滤芯主体长度</td><td class="num">1500 mm（含接头总长 1725mm）</td></tr>
        <tr><td>滤芯外径 OD</td><td class="num">65 mm</td></tr>
        <tr><td>密封形式</td><td>2.5" NPT（大端面朝外）</td></tr>
      </tbody>
    </table></div>
  </div>
  <p class="tnote">* 上表为典型工程配置示例，单根滤芯面积、总过滤面积、文丘里管尺寸等均按设备数量与工况核算；请提供设备编号、工艺单元、介质与温度，由工程师出具配置表。</p>

  <div class="g2 wide" style="margin-top:84px">
    <div class="rv"><h2 style="font-family:'Noto Serif SC',serif;font-size:26px;font-weight:900;margin-bottom:20px">选型建议</h2>
      <div class="prose">
        <p><strong>第一步定滤材</strong>：按介质与温度选烧结毡（高精度、大纳污）或烧结网（高强度、易反洗）。</p>
        <p><strong>第二步定结构</strong>：流量大、压差要求严时选折波增大面积；高粘度熔体工况选叶片滤盘；高温烟气选除尘滤芯或金属滤袋。</p>
        <p><strong>第三步定接口</strong>：按原设备的接头形式、密封面与安装长度配套，确保直接替换。</p>
        <div class="note" style="margin-top:24px"><b>进口替代</b>：公司国产化熔体滤芯已批量供应国内大型石化、化纤龙头企业，可按进口件图纸或实物测绘复刻。</div>
      </div>
    </div>
    <div class="rv d1"><h2 style="font-family:'Noto Serif SC',serif;font-size:26px;font-weight:900;margin-bottom:20px">常见问题</h2>
      {faq_block([
        ("金属纤维滤芯能清洗再用吗？", "可以。金属纤维烧结滤材耐高温、耐腐蚀，可反复清洗再生，寿命远长于滤纸滤布类产品。"),
        ("化纤熔体过滤该选多少精度？", "取决于纤维品种、纺丝规格与熔体洁净度要求。建议提供产品规格与现用滤材情况，由强纶工程师结合叶片滤盘与烧结滤芯给出精度方案。"),
        ("可以按进口滤芯复刻吗？", "可以。提供图纸或实物样品即可测绘复刻，公司已有多个进口替代批量供货案例。"),
        ("支持非标定制与打样吗？", "支持。可根据过滤精度、工况温度、介质、尺寸与接口等参数定制并提供样品测试。"),
        ("滤芯会提供检测报告吗？", "可提供检验报告，检测项目包括精度、气泡点、透气度等；具体以订单约定为准。"),
      ])}
    </div>
  </div>
</div></section>"""
 + ENDCTA + footer())

# ════════════════ 5 净化设备 · 收油系统
cases = [("广东芳源环保股份有限公司","2 套 15 m³/h 收油系统"),("福建常青新能源科技有限公司","2 套 1 m³/h；1 套 2.5 m³/h 槽体改造"),
 ("衢州华友钴新材料有限公司","1 套 15、2 套 100、1 套 40、1 套 240（槽体改造）、1 套 180、1 套 80 m³/h"),
 ("衢州华友资源再生有限公司","1 套 8 m³/h；1 套 30 m³/h 槽体改造"),("山东烟台凯实工业有限公司","1 套 15 m³/h"),
 ("江苏天能新材料有限公司","5 套收油系统"),("常熟市滨江化工有限公司","1 套 0.35 m³/h"),("江西铜业集团有限公司","1 套 8 m³/h"),
 ("福建紫金铜业有限公司","1 套 10 m³/h 过滤机"),("江苏强盛功能化学股份有限公司","2 套 0.35 m³/h；功能纤维收油系统"),
 ("广西巴莫科技有限公司","160 m³/h 收油系统"),("广西华友新材料有限公司","600 m³/h 收油系统"),("汉中锌业有限责任公司","1 套 5 m³/h"),
 ("中国恩菲工程技术有限公司","1 套 10、1 套 60 m³/h"),("格林美股份有限公司","1 套 60 m³/h"),("青海超频三新材料有限公司","2 套 50+5 m³/h"),
 ("湖北睿派新能源科技有限公司","1 套 38 m³/h 活性炭收油系统"),("郑州天一萃取科技有限公司","2 套 1+2 m³/h"),
 ("河南荣佳钪钒科技有限公司","1 套 60 m³/h 槽体改造"),("湖南邦普循环科技有限公司","功能纤维收油系统"),
 ("江苏凯实金桥新材料有限公司","7 套共 480 方"),("攀枝花市山青钒业有限公司","8 m³/h 反萃液收油系统"),
 ("金昌神泥科技有限公司","1 套 6 m³/h"),("江西佳纳能源科技有限公司","1 套 25 m³/h")]
case_rows = "".join(f'<tr><td><b>{a}</b></td><td>{b}</td></tr>' for a, b in cases)

w('p-equipment.html', head(
    "净化设备 · 强纶收油系统 | 功能纤维油水分离 — 强纶新材",
    "FTS 强纶收油系统采用表面改性亲油疏水金属纤维聚结除油，纯物理不加药剂，最大单套 600 m³/h，除油率 70%，已服务华友、格林美、邦普、江西铜业等 20 余家企业。",
    "收油系统,油水分离设备,聚结除油装置,湿法冶金除油,萃取液除油,FTS,预除油",
    "p-equipment.html", og_img="img/fts-site-bamo.webp")
 + header('products.html')
 + crumb([("产品中心", "products.html"), ("净化设备 · 收油系统", None)])
 + page_hero("05", "PURIFICATION EQUIPMENT", "净化设备 · 收油系统",
             "纯物理除油，<em>分出来的油还能用</em>",
             "强纶收油系统（FTS 功能纤维除油系统）以公司自产的亲油疏水金属纤维为聚结材料，通过「前置过滤器 + 油水分离器」实现高效油水分离，广泛用于镍钴湿法冶金、化工萃取等工艺的溶液除油与油份回收。",
             [("600", "m³/h", "最大单套处理量"), ("70", "%", "典型除油率"), ("5", "年", "核心材料最长未更换"), ("1–2", "年", "投资回收期")],
             bg="img/fts-site-bamo.webp")
 + f"""<section class="sec"><div class="wrap">
  <div class="g2 r7-5 wide">
    <div class="prose rv">
      <p class="lede">一句话定义：用改性金属纤维把微米级乳化油「抓住、养大、浮走」的预除油成套设备，不加破乳药剂、不产生化学污泥。</p>
      <h3>系统组成与工作原理</h3>
      <p><strong>前置过滤器</strong>去除液体中的杂质，保证后续油水分离装置不被堵塞或损坏；<strong>油水分离器</strong>通过特殊纤维捕捉油珠，油珠在纤维表面不断聚结变大后顺液体排出、快速上浮，进入上部储油腔定期排出，除油后的液体从出液口排出。分离出的油份可直接回收使用。</p>
      <h3>三大优势来源</h3>
      <ul>
        <li><strong>纯物理分离</strong>：不靠化学破乳，不产生化学污泥，无药剂引入，不影响后端料液（湿法冶金萃取液尤其关键），无二次污染；</li>
        <li><strong>擅长微米级乳化油</strong>：改性梯度金属纤维可捕捉常规斜板、气浮难以处理的微细乳化油，保护后端树脂、膜与生化系统不被油污堵塞中毒；</li>
        <li><strong>材质耐腐耐高温</strong>：核心为表面改性的金属滤芯，工况适应性强、寿命长。</li>
      </ul>
    </div>
    <aside class="rv d1">
      <div class="gal" style="grid-template-columns:1fr">
        <figure style="aspect-ratio:16/13;background:#fff"><img src="img/fts-principle.webp" alt="油水分离系统工作示意图" loading="lazy" style="object-fit:contain;padding:14px"><figcaption style="background:linear-gradient(0deg,rgba(10,10,12,.72),transparent)">工作原理示意</figcaption></figure>
        <figure style="aspect-ratio:16/11;background:#fff"><img src="img/fts-layout.webp" alt="油水分离设备组成" loading="lazy" style="object-fit:contain;padding:14px"><figcaption style="background:linear-gradient(0deg,rgba(10,10,12,.72),transparent)">设备组成</figcaption></figure>
      </div>
      {cta_row('收油系统')}
    </aside>
  </div>

  <div class="sec-h" style="margin:88px 0 24px"><h2>产品型谱</h2></div>
  <div class="g3">
    <article class="card rv"><span class="n">01</span><h3>罐式收油系统</h3><p>适用小流量需求（≤30 m³/h），可撬装，到客户现场直接连接管路即可使用。</p></article>
    <article class="card rv d1"><span class="n">02</span><h3>槽式收油系统</h3><p>适用大流量应用场景，占地更紧凑，投资成本更低。</p></article>
    <article class="card rv d2"><span class="n">03</span><h3>槽体改造收油系统</h3><p>利用原有澄清槽 / 槽体改造，降低投资、快速投用。</p></article>
  </div>

  <div class="sec-h" style="margin:80px 0 24px"><h2>主要参数</h2></div>
  <div class="tbl-wrap"><table class="tbl">
    <thead><tr><th>参数项</th><th>数据</th></tr></thead>
    <tbody>
      <tr><td>单套处理量</td><td>罐式 ≤30 m³/h；槽式 / 槽体改造按需设计；目前最大单套 <b>600 m³/h</b></td></tr>
      <tr><td>适用溶液</td><td>硫酸钴溶液、硫酸镍溶液等萃取工艺料液</td></tr>
      <tr><td>除油率</td><td class="num">70%（衢州 15 m³/h 项目，稳定运行 3 年）</td></tr>
      <tr><td>出口含油量</td><td class="num">5—30 mg/L（视工况）</td></tr>
      <tr><td>占地</td><td>约为每小时处理量的 1/3—2/3</td></tr>
      <tr><td>核心材料寿命</td><td>长期使用，最长应用 5 年未更换</td></tr>
      <tr><td>投资回收</td><td>镍钴行业应用证明 1—2 年</td></tr>
    </tbody>
  </table></div>

  <div class="sec-h" style="margin:80px 0 24px"><h2>与常用预除油手段对比</h2><p>收油系统定位于「预除油」环节：以最低运行成本将非溶解油去除并回收使用，从而降低后续深度除油的消耗成本。</p></div>
  <div class="tbl-wrap"><table class="tbl">
    <thead><tr><th>对比项</th><th>静置</th><th>气浮</th><th>阻拦聚结</th><th>强纶除油</th></tr></thead>
    <tbody>
      <tr><td><b>原理</b></td><td>长时间静置使油份自然上浮</td><td>结合静置，通过微小气泡增加上浮速度</td><td>对油份起拦截作用，油珠碰撞长大后逆液体上浮</td><td>特殊纤维捕捉油珠，油珠在纤维上长大后顺液体排出、快速上浮</td></tr>
      <tr><td><b>非溶解油分离效果</b></td><td>差</td><td>一般</td><td>好</td><td><b>最佳</b></td></tr>
      <tr><td><b>设备投资</b></td><td>少</td><td>较少</td><td>一般</td><td>一般（相比深度除油设备少很多）</td></tr>
      <tr><td><b>占地面积</b></td><td>大</td><td>中等</td><td>中等（易油份穿透，常需串联多级）</td><td><b>小</b>（约为每小时处理量的 1/3—2/3）</td></tr>
      <tr><td><b>运行成本</b></td><td>低</td><td>较高</td><td>较高（组件约 1 年更换或定期拆洗）</td><td><b>低</b>（除油组件无需更换，可一直使用）</td></tr>
      <tr><td><b>核心材料</b></td><td>无</td><td>无</td><td>纤维球、聚结树脂、化学纤维滤芯</td><td>表面改性的金属 / 化学滤芯</td></tr>
      <tr><td><b>核心材料寿命</b></td><td>无</td><td>无</td><td>1 年左右（除油效果持续衰减）</td><td><b>长期使用</b>（最长应用 5 年未更换）</td></tr>
    </tbody>
  </table></div>
  <p class="tnote">油水分离通常分「预除油」与「深度除油」两个环节：预除油以最低运行成本去除并回收非溶解油；深度除油（吸附树脂、活性炭、蒸发、催化氧化等）保证液体指标合格。根据萃取剂、混合方式与工艺不同，溶解度一般在 5—40 ppm。</p>

  <div class="sec-h" style="margin:80px 0 24px"><h2>现场与应用</h2></div>
  <div class="gal">
    <figure><img src="img/fts-site-bamo.webp" alt="广西巴莫收油系统现场" loading="lazy"><figcaption>槽式收油系统现场</figcaption></figure>
    <figure><img src="img/fts-site-huayou.webp" alt="广西华友收油系统现场" loading="lazy"><figcaption>大流量槽体方案</figcaption></figure>
    <figure><img src="img/fts-site-02.webp" alt="罐式收油系统现场" loading="lazy"><figcaption>罐式收油系统</figcaption></figure>
    <figure><img src="img/fts-scene-01.webp" alt="湿法冶金车间应用现场" loading="lazy"><figcaption>湿法冶金车间</figcaption></figure>
    <figure><img src="img/fts-site-04.webp" alt="收油系统管路与阀组" loading="lazy"><figcaption>管路与阀组</figcaption></figure>
    <figure><img src="img/fts-scene-02.webp" alt="收油系统安装现场" loading="lazy"><figcaption>安装调试</figcaption></figure>
    <figure><img src="img/fts-scene-03.webp" alt="过滤与除油联合装置" loading="lazy"><figcaption>联合装置</figcaption></figure>
    <figure><img src="img/media-10.webp" alt="前置过滤器" loading="lazy"><figcaption>前置过滤器</figcaption></figure>
  </div>

  <div class="sec-h" style="margin:80px 0 24px"><h2>部分业绩</h2><p>已为新能源与有色冶炼行业 20 余家企业提供收油系统及过滤服务。</p></div>
  <div class="tbl-wrap"><table class="tbl">
    <thead><tr><th>客户</th><th>配置 / 通量</th></tr></thead>
    <tbody>{case_rows}</tbody>
  </table></div>
  <p class="tnote">* 以上为公开可披露的合作信息，具体工艺参数与方案细节依保密约定不予展示。</p>

  <div class="g2 wide" style="margin-top:84px">
    <div class="rv"><h2 style="font-family:'Noto Serif SC',serif;font-size:26px;font-weight:900;margin-bottom:20px">选型建议</h2>
      <div class="prose">
        <p><strong>按处理量</strong>：小流量（≤30 m³/h）优先罐式收油系统，可撬装、即插即用；大流量工况采用槽式，占地更紧凑、投资更低；已有澄清槽 / 槽体可利用时，选槽体改造方案降低投资。</p>
        <p><strong>按溶液与工艺</strong>：针对硫酸钴、硫酸镍等萃取工艺溶液，结合溶解度（一般 5—40 ppm）判断「预除油 + 深度除油」的组合方案。</p>
        <p><strong>按工况定制</strong>：根据客户需求与现场实际完成个性化匹配设计；<strong>液体情况复杂的客户，可免费提供前期实验设备及技术人员入厂试验</strong>。</p>
      </div>
    </div>
    <div class="rv d1"><h2 style="font-family:'Noto Serif SC',serif;font-size:26px;font-weight:900;margin-bottom:20px">常见问题</h2>
      {faq_block([
        ("强纶收油系统是什么？主要解决什么问题？", "强纶收油系统是功能纤维除油系统，通过前置过滤器与油水分离器实现油水分离，用于去除工艺溶液中的非溶解油并回收油份，定位于预除油环节。"),
        ("与静置、气浮、阻拦聚结相比有什么优势？", "强纶除油对非溶解油分离效果好、占地面积小（约为每小时处理量的 1/3—2/3）、运行成本低，核心除油组件无需更换、可长期使用（最长应用 5 年未更换）。"),
        ("除油效果如何？", "以衢州 15 m³/h 项目为例，硫酸钴溶液除油率稳定在 70%，已使用 3 年；不同工况出口含油量一般在 5—30 mg/L 区间。"),
        ("处理量范围多大？", "罐式适用 ≤30 m³/h 的小流量需求；槽式及槽体改造方案适用于大流量场景，目前最大单套处理量 600 m³/h。"),
        ("除油组件需要更换吗？", "不需要频繁更换。核心材料为表面改性的金属/化学滤芯，可长期使用；与阻拦聚结类组件（约 1 年更换）相比运行成本更低。"),
        ("设备投资回收期多长？", "镍钴行业应用证明，1—2 年即可回收设备投资成本。"),
        ("设备运行维护复杂吗？", "设备运行简单，几乎不需要专人管理；公司同时提供设备保养、更换滤芯等后续维护及维修服务。"),
        ("可以定制吗？提供试验服务吗？", "支持根据客户需求和现场实际情况完成个性化匹配设计；针对液体情况复杂的客户，免费提供前期收油系统实验设备及专业技术人员入厂试验。"),
        ("预除油和深度除油如何配合？", "预除油以最低运行成本去除并回收非溶解油，降低后续深度除油（活性炭、树脂等）的消耗；再通过深度除油去除溶解油以保证指标合格，是最具普适性和经济效益的油水分离方式。"),
        ("产品是否附检测报告？", "可提供检验报告；报告类型与检测项目见检测能力页，具体以订单约定为准。"),
      ])}
    </div>
  </div>
</div></section>"""
 + ENDCTA + footer())
print('过滤元器件 / 净化设备 完成')
