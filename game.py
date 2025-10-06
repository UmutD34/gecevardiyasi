import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Elveda", page_icon="🌻")

HEADLINE = """Bu uygulama kapatıldı.
Sunucu 07.10.2025 00:01 (Europe/Istanbul) tarihinde durdurulacaktır.
"""

TOTAL_PARTS = 7609
DEADLINE_ISO = "2025-10-07T00:01:00+03:00"   # Bitiş: 07.10.2025 00:01 (TR)
ANCHOR_ISO   = "2025-10-04T22:11:00+03:00"   # Başlangıç: 04.10.2025 22:11 (TR)

components.html(f"""
<div style="
  font-family:-apple-system,Segoe UI,Roboto,Arial,sans-serif;
  -webkit-text-size-adjust:100%;
  display:flex;justify-content:center;padding-bottom:env(safe-area-inset-bottom,24px);">
  <div style="max-width:900px;margin:20px;text-align:center;width:100%;padding-bottom:24px;">

    <h2 style="margin:0 0 12px 0;font-weight:800;line-height:1.35;">
      {HEADLINE.replace('\\n','<br>')}
    </h2>

    <style>
      :root {{
        --accent:#d32f2f;
        --muted:#666;
      }}

      /* CANLI */
      #live #cd {{
        font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono','Courier New', monospace;
        font-weight:800; letter-spacing:.5px;
        font-size: clamp(24px, 8vw, 42px);
        margin-top: 8px; white-space: nowrap;
      }}
      #live #erase {{
        position: relative; display:inline-block; margin-top: 12px;
        font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono','Courier New', monospace;
        font-weight:800; font-size: clamp(16px, 4.8vw, 22px); color:var(--accent);
        letter-spacing:.3px;
      }}
      #live #erase::before {{
        content:""; position:absolute; left:-10%; top:50%; height:2px; width:0;
        background: currentColor; box-shadow:0 0 8px rgba(211,47,47,.6);
        transform:translateY(-50%); animation: strike 2.2s ease-in-out infinite;
      }}
      #live #erase::after {{
        content:""; position:absolute; top:-15%; left:-30%; width:22%; height:130%;
        background: rgba(211,47,47,.12); filter:blur(1.5px); transform:skewX(-15deg);
        animation: wipe 2.2s ease-in-out infinite;
      }}
      #live #erase.done::before, #live #erase.done::after {{ display:none; }}
      @keyframes strike {{
        0% {{ width:0; opacity:0; }}
        10%{{ opacity:1; }}
        50%{{ width:120%; }}
        80%{{ left:120%; width:0; }}
        100%{{ left:120%; width:0; opacity:0; }}
      }}
      @keyframes wipe {{ 0%{{left:-30%;}} 50%{{left:110%;}} 100%{{left:110%;}} }}

      #live #stats {{ 
        display:grid; grid-template-columns: 1fr 1fr; gap:8px; 
        margin-top:10px; justify-items:center; align-items:center;
      }}
      #live .stat {{ 
        font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono','Courier New', monospace;
        font-weight:800; font-size: clamp(14px, 4.2vw, 20px);
      }}
      #live .label {{ color:#444; margin-right:6px; font-weight:700; }}
      #live .num {{ color:#111; min-width: 6ch; display:inline-block; text-align:right; }}
      #live #bar {{ width:100%; height:10px; background:#eee; border-radius:6px; overflow:hidden; margin-top:8px; }}
      #live #fill {{ height:100%; width:0%; background:linear-gradient(90deg,#ef5350,#d32f2f); transition:width .3s linear; }}
      #live #dots {{ display:inline-block; width:1.5ch; text-align:left; margin-left:2px; }}

      /* Bitiş sayfası */
      #finish {{ display:none; text-align:center; padding-bottom: env(safe-area-inset-bottom,24px); }}

      #finish .title {{
        font-weight:800; font-size: clamp(18px, 5.6vw, 28px); margin-top:10px;
      }}

      #finish .summary {{
        display:grid; grid-template-columns: 1fr 1fr; gap:10px; 
        justify-items:center; align-items:center; margin:12px 0;
        font-family: ui-monospace, Menlo, Consolas, monospace; font-weight:800;
      }}
      #finish .badge {{ 
        display:inline-block; padding:2px 8px; border-radius:10px; 
        background:#eee; font-size:12px; margin-left:6px; color:#555;
      }}

      #finish ul {{ list-style: none; padding:0; margin:10px auto; max-width:700px; text-align:left; }}
      /* mobil uyumlu liste öğeleri: wrap ve responsive */
      #finish li {{ 
        padding:10px 12px; margin:8px 0; background:#fafafa; border:1px solid #eee; border-radius:10px;
        display:flex; align-items:center; justify-content:space-between; gap:12px; 
        box-sizing:border-box; flex-wrap:wrap;
      }}
      #finish li .name {{ font-weight:700; flex:1 1 60%; min-width:0; text-align:left; word-break:break-word; }}
      #finish li .badge {{
        flex:0 0 auto; margin-left:8px; background:#fff0f0; color:#b71c1c;
        padding:6px 8px; border-radius:8px; font-size:12px; white-space:nowrap;
      }}

      #finish .offline {{ color:#b71c1c; font-weight:800; margin-top:12px; }}
      #finish .muted {{ color:var(--muted); font-size:13px; margin-top:10px; line-height:1.4; }}

      .fade-in {{ animation: fade .5s ease-out forwards; }}
      @keyframes fade {{ from{{opacity:0}} to{{opacity:1}} }}

      @media (max-width:520px) {{
        #live #stats, #finish .summary {{ grid-template-columns: 1fr; }}
        h2 {{ font-size: 18px; }}
        #finish li {{ padding:12px; }}
      }}
    </style>

    <!-- CANLI GÖRÜNÜM -->
    <div id="live">
      <div id="cd">Kalan süre hesaplanıyor…</div>
      <div id="erase"><span id="total">{TOTAL_PARTS}</span> kod parçacığı siliniyor<span id="dots"></span></div>

      <div id="stats">
        <div class="stat"><span class="label">Silinen —</span> <span class="num" id="deleted">0</span></div>
        <div class="stat"><span class="label">Kalan —</span>   <span class="num" id="remaining">{TOTAL_PARTS}</span></div>
      </div>

      <div id="bar"><div id="fill"></div></div>
    </div>

    <!-- BİTİŞ SAYFASI -->
    <div id="finish">
      <div class="title">Bu uygulama <strong>07.10.2025 00:01</strong> tarihinde kapatıldı;<br>sunucu bağlantısı kesildi.</div>

      <div class="summary">
        <div>Silinen — <span id="fin_deleted">-</span></div>
        <div>Kalan — <span id="fin_remaining">-</span></div>
      </div>

      <div style="font-weight:800; margin-top:12px;">Veritabanından silinen oyun ve uygulamalar:</div>
      <ul>
        <li><span class="name">Gece vardiyası maratonu</span></li>
        <li><span class="name">Gece vardiyası bilgi yarışması</span></li>
        <li><span class="name">Kuzey ışıkları video yönlendiricisi</span></li>
        <li><span class="name">Gece vardiyası müdürle savaş</span><span class="badge">Aktifleştirilmemiş • tamamlanamamış proje</span></li>
        <li><span class="name">Gece vardiyası yalnızlık koruyucu eldiveni yakala</span><span class="badge">Aktifleştirilmemiş • tamamlanamamış proje</span></li>
        <li><span class="name">Gece vardiyası karanlık asansörle savaş</span><span class="badge">Aktifleştirilmemiş • tamamlanamamış proje</span></li>
        <li><span class="name">Gece vardiyası ayçiçeğimi kötü insanlardan koruyucu yumruklar</span><span class="badge">Aktifleştirilmemiş • tamamlanamamış proje</span></li>
      </ul>

      <div class="offline">Tüm veriler ve yedeklemeler kaldırıldı. Sunucu bağlantısı kesildi.</div>
      <div class="muted">Streamlit sunucularında barındırılan projelerin silinmesinin ardından, sunucu hizmetinin kullanılmamasına rağmen gerçekleştirilen aylık ödemelerden doğabilecek maddi zararlardan Streamlit sunucuları sorumlu tutulamaz. Projelerin kaldırılması halinde yer sağlayıcılık hizmetinin iptali veya durdurulması geliştiricinin sorumluluğundadır.</div>
    </div>

  </div>
</div>

<script>
(function(){{
  const DEADLINE = new Date("{DEADLINE_ISO}").getTime();
  const ANCHOR   = new Date("{ANCHOR_ISO}").getTime();
  const TOTAL    = {TOTAL_PARTS};
  const spanTotal = Math.max(1, DEADLINE - ANCHOR);

  const live    = document.getElementById('live');
  const finish  = document.getElementById('finish');
  const cdEl    = document.getElementById('cd');
  const eraseEl = document.getElementById('erase');
  const delEl   = document.getElementById('deleted');
  const remEl   = document.getElementById('remaining');
  const dotsEl  = document.getElementById('dots');
  const fillEl  = document.getElementById('fill');
  const finDel  = document.getElementById('fin_deleted');
  const finRem  = document.getElementById('fin_remaining');

  function pad(n) {{ return (n<10?'0':'')+n; }}
  function trNum(x) {{ return x.toLocaleString('tr-TR'); }}

  function renderLive(now){{
    // Sayaç
    let msLeft = DEADLINE - now;
    if (msLeft <= 0) {{
      cdEl.textContent = "⏳ 00:00:00";
    }} else {{
      const sec = Math.floor(msLeft/1000);
      const d = Math.floor(sec/86400);
      const h = Math.floor((sec % 86400)/3600);
      const m = Math.floor((sec % 3600)/60);
      const s = sec % 60;
      cdEl.textContent = (d>0? (d+" gün "):"") + pad(h)+":"+pad(m)+":"+pad(s);
    }}

    // Parçacıklar
    let ratio = (now - ANCHOR) / spanTotal;  // 0→1
    ratio = Math.min(1, Math.max(0, ratio));
    const deleted   = Math.round(TOTAL * ratio);
    const remaining = TOTAL - deleted;

    delEl.textContent = trNum(deleted);
    remEl.textContent = trNum(remaining);
    fillEl.style.width = (deleted / TOTAL * 100).toFixed(2) + "%";

    return {{ratio, deleted, remaining}};
  }}

  function showFinish(finalDeleted, finalRemaining){{
    // Canlı kısmı gizle, bitişi göster
    if (dotsEl) dotsEl.textContent = "";
    eraseEl.classList.add('done');
    live.style.display = 'none';
    // Son değerleri yaz
    finDel.textContent = trNum(finalDeleted);
    finRem.textContent = trNum(finalRemaining);
    finish.style.display = 'block';
    finish.classList.add('fade-in');
    // sayfanın altına in (mobilde görünürlüğü arttırmak için)
    try {{ window.scrollTo({{ top: document.body.scrollHeight, behavior: 'smooth' }}); }} catch(e){{}}
  }}

  function tick(){{
    const now = Date.now();
    const {{ratio, deleted, remaining}} = renderLive(now);
    if (ratio >= 1) {{
      showFinish(TOTAL, 0); // tamamlanmış versiyon
      clearInterval(loop);
    }}
  }}

  // Nokta animasyonu (…)
  let dot=0;
  function tickDots(){{
    dot=(dot+1)%4;
    if (eraseEl.classList.contains('done')) return;
    if (dotsEl) dotsEl.textContent = ".".repeat(dot);
  }}

  // İlk çizim
  tick();
  const loop = setInterval(tick, 1000);
  tickDots(); setInterval(tickDots, 400);

  // Sayfa zaten deadline SONRASI açılırsa, doğrudan bitişi göster
  if (Date.now() >= DEADLINE) {{
    showFinish(TOTAL, 0);
  }}
}})();
</script>
""", height=920)
