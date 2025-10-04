import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Elveda", page_icon="🌻")

HEADLINE = """Bu uygulama kapatıldı.
Sunucu 06.10.2025 00:01 (Europe/Istanbul) tarihinde durdurulacaktır.
Elveda 🌻"""

# Hedef an: 06 Ekim 2025, 00:01 (İstanbul = UTC+03)
DEADLINE_ISO = "2025-10-06T00:01:00+03:00"
DEADLINE_HUMAN = "06.10.2025 00:01 (Europe/Istanbul)"

components.html(f"""
<div style="font-family:-apple-system, Segoe UI, Roboto, Arial, sans-serif; display:flex; justify-content:center;">
  <div style="max-width:900px; margin:24px; text-align:center;">
    <h2 style="margin:0 0 12px 0; font-weight:700; line-height:1.35;">
      {HEADLINE.replace('\\n','<br>')}
    </h2>

    <div id="cd" style="font-size:40px; font-weight:800; letter-spacing:1px; margin-top:10px;">
      ⏳ Kapanışa kalan süre hesaplanıyor…
    </div>
    <div style="color:#666; margin-top:8px; font-size:14px;">
      Hedef: {DEADLINE_HUMAN}
    </div>
  </div>
</div>

<script>
(function() {{
  const DEADLINE = new Date("{DEADLINE_ISO}").getTime(); // 06.10.2025 00:01, UTC+03
  const cdEl = document.getElementById('cd');

  function pad(n) {{ return (n<10?'0':'') + n; }}

  function tick() {{
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

    cdEl.textContent = d > 0
      ? `⏳ {{"${{d}} gün "}}` + pad(h) + ":" + pad(m) + ":" + pad(s)
      : `⏳ ` + pad(h) + ":" + pad(m) + ":" + pad(s);
  }}

  tick();
  setInterval(tick, 1000);
}})();
</script>
""", height=230)
