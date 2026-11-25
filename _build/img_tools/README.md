# 产品图统一处理（2026.11.25 甲方 3.0 第 3/5/10 条）

- `unify.py pc.json`：把产品图抠出（rembg isnet-general-use），统一亮度（压高光防过曝、暗部提亮），
  放到同一浅灰白底、同一比例、同一投影上，输出 `img/pc-*.webp`（1200×900）。
  模式：`rembg`（默认）/ `white`（白底渲染图）/ `poly`（手工轮廓）/ `tubes`（排列圆管）/ `swatch`（满幅面料做样布块）。
- `brighten.py 图1 图2 …`：偏暗的现场照片提亮到中位亮度约 118，带高光软肩，不过曝。
- pc.json 中 `/home/claude/jlsite/raw/` 开头的是从 www.jl-fiber.com 下载的原站 1800px 原图。
- 依赖：`pip install "rembg[cpu]" onnxruntime pillow numpy`
