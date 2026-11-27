# -*- coding: utf-8 -*-
"""应用方案：总览 + 7 个行业页"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from layout import head, header, crumb, page_hero, footer, SITE, TEL, TEL_RAW
from common import w, ENDCTA
from divisions import DIVS
PBY = {(d["key"], p["id"]): (d, p) for d in DIVS for p in d["products"]}

IND = [
 dict(f="a-filtration.html", gal=[("img/fts-site-huayou.webp","大流量槽体方案"),("img/fts-bamo-03.webp","槽体与管路"),("img/fts-tank-02.webp","罐式收油系统"),("img/fts-scene-03.webp","过滤与除油联合装置")], en="FILTRATION", zh="过滤分离", img="img/jlw-cart.webp", hero="img/fts-scene-01.webp",
      claim="高温、高粘、强腐蚀，<em>常规滤材扛不住的地方</em>",
      pain="化纤熔体与黏胶应用场景下，传统滤纸滤布不耐高温高压、金属网易堵塞易碎；萃取料液中的微米级乳化油又会污染后端树脂与膜。",
      sol="以金属纤维烧结毡/烧结网为滤材的滤芯、滤盘与成套过滤器，配合 FTS 收油系统完成预除油，形成「除油 + 精滤」的完整链条。",
      prods=[("滤材事业部","p-felt.html","绝对精度 10–60μm，纳污量大、升压慢、可清洗再生"),
             ("机加工事业部","p-element.html","熔体滤芯、水滤芯、除尘滤芯、叶片滤盘，整体烧结成型"),
             ("净化事业部","p-equipment.html","纯物理预除油，单套可达 600 m³/h，油份可回收复用")],
      kpis=[("316L","","主流滤材材质"),("20","+","收油系统合作客户")],
      cases="广东芳源、衢州华友、江西铜业、格林美、湖南邦普、中国恩菲、紫金铜业等"),
 dict(f="a-glass.html", gal=[("img/sleeve-03.webp","钢化炉生产线现场"),("img/sleeve-04.webp","辊道包覆套管现场"),("img/sleeve-07.webp","扁平套管卷"),("img/tg-knit2.webp","针织金属套管")], en="GLASS", zh="玻璃深加工", img="img/yarn-glassbelt.webp", hero="img/yarn-glassbelt.webp",
      claim="钢化炉里的每一次接触，<em>都不能划伤玻璃</em>",
      pain="钢化炉陶瓷辊道、钢化齿条、玻璃吸盘与成型模具长期处于高温，常规包覆材料易老化、掉屑，直接造成玻璃划伤与良品率下降。",
      sol="耐高温金属纤维弹性套管、编织套管、带 / 布、绳、毡与线，耐 350~1100℃ 高温，用作物理钢化炉陶瓷辊套、化学钢化炉齿条防护套、玻璃吸盘与夹具缓冲垫、汽车玻璃成型模具框架包覆与模布等。",
      prods=[("热动事业部","p-fabric.html","弹性套管、编织套管、针织套管、机织带与机织布"),
             ("纱线事业部","p-yarn.html","织造原料，可按幅宽与厚度定制")],
      kpis=[("350~1100","℃","耐温范围"),("6","类","耐热缓冲材料")],
      cases="玻璃深加工、汽车玻璃成型、建筑幕墙玻璃产线"),
 dict(f="a-emi.html", en="EMI SHIELDING", zh="电磁屏蔽与防静电", img="img/yarn-fabric.webp", hero="img/hero-jl-blend.webp",
      claim="屏蔽能力<em>不会被洗掉</em>",
      pain="涂层型导电织物在反复洗涤后屏蔽效能衰减；生产线与库房的静电积聚存在起火风险。",
      sol="导电性来自纯金属纤维本体而非涂层，混纺纱可水洗机洗而屏蔽能力不降；金属纤维编织带可用于设备静电泄放与接地搭接。",
      prods=[("纱线事业部","p-yarn.html","混纺纱、缝纫线，按不锈钢纤维含量配比调整导电性"),
             ("热动事业部","p-fabric.html","机织布、编织带，用于屏蔽窗帘与接地搭接")],
      kpis=[("99","%+","典型屏蔽率"),("2","μm","纤维直径低至"),("316L","","标准材质")],
      cases="防静电工作服、防辐射服装、屏蔽窗帘、通讯电缆屏蔽层"),
 dict(f="a-aero.html", en="AEROSPACE", zh="航空航天与特种材料", img="img/media-09.webp", hero="img/hero-jl-felt.webp",
      claim="用在航空航天领域的<em>金属纤维材料</em>",
      pain="航空航天领域对材料的减震、耐高温与可靠性要求远高于常规工业件，材料需长期稳定、批次一致。",
      sol="强纶自主研发的金属纤维毡制品已应用于航空航天领域；金属纤维烧结毡也可用于飞机、舰船燃油过滤与液压系统过滤。",
      prods=[("滤材事业部","p-felt.html","金属纤维烧结毡，耐高温、可再生"),
             ("机加工事业部","p-element.html","燃油过滤、液压系统过滤元件")],
      kpis=[("57","项","授权专利"),("5+1","","参与国标/行标")],
      cases="航空航天领域配套；飞机、舰船燃油过滤与液压系统过滤"),
 dict(f="a-auto.html", en="AUTOMOTIVE", zh="汽车", img="img/yarn-carseat.webp", hero="img/hero-jl-yarn.webp",
      claim="座椅加热与尾气处理，<em>都要一根能发热的线</em>",
      pain="座椅加热线需要在反复弯折下保持稳定电阻与寿命；SCR 系统加热与尾气微粒过滤要求耐高温与耐腐蚀。",
      sol="连续不锈钢纱线可用于广泛的可加热纺织品，单独或合股绝缘后提升耐腐蚀、机械阻力与整体弯曲寿命，并使热量通过纺织材料均匀分布、有效防止热点。",
      prods=[("纱线事业部","p-yarn.html","强纶金属纤维线、包胶线，发热均匀"),
             ("机加工事业部","p-element.html","尾气微粒过滤与高温气体除尘元件")],
      kpis=[("1–100","Ω","米电阻可调"),("1000","芯","芯数可达"),("350–850","℃","耐温范围")],
      cases="汽车座椅加热、SCR 加热系统、尾气微粒过滤"),
 dict(f="a-textile.html", gal=[("img/yarn-rfid.webp","RFID 耐水洗标签"),("img/yarn-heatpad.webp","金属纤维发热片"),("img/yarn-thread.webp","金属纤维缝纫线"),("img/prod-heatwire.webp","强纶金属纤维线")], en="SMART TEXTILE", zh="功能纺织与智能穿戴", img="img/yarn-wearable.webp", hero="img/yarn-wearable.webp",
      claim="把金属<em>织进衣服里</em>",
      pain="智能穿戴的发热与信号传输要求材料柔软、耐水洗、弯折寿命长，普通金属丝难以兼顾。",
      sol="金属纤维可纺可织，制成导电纱、信号线、发热织物与吸音材料，兼具透气性与抗静电功能；公司金属纱线在电热面料领域应用广泛，发热服已用于冬奥会并出口俄罗斯等国家。",
      prods=[("纱线事业部","p-yarn.html","金属纤维线、信号线、RFID 水洗标用线"),
             ("热动事业部","p-fabric.html","发热织物、机织布")],
      kpis=[("2","μm","纤维直径低至"),("316L","","标准材质")],
      cases="智能发热马甲、围脖、鞋袜、抱枕、毯子、手套；RFID 水洗标"),
 dict(f="a-other.html", en="OTHERS", zh="其他应用", img="img/media-04.webp", hero="img/plant-06.webp",
      claim="还有很多应用场景，<em>金属纤维都能上</em>",
      pain="多孔催化、储能储热、吸声消音、氢能电池等新兴方向，对兼具导电、耐高温与多孔结构的材料有持续需求。",
      sol="金属纤维同时具备导电导热导磁、耐高温耐腐蚀与多孔高比表面积特性，可作为多孔催化材料、储能储热材料、吸声消音材料、红外辐射发热材料与氢能电池核心材料。",
      prods=[("滤材事业部","p-felt.html","制氢设备气体扩散层用毡、燃烧器用毡"),
             ("纱线事业部","p-yarn.html","导电刷、机器人用线"),
             ("机加工事业部","p-element.html","催化剂回收、医药食品气液分离")],
      kpis=[("10","大","系列产品"),("5","大","技术方向"),("6","个","研究室")],
      cases="催化剂回收、医药食品饮料过滤、燃气燃烧器、储热式热交换器多孔材料"),
]

REL = {'a-filtration.html': {'prods': [('media', 'felt'), ('media', 'composite'), ('media', 'alloy'), ('machining', 'fluid'), ('machining', 'hydraulic'), ('machining', 'dust'), ('machining', 'air'), ('machining', 'parts'), ('purify', 'tank'), ('purify', 'trough'), ('purify', 'retrofit'), ('yarn', 'thread')], 'img': 'img/jlw-cart.webp', 'hero': 'img/hero-jl-cart.webp'}, 'a-glass.html': {'prods': [('thermo', 'elastic'), ('thermo', 'braid'), ('thermo', 'tape'), ('thermo', 'rope'), ('thermo', 'felt'), ('thermo', 'thread'), ('yarn', 'tape'), ('yarn', 'cloth')], 'img': 'img/sleeve-06.webp', 'hero': 'img/yarn-glassbelt.webp'}, 'a-emi.html': {'prods': [('yarn', 'spun'), ('yarn', 'thread'), ('yarn', 'cloth'), ('yarn', 'tape'), ('thermo', 'braid'), ('thermo', 'tape')], 'img': 'img/yarn-cloth.webp', 'hero': 'img/hero-jl-blend.webp'}, 'a-aero.html': {'prods': [('media', 'felt'), ('media', 'alloy'), ('thermo', 'felt')], 'img': 'img/jlw-felt.webp', 'hero': 'img/hero-jl-felt.webp'}, 'a-auto.html': {'prods': [('yarn', 'thread'), ('yarn', 'coat'), ('yarn', 'cloth'), ('thermo', 'rope')], 'img': 'img/yarn-carseat.webp', 'hero': 'img/hero-jl-yarn.webp'}, 'a-textile.html': {'prods': [('yarn', 'thread'), ('yarn', 'coat'), ('yarn', 'spun'), ('yarn', 'fiber'), ('yarn', 'cloth'), ('thermo', 'thread')], 'img': 'img/yarn-wearable.webp', 'hero': 'img/hero-jl-yarn.webp'}, 'a-other.html': {'prods': [('media', 'felt'), ('media', 'alloy'), ('yarn', 'fiber'), ('yarn', 'thread'), ('yarn', 'cloth'), ('thermo', 'felt')], 'img': 'img/other-network.webp', 'hero': 'img/other-network.webp'}}
for _i in IND:
    _i.update(REL[_i['f']])

ov_cards = "".join(f"""<article class="mcard rv">
  <a href="{i['f']}" class="im"><img src="{i['img']}" alt="{i['zh']}" loading="lazy"></a>
  <div class="bd"><div class="cat">{i['en']}</div><h3>{i['zh']}</h3><p>{i['pain']}</p>
  <a class="more" href="{i['f']}">查看方案<svg class="i"><use href="#i-arrow"/></svg></a></div>
</article>""" for i in IND if i['f'] != 'a-other.html') + """<a class="othwide rv" href="a-other.html" style="--bg:url('img/other-network.webp')">
  <div><span class="cat">OTHERS · 其他应用</span><h3>您的行业不在上面？也许就是下一个</h3>
  <p>理论上，金属纤维可以用在各行各业。还有很多行业，我们暂时没有接触到、也暂时没有想到——欢迎带着需求来，和我们一起找到新的可能。</p></div>
  <span class="pill pill-gold">探索更多可能<svg class="i"><use href="#i-arrow"/></svg></span>
</a>"""

w('applications.html', head(
    "应用方案 | 过滤分离 · 玻璃深加工 · 电磁屏蔽 · 航空航天 · 汽车 · 智能穿戴",
    "强纶金属纤维材料在七大行业的应用方案：各行业的典型痛点、推荐产品与配套服务，覆盖过滤分离、玻璃深加工、电磁屏蔽与防静电、航空航天、汽车、功能纺织与智能穿戴。",
    "金属纤维应用,过滤分离方案,玻璃深加工,电磁屏蔽,防静电,航空航天材料,智能穿戴发热",
    "applications.html", og_img="img/jlw-cart.webp")
 + header('applications.html')
 + crumb([("应用方案", None)])
 + page_hero("01", "SOLUTIONS", "方案总览",
             "在严苛的应用场景里，<em>经受检验</em>",
             "七个行业，各有痛点。下面按行业给出强纶的应对方案与相关产品。",
             [("7","个","覆盖行业"),("5","类","产品"),("2002","","服务起始")])
 + f"""<section class="sec"><div class="wrap">
  <div class="g3">{ov_cards}</div>
</div></section>"""
 + ENDCTA + footer())

# 白底产品图整张显示（不裁切）；现场照片铺满 4:3 画框
SOL_CONTAIN = {"img/jlw-cart.webp", "img/jlw-felt.webp", "img/media-09.webp", "img/yarn-wearable.webp"}

def rel_cards(i):
    out = ""
    for k in i["prods"]:
        d, p = PBY[k]
        fit = " contain" if p.get("fit") == "contain" else ""
        out += f'''<a class="rpc rv" href="{d['file']}#{p['id']}"><div class="im{fit}"><img loading="lazy" src="{p['img']}" alt="{p['name']}"></div>
<div class="bd"><span class="cat">{d['cat']}</span><h3>{p['name']}</h3><p>{p['what']}</p><span class="more">查看产品<svg class="i"><use href="#i-arrow"/></svg></span></div></a>'''
    return out


for n, i in enumerate(IND):
    if i['f'] == 'a-other.html':
        continue
    kpi = [(a, b, c) for a, b, c in i['kpis']]
    names = "、".join(PBY[k][1]["name"] for k in i["prods"][:6])
    w(i['f'], head(
        f"{i['zh']} | 应用方案 — 强纶新材",
        f"{i['zh']}行业的金属纤维应用方案：{i['pain'][:60]}……相关产品：{names}等。",
        f"{i['zh']},金属纤维{i['zh']},{i['zh']}解决方案,强纶新材",
        i['f'], og_img=i['img'])
     + header('applications.html')
     + crumb([("应用方案", "applications.html"), (i['zh'], None)])
     + page_hero(f"{n+1:02d}", i['en'], i['zh'], i['claim'], i['pain'], kpi, bg=i['hero'])
     + f"""<section class="sec"><div class="wrap">
  <div class="g2 wide sol2">
    <div class="prose rv">
      <h3 style="margin-top:0">强纶的应对方案</h3>
      <p>{i['sol']}</p>
      <h3>典型应用</h3>
      <p>{i['cases']}</p>
    </div>
    <figure class="solimg{' contain' if i['img'] in SOL_CONTAIN else ''} rv d1"><img src="{i['img']}" alt="{i['zh']}" loading="lazy"></figure>
  </div>

  <div class="sec-h" style="margin:72px 0 26px"><h2>相关产品</h2><p>以下产品均可用于{i['zh']}，点击查看产品详情。</p></div>
  <div class="rpcs{' c4' if len(i['prods']) % 3 and len(i['prods']) % 4 == 0 else ''}">{rel_cards(i)}</div>

  <div class="buyrow" style="margin-top:48px">
    <a class="pill pill-ink" href="contact.html#inq">提交{i['zh']}询盘<svg class="i"><use href="#i-arrow"/></svg></a>
    <a class="pill pill-line" href="sample.html">申请样品</a>
    <a class="pill pill-line" href="contact.html">联系我们</a>
  </div>
</div></section>"""
     + ENDCTA + footer())

OTHER_PROPS = [
    ("导电 · 导热 · 导磁", "能传导电流、热量与信号，可做加热、屏蔽、防静电与传感。"),
    ("耐高温 · 耐腐蚀", "在高温、酸碱等严苛环境中长期稳定，不易老化。"),
    ("多孔 · 高比表面积", "烧结成毡后孔隙连通均匀，可过滤、可分离、可承载。"),
    ("柔软 · 可纺可织", "像纤维一样缝纫、编织、针织，能织进布料、缝进衣物。"),
    ("可烧结 · 可成型", "做成毡、滤芯、滤盘、套管与各类异形件。"),
    ("可复合 · 可定制", "材质、纤维直径与产品形态，可按需求组合开发。"),
]
OTHER_DIRS = [
    ("燃气燃烧器", "燃烧器用金属纤维毡"), ("氢能", "制氢设备气体扩散层用毡"), ("吸声降噪", "金属纤维吸声消音材料"),
    ("储能储热", "储热式热交换器多孔材料"), ("催化", "多孔催化材料、催化剂回收"), ("红外发热", "红外辐射发热材料"),
    ("医药食品", "医药、食品、饮料过滤与气液分离"), ("机器人与电子", "导电刷、机器人用线"),
]


def other_page(n, i):
    props = "".join(f'<div class="oprop rv"><span class="num">{k+1:02d}</span><h3>{t}</h3><p>{d}</p></div>' for k, (t, d) in enumerate(OTHER_PROPS))
    dirs = "".join(f'<div class="odir rv"><b>{t}</b><span>{d}</span></div>' for t, d in OTHER_DIRS)
    done = "".join(f'<a href="{x["f"]}">{x["zh"]}</a>' for x in IND if x["f"] != "a-other.html")
    w(i['f'], head(
        "其他应用 | 金属纤维的无限可能 — 强纶新材",
        "金属纤维兼具导电导热、耐高温耐腐蚀、多孔与可纺可织等特性，理论上可以用在各行各业。您的行业不在我们已列出的领域？欢迎带着需求联系强纶，一起开发新的应用。",
        "金属纤维新应用,金属纤维定制开发,金属纤维燃烧器,气体扩散层,吸声材料,强纶新材",
        i['f'], og_img=i['img'])
     + header('applications.html')
     + crumb([("应用方案", "applications.html"), (i['zh'], None)])
     + f"""<section class="ph has-bg othhero" style="--phbg:url('{i['hero']}')"><div class="wrap">
  <div class="idx"><b>{n+1:02d}</b>{i['en']} · {i['zh']}</div>
  <h1>金属纤维的应用，<br>远不止于此</h1>
  <p class="ph-lead">过滤分离、玻璃深加工、电磁屏蔽、航空航天、汽车、智能穿戴——这些是我们已经走过的路。理论上，金属纤维可以用在各行各业；还有很多行业，我们暂时没有接触到，也暂时没有想到。</p>
  <div class="othdone"><span>已走过的路</span>{done}</div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sh rv"><h2>为什么说金属纤维有无限可能</h2>
  <p>一根金属纤维，同时拥有金属与纤维两种属性。把下面这些特性组合起来，能用的地方远比我们列出的多。</p></div>
  <div class="oprops">{props}</div>
</div></section>

<section class="sec alt"><div class="wrap">
  <div class="sh rv"><h2>已经在探索的新方向</h2>
  <p>除了前面六个行业，金属纤维也已经用在这些方向上。下一个方向，可能就来自您的需求。</p></div>
  <div class="odirs">{dirs}</div>
</div></section>

<section class="othcall" style="--bg:url('{i['img']}')"><div class="wrap">
  <div class="oc-t rv">
    <span class="eb">YOUR INDUSTRY · 您的行业</span>
    <h2>您的行业，也许就是下一个</h2>
    <p>每个人都有自己的盲区：您最懂您的行业，我们最懂金属纤维。如果您觉得自己的行业也能用上金属纤维——哪怕只是一个想法——欢迎带着需求来找我们。一次交流，就可能打开一个新的应用方向。</p>
    <div class="acts"><a class="pill pill-gold" href="contact.html#inq">提交您的应用需求<svg class="i"><use href="#i-arrow"/></svg></a><a class="pill pill-line lt" href="tel:{TEL_RAW}">电话 {TEL}</a></div>
  </div>
  <ol class="oc-steps rv">
    <li><b>01</b><h3>告诉我们您的场景</h3><p>您的行业、使用环境，以及想解决的问题。</p></li>
    <li><b>02</b><h3>一起评估可行性</h3><p>研发与工程团队从材料、形态与工艺上一起分析。</p></li>
    <li><b>03</b><h3>共同把想法做成产品</h3><p>从材料选型到产品形态，和您一起推进。</p></li>
  </ol>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-h" style="margin:0 0 26px"><h2>可以从这些材料开始</h2><p>金属纤维、烧结毡、纱线与织物——新应用往往从这几种基础形态出发。</p></div>
  <div class="rpcs">{rel_cards(i)}</div>
  <p class="othend rv">每一个新需求，都会让金属纤维走得更远；这也是强纶面向未来的无限可能。</p>
</div></section>"""
     + ENDCTA + footer())


for n, i in enumerate(IND):
    if i['f'] == 'a-other.html':
        other_page(n, i)

print(f'应用方案完成：总览 + {len(IND)} 个行业页')
