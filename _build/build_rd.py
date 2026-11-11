# -*- coding: utf-8 -*-
"""科研创新子页：核心技术平台 / 研发中心与实验室 / 检测能力 / 专利与标准 / 产学研 / 科研成果"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from layout import head, header, crumb, page_hero, footer
from common import w, ENDCTA, rnav

# ════════ 核心技术平台（4 个方向）
PLAT = [
 ("01","超细纤维制备","复合拉拔核心工艺，将金属棒逐级拉拔成丝、再拉成纤维，最细可至 2μm，比头发丝细约 35 倍。材质覆盖 316L、304、铁铬铝、镍、钛、铜等。",
  "img/media-01.webp","纤维纱线 · 烧结毡",["直径低至 2μm 稳定量产","可按客户要求生产 4–100μm","纤维束根数可调整","直条与压花两种交货状态"]),
 ("02","烧结成型","多层梯度孔结构高温层压烧结，使纤维交点扩散结合形成整体刚性，兼顾过滤精度与纳污量，可焊接、可机加工、可反复清洗再生。",
  "img/media-05.webp","烧结毡 · 烧结网",["绝对精度 10–60μm","孔隙率 72%–86%","耐 480℃ 环境介质","可定制加强、加厚、密集网"]),
 ("03","过滤设备","从滤材到元件再到成套装备的自制能力：滤芯骨架、过滤器壳体、收油系统的精密加工、焊接与装配，以及过滤应用试验与效果分析。",
  "img/fts-site-bamo.webp","过滤元件 · 成套设备",["最大单套处理量 600 m³/h","可做过滤应用试验","设计过滤技术方案","产品应用效果分析"]),
 ("04","导电发热应用","金属纤维可纺可织，制成导电纱、发热线、信号线与发热织物。热量通过纺织材料均匀分布，有效防止热点，弯曲寿命长。",
  "img/yarn-heatpad.webp","纱线 · 智能穿戴",["米电阻 1–100Ω 可调","60/100/275/1000 芯","电热面料市占率全国第一","发热服已用于冬奥会"]),
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
    "lab.html", og_img="img/lab-01.webp")
 + header('rd.html')
 + crumb([("科研创新", "rd.html"), ("研发中心与实验室", None)])
 + page_hero("03", "R&D CENTER", "研发中心与实验室",
             "研发源于车间实践，<em>创新用于高端领域</em>",
             "强纶新材料创新研究院不同于其他科研院所：研发从车间里的真实问题出发，成果应用于航空航天等高端先进领域，拥有高端研究团队、创业团队、中试基地以及多维测试中心。",
             [("6","个","研究室"),("5","大","制研平台"),("12","%+","研发投入占收入"),("200","+","员工人数")],
             bg="img/lab-02.webp")
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

  <div class="sec-h" style="margin:86px 0 26px"><h2>实验室与中试</h2></div>
  <div class="gal c3">
    <figure><img src="img/lab-01.webp" alt="强纶实验室" loading="lazy"><figcaption>材料与应用实验室</figcaption></figure>
    <figure><img src="img/lab-02.webp" alt="中试基地" loading="lazy"><figcaption>中试基地</figcaption></figure>
    <figure><img src="img/plant-08.webp" alt="检测与试验设备" loading="lazy"><figcaption>检测与试验设备</figcaption></figure>
  </div>
  <div class="note" style="margin-top:34px"><b>VR 全景展示位置已预留</b>：甲方提供第三方 VR 全景链接后，由后台嵌入本页与首页；链接到期可更换或取消该板块。</div>
</div></section>"""
 + ENDCTA + footer())

# ════════ 检测能力
w('testing.html', head(
    "检测能力 | 检测项目 · 设备清单 · 报告类型 — 强纶新材",
    "强纶可出具的检测项目：绝对过滤等级、过滤效率、孔隙率、气泡点压强、透气度、厚度与面密度等，并可按订单约定提供 ROHS 等第三方检测报告。",
    "过滤材料检测,气泡点检测,透气度检测,孔隙率,检测报告,ROHS",
    "testing.html")
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
      <tr><td><b>电性能</b></td><td>室温电阻、米电阻；如需精确电阻指标可提供试样实测</td><td>导电纱、发热线、织物</td></tr>
      <tr><td><b>第三方检测</b></td><td>ROHS 四项等，由第三方机构出具（如金属纤维线 275×3，2026.05.16）</td><td>按订单约定</td></tr>
    </tbody>
  </table></div>

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
      <div class="gal c3" style="grid-template-columns:1fr;margin-top:20px"><figure><img src="img/plant-08.webp" alt="检测与试验设备" loading="lazy"><figcaption>检测与试验设备</figcaption></figure></div>
    </div>
  </div>
</div></section>"""
 + ENDCTA + footer())
print('技术平台 / 实验室 / 检测 完成')
