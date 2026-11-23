/* 强纶官网 · 进站动画 v6（2026.11.23）
   金银纤维旋流 → 汇聚成 logo 与公司全称 → 金属高光扫过 → 纤维炸散、金光铺开进入首页
   每次会话播一次；点击 / 按键 / 滚轮 / “跳过”可跳过；?intro=1 强制重放；减少动态效果时不播 */
(function () {
  var el = document.getElementById('qlintro');
  if (!el) return;
  var force = /[?&]intro=1/.test(location.search), seen = false;
  try { seen = sessionStorage.getItem('qlIntro6') === '1'; } catch (e) {}
  if ((seen && !force) || matchMedia('(prefers-reduced-motion: reduce)').matches) { el.remove(); return; }
  el.style.display = '';
  document.documentElement.classList.add('qi-lock');

  var cv = el.querySelector('canvas'), cx = cv.getContext('2d');
  var W, H, dpr = Math.min(2, window.devicePixelRatio || 1), mobile = innerWidth < 760;
  function size() { W = innerWidth; H = innerHeight; cv.width = W * dpr; cv.height = H * dpr; cv.style.width = W + 'px'; cv.style.height = H + 'px'; cx.setTransform(dpr, 0, 0, dpr, 0, 0); }
  size();

  var N = mobile ? 1300 : 2800, P = [], T0 = 0, done = false, raf, targetsReady = false;
  var GOLD = ['255,212,0', '255,196,0', '255,226,90', '255,179,0', '240,200,80'], SILV = ['226,230,236', '200,206,214', '245,247,250'];
  for (var i = 0; i < N; i++) {
    var a = Math.random() * Math.PI * 2, r = Math.max(W, H) * (0.35 + Math.random() * 0.75);
    P.push({
      a: a, r: r, sp: (Math.random() < .5 ? -1 : 1) * (0.6 + Math.random() * 1.2), z: Math.random(),
      x: W / 2 + Math.cos(a) * r, y: H / 2 + Math.sin(a) * r * 0.55, px: 0, py: 0,
      tx: W / 2, ty: H / 2, c: Math.random() < 0.72 ? GOLD[i % GOLD.length] : SILV[i % SILV.length],
      w: Math.random() < 0.15 ? 1.6 : 0.8, d: Math.random() * 0.35, vx: 0, vy: 0
    });
  }

  /* 目标点：logo 图形 + 公司全称字形 */
  function buildTargets() {
    var oc = document.createElement('canvas'), ow = Math.round(W), oh = Math.round(H);
    oc.width = ow; oc.height = oh;
    var o = oc.getContext('2d');
    var fs = Math.max(20, Math.min(62, W / 15));
    var logoR = Math.min(110, Math.max(64, W / 12));
    var cy = H / 2 - fs * 0.9;
    var img = el.querySelector('.qi-mark img');
    try {
      o.save(); o.beginPath(); o.arc(W / 2, cy - logoR * 0.55, logoR / 2, 0, Math.PI * 2); o.clip();
      o.drawImage(img, W / 2 - logoR / 2, cy - logoR * 1.05, logoR, logoR); o.restore();
    } catch (e) {}
    o.fillStyle = '#c00000';
    o.font = '900 ' + fs + 'px "Noto Serif SC","Songti SC","SimSun",serif';
    o.textAlign = 'center'; o.textBaseline = 'middle';
    var name = '福建强纶新材料股份有限公司';
    if (W < 560) { o.fillText('福建强纶新材料', W / 2, cy + fs * 1.0); o.fillText('股份有限公司', W / 2, cy + fs * 2.25); }
    else { o.fillText(name.split('').join(String.fromCharCode(8202)), W / 2, cy + fs * 1.15); }
    var data = o.getImageData(0, 0, ow, oh).data, pts = [], step = mobile ? 3 : 3;
    for (var y = 0; y < oh; y += step) for (var x = 0; x < ow; x += step) {
      var k = (y * ow + x) * 4, rr = data[k], gg = data[k + 1], aa = data[k + 3];
      if (aa > 128 && rr > 140 && gg < 120) pts.push([x, y]);
    }
    for (var j = pts.length - 1; j > 0; j--) { var q = Math.floor(Math.random() * (j + 1)), t = pts[j]; pts[j] = pts[q]; pts[q] = t; }
    if (pts.length) for (var n = 0; n < N; n++) { var p = P[n], tp = pts[n % pts.length]; p.tx = tp[0] + (Math.random() - .5) * 1.2; p.ty = tp[1] + (Math.random() - .5) * 1.2; }
    targetsReady = true;
    el.style.setProperty('--qfs', fs + 'px');
    el.style.setProperty('--qty', (W < 560 ? cy + fs * 1.62 : cy + fs * 1.15) + 'px');
    el.style.setProperty('--qly', (cy - logoR * 0.55) + 'px');
    el.style.setProperty('--qlr', logoR + 'px');
    el.classList.toggle('qi-narrow', W < 560);
  }

  function ease(t) { return t < 0 ? 0 : t > 1 ? 1 : 1 - Math.pow(1 - t, 3); }
  function easeIO(t) { return t < 0 ? 0 : t > 1 ? 1 : t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2; }

  function frame(now) {
    if (!T0) T0 = now;
    var e = (now - T0) / 1000;
    /* 拖尾：底色半透明覆盖 */
    cx.globalCompositeOperation = 'source-over';
    cx.fillStyle = e < 1.6 ? 'rgba(12,11,9,0.20)' : 'rgba(12,11,9,0.30)';
    cx.fillRect(0, 0, W, H);
    cx.globalCompositeOperation = 'lighter';
    var cxp = W / 2, cyp = H / 2;
    var form = easeIO((e - 1.0) / 1.3);              // 1.0s 起汇聚
    var burst = e > 3.85 ? (e - 3.85) : 0;            // 3.85s 起炸散
    var sweepX = (e - 2.75) / 0.9 * (W + 400) - 200;  // 高光扫过
    for (var i = 0; i < N; i++) {
      var p = P[i];
      p.px = p.x; p.py = p.y;
      var k = Math.max(0, Math.min(1, (e - p.d) / 1.6));
      var spin = p.a + p.sp * e * 1.25;
      var rr = p.r * (1 - 0.55 * ease(k));
      var sx = cxp + Math.cos(spin) * rr, sy = cyp + Math.sin(spin) * rr * 0.42 + Math.sin(spin * 2 + p.z * 6) * 18;
      var f = targetsReady ? Math.min(1, Math.max(0, form - p.d * 0.4) / (1 - p.d * 0.4)) : 0;
      var x = sx + (p.tx - sx) * f, y = sy + (p.ty - sy) * f;
      if (burst) {
        if (!p.vx) { var dx = p.x - cxp, dy = p.y - cyp, L = Math.hypot(dx, dy) || 1; var s = 6 + Math.random() * 16; p.vx = dx / L * s; p.vy = dy / L * s; }
        p.vx *= 1.06; p.vy *= 1.06; x = p.x + p.vx; y = p.y + p.vy;
      }
      p.x = x; p.y = y;
      var lum = 0.55 + p.z * 0.45;
      if (f > 0.9 && !burst) lum *= 1.9;
      if (f > 0.95 && !burst) { var dd = Math.abs(x - sweepX - (y - cyp) * 0.35); if (dd < 70) lum += (1 - dd / 70) * 1.2; }
      var al = Math.min(1, (0.25 + 0.75 * Math.min(1, e / 0.6)) * lum);
      cx.strokeStyle = 'rgba(' + p.c + ',' + al.toFixed(3) + ')';
      cx.lineWidth = p.w * (f > 0.9 && !burst ? 1.6 : 1);
      cx.beginPath(); cx.moveTo(p.px, p.py); cx.lineTo(x + 0.01, y + 0.01); cx.stroke();
    }
    /* 中心辉光 */
    var g = cx.createRadialGradient(cxp, cyp, 0, cxp, cyp, Math.max(W, H) * 0.45);
    var ga = 0.05 + 0.06 * form;
    g.addColorStop(0, 'rgba(255,200,60,' + ga + ')'); g.addColorStop(1, 'rgba(255,200,60,0)');
    cx.fillStyle = g; cx.fillRect(0, 0, W, H);
    if (!done) raf = requestAnimationFrame(frame);
  }

  var tm = [];
  function at(ms, fn) { tm.push(setTimeout(fn, ms)); }
  function start() {
    buildTargets();
    el.classList.add('qi-go');
    raf = requestAnimationFrame(frame);
    at(2500, function () { el.classList.add('qi-s2'); });
    at(3850, function () { el.classList.add('qi-s3'); });
    at(4450, finish);
  }
  function finish() {
    if (done) return; done = true;
    tm.forEach(clearTimeout); cancelAnimationFrame(raf);
    try { sessionStorage.setItem('qlIntro6', '1'); } catch (e) {}
    el.classList.add('qi-out');
    document.documentElement.classList.remove('qi-lock');
    setTimeout(function () { el.remove(); }, 900);
  }
  /* 等字体与 logo 就绪（最多 700ms），保证字形采样正确 */
  var img = el.querySelector('.qi-mark img'), waits = [];
  if (img && !img.complete) waits.push(new Promise(function (r) { img.onload = img.onerror = r; }));
  if (document.fonts && document.fonts.load) waits.push(document.fonts.load('900 60px "Noto Serif SC"', '福建强纶新材料股份有限公司').catch(function () {}));
  Promise.race([Promise.all(waits), new Promise(function (r) { setTimeout(r, 700); })]).then(start);
  at(9000, finish);

  el.querySelector('.qi-skip').onclick = function (e) { e.stopPropagation(); finish(); };
  el.addEventListener('click', finish);
  addEventListener('keydown', finish, { once: true });
  addEventListener('wheel', finish, { once: true, passive: true });
  addEventListener('touchmove', finish, { once: true, passive: true });
  addEventListener('resize', function () { if (!done) { size(); buildTargets(); } });
})();
