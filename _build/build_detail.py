# -*- coding: utf-8 -*-
"""产品详情页模板（以 25KIA3 烧结毡为示例实现，结构即合同约定的详情页模板）"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from layout import head, header, crumb, footer, SITE
from common import w, ENDCTA, video_block
from build_lines import faq_block

schema = '{"@context":"https://schema.org","@type":"Product","name":"金属纤维烧结毡 25KIA3","image":"%s/img/media-05.webp","description":"绝对过滤等级 25μm 的不锈钢金属纤维烧结毡，厚度 0.61mm，过滤率 80%%，气泡点压 1480Pa，200Pa 透气值 350。","brand":{"@type":"Brand","name":"强纶新材"},"manufacturer":{"@type":"Organization","name":"福建强纶新材料股份有限公司"},"material":"316L 不锈钢纤维","sku":"25KIA3"}' % SITE

w('p-detail.html', head(
    "金属纤维烧结毡 25KIA3 | 产品详情 — 强纶新材",
    "25KIA3 金属纤维烧结毡：绝对过滤等级 25μm，厚度 0.61mm，过滤率 80%，气泡点压 1480Pa，200Pa 透气值 350，材质 316L，可定制加强加厚规格。",
    "25KIA3,金属纤维烧结毡,25微米烧结毡,烧结毡参数,过滤精度25μm",
    "p-detail.html", schema=schema, og_img="img/media-05.webp")
 + header('products.html')
 + crumb([("产品中心", "products.html"), ("金属纤维烧结毡", "p-felt.html"), ("25KIA3", None)])
 + """<section class="sec" style="padding-top:132px"><div class="wrap">
  <div class="pd">
    <div class="pd-media rv">
      <figure class="pd-main"><img id="pdMain" src="img/media-05.webp" alt="金属纤维烧结毡 25KIA3"></figure>
      <div class="pd-thumbs">
        <button class="on" data-src="img/media-05.webp" aria-label="产品图"><img src="img/media-05.webp" alt=""></button>
        <button data-src="img/media-03.webp" aria-label="大幅面毡"><img src="img/media-03.webp" alt=""></button>
        <button data-src="img/media-01.webp" aria-label="烧结滤片"><img src="img/media-01.webp" alt=""></button>
        <button data-src="img/media-02.webp" aria-label="烧结网"><img src="img/media-02.webp" alt=""></button>
      </div>
      <p class="tnote">电镜图与产品视频位置已预留，资料到位后由后台上传，前台自动转码为多档清晰度播放。</p>
    </div>

    <div class="pd-info rv d1">
      <div class="idx"><b>25KIA3</b>SINTERED FIBER FELT · 金属纤维烧结毡</div>
      <h1>金属纤维烧结毡 25KIA3</h1>
      <p class="pd-def">一句话定义：绝对过滤等级 25μm 的多层梯度孔不锈钢纤维烧结毡，兼顾精度与通量，是化纤熔体与黏胶过滤的常用规格。</p>
      <dl class="spec pd-spec">
        <dt>绝对过滤等级</dt><dd><b class="num">25 μm</b></dd>
        <dt>厚度</dt><dd class="num">0.61 mm</dd>
        <dt>过滤率</dt><dd class="num">80 %</dd>
        <dt>气泡点压</dt><dd class="num">1480 Pa</dd>
        <dt>200Pa 透气值</dt><dd class="num">350</dd>
        <dt>材质</dt><dd>316L 不锈钢纤维（可选镍、钛、铁铬铝、哈氏合金、蒙乃尔、双相合金）</dd>
        <dt>可用温度</dt><dd class="num">≤ 480 ℃</dd>
        <dt>供货形式</dt><dd>按张供货，可分切、加强、加厚、密集网定制</dd>
      </dl>
      <div class="tags"><span class="hl">现货常备</span><span>可清洗再生</span><span>耐酸碱有机溶剂</span><span>可焊接加工</span></div>
      <div class="buyrow">
        <a class="pill pill-ink" href="contact.html#inq">询价 25KIA3<svg class="i"><use href="#i-arrow"/></svg></a>
        <a class="pill pill-line" href="sample.html">申请样品</a>
      </div>
      <div class="note" style="margin-top:22px"><b>同系列可选</b>：10 / 15 / 20 / 30 / 40 / 60KIA3，以及厚度 1.1mm 的 KIA3K 系列与 KIC 系列。<a href="specs.html" style="border-bottom:2px solid var(--gold)">查看完整参数对照表</a></div>
    </div>
  </div>

  <div class="g2 wide" style="margin-top:92px">
    <div class="rv">
      <h2 style="font-family:'Noto Serif SC',serif;font-size:26px;font-weight:900;margin-bottom:18px">适用工况</h2>
      <div class="prose">
        <p>化纤、聚酯薄膜、油脂、石油制品等行业的液体过滤与气固分离；高分子聚合物熔体过滤、黏胶过滤、高温气体除尘、超滤器预过滤、真空泵保护过滤器、滤膜支撑体、飞机舰船燃油过滤、液压系统过滤。</p>
        <h3>选型建议</h3>
        <p>25μm 是精度与通量较为平衡的常用档位。若下游对杂质要求更严，向 20 / 15 / 10KIA3 收紧；若现场压差升得快、换网频繁，可向 30 / 40KIA3 放宽，或改用厚度 1.1mm 的 25KIA3K 以获得更大纳污量。</p>
      </div>
    </div>
    <div class="rv d1">
      <h2 style="font-family:'Noto Serif SC',serif;font-size:26px;font-weight:900;margin-bottom:18px">资料下载</h2>
      <div class="dl-list">
        <div class="dl-i"><svg class="i"><use href="#i-doc"/></svg><div><h4>金属纤维烧结毡技术数据表</h4><p>全系列型号精度、厚度、过滤率、气泡点与透气值</p></div><span class="sz">PDF</span><a class="btn" href="downloads.html"><svg class="i"><use href="#i-dl"/></svg>获取</a></div>
        <div class="dl-i"><svg class="i"><use href="#i-doc"/></svg><div><h4>产品检验报告样本</h4><p>出厂检验项目与格式示例</p></div><span class="sz">PDF</span><a class="btn" href="downloads.html"><svg class="i"><use href="#i-dl"/></svg>获取</a></div>
        <div class="dl-i"><svg class="i"><use href="#i-doc"/></svg><div><h4>ISO 9001 质量管理体系认证证书</h4><p>证书号 00224Q21982R1M</p></div><span class="sz">PDF</span><a class="btn" href="downloads.html"><svg class="i"><use href="#i-dl"/></svg>获取</a></div>
      </div>
    </div>
  </div>

  <div style="margin-top:88px">
    <h2 class="rv" style="font-family:'Noto Serif SC',serif;font-size:26px;font-weight:900;margin-bottom:18px">常见问题</h2>
    """ + faq_block([
        ("25KIA3 和 25KIA3K 有什么区别？", "绝对过滤等级同为 25μm，但 KIA3K 系列厚度 1.1mm、过滤率 85%、透气值 470，纳污量与机械强度更高，适合流量大、要求换网周期长的工况。"),
        ("能按设备尺寸分切吗？", "可以。提供护网尺寸或设备型号即可按张分切，也可做加强、加厚、密集网等特殊规格。"),
        ("多久需要更换？", "取决于介质洁净度与运行压差。金属纤维烧结毡可反复清洗再生，通常以压差达到设定上限作为清洗或更换依据。"),
        ("是否提供检验报告？", "可提供。检验项目含过滤精度、气泡点压力、透气值、厚度与外观，随货交付。"),
    ]) + """
  </div>
</div></section>
<script>
document.querySelectorAll('.pd-thumbs button').forEach(function(b){
  b.addEventListener('click',function(){
    document.querySelectorAll('.pd-thumbs button').forEach(function(x){x.classList.remove('on')});
    b.classList.add('on');
    document.getElementById('pdMain').src=b.getAttribute('data-src');
  });
});
</script>"""
 + '<section class="sec"><div class="wrap"><div class="sec-h"><h2>产品视频</h2><p>后台上传后自动转码多档清晰度，电脑与手机按网络自适应播放。</p></div>' + video_block("img/media-01.webp", "25KIA3 金属纤维烧结毡", "25KIA3 产品视频 · 结构与使用说明") + '</div></section>'
 + ENDCTA + footer())
print('详情页模板完成')
