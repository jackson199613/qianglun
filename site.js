/* 强纶官网 · 公共交互（内页用；首页另有自有脚本） */
(function () {
  var d = document;
  var hdr = d.getElementById('hdr');
  if (hdr) {
    var onScroll = function () {
      hdr.classList.toggle('solid', scrollY > 10);
      var t = d.getElementById('toTop');
      if (t) t.classList.toggle('show', scrollY > 600);
    };
    addEventListener('scroll', onScroll, { passive: true }); onScroll();
  }
  var burger = d.getElementById('burger'), menu = d.getElementById('menu');
  if (burger && menu) burger.addEventListener('click', function () {
    var open = menu.classList.toggle('open');
    burger.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  var sBtn = d.getElementById('searchBtn'), sBox = d.getElementById('search'), sX = d.getElementById('searchX'), q = d.getElementById('q');
  if (sBtn && sBox) {
    sBtn.addEventListener('click', function () { sBox.hidden = !sBox.hidden; if (!sBox.hidden && q) q.focus(); });
    if (sX) sX.addEventListener('click', function () { sBox.hidden = true; });
    if (q) q.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' && q.value.trim()) location.href = 'search.html?q=' + encodeURIComponent(q.value.trim());
    });
  }
  var top = d.getElementById('toTop');
  if (top) top.addEventListener('click', function () { scrollTo({ top: 0, behavior: 'smooth' }); });

  /* 滚动揭示 */
  var rv = d.querySelectorAll('.rv');
  if (rv.length) {
    if (!('IntersectionObserver' in window)) { rv.forEach(function (e) { e.classList.add('in'); }); }
    else {
      var io = new IntersectionObserver(function (es) {
        es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
      }, { rootMargin: '0px 0px -8% 0px', threshold: .05 });
      rv.forEach(function (e) { io.observe(e); });
    }
  }
  /* 折叠问答 */
  d.querySelectorAll('.qa button').forEach(function (b) {
    b.addEventListener('click', function () {
      var qa = b.closest('.qa'); var open = qa.classList.toggle('open');
      b.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
  /* 企业宣传片：点击封面开始播放 */
  d.querySelectorAll('[data-player]').forEach(function (p) {
    var v = p.querySelector('video'), c = p.querySelector('.cover');
    if (!v || !c) return;
    c.addEventListener('click', function () {
      p.classList.add('playing');
      v.preload = 'auto';
      var r = v.play();
      if (r && r.catch) r.catch(function () {});
    });
    v.addEventListener('ended', function () { p.classList.remove('playing'); });
  });

  /* 页脚社交入口：移动端点一下展开二维码 */
  document.querySelectorAll('.sq').forEach(function (el) {
    el.addEventListener('click', function (e) {
      if (!window.matchMedia('(hover: none)').matches) return;   // 桌面用悬停
      var pop = el.querySelector('.pop');
      if (!pop) return;
      if (el.tagName === 'A') return;                            // 抖音等有链接的，直接跳转
      e.preventDefault();
      document.querySelectorAll('.sq.on').forEach(function (o) { if (o !== el) o.classList.remove('on'); });
      el.classList.toggle('on');
    });
  });
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.sq')) document.querySelectorAll('.sq.on').forEach(function (o) { o.classList.remove('on'); });
  });

  /* VR 全景：填入链接后自动嵌入 */
  d.querySelectorAll('[data-vr]').forEach(function (a) {
    var url = a.getAttribute('data-vr');
    if (!url) return;
    a.href = url; a.target = '_blank'; a.rel = 'noopener'; a.hidden = false;
    var box = d.querySelector('[data-vr-embed]');
    if (box) {
      var f = d.createElement('iframe');
      f.src = url; f.loading = 'lazy'; f.allowFullscreen = true;
      f.setAttribute('title', 'VR 全景');
      box.appendChild(f); box.classList.add('on');
    }
    var tip = d.querySelector('.vr-tip'); if (tip) tip.hidden = true;
  });

  /* 视频：后台填入地址后自动可播 */
  d.querySelectorAll('.vidbox video[data-src]').forEach(function (v) {
    var src = v.getAttribute('data-src');
    if (!src) return;
    v.src = src; v.preload = 'metadata';
    v.closest('.vidbox').classList.add('on');
  });

  /* 长表折叠 */
  d.querySelectorAll('.foldbtn[data-fold]').forEach(function (b) {
    var t = d.getElementById(b.getAttribute('data-fold'));
    if (!t) { b.hidden = true; return; }
    var rows = t.querySelectorAll('tbody tr').length;
    if (rows <= 8) { b.hidden = true; return; }
    b.addEventListener('click', function () {
      var on = t.classList.toggle('open');
      b.textContent = on ? b.getAttribute('data-less') : b.getAttribute('data-more');
    });
  });

  /* 筛选（产品/新闻等列表页通用：data-filter 控制 data-tag） */
  d.querySelectorAll('[data-filter]').forEach(function (bar) {
    var items = d.querySelectorAll(bar.getAttribute('data-filter'));
    bar.querySelectorAll('button').forEach(function (btn) {
      btn.addEventListener('click', function () {
        bar.querySelectorAll('button').forEach(function (x) { x.classList.remove('on'); });
        btn.classList.add('on');
        var v = btn.getAttribute('data-v');
        items.forEach(function (it) {
          var tag = it.getAttribute('data-tag') || '';
          it.hidden = !(v === 'all' || tag.split(' ').indexOf(v) > -1);
        });
      });
    });
  });
})();
