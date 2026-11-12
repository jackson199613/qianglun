# -*- coding: utf-8 -*-
"""产品中心：总览 + 5 条产品线 + 详情页模板"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from layout import head, header, crumb, page_hero, footer, SITE
from common import w, ENDCTA

LINES = [
 dict(id="yarn", file="p-yarn.html", en="METAL FIBER YARN", zh="金属纤维纱线",
      img="img/yarn-fabric.webp", tags="纺织",
      core="100% 316L 不锈钢 · 纤维直径低至 2μm",
      use="防静电织物 · 电磁屏蔽 · 导电发热",
      desc="由金属纤维捻搓、纺纱而成的线材，兼具金属的导电导热耐高温与纺织纤维的柔韧性，可直接用于机织、针织与缝制。"),
 dict(id="felt", file="p-felt.html", en="SINTERED FIBER FELT", zh="金属纤维烧结毡",
      img="img/media-05.webp", tags="过滤 耐高温",
      core="多层梯度孔结构 · 精度 10–60μm",
      use="化纤熔体 · 黏胶过滤 · 高温气体除尘",
      desc="微米级金属纤维无纺后高温层压烧结，形成三维网络梯度孔隙，纳污量大、压损小、可清洗再生。"),
 dict(id="fabric", file="p-fabric.html", en="METAL FIBER FABRIC", zh="金属纤维织物",
      img="img/sleeve-01.webp", tags="耐高温 纺织",
      core="100% 不锈钢纤维编织 · 耐温 350–1100℃",
      use="玻璃深加工 · 汽车玻璃成型 · 印刷",
      desc="金属纤维机织带、编织套管、针织套管与机织布，耐高温、柔软透气、导电防静电，是玻璃成型的理想缓冲包覆材料。"),
 dict(id="element", file="p-element.html", en="FILTER ELEMENTS", zh="过滤元器件",
      img="img/cart-01.webp", tags="过滤 成套",
      core="烧结毡/烧结网为滤材 · 整体烧结成型",
      use="化纤 · 石化 · 高温烟气过滤",
      desc="熔体滤芯、水滤芯、除尘滤芯与叶片滤盘，机械强度高、耐高温耐腐蚀、孔径分布均匀，可清洗再生、可焊接机加工。"),
 dict(id="equipment", file="p-equipment.html", en="PURIFICATION EQUIPMENT", zh="净化设备 · 收油系统",
      img="img/fts-site-bamo.webp", tags="油水分离 成套",
      core="前置过滤器 + 油水分离器 · 最大单套 600 m³/h",
      use="镍钴湿法冶金 · 化工萃取 · 资源再生",
      desc="以表面改性亲油疏水金属纤维为聚结材料的 FTS 收油系统，纯物理除油、不加破乳药剂，油份可回收复用。"),
]

cards = "".join(f"""<article class="mcard rv" data-tag="{l['tags']}">
  <a href="{l['file']}" class="im"><img src="{l['img']}" alt="{l['zh']}" loading="lazy"></a>
  <div class="bd"><div class="cat">{l['en']}</div><h3>{l['zh']}</h3><p>{l['desc']}</p>
    <dl class="spec"><dt>核心参数</dt><dd>{l['core']}</dd><dt>典型用途</dt><dd>{l['use']}</dd></dl>
    <a class="more" href="{l['file']}">进入产品线<svg class="i"><use href="#i-arrow"/></svg></a></div>
</article>""" for l in LINES)

schema = '{"@context":"https://schema.org","@type":"ItemList","name":"强纶产品线","itemListElement":[%s]}' % ",".join(
    '{"@type":"ListItem","position":%d,"name":"%s","url":"%s/%s"}' % (i+1, l['zh'], SITE, l['file']) for i, l in enumerate(LINES))

w('products.html', head(
    "产品中心 | 金属纤维纱线 · 烧结毡 · 织物 · 过滤元器件 · 净化设备",
    "强纶五条产品线：金属纤维纱线、金属纤维烧结毡、金属纤维织物、过滤元器件与净化设备（收油系统），可按产品线、应用行业、材质与精度筛选。",
    "金属纤维产品,不锈钢纤维纱线,金属纤维烧结毡,烧结滤芯,滤盘,收油系统,油水分离设备",
    "products.html", schema=schema, og_img="img/media-05.webp")
 + header('products.html')
 + crumb([("产品中心", None)])
 + page_hero("01", "PRODUCTS", "产品总览",
             "一根纤维，<em>五条产品线</em>",
             "从金属纤维出发，向下游延伸到纱线织物、烧结滤材、过滤元件，直到成套净化设备。每条产品线均可按工况参数定制，并提供样品测试。",
             [("5", "条", "产品线"), ("2", "μm", "最细纤维直径"), ("10–60", "μm", "烧结毡精度"), ("600", "m³/h", "最大单套处理量")], bg="img/hero-main.webp")
 + f"""<section class="sec"><div class="wrap">
  <div class="sec-h row"><div><h2>按<em>产品线</em>浏览</h2><p>也可按应用行业、材质与过滤精度快速筛选。</p></div>
    <a class="pill pill-line" href="selector.html">不确定选哪条？按工况选型<svg class="i"><use href="#i-arrow"/></svg></a></div>
  <nav class="pillbar" data-filter=".mcard" aria-label="产品筛选">
    <button class="on" data-v="all">全部</button><button data-v="过滤">过滤分离</button><button data-v="纺织">纺织与导电</button>
    <button data-v="耐高温">耐高温</button><button data-v="油水分离">油水分离</button><button data-v="成套">成套设备</button>
  </nav>
  <div class="g3">{cards}</div>

  <div class="sec-h" style="margin:92px 0 28px"><h2>按<em>材质与精度</em>快速定位</h2></div>
  <div class="tbl-wrap"><table class="tbl">
    <thead><tr><th>产品线</th><th>常用材质</th><th>精度 / 规格区间</th><th>耐温</th><th>典型行业</th></tr></thead>
    <tbody>
      <tr><td><b>金属纤维纱线</b></td><td>316L / 304 / 铁铬铝，可与芳纶、涤纶、PPS、棉混纺</td><td>纤维直径 2–100μm；60/100/275/1000 芯</td><td class="num">350–850℃</td><td>防静电服装、电磁屏蔽、智能穿戴、汽车加热</td></tr>
      <tr><td><b>金属纤维烧结毡</b></td><td>316L 不锈钢、铁铬铝、镍、钛、哈氏合金等</td><td>绝对精度 10–60μm；厚度 0.3–1.1mm</td><td class="num">≤480℃</td><td>化纤、石化、黏胶、高温气体除尘</td></tr>
      <tr><td><b>金属纤维织物</b></td><td>100% 316L 不锈钢纤维</td><td>织带厚 0.35–0.5mm；幅宽 1000/1200/1500mm</td><td class="num">350℃ 长期 · 1100℃ 短时</td><td>玻璃深加工、钢化炉、印刷、防静电</td></tr>
      <tr><td><b>过滤元器件</b></td><td>316L 滤材 + 304 骨架 / 支撑网</td><td>名义精度 10μm 起；可折波、可定制接口</td><td class="num">≤480℃</td><td>化纤熔体、石化、水处理、除尘</td></tr>
      <tr><td><b>净化设备 · 收油系统</b></td><td>改性金属纤维聚结芯 + 碳钢/不锈钢壳体</td><td>罐式 ≤30 m³/h；槽式按需；最大单套 600 m³/h</td><td class="num">按工况</td><td>镍钴湿法冶金、化工萃取、资源再生</td></tr>
    </tbody>
  </table></div>
  <p class="tnote">* 具体过滤精度、孔隙率、透气值、耐温等实测参数，以各产品详情页与检测报告为准；非标规格支持定制。</p>

  <div class="sec-h" style="margin:88px 0 26px"><h2>线上店铺与海外渠道</h2></div>
  <div class="g4">
    <a class="card rv" href="https://yarn.qlfiber.com/" target="_blank" rel="noopener"><h3>纱线事业部</h3><p>金属纤维纱线独立站，含纱线系列全规格与在线选购。</p><span class="more">前往<svg class="i"><use href="#i-arrow"/></svg></span></a>
    <a class="card rv d1" href="https://shop143818143.taobao.com/" target="_blank" rel="noopener"><h3>淘宝官方店</h3><p>小批量样品与常规现货规格。</p><span class="more">前往<svg class="i"><use href="#i-arrow"/></svg></span></a>
    <a class="card rv d2" href="https://shop68071416lu466.1688.com/" target="_blank" rel="noopener"><h3>1688 工厂店</h3><p>工厂直供，批量采购与定制对接。</p><span class="more">前往<svg class="i"><use href="#i-arrow"/></svg></span></a>
    <a class="card rv d3" href="https://qlfiber.en.alibaba.com/" target="_blank" rel="noopener"><h3>阿里国际站</h3><p>海外客户采购入口（英文）。</p><span class="more">前往<svg class="i"><use href="#i-arrow"/></svg></span></a>
  </div>
</div></section>"""
 + ENDCTA + footer())
print('产品总览完成')
