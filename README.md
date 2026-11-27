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

## 页面是怎么生成的（2026.11.23 起全部页面由脚本生成，含首页与科研总览）
```bash
cd _build
for s in home divisions about about2 rdmain rd rd2 apps select select2 insights news contact util articles; do python3 build_$s.py; done
```
- `divisions.py` —— 五大事业部（净化 / 机加工 / 滤材 / 纱线 / 热动）产品数据，文字取自各事业部上传资料
- `layout.py` —— 页头（公司全称 logo、下拉导航）、页脚
- `v5.css` —— 2026.11.23 明亮版主题（最后加载）；`home.css` —— 首页与产品树
- 已撤页面（platforms / specs / downloads / encyclopedia / qa / p-detail / news-20）在 `netlify.toml` 做 301 跳转

⚠️ **注意**：直接手改这些生成页面的 HTML，再次运行对应脚本时会被覆盖。改内容请改 `_build/` 里的脚本，或改完后不要再运行生成脚本。`index.html` 与 `rd.html` 为手工维护，不受生成脚本影响。

## 待补充的内容（需甲方提供）
- 企业微信 / 公众号 / 视频号 / 抖音二维码
- VR 全景链接（首页、关于强纶、研发中心与实验室三处已预留位置）
- 资料下载中心的 PDF 文件（手册、数据表、检测报告、证书）
- 产品电镜图与产品视频
- 百度统计代码与 ICP 备案接入

## 2026.11.27 甲方《修改意见 4.0》
- 第 1 条：进站动画重做（`intro.js` v7）。同一束纤维依次变成：一根丝（拉丝）→ 加捻成线 → 经纬织造 → 铺网烧结成毡 → 汇聚成 logo 与公司全称。标记与样式在 `_build/build_home.py` 的 INTRO 和 `home.css`。
- 第 7 条：行业方案页左文右图比例（`v5.css` 的 `.sol2` / `.solimg`），图片统一 4:3 并限高。
- 第 10 条：人才招聘首屏改为右侧相框照片（`.jobhero-g`），不再把合影放大做背景。
- 第 2–6、8、9 条及全站产品图：改为甲方原图 + image2 精修，清单与指令见修图包；精修图返回后替换 `img/pc-*.webp`。
- 2026.11.27 追加：24 张 image2 精修图已替换上线（第 2–6、8、9 条）。流程：`_build/img_tools/apply_retouched.py`（编号 → 网站文件名的对照表）→ `variants.py` 的 `flatten()` 把每张图的影棚背景校平成统一的 #f6f6f4 → 输出 `img/pc-*.webp`（1440×1080）。
  `variants.py` 另外生成不裁产品的衍生图：首页首屏拼图（`pc-media-felt-tall`、`pc-*-sq`）和内页首屏横幅（`hero-jl-cart/felt/yarn`）。
  `v5.css` 末尾规定 `img/pc-*` 一律整件显示（contain）、图框底色与图片背景同色，任何比例的图框都不会裁掉产品。
