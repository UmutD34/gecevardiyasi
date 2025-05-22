import streamlit as st
from PIL import Image

# 1) Asset yükleme
sunflower = Image.open("assets/dilay_sunflower.png")
umut = Image.open("assets/umut_hero.png")
# ... diğerleri

# 2) State yönetimi
if 'level' not in st.session_state:
    st.session_state.level = 1
    st.session_state.health = 100
    st.session_state.score = 0
    st.session_state.enemy_queue = ['gece', 'ogrenci', ...]

# 3) UI
st.image(sunflower, width=200)
st.image(umut, width=80)
st.progress(st.session_state.health / 100)

# 4) Saldırı butonu
if st.button("Saldır"):
    # düşmana hasar
    st.session_state.score += 10
    # canı güncelle
    st.session_state.health -= 5

# 5) Bölüm geçişi
if st.session_state.health <= 0:
    st.session_state.level += 1
    st.session_state.health = 100
