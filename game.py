import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Elveda", page_icon="🌻")

HEADLINE = """Bu uygulama kapatıldı.
Sunucu 06.10.2025 00:01 (Europe/Istanbul) tarihinde kendini kapatacaktır.
Elveda 🌻"""

# Sunucu kapatılıyor
DEADLINE_ISO = "2025-10-06T00:01:00+03:00"
DEADLINE_HUMAN = "06.10.2025 00:01 (Europe/Istanbul)"

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
      /* Küçük ekranda otomatik ölçekleme */
      #cd {{
        font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono','Courier New', monospace;
        font-weight: 800;
        letter-spacing: 0.5px;
        font-size: clamp(24px, 8vw, 42px);
        margin-top: 8px;
        white-space: nowrap;
      }}
      #sub {{
        color:#666; margin-top:8px; font-size: clamp(12px, 3.5vw, 14px);
      }}
      @media (max-width:420px) {{
        h2 {{ font-size: 18px; }}
      }}
    </style>

    <div id="cd">Kalan süre hesaplanıyor…</div>
    <div id="sub">Hedef: {DEADLINE_HUMAN}</div>
  </div>
</div>

<script>
(function() {{
  const DEADLINE = new Date("{DEADLINE_ISO}").getTime(); // sabit hedef (+03:00)
  const cdEl = document.getElementById('cd');

  function pad(n) {{ return (n<10?'0':'') + n; }}

  function tick() {{
    const now = Date.now();
    let ms = DEADLINE - now;

    if (ms <= 0) {{
      cdEl.textContent = "Geri sayım bitti — Sunucu kapanıyor";
      return;
    }}

    const totalSec = Math.floor(ms / 1000);
    const d = Math.floor(totalSec / 86400);
    const h = Math.floor((totalSec % 86400) / 3600);
    const m = Math.floor((totalSec % 3600) / 60);
    const s = totalSec % 60;

    // 'd gün HH:MM:SS' (gün 0 ise gizle)
    const dayStr = d > 0 ? (d + " gün ") : "";
    cdEl.textContent = dayStr + pad(h) + ":" + pad(m) + ":" + pad(s);
  }}

  tick();
  setInterval(tick, 1000);
}})();
</script>
""", height=320)  # mobilde kesilmesin diye yüksek tuttuk
