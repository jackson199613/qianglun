# -*- coding: utf-8 -*-
"""选型中心：选型指南(4步) / 参数对照表 / 名词解释 / 资料下载中心"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from layout import head, header, crumb, page_hero, footer
from common import w, ENDCTA, snav

# ════════ 选型指南（介质 → 温度 → 压力 → 精度）
w('selector.html', head(
    "选型指南 | 介质 → 温度 → 压力 → 精度 四步选型 — 强纶新材",
    "四步确定金属纤维过滤方案：选择介质、工况温度、工作压力与过滤精度，即可得到推荐产品线与配套建议，并一键带着条件询价。",
    "过滤选型,选型指南,过滤精度选择,烧结毡选型,滤芯选型,按工况选型",
    "selector.html")
 + header('selector.html')
 + crumb([("选型中心", None)])
 + page_hero("01", "SELECTOR", "选型指南",
             "四步，<em>找到对的过滤方案</em>",
             "依次选择介质、工况温度、工作压力与过滤精度，系统即时给出推荐产品线；工程师将按您的条件复核并给出正式选型表。", bg="img/ph-select.webp")
 + f"""<section class="sec"><div class="wrap">{snav(0)}
  <div class="sel" id="sel">
    <div class="sel-q">
      <div class="q"><div class="qh"><b class="num">01</b>过滤介质</div><div class="opts" data-k="m">
        <button data-v="melt" class="on">聚合物熔体</button><button data-v="gas">气体 / 烟气</button><button data-v="liquid">液体 / 料液</button><button data-v="oil">含油废水 / 萃取液</button></div></div>
      <div class="q"><div class="qh"><b class="num">02</b>工况温度</div><div class="opts" data-k="t">
        <button data-v="low" class="on">≤ 150 ℃</button><button data-v="mid">150 – 400 ℃</button><button data-v="high">&gt; 400 ℃</button></div></div>
      <div class="q"><div class="qh"><b class="num">03</b>工作压力</div><div class="opts" data-k="p">
        <button data-v="lp" class="on">低压 · ≤ 1 MPa</button><button data-v="mp">中压 · 1 – 5 MPa</button><button data-v="hp">高压 · &gt; 5 MPa</button><button data-v="np">常压 / 不确定</button></div></div>
      <div class="q"><div class="qh"><b class="num">04</b>过滤精度</div><div class="opts" data-k="a">
        <button data-v="coarse">粗滤 · &gt; 20 μm</button><button data-v="mid" class="on">中精度 · 5 – 20 μm</button><button data-v="fine">高精度 · &lt; 5 μm</button><button data-v="unk">不确定</button></div></div>
      <p class="sel-alt">不是过滤需求？导电纱、发热线、防静电织物请前往 <a href="p-yarn.html">金属纤维纱线</a> 或 <a href="p-fabric.html">金属纤维织物</a>。</p>
    </div>
    <div class="sel-r">
      <div class="r-im"><img id="rImg" src="img/media-05.webp" alt="推荐产品"></div>
      <div class="r-tx">
        <small>RECOMMENDED · 推荐产品线</small>
        <h3 id="rTitle">金属纤维烧结毡</h3>
        <p id="rDesc">多层梯度孔结构，纳污量大、升压慢，适合中精度熔体与料液过滤。</p>
        <div class="r-alt" id="rAlt"></div>
        <p class="r-note" id="rNote"></p>
        <a class="pill pill-gold" id="rGo" href="contact.html#inq">带着这些条件询价<svg class="i"><use href="#i-arrow"/></svg></a>
        <p class="r-disc">* 推荐基于常见工况，仅供参考，以工程师确认的正式选型为准。</p>
      </div>
    </div>
  </div>

  <div class="sec-h" style="margin:88px 0 26px"><h2>四个参数，<em>为什么是这四个</em></h2></div>
  <div class="g4">
    <article class="card rv"><span class="n">01</span><h3>介质</h3><p>决定材质与耐蚀等级。熔体看粘度与温度，萃取液看是否含油，烟气看粉尘特性。</p></article>
    <article class="card rv d1"><span class="n">02</span><h3>温度</h3><p>决定滤材体系。480℃ 以内常规不锈钢纤维可用；更高温需铁铬铝等耐热合金。</p></article>
    <article class="card rv d2"><span class="n">03</span><h3>压力</h3><p>决定结构强度。高压工况需加厚滤材、加强骨架或改用烧结网，避免变形与穿透。</p></article>
    <article class="card rv d3"><span class="n">04</span><h3>精度</h3><p>决定型号档位。精度越高气泡点压越高、透气值越低，需与流量和压差一并权衡。</p></article>
  </div>
</div></section>
<script>
(function(){{
  var S={{m:'melt',t:'low',p:'lp',a:'mid'}};
  var R={{
    melt:{{title:'金属纤维烧结毡 / 叶片滤盘',img:'img/media-05.webp',desc:'适合高粘度聚合物熔体过滤，过滤面积大、可清洗再生，常用于化纤与薄膜生产线。',alt:['金属纤维烧结毡','熔体滤芯','叶片滤盘'],url:'p-felt.html'}},
    gas:{{title:'除尘滤芯 / 耐高温金属滤袋',img:'img/cart-03.webp',desc:'高温气体除尘与气固分离，耐温耐腐蚀、可反吹清灰、可反复再生。',alt:['除尘滤芯','烧结毡','金属滤袋'],url:'p-element.html'}},
    liquid:{{title:'金属纤维烧结滤芯',img:'img/cart-01.webp',desc:'水与料液精滤，整体烧结成型、机械强度高，可清洗再生。',alt:['水滤芯','折波滤芯','烧结毡'],url:'p-element.html'}},
    oil:{{title:'净化设备 · 强纶收油系统',img:'img/fts-site-bamo.webp',desc:'纯物理聚结除油，不加破乳药剂，油份可回收复用；最大单套 600 m³/h。',alt:['罐式收油系统','槽式收油系统','槽体改造'],url:'p-equipment.html'}}
  }};
  var $=function(id){{return document.getElementById(id)}};
  function render(){{
    var r=R[S.m];
    $('rTitle').textContent=r.title; $('rDesc').textContent=r.desc;
    var im=$('rImg'); im.classList.add('fade');
    setTimeout(function(){{im.src=r.img; im.classList.remove('fade')}},180);
    $('rAlt').innerHTML=r.alt.map(function(x){{return '<span>'+x+'</span>'}}).join('');
    var n=[];
    if(S.t==='high') n.push('工况温度超过 400℃，建议改用铁铬铝等耐热合金纤维滤材。');
    else if(S.t==='mid') n.push('150–400℃ 工况下常规 316L 金属纤维滤材可用，长期运行建议留出温度余量。');
    if(S.p==='hp') n.push('高压工况建议加厚滤材（KIA3K 系列）或加强骨架，必要时改用烧结网。');
    if(S.a==='fine') n.push('高精度（<5μm）需结合气泡点与透气值权衡流量与压差，建议先做样品测试。');
    if(S.a==='unk') n.push('精度不确定时，可提供现用滤材型号或下游杂质要求，由工程师反推精度档位。');
    if(S.m==='oil') n.push('含油工况建议「预除油 + 深度除油」组合：先用收油系统回收非溶解油，再做深度处理。');
    $('rNote').textContent=n.join(' ');
    $('rGo').href='contact.html?m='+S.m+'&t='+S.t+'&p='+S.p+'&a='+S.a+'#inq';
  }}
  document.querySelectorAll('#sel .opts').forEach(function(box){{
    var k=box.getAttribute('data-k');
    box.querySelectorAll('button').forEach(function(b){{
      b.addEventListener('click',function(){{
        box.querySelectorAll('button').forEach(function(x){{x.classList.remove('on')}});
        b.classList.add('on'); S[k]=b.getAttribute('data-v'); render();
      }});
    }});
  }});
  render();
}})();
</script>"""
 + ENDCTA + footer())

# ════════ 参数对照表
rows = [("10KIA3",10,0.3,75,3700,110),("15KIA3",15,0.37,75,2470,190),("20KIA3",20,0.45,80,1850,300),
        ("25KIA3",25,0.61,80,1480,350),("30KIA3",30,0.63,80,1230,500),("40KIA3",40,0.66,78,925,620),
        ("60KIA3",60,0.7,86,620,1200),("10KIA3K",10,1.1,85,3500,140),("15KIA3K",15,1.1,85,2400,250),
        ("20KIA3K",20,1.1,85,1700,350),("25KIA3K",25,1.1,85,1400,470),("10KIC4",10,0.4,72,3700,100),
        ("15KIC2",15,0.4,72,2470,150),("20KIC2",20,0.4,72,1850,200),("25KIC4",25,0.5,72,1480,280)]
trs = "".join(f'<tr data-tag="{"KIA3K" if "KIA3K" in a else ("KIC" if "KIC" in a else "KIA3")}"><td><b>{a}</b></td><td class="num">{b}</td><td class="num">{c}</td><td class="num">{d}</td><td class="num">{e}</td><td class="num">{f}</td></tr>' for a,b,c,d,e,f in rows)

w('specs.html', head(
    "参数对照表 | 金属纤维烧结毡全系列技术参数 — 强纶新材",
    "金属纤维烧结毡 KIA3 / KIA3K / KIC 三大系列 15 个型号的绝对过滤等级、厚度、过滤率、气泡点压与 200Pa 透气值对照表。",
    "烧结毡参数,过滤精度对照,气泡点压,透气值,KIA3,KIA3K,技术参数表",
    "specs.html")
 + header('selector.html')
 + crumb([("选型中心", "selector.html"), ("参数对照表", None)])
 + page_hero("02", "SPECS", "参数对照表",
             "一张表，<em>看懂精度与通量的取舍</em>",
             "气泡点压反映最大孔径——越高孔径越细、精度越高；200Pa 透气值反映通过能力——越大压损越小、流量越大。两者通常此消彼长，选型即是在二者之间取平衡。", bg="img/ph-select.webp")
 + f"""<section class="sec"><div class="wrap">{snav(1)}
  <nav class="pillbar" data-filter=".tbl tbody tr" aria-label="系列筛选">
    <button class="on" data-v="all">全部系列</button><button data-v="KIA3">KIA3 标准系列</button><button data-v="KIA3K">KIA3K 加厚系列</button><button data-v="KIC">KIC 系列</button>
  </nav>
  <div class="tbl-wrap"><table class="tbl">
    <caption>金属纤维烧结毡技术参数 · Technology Parameter（型号中的数字代表绝对过滤等级 μm）</caption>
    <thead><tr><th>系列型号</th><th class="num">绝对过滤等级 μm</th><th class="num">厚度 mm</th><th class="num">过滤率 %</th><th class="num">气泡点压 Pa</th><th class="num">200Pa 透气值</th></tr></thead>
    <tbody>{trs}</tbody>
  </table></div>
  <p class="tnote">材质：不锈钢、镍、哈氏合金、铁合金、蒙乃尔合金、双相合金等。各型号气泡点与透气值不同，上表为常规值，实际以出厂检验报告为准；可按客户要求定制加强、加厚、密集网等特殊规格。</p>

  <div class="sec-h" style="margin:86px 0 24px"><h2>各产品线<em>规格区间</em>速查</h2></div>
  <div class="tbl-wrap"><table class="tbl">
    <thead><tr><th>产品线</th><th>常用材质</th><th>精度 / 规格区间</th><th>耐温</th></tr></thead>
    <tbody>
      <tr><td><b>金属纤维纱线</b></td><td>316L / 304 / 铁铬铝；可混纺芳纶、涤纶、PPS、棉</td><td>纤维直径 2–100μm；发热线 60/100/275/1000 芯；米电阻 1–100Ω</td><td class="num">350–850℃</td></tr>
      <tr><td><b>金属纤维烧结毡</b></td><td>316L、铁铬铝、镍、钛、哈氏合金、蒙乃尔、双相合金</td><td>绝对精度 10–60μm；厚度 0.3–1.1mm</td><td class="num">≤480℃</td></tr>
      <tr><td><b>金属纤维织物</b></td><td>100% 316L（可定制铁铬铝）</td><td>织带厚 0.35–0.5mm；幅宽 1000/1200/1500mm</td><td class="num">350℃ 长期 / 1100℃ 短时</td></tr>
      <tr><td><b>过滤元器件</b></td><td>316L 滤材 + 304 骨架与支撑网</td><td>名义精度 10μm 起；孔隙率约 72%；可折波、定制接口</td><td class="num">≤480℃</td></tr>
      <tr><td><b>净化设备 · 收油系统</b></td><td>改性金属纤维聚结芯</td><td>罐式 ≤30 m³/h；最大单套 600 m³/h；除油率 70%；出口含油 5–30 mg/L</td><td>按工况</td></tr>
    </tbody>
  </table></div>
</div></section>"""
 + ENDCTA + footer())
print('选型指南 / 参数对照表 完成')
