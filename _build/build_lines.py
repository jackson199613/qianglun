# -*- coding: utf-8 -*-
"""5 条产品线页面"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from layout import head, header, crumb, page_hero, footer, SITE
from common import w, ENDCTA

def faq_block(items):
    qs = "".join(f"""<div class="qa"><button type="button" aria-expanded="false"><span class="n num">{i+1:02d}</span><span>{q}</span><span class="pm"><svg class="i"><use href="#i-x"/></svg></span></button><div class="ans"><div><p>{a}</p></div></div></div>""" for i, (q, a) in enumerate(items))
    sc = '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[%s]}' % ",".join(
        '{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}' % (q.replace('"', "'"), a.replace('"', "'")) for q, a in items)
    return f'<div class="qa-list">{qs}</div><script type="application/ld+json">{sc}</script>'

def cta_row(name):
    return f"""<div class="buyrow">
  <a class="pill pill-ink" href="contact.html#inq">针对{name}询价<svg class="i"><use href="#i-arrow"/></svg></a>
  <a class="pill pill-line" href="sample.html">申请样品</a>
  <a class="pill pill-line" href="downloads.html">下载资料</a>
</div>"""

# ════════════════ 1 金属纤维纱线
w('p-yarn.html', head(
    "金属纤维纱线 | 导电纱 · 发热线 · 缝纫线 — 强纶新材",
    "100% 316L 不锈钢金属纤维纱线，纤维直径低至 2μm，可混纺芳纶/涤纶/PPS/棉，用于防静电、电磁屏蔽、智能穿戴发热与汽车座椅加热。",
    "金属纤维纱线,不锈钢纤维纱,导电纱,发热线,缝纫线,防静电纱线,电磁屏蔽",
    "p-yarn.html", og_img="img/yarn-fabric.webp")
 + header('products.html')
 + crumb([("产品中心", "products.html"), ("金属纤维纱线", None)])
 + page_hero("01", "METAL FIBER YARN", "金属纤维纱线",
             "能导电、能发热、<em>还能缝上去</em>",
             "金属纤维纱线由不锈钢等金属纤维经拉拔、捻搓与纺纱制成。除保留金属的高强度、导电导热与耐高温外，还具备纺织纤维的柔韧性与高比表面积，可直接机织、针织与缝制。",
             [("2", "μm", "最细纤维直径"), ("1–100", "Ω", "米电阻可调"), ("350–850", "℃", "耐温范围"), ("No.1", "", "电热面料市占率")],
             bg="img/yarn-fabric.webp")
 + f"""<section class="sec"><div class="wrap">
  <div class="g2 r7-5 wide">
    <div class="prose rv">
      <p class="lede">一句话定义：由金属纤维捻搓纺制而成的线材，兼具金属功能性与纺织加工性。</p>
      <h3>主要品类</h3>
      <ul>
        <li><strong>发热线</strong>：60 / 100 / 275 / 1000 芯，可包胶；米电阻 1–100Ω 可调，用于发热服饰、座椅加热、SCR 加热。</li>
        <li><strong>缝纫用线</strong>：本色与红色线，可上浆、PTFE 处理，用于导电缝合与接地搭接。</li>
        <li><strong>金属纤维纱</strong>：单纱支数 11/2、11/3、7/2 等股数规格，可上浆。</li>
        <li><strong>混纺纱</strong>：与芳纶、涤纶、PPS、棉等混纺，兼顾导电性与手感，水洗机洗不降低屏蔽能力。</li>
        <li><strong>机器人用线 / 智能穿戴信号线 / 导电刷</strong>：按客户线径与电阻要求定制。</li>
      </ul>
      <h3>性能特点</h3>
      <p>导电性来自纯金属本体，不依赖涂层，因此<strong>抗静电与电磁屏蔽能力不会因洗涤而衰减</strong>；同时具备耐高温、防切割、耐腐蚀与高比表面积等特性。</p>
    </div>
    <aside class="rv d1">
      <div class="gal" style="grid-template-columns:1fr 1fr">
        <figure><img src="img/yarn-thread.webp" alt="金属纤维缝纫线应用" loading="lazy"><figcaption>缝纫线</figcaption></figure>
        <figure><img src="img/yarn-heatpad.webp" alt="金属纤维发热片" loading="lazy"><figcaption>发热片</figcaption></figure>
        <figure><img src="img/yarn-wearable.webp" alt="智能发热马甲" loading="lazy"><figcaption>智能发热服</figcaption></figure>
        <figure><img src="img/yarn-carseat.webp" alt="汽车座椅加热" loading="lazy"><figcaption>座椅加热</figcaption></figure>
      </div>
      {cta_row('金属纤维纱线')}
    </aside>
  </div>

  <div class="sec-h" style="margin:88px 0 26px"><h2>规格与参数</h2></div>
  <div class="tbl-wrap"><table class="tbl">
    <thead><tr><th>品类</th><th>规格</th><th>材质</th><th>关键参数</th><th>典型应用</th></tr></thead>
    <tbody>
      <tr><td><b>发热线</b></td><td class="num">60 / 100 / 275 / 1000 芯</td><td>316L 不锈钢纤维</td><td>米电阻 1–100Ω（按股数调整），可包胶绝缘</td><td>发热马甲、围脖、鞋袜、毯子、汽车座椅、SCR 加热</td></tr>
      <tr><td><b>缝纫用线</b></td><td>本色 / 红色；可上浆、PTFE</td><td>316L 不锈钢纤维</td><td>按芯数、股数、米克重定制</td><td>导电缝合、接地搭接、电子标签缝制</td></tr>
      <tr><td><b>金属纤维纱</b></td><td class="num">11/2、11/3、7/2 等</td><td>316L / 304</td><td>单纱支数与股数可选，可上浆</td><td>机织布、针织面料、编织带</td></tr>
      <tr><td><b>混纺纱</b></td><td>按不锈钢纤维含量配比</td><td>不锈钢 + 芳纶 / 涤纶 / PPS / 棉</td><td>导电性随含量调整；耐水洗机洗</td><td>防静电工作服、防辐射服、屏蔽窗帘</td></tr>
      <tr><td><b>纤维条 / 预混条</b></td><td>平均长度 30–80mm</td><td>100% 不锈钢或混合纤维</td><td>可直接纺纱织布，分散性好</td><td>非织造导电纤维原料、防静电无纺布</td></tr>
    </tbody>
  </table></div>
  <p class="tnote">备注：① 纤维束材质含 316L、302、304、FeCrAl 等不锈钢及高温合金；② 除标准直径外，可按客户要求生产 4–100μm 纤维；③ 纤维束根数可调整；④ 纤维室温电阻随状态变化，如需限定请在询价时声明；⑤ 交货状态有直条与压花两种。</p>

  <div class="g2 wide" style="margin-top:84px">
    <div class="rv"><h2 style="font-family:'Noto Serif SC',serif;font-size:26px;font-weight:900;margin-bottom:20px">适用工况与选型建议</h2>
      <div class="prose">
        <p><strong>按功能选</strong>：只要导电防静电 → 混纺纱即可；要发热 → 选发热线并给出工作电压与目标功率，由工程师反推米电阻与芯数；要屏蔽 → 按屏蔽频段与屏蔽效能确定不锈钢纤维含量与织物结构。</p>
        <p><strong>按工艺选</strong>：机织优先选股线，针织优先选柔软的混纺纱，缝制选缝纫用线并注意针号匹配。</p>
        <p><strong>按环境选</strong>：长期高温或有明火风险选纯不锈钢纤维；需柔软手感与染色选混纺。</p>
      </div>
    </div>
    <div class="rv d1"><h2 style="font-family:'Noto Serif SC',serif;font-size:26px;font-weight:900;margin-bottom:20px">常见问题</h2>
      {faq_block([
        ("金属纤维纱线能做到多细？", "纤维直径可低至 2μm 并稳定量产；常规供货区间 4–100μm，可按客户要求定制。"),
        ("洗涤会不会让防静电失效？", "不会。导电性来自纯金属纤维本体而非涂层，可水洗与机洗，抗静电与电磁屏蔽能力不因洗涤降低，洗涤方式与普通面料相同。"),
        ("发热线的电阻能定制吗？", "可以。按工作电压与目标发热功率确定米电阻，常用总电阻范围 1–100Ω，通过芯数与股数组合实现。"),
        ("可以和哪些纤维混纺？", "芳纶、涤纶、PPS、棉等均可，按不锈钢纤维含量配比确定导电性与手感。"),
        ("能提供样品吗？", "可提供免费小样，运费到付；标准现货样品一般 1–3 天寄出。"),
      ])}
    </div>
  </div>
</div></section>"""
 + ENDCTA + footer())

# ════════════════ 2 金属纤维烧结毡
rows = [("10KIA3",10,0.3,75,3700,110),("15KIA3",15,0.37,75,2470,190),("20KIA3",20,0.45,80,1850,300),
        ("25KIA3",25,0.61,80,1480,350),("30KIA3",30,0.63,80,1230,500),("40KIA3",40,0.66,78,925,620),
        ("60KIA3",60,0.7,86,620,1200),("10KIA3K",10,1.1,85,3500,140),("15KIA3K",15,1.1,85,2400,250),
        ("20KIA3K",20,1.1,85,1700,350),("25KIA3K",25,1.1,85,1400,470),("10KIC4",10,0.4,72,3700,100),
        ("15KIC2",15,0.4,72,2470,150),("20KIC2",20,0.4,72,1850,200),("25KIC4",25,0.5,72,1480,280)]
trs = "".join(f'<tr><td><b>{a}</b></td><td class="num">{b}</td><td class="num">{c}</td><td class="num">{d}</td><td class="num">{e}</td><td class="num">{f}</td></tr>' for a,b,c,d,e,f in rows)

w('p-felt.html', head(
    "金属纤维烧结毡 | 精度 10–60μm 多层梯度孔滤材 — 强纶新材",
    "不锈钢金属纤维烧结毡，绝对过滤精度 10–60μm，孔隙率高、纳污量大、压损小、可清洗再生，耐 480℃，用于化纤熔体、黏胶过滤与高温气体除尘。",
    "金属纤维烧结毡,不锈钢纤维烧结毡,烧结滤毡,KKF滤机毡,熔体过滤,精度10微米",
    "p-felt.html", og_img="img/media-05.webp")
 + header('products.html')
 + crumb([("产品中心", "products.html"), ("金属纤维烧结毡", None)])
 + page_hero("02", "SINTERED FIBER FELT", "金属纤维烧结毡",
             "三维网络梯度孔，<em>纳污量大、升压慢</em>",
             "由微米级金属纤维无纺成网后经高温层压烧结而成。多层结构形成由粗到细的孔隙梯度，既能控制极高的过滤精度，又比单层获得更大的纳污量。",
             [("10–60", "μm", "绝对过滤精度"), ("72–86", "%", "过滤率"), ("480", "℃", "可用温度"), ("0.3–1.1", "mm", "厚度范围")],
             bg="img/media-03.webp")
 + f"""<section class="sec"><div class="wrap">
  <div class="g2 r7-5 wide">
    <div class="prose rv">
      <p class="lede">一句话定义：微米级金属纤维高温烧结而成的多层梯度孔过滤材料，是耐高温、耐腐蚀、高精度工况下的理想滤材。</p>
      <h3>产品特点</h3>
      <ul>
        <li>纳污量大、过滤精度高、升压慢、更换周期长；</li>
        <li>孔隙率高、渗透性好、压力损失小、流量大；</li>
        <li>耐腐蚀、耐高温，耐酸碱、有机溶剂与药物腐蚀，可在 480℃ 环境介质中使用；</li>
        <li>易于加工、成型与焊接；</li>
        <li>可按用户要求特殊生产，提供加强、加厚、密集网等多种规格。</li>
      </ul>
      <h3>行业位置</h3>
      <p>强纶金属烧结毡稳居黏胶行业国内首位，先后研制出国内<strong>首张 KKF 滤机烧结毡</strong>、<strong>最大规格 KKF 滤机烧结毡</strong>以及<strong>首张国产金属纤维针刺毡</strong>；针刺毡产品已应用于长征五号 B、长征五号遥五运载火箭发动机。</p>
    </div>
    <aside class="rv d1">
      <div class="gal" style="grid-template-columns:1fr 1fr">
        <figure><img src="img/media-05.webp" alt="金属纤维烧结毡" loading="lazy"><figcaption>烧结毡</figcaption></figure>
        <figure><img src="img/media-03.webp" alt="金属纤维烧结毡板材" loading="lazy"><figcaption>大幅面毡</figcaption></figure>
        <figure><img src="img/media-01.webp" alt="金属纤维烧结滤片" loading="lazy"><figcaption>烧结滤片</figcaption></figure>
        <figure><img src="img/media-02.webp" alt="烧结网与滤片" loading="lazy"><figcaption>烧结网</figcaption></figure>
      </div>
      {cta_row('烧结毡')}
    </aside>
  </div>

  <div class="sec-h" style="margin:88px 0 24px"><h2>技术参数表</h2><p>材质：不锈钢、镍、哈氏合金、铁合金、蒙乃尔合金、双相合金等。</p></div>
  <div class="tbl-wrap"><table class="tbl">
    <caption>Technology Parameter · 型号中的数字代表绝对过滤等级（μm）</caption>
    <thead><tr><th>系列型号</th><th class="num">绝对过滤等级 μm</th><th class="num">厚度 mm</th><th class="num">过滤率 %</th><th class="num">气泡点压 Pa</th><th class="num">200Pa 透气值</th></tr></thead>
    <tbody>{trs}</tbody>
  </table></div>
  <p class="tnote">* 各型号气泡点与透气值不同，上表为常规区间值；实际以出厂检验报告为准。可按客户要求定制加强、加厚、密集网等特殊规格。</p>

  <div class="g2 wide" style="margin-top:84px">
    <div class="rv"><h2 style="font-family:'Noto Serif SC',serif;font-size:26px;font-weight:900;margin-bottom:20px">主要用途</h2>
      <div class="prose">
        <p>用于化纤、聚酯薄膜、油脂、石油制品等行业的<strong>液体过滤及气固分离</strong>：高分子聚合物熔体过滤、黏胶过滤、高温气体除尘、超滤器预过滤、真空泵保护过滤器、滤膜支撑体、飞机舰船燃油过滤、液压系统过滤等。</p>
        <h3>选型建议</h3>
        <p><strong>先定精度</strong>：按下游产品对杂质的要求确定绝对过滤等级；<strong>再看压差</strong>：流量大、要求升压慢时选高孔隙率、大透气值型号（如 40/60KIA3）；<strong>最后看结构</strong>：需要更大纳污量与机械强度时选 KIA3K 系列（厚度 1.1mm）。</p>
      </div>
    </div>
    <div class="rv d1"><h2 style="font-family:'Noto Serif SC',serif;font-size:26px;font-weight:900;margin-bottom:20px">常见问题</h2>
      {faq_block([
        ("烧结毡和滤布怎么选？", "高温、高粘度或腐蚀性工况下选金属纤维烧结毡：耐温耐腐蚀且可清洗再生；常温、低要求工况可用滤布。具体以介质、温度与精度要求为准。"),
        ("能清洗再用吗？", "可以。金属纤维烧结滤材耐高温耐腐蚀，可反复清洗再生，有效克服金属网易堵塞易碎、滤纸滤布不耐高温高压的缺陷。"),
        ("最高能用到多少温度？", "常规金属纤维烧结毡可在 480℃ 环境介质中使用；更高温度需改用铁铬铝等耐热合金纤维，请在询价时说明工况温度。"),
        ("气泡点压和透气值代表什么？", "气泡点压反映最大孔径，数值越高孔径越细、精度越高；200Pa 透气值反映通过能力，数值越大压损越小、流量越大。两者通常此消彼长。"),
        ("可以做多大幅面？", "可按设备要求定制，公司已研制出最大规格 KKF 滤机烧结毡；超大幅面请提供设备型号与护网尺寸。"),
      ])}
    </div>
  </div>
</div></section>"""
 + ENDCTA + footer())
print('纱线 / 烧结毡 完成')
