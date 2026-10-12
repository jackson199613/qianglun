# 强论 · 社区首页

纯静态网站（HTML + CSS + JS），无需安装任何依赖。

## 文件说明
- `index.html` —— 首页（板块、热帖、今日辩题投票、深浅色切换、搜索过滤）
- `netlify.toml` —— Netlify 部署配置
- `README.md` —— 本说明

## 一次性设置：GitHub → Netlify 自动部署

### 1. 上传到 GitHub
1. 登录 github.com，右上角 **+ → New repository**，起名如 `qianglun`，点 **Create repository**。
2. 在新仓库页面点 **uploading an existing file**（或 **Add file → Upload files**）。
3. 把 `index.html`、`netlify.toml`、`README.md` 拖进去，点 **Commit changes**。

> 注意：文件要直接在仓库根目录，不要套一层文件夹。

### 2. 连接 Netlify
1. 登录 app.netlify.com（可直接用 GitHub 账号登录）。
2. **Add new site → Import an existing project → GitHub**，授权后选择 `qianglun` 仓库。
3. Build command 留空，Publish directory 填 `.`（netlify.toml 已经写好，一般会自动带出）。
4. 点 **Deploy**，几十秒后得到 `xxx.netlify.app` 网址。

### 3. 以后怎么更新
在 GitHub 仓库里修改或重新上传文件 → Commit，Netlify 会**自动重新部署**，1 分钟内生效。

### 可选：绑定自己的域名
Netlify 站点 → **Domain management → Add a domain**，按提示在域名服务商处添加 DNS 记录，HTTPS 证书会自动签发。

## 修改内容
板块、帖子、活跃用户都在 `index.html` 底部 `<script>` 里的示例数据中（`boards`、`threads`、`users`），直接改文字即可。

## 下一步（让论坛真正能发帖）
目前是静态展示页，登录/注册/发帖还需要后端。常见做法：
- **Supabase / Firebase**：提供账号登录和数据库，前端直接调用，仍可部署在 Netlify；
- **Discourse / Flarum**：成熟的开源论坛程序，需要自己的服务器；
- 首页继续用这个静态页，"进入论坛"按钮跳转到论坛程序。
