# -*- coding: utf-8 -*-
"""名词解释 / 资料下载中心"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from layout import head, header, crumb, page_hero, footer
from common import w, ENDCTA, snav

TERMS = [
 ("过滤精度", "filtration rating", "滤材能够拦截的颗粒尺寸指标。分「名义精度」与「绝对精度」：名义精度指对该尺寸颗粒有一定拦截率（如 98%）；绝对精度指对该尺寸及以上颗粒基本全部拦截。强纶烧结毡型号中的数字即绝对过滤等级，如 25KIA3 为 25μm。"),
 ("孔隙率", "porosity", "滤材中孔隙体积占总体积的百分比。孔隙率越高，可通过的流量越大、压力损失越小，同时纳污空间也越大。金属纤维烧结毡典型孔隙率约 72%–86%。"),
 ("透气度 / 透气值", "air permeability", "在规定压差下单位面积滤材的空气通过量，强纶通常标注「200Pa 透气值」。数值越大说明通过能力越强、压损越小；同精度下透气值高意味着寿命与流量更有优势。"),
 ("气泡点压", "bubble point pressure", "滤材完全浸润后，气体首次从大孔隙中逸出所需的压力。气泡点压越高说明大孔孔径越小、过滤精度越高。强纶同时标注「平均起泡压强」与「初始起泡压强」。"),
 ("纳污量", "dirt holding capacity", "滤材在压差达到上限前所能容纳的污物总量。多层梯度孔结构由粗到细逐层拦截，纳污量显著大于单层结构，表现为「升压慢、更换周期长」。"),
 ("压差 / 压力损失", "pressure drop", "流体通过滤材前后的压力差。运行中压差随污物累积而升高，达到设定上限即需清洗或更换。选型时需在精度与压差之间取平衡。"),
 ("梯度孔结构", "gradient pore structure", "由不同孔径的纤维层叠压烧结形成的孔隙梯度，上游粗、下游细。可在保证整体精度的同时大幅提高纳污量，是金属纤维烧结毡区别于单层滤网的核心结构特征。"),
 ("烧结", "sintering", "将金属纤维无纺层在高温与压力下使纤维交点扩散结合的工艺。烧结后滤材具备整体刚性与机械强度，可焊接、可机加工、可反复清洗再生。"),
 ("针刺毡", "needle-punched felt", "通过机械针刺使纤维层互相缠结成毡的工艺。强纶金属纤维毡制品已应用于航空航天领域。"),
 ("预除油 / 深度除油", "pre-deoiling / deep deoiling", "油水分离的两个环节：预除油以较低运行成本去除并回收非溶解油；深度除油（吸附树脂、活性炭、蒸发、催化氧化等）去除溶解油以保证指标合格。强纶收油系统定位于预除油。"),
 ("聚结", "coalescence", "分散的微小油滴在聚结材料表面不断碰撞、吸附、长大，进而形成大油滴而快速上浮分离的过程。强纶采用表面改性的亲油疏水金属纤维作为聚结材料。"),
 ("乳化油 / 非溶解油 / 溶解油", "emulsified / insoluble / dissolved oil", "乳化油是以微米级液滴分散在水中的油；非溶解油指未溶于液体、可通过物理方法分离的油份；溶解油需通过深度除油去除。萃取工艺中溶解度一般在 5–40 ppm。"),
 ("米电阻", "resistance per meter", "导电纱线每米长度的电阻值，单位 Ω/m。是金属纤维线设计的核心参数：按工作电压与目标功率反推所需米电阻，再按规格选型。强纶金属纤维线常用区间 1–100Ω。"),
 ("电磁屏蔽效能", "shielding effectiveness", "材料对电磁波的衰减能力，单位 dB。金属纤维混纺织物的屏蔽能力来自纯金属纤维本体而非涂层，因此不会因洗涤衰减。"),
 ("目数", "mesh", "金属丝网每英寸长度上的网孔数量。目数越高网孔越密。强纶滤芯内部支撑网常用 48 目、外部保护网常用 40 目。"),
]
rows = "".join(f'<div class="row-i" data-tag="{t}"><span class="dt">{en}</span><div><h4>{t}</h4><p>{d}</p></div></div>' for t, en, d in TERMS)
sc = '{"@context":"https://schema.org","@type":"DefinedTermSet","name":"金属纤维与过滤术语","hasDefinedTerm":[%s]}' % ",".join(
    '{"@type":"DefinedTerm","name":"%s","description":"%s"}' % (t, d.replace('"', "'")) for t, en, d in TERMS)

w('glossary.html', head(
    "名词解释 | 过滤精度 · 孔隙率 · 透气度等术语 — 强纶新材",
    "金属纤维与过滤行业常用术语解释：过滤精度、孔隙率、透气度、气泡点压、纳污量、梯度孔结构、聚结、米电阻等 15 个关键概念。",
    "过滤术语,过滤精度,孔隙率,透气度,气泡点压,纳污量,名词解释",
    "glossary.html", schema=sc)
 + header('selector.html')
 + crumb([("选型中心", "selector.html"), ("名词解释", None)])
 + page_hero("03", "GLOSSARY", "名词解释",
             "把参数表上的词，<em>一个个讲清楚</em>",
             "选型沟通中容易产生误解的，往往不是产品本身，而是对同一个参数的不同理解。以下是强纶参数表与方案中常用术语的统一口径。", bg="img/mfg-qc-office.webp")
 + f"""<section class="sec"><div class="wrap">{snav(2)}
  <div class="rows">{rows}</div>
  <div class="note" style="margin-top:40px"><b>没找到想了解的术语？</b> 可在<a href="faq.html" style="border-bottom:2px solid var(--gold)">常见问题库</a>查找，或直接<a href="contact.html#inq" style="border-bottom:2px solid var(--gold)">联系工程师</a>。</div>
</div></section>"""
 + ENDCTA + footer())

# ════════ 资料下载中心
DL = [
 ("产品手册", [
   ("强纶新材企业产品画册（中英文版）", "公司简介、全系列产品与应用概览", "PDF"),
   ("强纶新材 · 纤维及滤芯分册", "金属纤维、纱线、织物与滤芯产品说明（中英文）", "PDF"),
   ("强纶新材 · 滤材及油水分离设备分册", "过滤材料与油水分离设备产品说明", "PDF"),
   ("强纶新材 · 滤芯产品画册（26 年版）", "滤芯产品线新版画册", "PDF"),
   ("强纶公司产品谱系图", "一级产品形态 → 应用场景 → 细分形态 → 型号", "PDF"),
 ]),
 ("技术数据表", [
   ("金属纤维烧结毡技术参数表", "KIA3 / KIA3K / KIC 全系列精度、厚度、过滤率、气泡点与透气值", "PDF"),
   ("金属纤维纱线规格表", "金属纤维线、缝纫线、纱与混纺纱规格区间", "PDF"),
   ("金属纤维织物型号表", "TGZ / TGBX / FSE / ZDJX / ZDJF 系列规格", "PDF"),
   ("收油系统选型与参数表", "罐式 / 槽式 / 槽体改造型谱与主要参数", "PDF"),
 ]),
 ("检测报告", [
   ("ROHS 四项检测报告（275×3）", "铅、镉、汞、六价铬限值 · 华测检测认证集团 CTI · 2026.05.16", "PDF", "rohs275"),
   ("ROHS 四项检测报告（1000×3）", "铅、镉、汞、六价铬限值 · 华测检测认证集团 CTI · 2026.05.16", "PDF", "rohs1000"),
   ("ROHS 四项检测报告（100×3）", "铅、镉、汞、六价铬限值 · 华测检测认证集团 CTI · 2026.05.16", "PDF", "rohs100"),
   ("316L 材质报告（275×3）", "牌号化学成分鉴定 · 华测检测认证集团 CTI · 2026.05.22", "PDF", "mat316l"),
   ("316L 材质报告 · 英文版", "Material Test Report，海外客户与出口项目使用", "PDF", "mat316len"),
   ("金属纤维线拉伸试验报告", "275×3 抗拉强度与断裂伸长 · 上海复达检测技术集团", "PDF", "tensile"),
   ("水洗前后电阻检测报告", "水洗循环前后电阻变化，验证导电持久性 · 斯坦德检测集团", "PDF", "reswash"),
   ("远红外性能检测报告", "远红外发射率，依据 GB/T 30127-2013", "PDF", "farir"),
   ("红外反射能谱报告", "275×3 红外波段反射特性 · 上海复达检测技术集团", "PDF", "irref"),
   ("磁性能检测报告", "100×3 磁性能表征 · 上海复达检测技术集团", "PDF", "magnetic"),
   ("产品检验报告样本", "出厂检验项目与格式示例", "PDF"),
 ]),
 ("资质证书", [
   ("ISO 9001 质量管理体系认证证书", "证书号 00224Q21982R1M，有效期至 2027.04.11", "PDF"),
   ("环境管理体系认证证书", "ISO 14001", "PDF"),
   ("职业健康安全管理体系认证证书", "ISO 45001", "PDF"),
   ("三体系认证证书（英文版）", "海外客户与出口项目使用", "PDF"),
 ]),
]
blocks = ""
for cat, items in DL:
    def _li(it):
        t, d, e = it[0], it[1], it[2]
        key = it[3] if len(it) > 3 else None
        rdy = '<span class="rdy">现可下载</span>' if key else ''
        href = f'contact.html?doc={key}#inq' if key else 'contact.html#inq'
        return (f'<div class="dl-i{" has" if key else ""}" data-tag="{cat}"><svg class="i"><use href="#i-doc"/></svg>'
                f'<div><h4>{t}{rdy}</h4><p>{d}</p></div><span class="sz">{e}</span>'
                f'<a class="btn" href="{href}"><svg class="i"><use href="#i-dl"/></svg>留资获取</a></div>')
    lis = "".join(_li(it) for it in items)
    blocks += f'<h3 class="rv" style="font-family:\'Noto Serif SC\',serif;font-size:22px;font-weight:700;margin:50px 0 6px">{cat} <span class="hcnt">{len(items)} 项</span></h3><div class="dl-list">{lis}</div>'

w('downloads.html', head(
    "资料下载中心 | 产品手册 · 技术数据表 · 检测报告 · 资质证书 — 强纶新材",
    "下载强纶产品手册、金属纤维烧结毡技术数据表、ROHS 检测报告与 ISO 9001 等资质证书；部分资料需留下联系方式后由工程师发送。",
    "强纶资料下载,产品手册,技术数据表,检测报告,资质证书下载",
    "downloads.html")
 + header('selector.html')
 + crumb([("选型中心", "selector.html"), ("资料下载中心", None)])
 + page_hero("04", "DOWNLOADS", "资料下载中心",
             "手册、参数表、报告与证书，<em>都在这里</em>",
             "产品手册与技术数据表可直接下载；检测报告与资质证书需留下联系方式，由工程师核对用途后发送，以便追溯资料流向。", bg="img/hero-jl-felt.webp")
 + f"""<section class="sec"><div class="wrap">{snav(3)}
  <div class="note" style="margin-bottom:10px"><b>关于下载方式</b>：网站后台支持「直接下载」与「留资下载」两种模式。为保护客户信息与资料版本一致性，检测报告与认证证书默认采用留资下载，提交后由专人发送新版本。</div>
  {blocks}
  <div class="note warn" style="margin-top:44px"><b>说明</b>：标注「现可下载」的 10 份检测报告已可索取，填写联系方式后立即下载；其余资料待甲方确认定稿后由后台上传。涉及具体客户的设备数据表、工程配置表属于项目保密资料，不在公开下载范围内。</div>
</div></section>"""
 + ENDCTA + footer())
print('名词解释 / 资料下载 完成')
