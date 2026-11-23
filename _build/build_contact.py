# -*- coding: utf-8 -*-
"""联系我们 / 样品申请 / 搜索结果 / 404 / 隐私政策 / 网站地图"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from layout import head, header, crumb, page_hero, footer, SITE, TEL, TEL_RAW, ADDR
from common import w, ENDCTA

QL_DOCS_JS = ""  # 2026.11.23：资料下载与检测报告已下线

INQ_FORM = QL_DOCS_JS + """<form class="form" id="inqForm" name="inquiry" method="POST"
  data-netlify="true" netlify-honeypot="bot-field" enctype="multipart/form-data" novalidate>
  <input type="hidden" name="form-name" value="inquiry">
  <input type="hidden" name="doc" id="inqDoc">
  <p hidden><label>请勿填写：<input name="bot-field"></label></p>
  <div class="docnote" id="docNote" hidden></div>
  <h3>在线询价</h3>
  <p class="hint">带 * 为必填。提交后信息将推送至企业微信与指定邮箱，工程师在 1 个工作日内回复。</p>
  <label>姓名 *<input name="name" required autocomplete="name"></label>
  <label>手机 *<input name="tel" type="tel" required autocomplete="tel"></label>
  <label>公司<input name="company" autocomplete="organization"></label>
  <label>邮箱<input name="email" type="email" autocomplete="email"></label>
  <label>产品类别
    <select name="cat">
      <option>净化事业部 · 收油系统</option><option>机加工事业部 · 滤芯与金属构件</option><option>滤材事业部 · 金属烧结毡</option><option>纱线事业部 · 金属纤维纱线</option><option>热动事业部 · 耐高温套管与织带</option><option>不确定 / 请工程师推荐</option>
    </select></label>
  <label>过滤介质
    <select name="medium"><option>聚合物熔体</option><option>气体 / 烟气</option><option>液体 / 料液</option><option>含油废水 / 萃取液</option><option>其他</option></select></label>
  <label>使用温度
    <select name="temp"><option>≤ 150 ℃</option><option>150 – 400 ℃</option><option>&gt; 400 ℃</option><option>不确定</option></select></label>
  <label>工作压力
    <select name="pressure"><option>低压 · ≤ 1 MPa</option><option>中压 · 1 – 5 MPa</option><option>高压 · &gt; 5 MPa</option><option>常压 / 不确定</option></select></label>
  <label>过滤精度
    <select name="acc"><option>粗滤 · &gt; 20 μm</option><option>中精度 · 5 – 20 μm</option><option>高精度 · &lt; 5 μm</option><option>不确定</option></select></label>
  <label>处理流量<input name="flow" placeholder="例如 15 m³/h"></label>
  <label class="full">上传图纸或参数文件<input name="file" type="file" accept=".pdf,.doc,.docx,.xls,.xlsx,.dwg,.zip,.rar,.jpg,.png" multiple></label>
  <label class="full">补充说明<textarea name="msg" placeholder="现用滤材型号、设备接口、更换周期、遇到的问题等"></textarea></label>
  <button class="pill pill-ink" type="submit">提交询盘<svg class="i"><use href="#i-arrow"/></svg></button>
  <p class="ok" id="inqOk"></p>
</form>
<script>
(function(){
  var f=document.getElementById('inqForm'); if(!f) return;
  // 从选型指南带过来的条件自动回填
  var p=new URLSearchParams(location.search);
  var map={m:{melt:'聚合物熔体',gas:'气体 / 烟气',liquid:'液体 / 料液',oil:'含油废水 / 萃取液'},
           t:{low:'≤ 150 ℃',mid:'150 – 400 ℃',high:'> 400 ℃'},
           p:{lp:'低压 · ≤ 1 MPa',mp:'中压 · 1 – 5 MPa',hp:'高压 · > 5 MPa',np:'常压 / 不确定'},
           a:{coarse:'粗滤 · > 20 μm',mid:'中精度 · 5 – 20 μm',fine:'高精度 · < 5 μm',unk:'不确定'}};
  var names={m:'medium',t:'temp',p:'pressure',a:'acc'};
  var cq=p.get('cat'); if(cq){var cs=f.querySelector('[name=cat]'); if(cs){[].forEach.call(cs.options,function(o,i){if(o.text.indexOf(cq)===0)cs.selectedIndex=i});}}
  Object.keys(names).forEach(function(k){
    var v=p.get(k); if(!v||!map[k][v])return;
    var sel=f.elements[names[k]]; if(!sel)return;
    [].forEach.call(sel.options,function(o){ if(o.text.replace(/\\s/g,'')===map[k][v].replace(/\\s/g,'')) sel.value=o.value||o.text; });
  });
  // 资料索取：从 ?doc= 带入要索取的文件
  var DOCS={};
  var dk=p.get('doc'), doc=dk&&DOCS[dk]?DOCS[dk]:null;
  if(doc){
    f.elements.doc.value=doc.t;
    var dn=document.getElementById('docNote');
    dn.hidden=false;
    dn.innerHTML='您正在索取：<b>《'+doc.t+'》</b><br><span>填写联系方式后即可下载，我们也会把文件发到您的邮箱。</span>';
    var m=f.elements.msg; if(m&&!m.value) m.value='索取资料：'+doc.t;
  }
  function done(okText,cls){
    var o=document.getElementById('inqOk');
    o.className='ok'+(cls?' '+cls:''); o.innerHTML=okText; o.style.display='block';
    o.scrollIntoView({behavior:'smooth',block:'center'});
  }
  f.addEventListener('submit',function(e){
    e.preventDefault();
    if(!f.elements.name.value.trim()||!f.elements.tel.value.trim()){alert('请填写姓名与手机');return;}
    var btn=f.querySelector('button[type=submit]'), lab=btn?btn.innerHTML:'';
    if(btn){btn.disabled=true;btn.innerHTML='提交中…';}
    var fd=new FormData(f); fd.set('form-name','inquiry');
    fetch('/',{method:'POST',body:fd}).then(function(r){
      if(!r.ok) throw new Error(r.status);
      if(btn){btn.disabled=false;btn.innerHTML=lab;}
      if(doc){
        done('提交成功，正在为您下载 <b>《'+doc.t+'》</b>。如果浏览器没有自动开始，'
           +'<a href="files/'+doc.f+'" download>点这里下载</a>。工程师会在 1 个工作日内与您联系。','ok-doc');
        var a=document.createElement('a'); a.href='files/'+doc.f; a.download=doc.f;
        document.body.appendChild(a); a.click(); a.remove();
      } else {
        done('提交成功，询盘已送达。工程师将在 1 个工作日内与您联系。');
      }
      f.reset();
    }).catch(function(){
      if(btn){btn.disabled=false;btn.innerHTML=lab;}
      var body=[]; new FormData(f).forEach(function(v,k){
        if(v instanceof File||k==='form-name'||k==='bot-field'||!String(v).trim())return;
        body.push(k+'：'+v);});
      done('这次没能从页面提交。已为您打开邮件草稿，发送即可；也可直接写信至 '
         +'<a href="mailto:hcq@jl-jiber.com">hcq@jl-jiber.com</a>。您填写的内容没有丢失。','warn');
      location.href='mailto:hcq@jl-jiber.com?subject='+encodeURIComponent('官网询盘 '+(f.elements.company.value||f.elements.name.value))
        +'&body='+encodeURIComponent(body.join(String.fromCharCode(10)));
    });
  });
})();
</script>"""

w('contact.html', head(
    "联系我们 | 电话 · 地址 · 在线询价 — 强纶新材",
    "福建强纶新材料股份有限公司联系方式：电话 153 5992 7344 / 0597-2799968，地址福建省龙岩市东肖镇经济技术开发区黄邦路 11 号；可在线提交在线询价并上传图纸。",
    "强纶联系方式,强纶电话,强纶地址,在线询价,金属纤维询价",
    "contact.html",
    schema='{"@context":"https://schema.org","@type":"ContactPage","mainEntity":{"@type":"Organization","name":"福建强纶新材料股份有限公司","telephone":"+86-15359927344","email":"hcq@jl-jiber.com","address":{"@type":"PostalAddress","streetAddress":"龙岩市东肖镇经济技术开发区黄邦路11号","addressLocality":"龙岩市","addressRegion":"福建省","addressCountry":"CN"}}}')
 + header('contact.html')
 + crumb([("联系我们", None)])
 + page_hero("01", "CONTACT", "联系我们",
             "把应用场景发过来，<em>剩下的交给工程师</em>",
             "提供介质、温度、压力与过滤精度，并可上传图纸或参数文件；我们会在 1 个工作日内回复初步选型建议。", bg="img/en-ph-contact.webp")
 + f"""<section class="sec"><div class="wrap">
  <div class="g2 r5-7 wide">
    <div class="rv">
      <h2 style="font-family:'Noto Serif SC',serif;font-size:26px;font-weight:900;margin-bottom:24px">联系方式</h2>
      <div class="ct-list">
        <div><small>销售与技术咨询</small><a class="num" href="tel:{TEL_RAW}">{TEL}</a></div>
        <div><small>公司总机</small><a class="num" href="tel:05972799968">0597-2799968</a></div>
        <div><small>企业邮箱</small><span><a href="mailto:hcq@jl-jiber.com">hcq@jl-jiber.com</a></span></div>
        <div><small>招聘投递</small><span><a href="mailto:hcq@jl-jiber.com">hcq@jl-jiber.com</a></span></div>
        <div><small>公司地址</small><span>{ADDR}</span></div>
        <div><small>英文名称</small><span>FUJIAN QL METAL FIBER CO., LTD</span></div>
      </div>
      <div id="wx" class="note" style="margin-top:30px"><b>企业微信</b><br>销售电话 {TEL} 微信同号，可直接添加沟通应用场景与报价。<br><small style="color:var(--muted)">企业微信二维码待甲方提供后由后台上传。</small></div>
      <div class="map-ph" style="margin-top:22px">
        <div>
          <b>公司位置</b>
          <p>{ADDR}</p>
          <small>地图组件待上线时接入（百度地图），当前以文字地址为准。</small>
        </div>
      </div>
      <div class="buyrow"><a class="pill pill-line" href="sample.html">申请样品</a><a class="pill pill-line" href="selector.html">选型指南</a></div>
    </div>
    <div class="rv d1" id="inq">{INQ_FORM}</div>
  </div>
</div></section>"""
 + ENDCTA + footer())

w('sample.html', head(
    "样品申请 | 免费小样 · 1–3 天寄出 — 强纶新材",
    "强纶提供免费小样（运费到付），标准现货样品 1–3 天寄出。填写产品、规格、用途与收件信息即可申请。",
    "强纶样品申请,金属纤维样品,烧结毡样品,免费小样",
    "sample.html")
 + header('contact.html')
 + crumb([("联系我们", "contact.html"), ("样品申请", None)])
 + page_hero("02", "SAMPLE", "样品申请",
             "先拿样品，<em>在你的产线上验证</em>",
             "可提供免费小样（运费到付），标准现货样品一般 1–3 天寄出；应用场景复杂的项目可安排技术人员入厂试验。", bg="img/en-ph-contact.webp")
 + """<section class="sec"><div class="wrap">
  <div class="g2 r5-7 wide">
    <div class="rv">
      <h2 style="font-family:'Noto Serif SC',serif;font-size:26px;font-weight:900;margin-bottom:20px">申请说明</h2>
      <div class="prose">
        <p><strong>样品政策</strong>：常规现货规格提供免费小样，运费到付；特殊定制规格（特殊幅宽、特殊合金、非标接口）需评估后确认，可能产生打样费用。</p>
        <p><strong>寄出时效</strong>：标准现货样品 1–3 天寄出；定制样品按工艺周期另行告知。</p>
        <p><strong>入厂试验</strong>：针对液体情况复杂的客户，公司可<strong>免费提供前期收油系统实验设备及专业技术人员入厂试验</strong>，用实测数据确定方案后再定型。</p>
      </div>
      <div class="note" style="margin-top:26px"><b>提高效率的小建议</b><br>如能同时提供现用滤材型号、设备接口尺寸或图纸，我们可以直接寄出可对比验证的规格，减少一轮来回。</div>
    </div>
    <div class="rv d1">
      <form class="form" id="smpForm" name="sample" method="POST"
          data-netlify="true" netlify-honeypot="bot-field" enctype="multipart/form-data" novalidate>
        <input type="hidden" name="form-name" value="sample">
        <p hidden><label>请勿填写：<input name="bot-field"></label></p>
        <h3>样品申请</h3>
        <p class="hint">带 * 为必填。提交后由专人联系确认规格与寄送方式。</p>
        <label>姓名 *<input name="name" required autocomplete="name"></label>
        <label>手机 *<input name="tel" type="tel" required autocomplete="tel"></label>
        <label>公司 *<input name="company" required autocomplete="organization"></label>
        <label>邮箱<input name="email" type="email" autocomplete="email"></label>
        <label>申请产品
          <select name="prod"><option>净化事业部 · 收油系统</option><option>机加工事业部 · 滤芯与金属构件</option><option>滤材事业部 · 金属烧结毡</option><option>纱线事业部 · 金属纤维纱线</option><option>热动事业部 · 耐高温套管与织带</option><option>不确定 / 请工程师推荐</option></select></label>
        <label>规格 / 型号<input name="spec" placeholder="例如 25KIA3，或现用型号"></label>
        <label class="full">用途与应用场景<textarea name="use" placeholder="介质、温度、压力、精度要求，以及希望验证的内容"></textarea></label>
        <label class="full">收件信息 *<textarea name="addr" required placeholder="收件人、电话、详细地址"></textarea></label>
        <label class="full">上传图纸或参数文件<input name="file" type="file" accept=".pdf,.doc,.docx,.xls,.xlsx,.dwg,.zip,.rar,.jpg,.png" multiple></label>
        <button class="pill pill-ink" type="submit">提交申请<svg class="i"><use href="#i-arrow"/></svg></button>
        <p class="ok" id="smpOk"></p>
      </form>
      <script>
      (function(){var f=document.getElementById('smpForm');if(!f)return;
        var o=document.getElementById('smpOk');
        function done(h,c){o.className='ok'+(c?' '+c:'');o.innerHTML=h;o.style.display='block';
          o.scrollIntoView({behavior:'smooth',block:'center'});}
        f.addEventListener('submit',function(e){e.preventDefault();
          if(!f.elements.name.value.trim()||!f.elements.tel.value.trim()||!f.elements.company.value.trim()||!f.elements.addr.value.trim()){alert('请填写姓名、手机、公司与收件信息');return;}
          var btn=f.querySelector('button[type=submit]'),lab=btn?btn.innerHTML:'';
          if(btn){btn.disabled=true;btn.innerHTML='提交中…';}
          var fd=new FormData(f); fd.set('form-name','sample');
          fetch('/',{method:'POST',body:fd}).then(function(r){
            if(!r.ok) throw new Error(r.status);
            if(btn){btn.disabled=false;btn.innerHTML=lab;}
            done('申请已提交，专人会在 1 个工作日内联系您确认规格与寄送方式。'); f.reset();
          }).catch(function(){
            if(btn){btn.disabled=false;btn.innerHTML=lab;}
            var body=[]; new FormData(f).forEach(function(v,k){
              if(v instanceof File||k==='form-name'||k==='bot-field'||!String(v).trim())return;
              body.push(k+'：'+v);});
            done('这次没能从页面提交。已为您打开邮件草稿，发送即可；也可直接写信至 '
               +'<a href="mailto:hcq@jl-jiber.com">hcq@jl-jiber.com</a>。您填写的内容没有丢失。','warn');
            location.href='mailto:hcq@jl-jiber.com?subject='+encodeURIComponent('样品申请 '+f.elements.company.value)
              +'&body='+encodeURIComponent(body.join(String.fromCharCode(10)));
          });});})();
      </script>
    </div>
  </div>
</div></section>"""
 + ENDCTA + footer())
print('联系 / 样品完成')
