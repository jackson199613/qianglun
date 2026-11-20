# -*- coding: utf-8 -*-
"""科研创新子页：核心技术平台 / 研发中心与实验室 / 检测能力 / 专利与标准 / 产学研 / 科研成果"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from layout import head, header, crumb, page_hero, footer
from common import w, ENDCTA, rnav, vr_block

# ════════ 核心技术平台（4 个方向）
PLAT = [
 ("01","超细纤维制备","复合拉拔核心工艺，将金属棒逐级拉拔成丝、再拉成纤维，最细可至 2μm，比头发丝细约 35 倍。材质覆盖 316L、304、铁铬铝、镍、钛、铜等。",
  "img/media-01.webp","纤维纱线 · 烧结毡",["直径低至 2μm 稳定量产","可按客户要求生产 4–100μm","直条与压花两种交货状态"]),
 ("02","烧结成型","多层梯度孔结构高温层压烧结，使纤维交点扩散结合形成整体刚性，兼顾过滤精度与纳污量，可焊接、可机加工、可反复清洗再生。",
  "img/jl-felt.webp","烧结毡 · 烧结网",["绝对精度 10–60μm","孔隙率 72%–86%","耐 480℃ 环境介质","可定制加强、加厚、密集网"]),
 ("03","过滤设备","从滤材到元件再到成套装备的自制能力：滤芯骨架、过滤器壳体、收油系统的精密加工、焊接与装配，以及过滤应用试验与效果分析。",
  "img/fts-site-bamo.webp","过滤元件 · 成套设备",["最大单套处理量 600 m³/h","可做过滤应用试验","设计过滤技术方案","产品应用效果分析"]),
 ("04","导电发热应用","金属纤维可纺可织，制成导电纱、金属纤维线、信号线与发热织物。热量通过纺织材料均匀分布，有效防止热点，弯曲寿命长。",
  "img/yarn-heatpad.webp","纱线 · 智能穿戴",["米电阻 1–100Ω 可调","100/275/1000","电热面料市占率全国第一","发热服已用于冬奥会"]),
]
plat_cards = "".join(f"""<article class="mcard rv">
  <div class="im"><img src="{img}" alt="{t}" loading="lazy"></div>
  <div class="bd"><div class="cat">{n} · {tag}</div><h3>{t}</h3><p>{d}</p>
  <ul class="ticks">{"".join(f'<li><svg class="i"><use href="#i-check"/></svg>{x}</li>' for x in pts)}</ul></div>
</article>""" for n, t, d, img, tag, pts in PLAT)

w('platforms.html', head(
    "核心技术平台 | 超细纤维制备 · 烧结成型 · 过滤设备 · 导电发热 — 强纶新材",
    "强纶四大核心技术平台：超细纤维制备（2μm 稳定量产）、烧结成型（10–60μm 梯度孔）、过滤设备（最大 600 m³/h）与导电发热应用（米电阻 1–100Ω）。",
    "超细纤维制备,复合拉拔,烧结成型,过滤设备,导电发热,核心技术",
    "platforms.html", og_img="img/media-01.webp")
 + header('rd.html')
 + crumb([("科研创新", "rd.html"), ("核心技术平台", None)])
 + page_hero("02", "PLATFORMS", "核心技术平台",
             "四个平台，<em>撑起一条产业链</em>",
             "从把金属拉成纤维，到把纤维烧成滤材，再到把滤材做成设备——四个技术平台互相衔接，构成强纶自主可控的完整能力。")
 + f"""<section class="sec"><div class="wrap">{rnav(1)}
  <div class="g2" style="gap:22px">{plat_cards}</div>
  <div class="note" style="margin-top:44px"><b>五大制研支撑平台</b>：金属复合丝拉拔（金纶新材料）、压制烧结（金山粉末）、纺纱编织（柔银新材料）、电化学材料加工（强纶新材）、精密机械加工（龙象机械），并设有氢能源研究室开展新能源板块开发。</div>
</div></section>"""
 + ENDCTA + footer())

# ════════ 研发中心与实验室
ROOMS = [
 ("流体净化研究室","黄朝强 · 董事长兼技术总工","过滤净化方向研发，已成功研制纯物理方法将油与水分离的设备。福建省创业之星人才、全国筛标委副秘书长、中国化工学会过滤与分离行业专家。"),
 ("氢能源研究室","陈作锋 · 同济大学教授","国家高层次青年人才，研发方向为能源电催化、氢能开发以及新能源材料。"),
 ("金属橡胶研究室","张明 · 技术副总工","资深研究员、国家级科技成果评审专家，负责金属橡胶材料、减震吸能结构与航空航天发动机配套方向的研发。"),
 ("电化学研究室","方惠会 · 公司董事","中南大学教授级高工，主要进行多孔材料、新能源方向的研发。"),
 ("金属学研究室","孙锦辉 · 博士","金属显微组织与强韧化、多孔金属吸油耐磨性能研究。"),
 ("多孔介质燃烧研究室","李工 · 高级工程师","原龙工高级工程师，负责低热值燃烧技术、高温除尘材料及设备研发。"),
]
room_cards = "".join(f'<article class="card rv"><h3>{t}</h3><p style="color:var(--champ-ink);font-size:13.5px;margin-top:6px">{who}</p><p>{d}</p></article>' for t, who, d in ROOMS)

w('lab.html', head(
    "研发中心与实验室 | 强纶新材料创新研究院",
    "强纶新材料创新研究院设有流体净化、氢能源、金属橡胶、电化学、金属学、多孔介质燃烧六个研究室，拥有省级新型研发机构、省级企业技术中心与博士后创新实践基地。",
    "强纶研究院,研发中心,实验室,省级新型研发机构,博士后创新实践基地",
    "lab.html", og_img="img/lab-wide-01.webp")
 + header('rd.html')
 + crumb([("科研创新", "rd.html"), ("研发中心与实验室", None)])
 + page_hero("03", "R&D CENTER", "研发中心与实验室",
             "研发源于车间实践，<em>创新用于高端领域</em>",
             "强纶新材料创新研究院不同于其他科研院所：研发从车间里的真实问题出发，成果应用于航空航天等高端先进领域，拥有高端研究团队、创业团队、中试基地以及多维测试中心。",
             [("6","个","研究室"),("5","大","制研平台"),("12","%+","研发投入占收入"),("200","+","员工人数")],
             bg="img/lab-wide-01.webp")
 + f"""<section class="sec"><div class="wrap">{rnav(2)}
  <div class="sec-h"><h2>六个研究室</h2><p>每个研究室由一位技术带头人负责，覆盖从基础材料到应用装备的完整链条。</p></div>
  <div class="g3">{room_cards}</div>

  <div class="sec-h" style="margin:86px 0 26px"><h2>研发团队</h2></div>
  <div class="tbl-wrap"><table class="tbl">
    <thead><tr><th>姓名</th><th>职务</th><th>背景与方向</th></tr></thead>
    <tbody>
      <tr><td><b>黄朝强</b></td><td>董事长兼总工（领军）</td><td>中南大学硕士，深耕金属纤维行业 30 余年，行业国标牵头制定人，福建省 C 类高层次人才</td></tr>
      <tr><td><b>方惠会</b></td><td>副总经理</td><td>原中南大学高级工程师／副教授，负责烧结毡研发生产销售，参与多项国家级科研项目与国标编制</td></tr>
      <tr><td><b>黄昊辰</b></td><td>总经理</td><td>长沙理工大学学士，助理工程师，负责经营管理，主持多项市厅级科技项目，专利成果丰富</td></tr>
      <tr><td><b>孙锦辉</b></td><td>金属材料研究员</td><td>材料加工工程硕士，主攻金属微丝强韧化、多孔材料性能，发表多篇 SCI／EI 论文</td></tr>
      <tr><td><b>胡剑锋</b></td><td>市场项目主管</td><td>有色金属冶金硕士，负责新能源、资源回收方向应用技术开发</td></tr>
    </tbody>
  </table></div>

  <div class="sec-h" style="margin:86px 0 26px"><h2>实验室实景</h2>
    <p>材料与应用实验室、样品前处理区、仪器分析区与电镜室，以下均为实拍。</p></div>
  <div class="gal bento">
    <figure class="big"><img src="img/lab-wide-01.webp" alt="强纶材料与应用实验室全景" loading="lazy"><figcaption>材料与应用实验室</figcaption></figure>
    <figure><img src="img/lab-chem-02.webp" alt="分析天平与试剂区" loading="lazy"><figcaption>分析天平与试剂区</figcaption></figure>
    <figure><img src="img/lab-op-01.webp" alt="检测数据采集工作站" loading="lazy"><figcaption>检测数据采集工作站</figcaption></figure>
  </div>
  <div class="gal c3" style="margin-top:14px">
    <figure><img src="img/lab-chem-01.webp" alt="通风橱与样品前处理区" loading="lazy"><figcaption>通风橱与样品前处理</figcaption></figure>
    <figure><img src="img/lab-chem-03.webp" alt="滴定与比色分析区" loading="lazy"><figcaption>滴定与比色分析</figcaption></figure>
    <figure><img src="img/lab-chem-04.webp" alt="化学分析实验台" loading="lazy"><figcaption>化学分析实验台</figcaption></figure>
    <figure><img src="img/lab-chem-05.webp" alt="试剂与耗材储备区" loading="lazy"><figcaption>试剂与耗材储备</figcaption></figure>
    <figure><img src="img/lab-wide-02.webp" alt="实验室洁净区" loading="lazy"><figcaption>实验室洁净区</figcaption></figure>
    <figure><img src="img/lab-op-02.webp" alt="仪器操作与数据读取" loading="lazy"><figcaption>仪器操作与数据读取</figcaption></figure>
  </div>

</div></section>"""
 + vr_block("img/lab-wide-02.webp", "实验室与检测区全景", "无需到场即可查看实验室布局、检测设备与样品处理区，配合检测能力清单一起看更直观。")
 + ENDCTA + footer())

# ════════ 检测能力
w('testing.html', head(
    "检测能力 | 检测项目 · 设备清单 · 报告类型 — 强纶新材",
    "强纶可出具的检测项目：绝对过滤等级、过滤效率、孔隙率、气泡点压强、透气度、厚度与面密度等，并可按订单约定提供 ROHS 等第三方检测报告。",
    "过滤材料检测,气泡点检测,透气度检测,孔隙率,检测报告,ROHS",
    "testing.html", og_img="img/eq-sem.webp")
 + header('rd.html')
 + crumb([("科研创新", "rd.html"), ("检测能力", None)])
 + page_hero("04", "TESTING", "检测能力",
             "参数不是标出来的，<em>是测出来的</em>",
             "公司拥有一系列专业测试仪器和完善的材料性能分析体系，并可进行过滤应用试验、设计过滤技术方案与产品应用效果分析。")
 + f"""<section class="sec"><div class="wrap">{rnav(3)}
  <div class="sec-h"><h2>检测项目</h2><p>以下为常规可出具的检测项目，具体以订单约定为准。</p></div>
  <div class="tbl-wrap"><table class="tbl">
    <thead><tr><th>检测项目</th><th>说明</th><th>适用产品</th></tr></thead>
    <tbody>
      <tr><td><b>绝对过滤等级</b></td><td>滤材能够基本全部拦截的颗粒尺寸，单位 μm</td><td>烧结毡、烧结网、滤芯</td></tr>
      <tr><td><b>过滤效率</b></td><td>对指定粒径颗粒的拦截比例，如气体过滤 99.9% @ 1μm</td><td>烧结毡、滤芯</td></tr>
      <tr><td><b>孔隙率</b></td><td>孔隙体积占总体积百分比，典型值 72%–86%</td><td>烧结毡、多孔材料</td></tr>
      <tr><td><b>平均起泡压强</b></td><td>反映平均最大孔径，偏差通常 ±10%</td><td>烧结毡、滤芯</td></tr>
      <tr><td><b>第一起泡压强</b></td><td>反映最大单个孔径，用于判断是否存在缺陷孔</td><td>烧结毡、滤芯</td></tr>
      <tr><td><b>透气度</b></td><td>规定压差下单位面积通气量，如 71 L/min/dm² @ 200Pa</td><td>烧结毡、织物</td></tr>
      <tr><td><b>厚度与面密度</b></td><td>厚度 mm 与单位面积克重</td><td>烧结毡、织物、织带</td></tr>
      <tr><td><b>力学性能</b></td><td>强力、耐压、耐磨等</td><td>纱线、织物、滤芯</td></tr>
      <tr><td><b>电性能</b></td><td>米电阻；如需精确电阻指标可提供试样实测</td><td>导电纱、金属纤维线、织物</td></tr>
      <tr><td><b>第三方检测</b></td><td>ROHS 四项等，由第三方机构出具（如金属纤维线 275×3，2026.05.16）</td><td>按订单约定</td></tr>
    </tbody>
  </table></div>

  <div class="sec-h" style="margin:86px 0 26px"><h2>检测设备</h2>
    <p>以下为公司自有的主要分析设备，均为实拍。复杂课题可联合高校院所共同攻关。</p></div>
  <div class="g2 wide">
    <div class="rv">
      <figure class="eqfig"><img src="img/sem-screen.webp" alt="扫描电镜下的金属纤维形貌与能谱分析" loading="lazy">
        <figcaption><b>形貌与成分同步分析</b>电镜下可直接读出纤维直径、搭接形态与烧结结合点，配合能谱判定元素组成。</figcaption></figure>
    </div>
    <div class="rv d1">
      <div class="eqlist">
        <div class="eq"><img src="img/eq-sem.webp" alt="KYKY-EM8000F 扫描电子显微镜" loading="lazy">
          <div><h4>扫描电子显微镜</h4><span class="mod">KYKY-EM8000F</span>
            <p>纤维直径与直径分布、三维搭接形貌、烧结结合点质量、多层毡的断面梯度结构。</p></div></div>
        <div class="eq"><img src="img/eq-afs.webp" alt="GGX-810 原子荧光光度计" loading="lazy">
          <div><h4>原子荧光光度计</h4><span class="mod">GGX-810</span>
            <p>金属元素含量分析，用于材质判定、杂质控制与来料验证。</p></div></div>
        <div class="eq"><img src="img/eq-sem-col.webp" alt="电镜镜筒与探测器" loading="lazy">
          <div><h4>电镜镜筒与探测器</h4><span class="mod">二次电子 / 背散射</span>
            <p>不同探测模式分别用于表面形貌与成分衬度观察。</p></div></div>
        <div class="eq"><img src="img/sem-sample.webp" alt="电镜样品仓装样" loading="lazy">
          <div><h4>样品制备与装载</h4><span class="mod">样品仓</span>
            <p>纤维与毡材的取样、固定与导电处理，直接影响成像质量与结果可比性。</p></div></div>
      </div>
    </div>
  </div>

  <div class="sec-h" style="margin:86px 0 26px"><h2>线材检测报告</h2>
    <p>以金属纤维线为例，下列报告均已出具，可按订单需要提供。</p></div>
  <div class="tbl-wrap"><table class="tbl">
    <thead><tr><th>报告名称</th><th>检测内容</th><th>出具方</th></tr></thead>
    <tbody>
      <tr><td><b>ROHS 四项</b>（1000×3 / 275×3 / 100×3）</td><td>铅、镉、汞、六价铬限值，2026.05.16</td><td>第三方机构</td></tr>
      <tr><td><b>材质报告</b>（275×3，316L）</td><td>材质成分验证，2026.05.13；另备英文版</td><td>第三方机构</td></tr>
      <tr><td><b>拉伸试验报告</b></td><td>金属纤维线抗拉强度与断裂伸长</td><td>本公司实验室</td></tr>
      <tr><td><b>水洗前后电阻</b></td><td>水洗循环前后的电阻变化，验证导电持久性</td><td>本公司实验室</td></tr>
      <tr><td><b>远红外性能报告</b></td><td>远红外发射率，用于发热与功能纺织应用</td><td>第三方机构</td></tr>
      <tr><td><b>红外反射能谱</b></td><td>红外波段反射特性</td><td>第三方机构</td></tr>
      <tr><td><b>磁性报告</b></td><td>磁性能表征，用于屏蔽与特殊工况选型</td><td>第三方机构</td></tr>
    </tbody>
  </table></div>
  <p class="tnote" style="margin-top:14px">以上为金属纤维线的既有报告清单。其他产品线的报告可按订单约定出具或委托第三方检测。</p>

  <div class="g2 wide" style="margin-top:82px">
    <div class="prose rv">
      <h3 style="margin-top:0">报告类型</h3>
      <p><strong>出厂检验报告</strong>：随货交付，含该批次的精度、气泡点、透气值、厚度与外观检验结果，可追溯到批次号与工艺参数。</p>
      <p><strong>型式检验报告</strong>：针对新型号或新工艺的完整性能验证。</p>
      <p><strong>第三方检测报告</strong>：按客户或出口要求，委托第三方机构检测并出具，如 ROHS 四项。</p>
      <h3>过滤应用试验</h3>
      <p>公司可进行过滤应用试验，为客户设计过滤技术方案并分析产品应用效果；对液体情况复杂的客户，可免费提供前期实验设备及技术人员入厂试验。</p>
    </div>
    <div class="rv d1">
      <div class="note"><b>外部技术支持</b><br>与天津大学、上海化工研究院、中南大学、厦门大学、同济大学等院校保持长期合作交流，复杂课题可联合攻关。</div>
      <div class="gal c3" style="grid-template-columns:1fr;margin-top:20px"><figure><img src="img/lab-op-02.webp" alt="仪器操作与数据读取" loading="lazy"><figcaption>仪器操作与数据读取</figcaption></figure></div>
    </div>
  </div>
</div></section>"""
 + ENDCTA + footer())
print('技术平台 / 实验室 / 检测 完成')
