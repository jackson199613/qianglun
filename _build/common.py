# -*- coding: utf-8 -*-
"""各栏目构建脚本共用的小工具"""
import os
OUT = os.path.join(os.path.dirname(__file__), '..')

def w(name, html):
    open(os.path.join(OUT, name), 'w', encoding='utf-8').write(html)
    print('  ✓', name)

_ABOUT_NAV = """<nav class="pillbar" style="margin-top:0">
<a class="pb {a0}" href="about.html">企业简介</a><a class="pb {a1}" href="history.html">发展历程</a><a class="pb {a2}" href="manufacturing.html">制造能力</a><a class="pb {a3}" href="quality.html">质量体系</a><a class="pb {a4}" href="honors.html">资质荣誉</a><a class="pb {a5}" href="culture.html">企业文化与社会责任</a><a class="pb {a6}" href="investor.html">投资者关系</a></nav>"""
def anav(i):
    return _ABOUT_NAV.format(**{f'a{k}': ('on' if k == i else '') for k in range(7)})

_RD_NAV = """<nav class="pillbar" style="margin-top:0">
<a class="pb {a0}" href="rd.html">科研总览</a><a class="pb {a1}" href="platforms.html">核心技术平台</a><a class="pb {a2}" href="lab.html">研发中心与实验室</a><a class="pb {a3}" href="testing.html">检测能力</a><a class="pb {a4}" href="patents.html">专利与标准</a><a class="pb {a5}" href="coop.html">产学研合作</a><a class="pb {a6}" href="achievements.html">科研成果</a></nav>"""
def rnav(i):
    return _RD_NAV.format(**{f'a{k}': ('on' if k == i else '') for k in range(7)})

_SEL_NAV = """<nav class="pillbar" style="margin-top:0">
<a class="pb {a0}" href="selector.html">选型指南</a><a class="pb {a1}" href="specs.html">参数对照表</a><a class="pb {a2}" href="glossary.html">名词解释</a><a class="pb {a3}" href="downloads.html">资料下载中心</a></nav>"""
def snav(i):
    return _SEL_NAV.format(**{f'a{k}': ('on' if k == i else '') for k in range(4)})

_INS_NAV = """<nav class="pillbar" style="margin-top:0">
<a class="pb {a0}" href="insights.html">技术文章</a><a class="pb {a1}" href="faq.html">常见问题库</a><a class="pb {a2}" href="encyclopedia.html">术语百科</a></nav>"""
def inav(i):
    return _INS_NAV.format(**{f'a{k}': ('on' if k == i else '') for k in range(3)})

ENDCTA = """<section class="endcta"><div class="wrap">
  <div><h2>把<em>工况</em>告诉我们，<br>让工程师给出完整选型方案</h2>
  <p>提供介质、温度、压力与过滤精度，强纶工程师将结合材料、元件与成套设备给出可落地的方案与样品测试建议。</p></div>
  <div class="acts"><a class="pill pill-gold" href="contact.html#inq">在线询价<svg class="i"><use href="#i-arrow"/></svg></a><a class="pill pill-line" style="border-color:rgba(255,255,255,.4);color:#fff" href="selector.html">按工况选型</a></div>
</div></section>"""


def vr_block(poster, title, lead, idx="VR"):
    """VR 全景展示板块：甲方提供第三方链接后，把 data-vr 换成真实地址即可。"""
    return f'''<section class="sec alt vrsec" id="vr"><div class="wrap vr2">
  <div class="rv">
    <div class="idx"><b>{idx}</b>PANORAMA</div>
    <h2 class="vr-h">{title}</h2>
    <p class="vr-p">{lead}</p>
    <a class="pill pill-ink vr-go" data-vr href="#" hidden>进入全景漫游<svg class="i"><use href="#i-arrow"/></svg></a>
    <p class="vr-tip">全景链接由甲方提供，后台填入后此处自动嵌入；链接到期可随时更换或取消本板块。</p>
  </div>
  <figure class="vrframe rv" data-vr-embed>
    <img src="{poster}" alt="{title}" loading="lazy">
    <span class="vrbadge"><svg class="i"><use href="#i-arrow"/></svg>VR 全景</span>
  </figure>
</div></section>
'''


def video_block(poster, title, cap):
    """视频播放模块：后台上传并转码后，把 data-src 换成播放地址即可。"""
    return f'''<figure class="vidbox rv">
  <video controls playsinline preload="none" poster="{poster}" data-src="" aria-label="{title}"></video>
  <span class="vidtip">视频待甲方提供，上传后自动转码多档清晰度，按网络自适应播放</span>
  <figcaption>{cap}</figcaption>
</figure>
'''
