import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Elveda", page_icon="🌻")

HEADLINE = """Bu uygulama kapatıldı.
Sunucu 06.10.2025 00:01 (Europe/Istanbul) tarihinde durdurulacaktır.
Elveda 🌻"""

TOTAL_PARTS = 7609
DEADLINE_ISO = "2025-10-06T00:01:00+03:00"   # 06 Ekim 2025 00:01 (TR)
ANCHOR_ISO   = "2025-10-04T22:11:00+03:00"   # Başlangıç: 04 Ekim 2025 22:11 (TR)

components.html(f"""
<div style="font-family:-apple-system,Segoe UI,Roboto,Arial,sans-serif; -webkit-text-size-adjust:100%;
            display:flex; justify-content:center;">
  <div style="max-width:900px; margin:20px; text-align:center;">
    <h2 style="margin:0 0 12px 0; font-weight:800; line-height:1.35;">
      {HEADLINE.replace('\\n','<br>')}
    </h2>

    <style>
      #cd {{
        font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono','Courier New', monospace;
        font-weight: 800; letter-spacing: 0.5px;
        font-size: clamp(24px, 8vw, 42px);
        margin-top: 8px; white-space: nowrap;
      }}

      #erase {{
        position: relative; display:inline-block; margin-top: 12px;
        font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono','Courier New', monospace;
        font-weight: 800; font-size: clamp(16px, 4.8vw, 22px); color:#d32f2f;
        letter-spacing:.3px;
      }}
      /* Silme/wipe animasyonu */
      #erase::before {{
        content:""; position:absolute; left:-10%; top:50%; height:2px; width:0;
        background: currentColor; box-shadow:0 0 8px rgba(211,47,47,.6);
        transform:translateY(-50%); animation: strike 2.2s ease-in-out infinite;
      }}
      #erase::after {{
        content:""; position:absolute; top:-15%; left:-30%; width:22%; height:130%;
        background: rgba(211,47,47,.12); filter:blur(1.5px); transform:skewX(-15deg);
        animation: wipe 2.2s ease-in-out infinite;
      }}
      #erase.done::before, #erase.done::after {{ display:none; }}
      @keyframes strike {{
        0% {{ width:0; opacity:0; }}
        10%{{ opacity:1; }}
        50%{{ width:120%; }}
        80%{{ left:120%; width:0; }}
        100%{{ left:120%; width:0; opacity:0; }}
      }}
      @keyframes wipe {{
        0% {{ left:-30%; }} 50% {{ left:110%; }} 100% {{ left:110%; }}
      }}

      #stats {{ 
        display:grid; grid-template-columns: 1fr 1fr; gap:8px; 
        margin-top:10px; justify-items:center; align-items:center;
      }}
      .stat {{ 
        font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono','Courier New', monospace;
        font-weight:800; font-size: clamp(14px, 4.2vw, 20px);
      }}
      .label {{ color:#444; margin-right:6px; font-weight:700; }}
      .num {{ color:#111; min-width: 6ch; display:inline-block; text-align:right; }}

      #bar {{ width:100%; height:10px; background:#eee; border-radius:6px; overflow:hidden; margin-top:8px; }}
      #fill {{ height:100%; width:0%; background:linear-gradient(90deg,#ef5350,#d32f2f); transition:width .3s linear; }}

      #dots {{ display:inline-block; width: 1.5ch; text-align:left; margin-left: 2px; }}

      @media (max-width:520px) {{
        #stats {{ grid-template-columns: 1fr; }}
        h2 {{ font-size: 18px; }}
      }}
    </style>

    <!-- Geri sayım -->
    <div id="cd">Kalan süre hesaplanıyor…</div>

    <!-- Animasyonlu başlık -->
    <div id="erase"><span id="total">{TOTAL_PARTS}</span> kod parçacığı siliniyor<span id="dots"></span></div>

    <!-- Silinen / Kalan -->
    <div id="stats">
      <div class="stat"><span class="label">Silinen —</span> <span class="num" id="deleted">0</span></div>
      <div class="stat"><span class="label">Kalan —</span>   <span class="num" id="remaining">{TOTAL_PARTS}</span></div>
    </div>

    <!-- İlerleme çubuğu -->
    <div id="bar"><div id="fill"></div></div>
  </div>
</div>

<script>
(function(){{
  const DEADLINE = new Date("{DEADLINE_ISO}").getTime();
  const ANCHOR   = new Date("{ANCHOR_ISO}").getTime();
  const TOTAL    = {TOTAL_PARTS};

  const spanTotal = DEADLINE - ANCHOR > 0 ? (DEADLINE - ANCHOR) : 1;

  const cdEl = document.getElementById('cd');
  const eraseEl = document.getElementById('erase');
  const delEl = document.getElementById('deleted');
  const remEl = document.getElementById('remaining');
  const dotsEl = document.getElementById('dots');
  const fillEl = document.getElementById('fill');

  function pad(n) {{ return (n<10?'0':'')+n; }}
  function trNum(x) {{ return x.toLocaleString('tr-TR'); }}

  function tick(){{
    const now = Date.now();

    // Sayaç (kalan süre)
    let msLeft = DEADLINE - now;
    if (msLeft <= 0) {{
      cdEl.textContent = "⏳ 00:00:00";
    }} else {{
      const sec = Math.floor(msLeft / 1000);
      const d = Math.floor(sec / 86400);
      const h = Math.floor((sec % 86400)/3600);
      const m = Math.floor((sec % 3600)/60);
      const s = sec % 60;
      cdEl.textContent = (d>0 ? (d + " gün ") : "") + pad(h)+":"+pad(m)+":"+pad(s);
    }}

    // Parçacıklar (04.10.25 22:11 → 06.10.25 00:01 aralığına sabit)
    let ratio = (now - ANCHOR) / spanTotal;   // 0→1
    if (ratio < 0) ratio = 0;
    if (ratio > 1) ratio = 1;

    const deleted = Math.round(TOTAL * ratio);
    const remaining = TOTAL - deleted;

    delEl.textContent = trNum(deleted);
    remEl.textContent = trNum(remaining);
    fillEl.style.width = (deleted / TOTAL * 100).toFixed(2) + "%";

    // Bittiğinde mesajı değiştir
    if (ratio >= 1) {{
      eraseEl.classList.add('done');
      eraseEl.textContent = "İşlem tamamlandı — sunucu kapanıyor";
      dotsEl && (dotsEl.textContent = "");
    }}
  }}

  // Nokta animasyonu (…)
  let dot = 0;
  function tickDots(){{
    dot = (dot + 1) % 4;
    if (document.getElementById('erase').classList.contains('done')) return;
    dotsEl.textContent = ".".repeat(dot);
  }}

  tick();
  setInterval(tick, 1000);
  tickDots();
  setInterval(tickDots, 400);
}})();
</script>
""", height=450)
