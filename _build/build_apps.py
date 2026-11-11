# -*- coding: utf-8 -*-
"""应用方案：总览 + 7 个行业页"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from layout import head, header, crumb, page_hero, footer, SITE
from common import w, ENDCTA

IND = [
 dict(f="a-filtration.html", en="FILTRATION", zh="过滤分离", img="img/media-10.webp", hero="img/fts-scene-01.webp",
      claim="高温、高粘、强腐蚀，<em>常规滤材扛不住的地方</em>",
      pain="化纤熔体与黏胶工况下，传统滤纸滤布不耐高温高压、金属网易堵塞易碎；萃取料液中的微米级乳化油又会污染后端树脂与膜。",
      sol="以金属纤维烧结毡/烧结网为滤材的滤芯、滤盘与成套过滤器，配合 FTS 收油系统完成预除油，形成「除油 + 精滤」的完整链条。",
      prods=[("金属纤维烧结毡","p-felt.html","绝对精度 10–60μm，纳污量大、升压慢、可清洗再生"),
             ("过滤元器件","p-element.html","熔体滤芯、水滤芯、除尘滤芯、叶片滤盘，整体烧结成型"),
             ("净化设备 · 收油系统","p-equipment.html","纯物理预除油，最大单套 600 m³/h，油份可回收复用")],
      kpis=[("10–60","μm","过滤精度区间"),("480","℃","滤材可用温度"),("600","m³/h","最大单套处理量"),("20","+","行业客户")],
      cases="广东芳源、衢州华友、江西铜业、格林美、湖南邦普、中国恩菲、紫金铜业等"),
 dict(f="a-glass.html", en="GLASS", zh="玻璃深加工", img="img/yarn-glassbelt.webp", hero="img/yarn-glassbelt.webp",
      claim="钢化炉里的每一次接触，<em>都不能划伤玻璃</em>",
      pain="钢化炉陶瓷辊道、测温探头、热风管路与钢化齿条长期处于高温，常规包覆材料易老化、掉屑，直接造成玻璃划伤与良品率下降。",
      sol="100% 不锈钢纤维编织的套管、织带与模布，长期耐温 350℃、短时峰值 1100℃，柔软不掉屑，直接包覆在高温接触面上。",
      prods=[("金属纤维织物","p-fabric.html","弹性套管、编织套管、针织套管、机织带与机织布"),
             ("金属纤维纱线","p-yarn.html","织造原料，可按幅宽与厚度定制")],
      kpis=[("350","℃","长期连续耐温"),("1100","℃","短时峰值"),("0.35–0.5","mm","织带厚度"),("1500","mm","最大常规幅宽")],
      cases="玻璃深加工、汽车玻璃成型、建筑幕墙玻璃产线"),
 dict(f="a-emi.html", en="EMI SHIELDING", zh="电磁屏蔽与防静电", img="img/yarn-fabric.webp", hero="img/yarn-fabric.webp",
      claim="屏蔽能力<em>不会被洗掉</em>",
      pain="涂层型导电织物在反复洗涤后屏蔽效能衰减；生产线与库房的静电积聚存在起火风险。",
      sol="导电性来自纯金属纤维本体而非涂层，混纺纱可水洗机洗而屏蔽能力不降；金属纤维编织带可用于设备静电泄放与接地搭接。",
      prods=[("金属纤维纱线","p-yarn.html","混纺纱、缝纫线，按不锈钢纤维含量配比调整导电性"),
             ("金属纤维织物","p-fabric.html","机织布、编织带，用于屏蔽窗帘与接地搭接")],
      kpis=[("99","%+","典型屏蔽率"),("2","μm","最细纤维直径"),("316L","","标准材质")],
      cases="防静电工作服、防辐射服装、屏蔽窗帘、通讯电缆屏蔽层"),
 dict(f="a-aero.html", en="AEROSPACE", zh="航空航天与特种材料", img="img/media-09.webp", hero="img/media-09.webp",
      claim="配套国家航天工程的<em>金属纤维毡</em>",
      pain="火箭发动机与航空装备对减震、耐高温与可靠性的要求远高于常规工业件，材料需长期稳定且可追溯。",
      sol="作为国内最早配套航天工程的金属纤维毡供应商，自研针刺毡已成功应用于长征五号 B、长征五号遥五运载火箭发动机；同时供应燃油过滤、消音与减震类元件。",
      prods=[("金属纤维烧结毡","p-felt.html","针刺毡与烧结毡，减震、耐高温"),
             ("过滤元器件","p-element.html","燃油过滤、液压系统过滤元件")],
      kpis=[("2020","","配套长征五号 B"),("57","项","授权专利"),("5+1","","参与国标/行标")],
      cases="长征五号 B、长征五号遥五运载火箭发动机；航空舰船燃油过滤"),
 dict(f="a-auto.html", en="AUTOMOTIVE", zh="汽车", img="img/yarn-carseat.webp", hero="img/yarn-carseat.webp",
      claim="座椅加热与尾气处理，<em>都要一根能发热的线</em>",
      pain="座椅加热线需要在反复弯折下保持稳定电阻与寿命；SCR 系统加热与尾气微粒过滤要求耐高温与耐腐蚀。",
      sol="连续不锈钢纱线可用于广泛的可加热纺织品，单独或合股绝缘后提升耐腐蚀、机械阻力与整体弯曲寿命，并使热量通过纺织材料均匀分布、有效防止热点。",
      prods=[("金属纤维纱线","p-yarn.html","发热线 60/100/275/1000 芯，米电阻 1–100Ω 可调"),
             ("过滤元器件","p-element.html","尾气微粒过滤与高温气体除尘元件")],
      kpis=[("1–100","Ω","米电阻可调"),("1000","芯","最大芯数"),("350–850","℃","耐温范围")],
      cases="汽车座椅加热、SCR 加热系统、尾气微粒过滤"),
 dict(f="a-textile.html", en="SMART TEXTILE", zh="功能纺织与智能穿戴", img="img/yarn-wearable.webp", hero="img/yarn-wearable.webp",
      claim="把金属<em>织进衣服里</em>",
      pain="智能穿戴的发热与信号传输要求材料柔软、耐水洗、弯折寿命长，普通金属丝难以兼顾。",
      sol="金属纤维可纺可织，制成导电纱、信号线、发热织物与吸音材料，兼具透气性与抗静电功能；公司金属纱线在电热面料领域市占率全国第一，发热服已用于冬奥会并出口俄罗斯等国家。",
      prods=[("金属纤维纱线","p-yarn.html","发热线、信号线、RFID 水洗标用线"),
             ("金属纤维织物","p-fabric.html","发热织物、机织布")],
      kpis=[("No.1","","电热面料市占率"),("2","μm","最细纤维直径"),("1–3","天","现货样品寄出")],
      cases="智能发热马甲、围脖、鞋袜、抱枕、毯子、手套；RFID 水洗标"),
 dict(f="a-other.html", en="OTHERS", zh="其他应用", img="img/media-04.webp", hero="img/plant-06.webp",
      claim="还有很多工况，<em>金属纤维都能上</em>",
      pain="多孔催化、储能储热、吸声消音、氢能电池等新兴方向，对兼具导电、耐高温与多孔结构的材料有持续需求。",
      sol="金属纤维同时具备导电导热导磁、耐高温耐腐蚀与多孔高比表面积特性，可作为多孔催化材料、储能储热材料、吸声消音材料、红外辐射发热材料与氢能电池核心材料。",
      prods=[("金属纤维烧结毡","p-felt.html","制氢设备气体扩散层用毡、燃烧器用毡"),
             ("金属纤维纱线","p-yarn.html","导电刷、机器人用线"),
             ("过滤元器件","p-element.html","催化剂回收、医药食品气液分离")],
      kpis=[("10","大","系列产品"),("5","大","技术方向"),("6","个","研究室")],
      cases="催化剂回收、医药食品饮料过滤、燃气燃烧器、储热式热交换器多孔材料"),
]

ov_cards = "".join(f"""<article class="mcard rv">
  <a href="{i['f']}" class="im"><img src="{i['img']}" alt="{i['zh']}" loading="lazy"></a>
  <div class="bd"><div class="cat">{i['en']}</div><h3>{i['zh']}</h3><p>{i['pain']}</p>
  <a class="more" href="{i['f']}">查看方案<svg class="i"><use href="#i-arrow"/></svg></a></div>
</article>""" for i in IND)

w('applications.html', head(
    "应用方案 | 过滤分离 · 玻璃深加工 · 电磁屏蔽 · 航空航天 · 汽车 · 智能穿戴",
    "强纶金属纤维材料在七大行业的应用方案：各行业的典型痛点、推荐产品与配套服务，覆盖过滤分离、玻璃深加工、电磁屏蔽与防静电、航空航天、汽车、功能纺织与智能穿戴。",
    "金属纤维应用,过滤分离方案,玻璃深加工,电磁屏蔽,防静电,航空航天材料,智能穿戴发热",
    "applications.html", og_img="img/fts-scene-01.webp")
 + header('applications.html')
 + crumb([("应用方案", None)])
 + page_hero("01", "SOLUTIONS", "方案总览",
             "在最苛刻的工况里，<em>经受检验</em>",
             "七个行业，各有痛点。下面按行业给出强纶的应对方案与推荐产品，每个方案均可提供样品测试与现场试验支持。",
             [("7","个","覆盖行业"),("5","条","产品线"),("20","+","行业客户"),("2002","","服务起始")])
 + f"""<section class="sec"><div class="wrap">
  <div class="g3">{ov_cards}</div>
</div></section>"""
 + ENDCTA + footer())

for n, i in enumerate(IND):
    prod_cards = "".join(f'<a class="card rv" href="{u}"><h3>{t}</h3><p>{d}</p><span class="more">了解产品线<svg class="i"><use href="#i-arrow"/></svg></span></a>' for t, u, d in i['prods'])
    kpi = [(a, b, c) for a, b, c in i['kpis']]
    w(i['f'], head(
        f"{i['zh']} | 应用方案 — 强纶新材",
        f"{i['zh']}行业的金属纤维应用方案：{i['pain'][:60]}……强纶提供{ '、'.join(t for t,_,_ in i['prods']) }等产品与配套服务。",
        f"{i['zh']},金属纤维{i['zh']},{i['zh']}解决方案,强纶新材",
        i['f'], og_img=i['img'])
     + header('applications.html')
     + crumb([("应用方案", "applications.html"), (i['zh'], None)])
     + page_hero(f"{n+1:02d}", i['en'], i['zh'], i['claim'], i['pain'], kpi, bg=i['hero'])
     + f"""<section class="sec"><div class="wrap">
  <div class="g2 wide">
    <div class="prose rv">
      <h3 style="margin-top:0">强纶的应对方案</h3>
      <p>{i['sol']}</p>
      <h3>典型应用</h3>
      <p>{i['cases']}</p>
      <div class="note" style="margin-top:26px"><b>试样与验证</b>：可提供免费小样（运费到付），标准现货样品 1–3 天寄出；工况复杂的项目可安排技术人员入厂试验，用实测数据确定方案后再定型。</div>
    </div>
    <div class="rv d1">
      <div class="gal c3" style="grid-template-columns:1fr;margin:0"><figure style="aspect-ratio:4/3;margin:0"><img src="{i['img']}" alt="{i['zh']}应用场景" loading="lazy"><figcaption>{i['zh']} · 应用场景</figcaption></figure></div>
    </div>
  </div>

  <div class="sec-h" style="margin:84px 0 26px"><h2>推荐产品</h2></div>
  <div class="g3">{prod_cards}</div>

  <div class="sec-h" style="margin:80px 0 20px"><h2>下一步</h2></div>
  <div class="buyrow">
    <a class="pill pill-ink" href="selector.html">按工况选型<svg class="i"><use href="#i-arrow"/></svg></a>
    <a class="pill pill-line" href="contact.html#inq">提交{i['zh']}询盘</a>
    <a class="pill pill-line" href="sample.html">申请样品</a>
  </div>
</div></section>"""
     + ENDCTA + footer())

print(f'应用方案完成：总览 + {len(IND)} 个行业页')
