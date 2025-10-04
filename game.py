import streamlit as st
import json
import streamlit.components.v1 as components

st.set_page_config(page_title="Elveda", page_icon="🌻")

POPUP_MESSAGE = """Toplam 7609 kod parçacıgından oluşan bu web uygulaması sonsuz bir hatıra üzerine kapatılmıştır. Sunucu bu hafta içerisinde kapanacaktır.
Elveda 🌻"""

# Tek bir HTML bileşeninde pop-up + geri sayım
components.html(f"""
<div id="cd" style="font-family:-apple-system,Segoe UI,Roboto,Arial,sans-serif;
                   font-size:14px; color:#555; text-align:center; margin-top:12px;">
  ⏳ Geri Sayım hazırlanıyor…
</div>
<script>
(function(){{
  const MESSAGE = {json.dumps(POPUP_MESSAGE)};
  const LS_KEY_SHOWN = 'gv_popup_shown';
  const LS_KEY_START = 'gv_countdown_start';
  const FORTYEIGHT_H = 48*60*60*1000; // 48 saat
  const HARD_DEADLINE = new Date('2025-10-06T23:59:59+03:00').getTime(); // 6 Ekim 2025

  // Başlangıç zamanını oku
  let start = Number(localStorage.getItem(LS_KEY_START)) || 0;

  // Pop-up sadece bir kez gösterilsin
  if (!localStorage.getItem(LS_KEY_SHOWN)) {{
    alert(MESSAGE);                 // "Tamam" denene kadar bloklar
    localStorage.setItem(LS_KEY_SHOWN, '1');
    start = Date.now();             // Tam "Tamam" anında başlat
    localStorage.setItem(LS_KEY_START, String(start));
  }} else if (!start) {{
    // Kenar durum: daha önce gösterildi ama start yazılmadıysa başlat
    start = Date.now();
    localStorage.setItem(LS_KEY_START, String(start));
  }}

  // Bitiş zamanı: 48 saat sonra, ama 6 Ekim 2025'i aşamaz (kilit)
  const deadline = Math.min(start + FORTYEIGHT_H, HARD_DEADLINE);

  function pad(n) {{ return n < 10 ? '0' + n : '' + n; }}
  const cdEl = document.getElementById('cd');
  let timerId = null;

  function tick(){{
    const now = Date.now();
    let ms = deadline - now;

    if (ms <= 0) {{
      cdEl.textContent = '⏳ Geri sayım bitti — 6 Ekim 2025';
      if (timerId) clearInterval(timerId);
      return;
    }}

    const totalSec = Math.floor(ms / 1000);
    const h = Math.floor(totalSec / 3600);
    const m = Math.floor((totalSec % 3600) / 60);
    const s = totalSec % 60;

    cdEl.textContent = '⏳ Geri Sayım: ' + pad(h) + ':' + pad(m) + ':' + pad(s)
                     + ' (Bitiş: 6 Ekim 2025)';
  }}

  tick();
  timerId = setInterval(tick, 1000);
}})();
</script>
""", height=60)
