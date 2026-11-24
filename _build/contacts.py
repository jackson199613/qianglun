# -*- coding: utf-8 -*-
"""联系方式（2026.11.24 甲方《强纶联系方式》表格，原样照录）"""
DEPTS = [
    {"key": "sales", "name": "销售管理部", "people": [("骆女士", "15359927344"), ("赖女士", "19559742413")], "email": "hcq@jl-jiber.com"},
    {"key": "media", "name": "滤材事业部", "people": [("方女士", "13348342686"), ("石女士", "18950896159")], "email": "sale@jl-fiber.com"},
    {"key": "yarn", "name": "纱线事业部", "people": [("叶先生", "13313994499"), ("杨女士", "18159821773")], "email": "yrh@jl-jiber.com"},
    {"key": "purify", "name": "净化事业部", "people": [("廖女士", "13959721647"), ("江女士", "19859711431")], "email": "whr@jl-jiber.com"},
    {"key": "thermo", "name": "热动事业部", "people": [("石女士", "18760102933"), ("陈女士", "19906971337")], "email": "chejian@jl-fiber.com"},
    {"key": "machining", "name": "机加工事业部", "people": [("曹先生", "18006070316")], "email": ""},
    {"key": "hr", "name": "行政人事部", "people": [("钟女士", "0597-2799968"), ("曹女士", "15759000025")], "email": ""},
]
BY_KEY = {d["key"]: d for d in DEPTS}
OFFICES = [
    ("强纶注册地址", "龙岩经济技术开发区黄邦路11号"),
    ("厦门办事处", "厦门火炬高新区软件园二期观日路 22 号 204-7 单元"),
    ("广州办事处", "广州市天河区软件路15号9楼03单元"),
]

PHONE_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>'


def tel_href(n):
    return "tel:" + n.replace("-", "").replace(" ", "")


def dept_block(d, title=None):
    """单个部门联系块：图标 + 部门名 + 联系人/电话/邮箱 行"""
    rows = "".join(
        f'<li><span class="who">联系人：{p}</span><a class="tel num" href="{tel_href(t)}">{t}</a>'
        + (f'<a class="mail" href="mailto:{d["email"]}">{d["email"]}</a>' if d["email"] else '<span class="mail"></span>') + '</li>'
        for p, t in d["people"])
    return f'<div class="cdept"><h3><i>{PHONE_SVG}</i>{title or d["name"]}</h3><ul>{rows}</ul></div>'
