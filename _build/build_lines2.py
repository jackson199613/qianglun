# -*- coding: utf-8 -*-
"""产品线：织物 / 过滤元器件 / 净化设备"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from layout import head, header, crumb, page_hero, footer
from common import w, ENDCTA
from build_lines import faq_block, cta_row

# ════════════════ 3 金属纤维织物
w('p-fabric.html', head(
    "金属纤维织物 | 编织套管 · 机织带 · 机织布 — 强纶新材",
    "100% 316L 不锈钢纤维编织的套管、机织带与机织布，长期耐温 350℃、短时峰值 1100℃，柔软导电、缓冲吸音，用于玻璃深加工、钢化炉与防静电。",
    "金属纤维织物,不锈钢编织套管,金属纤维机织带,耐高温套管,玻璃成型包覆,防静电织带",
    "p-fabric.html", og_img="img/sleeve-01.webp")
 + header('products.html')
 + crumb([("产品中心", "products.html"), ("金属纤维织物", None)])
 + page_hero("03", "METAL FIBER FABRIC", "金属纤维织物",
             "玻璃成型线上，<em>最耐得住的那层包覆</em>",
             "100% 不锈钢纤维编织而成的套管、织带与机织布，耐高温、柔软透气、导电防静电，兼具隔热保温、吸音减震与缓冲性能，是玻璃工业耐高温缓冲材料的首选。",
             [("350", "℃", "长期连续耐温"), ("1100", "℃", "短时峰值"), ("0.35–0.5", "mm", "织带厚度"), ("1500", "mm", "最大常规幅宽")],
             bg="img/sleeve-06.webp")
 + f"""<section class="sec"><div class="wrap">
  <div class="g2 r7-5 wide">
    <div class="prose rv">
      <p class="lede">一句话定义：用金属纤维纱织成的耐高温柔性织物，在高温接触面上替代玻纤与石棉，既不划伤工件也不掉屑。</p>
      <h3>主要品类</h3>
      <ul>
        <li><strong>弹性套管（TGZ112）</strong>：弹性大、回弹好，适合辊轴与外径固定工件紧裹防护；</li>
        <li><strong>编织套管（TGBX112 / TGBX113）</strong>：柔性更好、可拉伸，适合管线与热电偶引线，方便穿线布线；</li>
        <li><strong>针织金属套管</strong>：延展性好，适形能力强；</li>
        <li><strong>金属纤维绳（圆形 / 方形）</strong>：圆绳适合环形密封与穿绳绑扎；方绳接触面积更大，适合平面压合密封与缓冲减震；</li>
        <li><strong>机织带与机织布</strong>：用于玻璃成型模布、夹具包覆套、辊道套管、吸盘毡与燃烧器用布。</li>
      </ul>
      <h3>性能特点</h3>
      <p>耐高温、柔软、导电、耐用性高、透气、隔热保温、吸音减震、可过滤。成品经后整理定型，正常裁切使用不易起毛掉屑；<strong>尖锐切口或强摩擦工况建议预先封边</strong>，降低掉丝风险。</p>
    </div>
    <aside class="rv d1">
      <div class="gal" style="grid-template-columns:1fr 1fr">
        <figure><img src="img/tg-braid.webp" alt="斜编金属套管" loading="lazy"><figcaption>编织套管</figcaption></figure>
        <figure><img src="img/tg-knit.webp" alt="针织金属套管" loading="lazy"><figcaption>针织套管</figcaption></figure>
        <figure><img src="img/tg-belt.webp" alt="金属纤维织带" loading="lazy"><figcaption>金属织带</figcaption></figure>
        <figure><img src="img/sleeve-07.webp" alt="金属纤维扁平套管卷" loading="lazy"><figcaption>扁平套管卷</figcaption></figure>
        <figure><img src="img/tg-knit2.webp" alt="针织金属纤维套管" loading="lazy"><figcaption>针织套管</figcaption></figure>
        <figure><img src="img/sleeve-02.webp" alt="金属纤维织带盘" loading="lazy"><figcaption>织带盘装</figcaption></figure>
        <figure><img src="img/sleeve-05.webp" alt="金属纤维窄幅织带" loading="lazy"><figcaption>窄幅织带</figcaption></figure>
        <figure><img src="img/tg-rope.webp" alt="金属纤维绳盘" loading="lazy"><figcaption>金属纤维绳</figcaption></figure>
        <figure><img src="img/yarn-glassbelt.webp" alt="玻璃制造中使用的金属织带" loading="lazy"><figcaption>玻璃成型现场</figcaption></figure>
      </div>
      {cta_row('金属纤维织物')}
    </aside>
  </div>

  <figure class="leadfig rv"><img src="img/sh-belt.webp" alt="金属纤维织带" loading="lazy"><figcaption>金属纤维织带 · 316L 本体导电，厚度 0.35—0.5mm，幅宽可定制</figcaption></figure>

  <div class="sec-h" style="margin:88px 0 24px"><h2>型号与规格</h2></div>
  <div class="tbl-wrap"><table class="tbl">
    <thead><tr><th>型号</th><th>品类</th><th>标准材质</th><th>耐温</th><th>特点与适用</th></tr></thead>
    <tbody>
      <tr><td class="num">TGZ112</td><td>弹性套管</td><td>316L 不锈钢纤维</td><td class="num">350℃ 长期 / 1100℃ 短时</td><td>弹性大、回弹好；辊轴、外径固定工件紧裹防护</td></tr>
      <tr><td class="num">TGBX112</td><td>编织套管</td><td>316L 不锈钢纤维</td><td class="num">350℃ 长期 / 1100℃ 短时</td><td>柔性好、可拉伸；管线、热电偶引线穿线布线</td></tr>
      <tr><td class="num">TGBX113</td><td>编织套管</td><td>316L 不锈钢纤维</td><td class="num">350℃ 长期 / 1100℃ 短时</td><td>同上，规格区间不同</td></tr>
      <tr><td class="num">FSE112</td><td>金属纤维绳</td><td>316L 不锈钢纤维</td><td class="num">350℃ 长期 / 1100℃ 短时</td><td>圆形绳；环形密封、穿绳绑扎</td></tr>
      <tr><td class="num">ZDJX113</td><td>针织金属套</td><td>316L 不锈钢纤维</td><td class="num">350℃ 长期 / 1100℃ 短时</td><td>适形性好，包覆异形件</td></tr>
      <tr><td class="num">ZDJF113</td><td>针织金属套</td><td>316L 不锈钢纤维</td><td class="num">350℃ 长期 / 1100℃ 短时</td><td>同上，规格区间不同</td></tr>
      <tr><td>—</td><td>金属纤维织带</td><td>316L 不锈钢纤维</td><td class="num">350℃ 长期 / 1100℃ 短时</td><td>标准厚度 0.35–0.5mm；常规幅宽 1000 / 1200 / 1500mm，支持分切与窄幅定制</td></tr>
    </tbody>
  </table></div>
  <p class="tnote">* 如需更高耐蚀或更高耐温，可定制铁铬铝材质，起订量另议。1100℃ 为短时峰值，不建议长时间持续使用；高温有氧环境下氧化速率会明显加快。特殊厚度需评估开模。</p>

  <div class="g2 wide" style="margin-top:84px">
    <div class="rv"><h2 style="font-family:'Noto Serif SC',serif;font-size:26px;font-weight:900;margin-bottom:20px">典型应用</h2>
      <div class="prose">
        <p><strong>玻璃深加工</strong>：钢化炉陶瓷辊道套管、测温探头与热风管路包覆、钢化齿条包覆、玻璃成型模布、夹具包覆套、吸盘毡，杜绝玻璃划伤、提升良品率。</p>
        <p><strong>防静电与电磁屏蔽</strong>：生产线设备静电泄放、接地搭接、中低频电磁屏蔽；半成品与成品库房、空气对流不良场所的导电消静电装置。</p>
        <p><strong>其他高温工况</strong>：耐高温输送带、隔热保温、吸音减震、燃烧器用布。</p>
      </div>
    </div>
    <div class="rv d1"><h2 style="font-family:'Noto Serif SC',serif;font-size:26px;font-weight:900;margin-bottom:20px">常见问题</h2>
      {faq_block([
        ("材质都是 316L 吗？有其他材质可选吗？", "TGZ112、TGBX112、TGBX113、FSE112、ZDJX113、ZDJF113 标准材质均为 316L 不锈钢纤维；如需更高耐蚀、更高耐温，可定制铁铬铝材质，起订量另议。"),
        ("标注耐温 350~1100℃，是长期连续使用温度吗？", "350℃ 为长期连续推荐使用温度；短时峰值可以到 1100℃。1100℃ 不建议长时间持续使用，高温有氧环境下氧化速率会明显加快。"),
        ("弹性套管和编织套管怎么选？", "TGZ112 弹性套管弹性大、回弹好，适合辊轴、外径固定工件紧裹防护；TGBX112/113 编织套管柔性更好、可拉伸，适合管线、热电偶引线，方便穿线布线。"),
        ("金属纤维绳方形和圆形怎么选？", "圆形绳适合环形密封、穿绳绑扎；方形绳接触面积更大，适合平面压合密封、缓冲减震，优先看客户密封槽结构。"),
        ("织带宽度、厚度能不能定制？", "可以。标准厚度 0.35~0.5mm，常规幅宽 1000/1200/1500mm，支持分切、定制窄幅织带；特殊厚度需要评估开模。"),
        ("会不会掉屑掉丝、污染玻璃或精密工件？", "成品经过后整理定型工艺，正常裁切使用不易起毛掉屑；但尖锐切口、强摩擦工况下，建议预先做封边处理，降低掉丝风险。"),
        ("导电性能怎么样，能用于防静电、接地、电磁屏蔽吗？", "316L 金属纤维连续交织，本身具备良好导电能力，可用于静电泄放、接地搭接、中低频电磁屏蔽；如需精确电阻指标，可提供试样实测。"),
        ("耐酸碱、盐雾能力怎么样？", "316L 基材具备优良耐弱酸、盐雾能力；强还原性酸、浓氯离子长期浸泡工况，建议升级合金材质，先做盐雾试样验证。"),
        ("按米计价吗？最小起订量多少？", "标准规格按米销售；常规现货小批量几米即可试样；特殊定制规格（特殊幅宽、特殊合金）有最低起订长度。"),
        ("有样品吗？试样周期多久？", "可以提供免费小样（少量长度），运费到付；标准现货样品 1~3 天寄出。"),
      ])}
    </div>
  </div>
</div></section>"""
 + ENDCTA + footer())
print('织物完成')
