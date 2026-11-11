# 福建强纶新材料 · 中文官网

静态站点，推送到 GitHub 后由 Netlify 自动部署。

## 目录结构
- `index.html` —— 首页（首屏、科研实力、全产业链、产品中心、按工况选型、行业方案、客户案例、常见问题、技术专栏与新闻、询盘）
- `rd.html` 等 48 个页面 —— 按《网站建设服务合同》附件一《中文官网服务清单》搭建
- `site.css` —— 全站公共样式；`page.css` —— 内页样式；`theme-v4.css` —— 黄灰主题（最后加载，统一覆盖）
- `site.js` —— 内页公共交互（首页另有自带脚本）
- `img/` —— 站点图片（WebP）
- `sitemap.xml` / `robots.txt` / `llms.txt` —— 搜索引擎与 AI 平台收录配置
- `netlify.toml` —— 部署配置
- `_build/` —— 页面生成脚本（见下）

## 页面是怎么生成的
除 `index.html`、`rd.html` 外，其余页面由 `_build/` 下的脚本生成，以保证 40 多个页面的页头、页脚、面包屑与结构化数据完全一致。

```bash
python3 _build/build_about.py      # 关于强纶
python3 _build/build_about2.py
python3 _build/build_products.py   # 产品中心
python3 _build/build_lines.py
python3 _build/build_lines2.py
python3 _build/build_lines3.py
python3 _build/build_detail.py
python3 _build/build_apps.py       # 应用方案
python3 _build/build_select.py     # 选型中心
python3 _build/build_select2.py
python3 _build/build_insights.py   # 技术专栏
python3 _build/build_misc.py
python3 _build/build_news.py       # 新闻 / 招聘
python3 _build/build_contact.py    # 联系 / 样品
python3 _build/build_util.py       # 搜索 / 404 / 隐私 / 网站地图
python3 _build/build_rd.py         # 科研子页
python3 _build/build_rd2.py
python3 _build/check.py            # 全站校验：标签闭合、图片与内链
```

⚠️ **注意**：直接手改这些生成页面的 HTML，再次运行对应脚本时会被覆盖。改内容请改 `_build/` 里的脚本，或改完后不要再运行生成脚本。`index.html` 与 `rd.html` 为手工维护，不受生成脚本影响。

## 待补充的内容（需甲方提供）
- 企业微信 / 公众号 / 视频号 / 抖音二维码
- VR 全景链接（首页、关于强纶、研发中心与实验室三处已预留位置）
- 资料下载中心的 PDF 文件（手册、数据表、检测报告、证书）
- 产品电镜图与产品视频
- 百度统计代码与 ICP 备案接入
