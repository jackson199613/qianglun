# -*- coding: utf-8 -*-
"""简单的 HTML 结构校验：标签闭合、图片存在、内链有效"""
import sys, os, re, html.parser, glob
ROOT = os.path.join(os.path.dirname(__file__), '..')
VOID = {'meta','link','img','br','hr','input','source','area','base','col','embed','param','track','wbr','use','path','circle','rect','line','polyline','polygon','ellipse','stop'}

class P(html.parser.HTMLParser):
    def __init__(s): super().__init__(convert_charrefs=True); s.st=[]; s.err=[]
    def handle_startendtag(s,t,a): pass
    def handle_starttag(s,t,a):
        if t not in VOID: s.st.append((t, s.getpos()[0]))
    def handle_endtag(s,t):
        if t in VOID: return
        if not s.st: s.err.append(f'第{s.getpos()[0]}行 多余 </{t}>'); return
        if s.st[-1][0]==t: s.st.pop()
        else: s.err.append(f'第{s.getpos()[0]}行 </{t}> 不匹配，当前未闭合 <{s.st[-1][0]}>(第{s.st[-1][1]}行)')

def check(files):
    bad=0
    for f in files:
        s=open(os.path.join(ROOT,f),encoding='utf-8').read()
        p=P(); p.feed(s)
        errs=list(p.err)+[f'未闭合 <{t}>(第{n}行)' for t,n in p.st]
        # 图片存在
        for m in re.findall(r'<img[^>]+src="([^"]+)"', s):
            if not m.startswith(('http','data:')) and not os.path.exists(os.path.join(ROOT,m)):
                errs.append(f'图片不存在: {m}')
        for m in re.findall(r"url\('([^']+)'\)", s):
            if not m.startswith(('http','data:')) and not os.path.exists(os.path.join(ROOT,m)):
                errs.append(f'背景图不存在: {m}')
        # 内链存在
        for m in set(re.findall(r'href="([^"#?][^"]*?\.html)(?:[#?][^"]*)?"', s)):
            if m.startswith(('http','//','mailto','tel')): continue
            if not os.path.exists(os.path.join(ROOT,m)): errs.append(f'内链缺失: {m}')
        if errs:
            bad+=1; print(f'✗ {f}')
            for e in errs[:8]: print('   -',e)
        else: print(f'✓ {f}')
    print(('全部通过' if not bad else f'{bad} 个文件有问题'))
    return bad

if __name__=='__main__':
    fs = sys.argv[1:] or sorted(os.path.basename(x) for x in glob.glob(os.path.join(ROOT,'*.html')))
    sys.exit(1 if check(fs) else 0)
