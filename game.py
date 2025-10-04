import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Elveda", page_icon="🌻")

HEADLINE = """Bu uygulama kapatıldı.
Sunucu 06.10.2025 00:01 (Europe/Istanbul) tarihinde durdurulacaktır.
"""

# Hedef: 06 Ekim 2025, 00:01 (İstanbul, UTC+03)
DEADLINE_ISO = "2025-10-06T00:01:00+03:00"

components.html(f"""
<div style="
  font-family:-apple-system,Segoe UI,Roboto,Arial,sans-serif;
  -webkit-text-size-adjust:100%;
  display:flex;justify-content:center;">
  <div style="max-width:900px;margin:20px;text-align:center;">
    <h2 style="margin:0 0 12px 0;font-weight:800;line-height:1.35;">
      {HEADLINE.replace('\\n','<br>')}
    </h2>

    <style>
      /* Sayaç (responsive) */
      #cd {{
        font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono','Courier New', monospace;
        font-weight: 800;
        letter-spacing: 0.5px;
        font-size: clamp(24px, 8vw, 42px);
        margin-top: 8px;
        white-space: nowrap;
      }}
      /* Silme animasyonlu alt yazı */
      #erase {{
        font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono','Courier New', monospace;
        font-weight: 800;
        font-size: clamp(16px, 4.8vw, 22px);
        color: #d32f2f; /* kırmızı vurgu */
        display:inline-block;
        position: relative;
        margin-top: 12px;
        letter-spacing: .3px;
      }}
      /* Kayan silme vuruşu (strike) */
      #erase::before {{
        content: "";
        position:absolute;
        left:-10%;
        top:50%;
        height:2px;
        width:0;
        background: currentColor;
        box-shadow: 0 0 8px rgba(211,47,47,.6);
        transform: translateY(-50%);
        animation: strike 2.2s ease-in-out infinite;
      }}
      /* Silgi izi efekti */
      #erase::after {{
        content: "";
        position:absolute;
        top:-15%;
        left:-30%;
        width:22%;
        height:130%;
        background: rgba(211,47,47,0.12);
        filter: blur(1.5px);
        transform: skewX(-15deg);
        animation: wipe 2.2s ease-in-out infinite;
      }}
      @keyframes strike {{
        0%   {{ width:0; opacity:0; }}
        10%  {{ opacity:1; }}
        50%  {{ width:120%; }}
        80%  {{ left:120%; width:0; }}
        100% {{ left:120%; width:0; opacity:0; }}
      }}
      @keyframes wipe {{
        0%   {{ left:-30%; }}
        50%  {{ left:110%; }}
        100% {{ left:110%; }}
      }}
      /* Nokta animasyonu */
      #dots {{
        display:inline-block;
        width: 1.5ch;
        text-align: left;
        margin-left: 2px;
      }}

      @media (max-width:420px) {{
        h2 {{ font-size: 18px; }}
      }}
    </style>

    <div id="cd">Kalan süre hesaplanıyor…</div>

    <!-- Animasyonlu alt yazı -->
    <div id="erase">7609 kod parçacığı siliniyor<span id="dots"></span></div>
  </div>
</div>

<script>
(function() {{
  // Sabit hedef saati (+03:00)
  const DEADLINE = new Date("{DEADLINE_ISO}").getTime();
  const cdEl = document.getElementById('cd');
  const dotsEl = document.getElementById('dots');

  function pad(n) {{ return (n<10?'0':'') + n; }}

  function tickCountdown() {{
    const now = Date.now();
    let ms = DEADLINE - now;

    if (ms <= 0) {{
      cdEl.textContent = "⏳ Geri sayım bitti — Sunucu kapanıyor";
      return;
    }}

    const totalSec = Math.floor(ms / 1000);
    const d = Math.floor(totalSec / 86400);
    const h = Math.floor((totalSec % 86400) / 3600);
    const m = Math.floor((totalSec % 3600) / 60);
    const s = totalSec % 60;

    cdEl.textContent = (d>0 ? (d + " gün ") : "") + pad(h) + ":" + pad(m) + ":" + pad(s);
  }}

  // Nokta animasyonu (…)
  let dot = 0;
  function tickDots() {{
    dot = (dot + 1) % 4;
    dotsEl.textContent = ".".repeat(dot);
  }}

  tickCountdown();
  setInterval(tickCountdown, 1000);
  tickDots();
  setInterval(tickDots, 400);
}})();
</script>
""", height=360)
