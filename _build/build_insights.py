# -*- coding: utf-8 -*-
"""技术专栏：技术文章列表 / 常见问题库 / 术语百科 + 文章与问答详情模板"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from layout import head, header, crumb, page_hero, footer, SITE
from common import w, ENDCTA, inav
from build_lines import faq_block

ARTS = [
 ("选型","烧结毡和滤布到底怎么选？四个判断条件","2026-10-28","从介质温度、腐蚀性、精度要求与再生需求四个维度，给出金属纤维烧结毡与常规滤布的分界线。","article-1.html"),
 ("对比","气泡点压和透气值，为什么总是此消彼长","2026-10-14","用孔径分布解释两个参数的物理含义，以及选型时如何在精度与流量之间取平衡。","article-2.html"),
 ("应用","化纤熔体过滤：精度选高了会怎样","2026-09-30","精度并非越高越好。结合纺丝规格与换网周期，说明过度收紧精度带来的压差与成本代价。","article-3.html"),
 ("原理","预除油为什么能省下深度除油的钱","2026-09-18","从溶解度与运行成本出发，解释「预除油 + 深度除油」组合方案的经济性。","article-4.html"),
 ("应用","玻璃钢化炉上的金属纤维套管，解决的是哪三个问题","2026-09-05","划伤、掉屑与老化——耐高温包覆材料在玻璃深加工线上的实际价值。","article-5.html"),
 ("原理","为什么金属纤维的屏蔽能力不会被洗掉","2026-08-22","涂层导电与本体导电的区别，以及混纺纱在反复水洗后的性能表现。","article-6.html"),
 ("选型","发热线怎么定米电阻：从电压和功率反推","2026-08-08","给出按工作电压与目标功率计算米电阻的方法，以及芯数股数的组合思路。","article-7.html"),
 ("对比","金属纤维烧结毡 vs 金属丝网：强度、精度与再生性","2026-07-25","两类金属滤材的结构差异，决定了它们各自适合的工况边界。","article-8.html"),
]
art_rows = "".join(f'<a class="row-i" href="{u}" data-tag="{c}"><span class="dt">{d}</span><div><h4>{t}</h4><p>{s}</p></div><span class="tg">{c}</span></a>' for c, t, d, s, u in ARTS)

w('insights.html', head(
    "技术专栏 | 选型、对比、应用与原理文章 — 强纶新材",
    "强纶技术专栏：金属纤维与过滤材料的选型方法、参数对比、行业应用与工作原理解析，由一线工程师整理，面向采购与技术人员。",
    "金属纤维技术文章,过滤选型文章,烧结毡对比,技术专栏",
    "insights.html")
 + header('insights.html')
 + crumb([("技术专栏", None)])
 + page_hero("01", "INSIGHTS", "技术文章",
             "工程师写给<em>工程师</em>的文章",
             "不讲概念，只讲工况。这里整理的是客户在选型、调试与运行中真正会遇到的问题，以及我们给出的判断依据。", bg="img/ph-insights.webp")
 + f"""<section class="sec"><div class="wrap">{inav(0)}
  <nav class="pillbar" data-filter=".row-i" aria-label="文章分类">
    <button class="on" data-v="all">全部</button><button data-v="选型">选型</button><button data-v="对比">对比</button><button data-v="应用">应用</button><button data-v="原理">原理</button>
  </nav>
  <div class="rows">{art_rows}</div>
  <div class="note" style="margin-top:40px"><b>内容更新</b>：技术文章由公司技术团队持续撰写，后台可自主发布与编辑。欢迎提出您关心的选型话题。</div>
</div></section>"""
 + ENDCTA + footer())

# ════════ 常见问题库（汇总各产品线 FAQ）
FAQ_ALL = [
 ("烧结毡","强纶的不锈钢纤维最细能做到多少？","超细不锈钢纤维直径可低至 2μm，并已实现稳定量产；常规供货区间 4–100μm，可按客户要求定制。"),
 ("烧结毡","烧结毡和滤布怎么选？","高温、高粘度或腐蚀性工况下选金属纤维烧结毡：耐温耐腐蚀且可清洗再生；常温、低要求工况可用滤布。具体以介质、温度与精度要求为准。"),
 ("烧结毡","最高能用到多少温度？","常规金属纤维烧结毡可在 480℃ 环境介质中使用；更高温度需改用铁铬铝等耐热合金纤维，请在询价时说明工况温度。"),
 ("烧结毡","气泡点压和透气值代表什么？","气泡点压反映最大孔径，数值越高孔径越细、精度越高；200Pa 透气值反映通过能力，数值越大压损越小、流量越大。两者通常此消彼长。"),
 ("滤芯","金属纤维滤芯能清洗再用吗？","可以。金属纤维烧结滤材耐高温、耐腐蚀，可反复清洗再生，寿命远长于滤纸滤布类产品。"),
 ("滤芯","化纤熔体过滤该选多少精度？","取决于纤维品种、纺丝规格与熔体洁净度要求。建议提供产品规格与现用滤材情况，由强纶工程师结合叶片滤盘与烧结滤芯给出精度方案。"),
 ("滤芯","可以按进口滤芯复刻吗？","可以。提供图纸或实物样品即可测绘复刻，公司已有多个进口替代批量供货案例。"),
 ("滤芯","是否支持非标定制与打样？","支持。可根据过滤精度、工况温度、介质、尺寸与接口等参数定制并提供样品测试。"),
 ("纱线","洗涤会不会让防静电失效？","不会。导电性来自纯金属纤维本体而非涂层，可水洗与机洗，抗静电与电磁屏蔽能力不因洗涤降低，洗涤方式与普通面料相同。"),
 ("纱线","发热线的电阻能定制吗？","可以。按工作电压与目标发热功率确定米电阻，常用总电阻范围 1–100Ω，通过芯数与股数组合实现。"),
 ("纱线","可以和哪些纤维混纺？","芳纶、涤纶、PPS、棉等均可，按不锈钢纤维含量配比确定导电性与手感。"),
 ("织物","材质都是 316L 吗？有其他材质可选吗？","标准材质均为 316L 不锈钢纤维；如需更高耐蚀、更高耐温，可定制铁铬铝材质，起订量另议。"),
 ("织物","标注耐温 350~1100℃，是长期连续使用温度吗？","350℃ 为长期连续推荐使用温度；短时峰值可以到 1100℃，不建议长时间持续使用，高温有氧环境下氧化速率会明显加快。"),
 ("织物","会不会掉屑掉丝、污染玻璃或精密工件？","成品经过后整理定型工艺，正常裁切使用不易起毛掉屑；但尖锐切口、强摩擦工况下，建议预先做封边处理。"),
 ("织物","按米计价吗？最小起订量多少？","标准规格按米销售；常规现货小批量几米即可试样；特殊定制规格有最低起订长度。"),
 ("收油系统","强纶收油系统是什么？主要解决什么问题？","功能纤维除油系统，通过前置过滤器与油水分离器实现油水分离，用于去除工艺溶液中的非溶解油并回收油份，定位于预除油环节。"),
 ("收油系统","除油效果如何？","以衢州 15 m³/h 项目为例，硫酸钴溶液除油率稳定在 70%，已使用 3 年；不同工况出口含油量一般在 5—30 mg/L 区间。"),
 ("收油系统","处理量范围多大？","罐式适用 ≤30 m³/h 的小流量需求；槽式及槽体改造方案适用于大流量场景，目前最大单套处理量 600 m³/h。"),
 ("收油系统","除油组件需要更换吗？","不需要频繁更换。核心材料为表面改性的金属/化学滤芯，可长期使用，最长应用 5 年未更换。"),
 ("收油系统","设备投资回收期多长？","镍钴行业应用证明，1—2 年即可回收设备投资成本。"),
 ("通用","能提供样品吗？试样周期多久？","可以提供免费小样（少量长度 / 少量面积），运费到付；标准现货样品 1~3 天寄出。"),
 ("通用","产品是否附检测报告？","可提供检验报告；报告类型与检测项目见检测能力页，具体以订单约定为准。"),
]
groups = {}
for c, q, a in FAQ_ALL: groups.setdefault(c, []).append((q, a))
faq_blocks = ""
for c, items in groups.items():
    qs = "".join(f'<div class="qa" data-tag="{c}"><button type="button" aria-expanded="false"><span class="n num">{i+1:02d}</span><span>{q}</span><span class="pm"><svg class="i"><use href="#i-x"/></svg></span></button><div class="ans"><div><p>{a}</p></div></div></div>' for i, (q, a) in enumerate(items))
    faq_blocks += f'<h3 class="rv" style="font-family:\'Noto Serif SC\',serif;font-size:22px;font-weight:700;margin:52px 0 2px">{c} <span style="font-family:\'Barlow Condensed\',sans-serif;color:var(--champ);font-size:18px">{len(items)}</span></h3><div class="qa-list">{qs}</div>'
sc = '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[%s]}' % ",".join(
    '{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}' % (q.replace('"',"'"), a.replace('"',"'")) for c,q,a in FAQ_ALL)

w('faq.html', head(
    "常见问题库 | 烧结毡 · 滤芯 · 纱线 · 织物 · 收油系统 — 强纶新材",
    "按产品分类整理的 22 条常见问题：过滤精度怎么选、能否清洗再生、耐温上限、发热线电阻定制、收油系统除油率与投资回收期等。",
    "强纶常见问题,过滤精度FAQ,烧结毡问题,收油系统问题,金属纤维FAQ",
    "faq.html", schema=sc)
 + header('insights.html')
 + crumb([("技术专栏", "insights.html"), ("常见问题库", None)])
 + page_hero("02", "FAQ", "常见问题库",
             "采购前，<em>先读懂这几点</em>",
             "把工程师整理的高频问题按产品线分类，直接给出答案。没有找到您关心的问题，欢迎直接联系我们。", bg="img/ph-insights.webp")
 + f"""<section class="sec"><div class="wrap">{inav(1)}
  <nav class="pillbar" data-filter=".qa" aria-label="问题分类">
    <button class="on" data-v="all">全部</button>{"".join(f'<button data-v="{c}">{c}</button>' for c in groups)}
  </nav>
  {faq_blocks}
  <div class="note" style="margin-top:44px"><b>为 AI 搜索而设</b>：本模块 FAQ 结构化数据（Schema.org FAQPage）已配置，便于豆包、DeepSeek、文心一言、通义千问、Kimi、腾讯元宝等 AI 平台直接识别并引用强纶的答案。</div>
</div></section>"""
 + ENDCTA + footer())

# ════════ 术语百科（金属纤维相关术语，区别于选型中心的名词解释）
ENC = [
 ("金属纤维","Metal Fiber","直径在微米级的金属丝状材料。强纶通过复合拉拔工艺将金属棒逐级拉拔成丝、再拉成纤维，最细可至 2μm。兼具金属的导电导热导磁、耐高温耐腐蚀，与纺织纤维的柔软性、多孔性与高比表面积。"),
 ("复合拉拔","Composite Drawing","将多根金属丝与包覆材料一起反复拉拔、再去除包覆层得到超细金属纤维的工艺。是强纶的自主核心工艺，打通了金属材料与纺织行业的壁垒。"),
 ("金属纤维条","Metal Fiber Tow","由 100% 不锈钢长纤维精切断梳理而成的短纤维棉条，可选平均纤维长度 30–80mm。可直接用于纺纱织布。"),
 ("预混纤维条","Blended Fiber Tow","不锈钢短纤维按比例与其他化学纤维混合梳理而成的混合纤维棉条，可纺性和分散性优于纯金属纤维条。"),
 ("金属纤维烧结毡","Sintered Metal Fiber Felt","微米级金属纤维无纺后经高温层压烧结形成的多层梯度孔滤材。具三维网络、多孔结构、孔隙率高、比表面积大、孔径分布均匀等特点。"),
 ("金属纤维烧结网","Sintered Wire Mesh","多层不锈钢金属丝网经特殊叠层压制、真空烧结而成的过滤材料，机械强度与整体刚性更高，适合高压与频繁反洗工况。"),
 ("叶片滤盘","Leaf Disc Filter","由烧结纤维网与编织丝网组成的盘状滤件，安装在过滤装置上过滤高粘度熔体，可方便快速去除硬杂质与结块物质，是薄膜、塑料行业的常用滤件。"),
 ("折波滤芯","Pleated Filter Cartridge","将滤材折叠成波纹状以在相同外径下获得更大过滤面积的滤芯形式。流量更大、压差更低、更换周期更长。"),
 ("气体扩散层","Gas Diffusion Layer","制氢设备中用于均匀分配气体并导电导热的多孔层。金属纤维毡因兼具多孔结构与导电性，是该部位的候选材料之一。"),
 ("电磁屏蔽织物","EMI Shielding Fabric","由含金属纤维的纱线织造而成、能够衰减电磁波的织物。强纶混纺织物屏蔽率可达 99% 以上，用于防辐射服装、屏蔽窗帘与通讯电缆屏蔽层。"),
 ("防切割","Cut Resistance","材料抵抗刀具切割的能力。不锈钢纤维与 PBO 等高性能纤维混纺制成的手套具备耐磨防切割性能。"),
 ("针刺毡","Needle-punched Felt","通过机械针刺使纤维层互相缠结成毡，不经烧结即具备一定强度。强纶自研金属纤维针刺毡应用于长征五号系列运载火箭发动机。"),
 ("KKF 滤机烧结毡","KKF Filter Press Felt","用于 KKF 型滤机的专用烧结毡。强纶先后研制出国内首张 KKF 滤机烧结毡与最大规格 KKF 滤机烧结毡。"),
 ("亲油疏水改性","Oleophilic-Hydrophobic Modification","通过表面处理使金属纤维对油相亲和、对水相排斥，从而高效捕捉并聚结水中的微细油滴。是强纶收油系统的核心技术之一。"),
 ("多孔材料","Porous Material","内部含有大量孔隙的材料。金属多孔材料兼具金属强度与孔隙功能，可用于催化、储能储热、吸声消音与过滤分离。"),
]
enc_rows = "".join(f'<div class="row-i"><span class="dt">{en}</span><div><h4>{t}</h4><p>{d}</p></div></div>' for t, en, d in ENC)
sc2 = '{"@context":"https://schema.org","@type":"DefinedTermSet","name":"金属纤维术语百科","hasDefinedTerm":[%s]}' % ",".join(
    '{"@type":"DefinedTerm","name":"%s","description":"%s"}' % (t, d.replace('"',"'")) for t, en, d in ENC)

w('encyclopedia.html', head(
    "术语百科 | 金属纤维相关术语 — 强纶新材",
    "金属纤维术语百科：金属纤维、复合拉拔、纤维条、烧结毡、烧结网、叶片滤盘、折波滤芯、针刺毡、亲油疏水改性等 15 个术语的中英文对照与解释。",
    "金属纤维术语,复合拉拔,烧结网,叶片滤盘,针刺毡,术语百科",
    "encyclopedia.html", schema=sc2)
 + header('insights.html')
 + crumb([("技术专栏", "insights.html"), ("术语百科", None)])
 + page_hero("03", "ENCYCLOPEDIA", "术语百科",
             "金属纤维这个行业，<em>词汇并不通用</em>",
             "同一个产品，在金属行业与纺织行业有不同叫法。这里按中英文对照整理金属纤维相关术语，便于跨行业沟通与海外询盘对接。", bg="img/ph-insights.webp")
 + f"""<section class="sec"><div class="wrap">{inav(2)}
  <div class="rows">{enc_rows}</div>
  <div class="note" style="margin-top:40px">过滤参数类术语（过滤精度、孔隙率、透气度、气泡点压等）见<a href="glossary.html" style="border-bottom:2px solid var(--gold)">选型中心 · 名词解释</a>。</div>
</div></section>"""
 + ENDCTA + footer())
print('技术专栏 3 页完成')
