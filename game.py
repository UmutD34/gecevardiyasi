import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Elveda", page_icon="🌻")

HEADLINE = """Bu uygulama kapatıldı.
Sunucu 06.10.2025 tarihinde durdurulacaktır.
Elveda 🌻"""

components.html(f"""
<div style="font-family:-apple-system, Segoe UI, Roboto, Arial, sans-serif; display:flex; justify-content:center;">
  <div style="max-width:900px; margin:24px; text-align:center;">
    <h2 style="margin:0 0 12px 0; font-weight:700; line-height:1.35;">
      {HEADLINE.replace('\\n','<br>')}
    </h2>

    <div style="font-size:36px; font-weight:700; letter-spacing:1px; margin-top:8px;">
      sunucu kapatılıyor
    </div>
  </div>
</div>
""", height=200)
