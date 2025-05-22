import streamlit as st

# ----------------------
# Başlangıç: State Yönetimi
# ----------------------
if 'level' not in st.session_state:
    st.session_state.level = 1
    st.session_state.health = 100
    st.session_state.score = 0
    st.session_state.enemy_health = 100

# ----------------------
# Yardımcı Fonksiyonlar
# ----------------------
def reset_enemy():
    st.session_state.enemy_health = 100


def next_level():
    st.session_state.level += 1
    st.session_state.health = 100
    reset_enemy()


def check_defeat():
    # Düşman yenildiyse seviye atla
    if st.session_state.enemy_health <= 0:
        st.success("Düşmanı yendin! Bir sonraki bölüme geçiliyor.")
        next_level()
    # Oyuncunun canı sıfırsa oyun biter
    if st.session_state.health <= 0:
        st.error("Canın tükendi! Oyunu kaybettin.")
        if st.button("Baştan Başla"):
            st.session_state.level = 1
            st.session_state.health = 100
            st.session_state.score = 0
            reset_enemy()

# ----------------------
# UI Bileşenleri
# ----------------------
def render_ui():
    st.title(f"🌻 DİLAY'I KORU - Seviye {st.session_state.level}")
    # Barlar
    st.progress(st.session_state.health / 100, text="Can")
    st.progress(st.session_state.enemy_health / 100, text="Düşman Can")
    st.markdown(f"**Skor:** {st.session_state.score}")
    st.write("---")

# ----------------------
# Bölüm Fonksiyonları
# ----------------------
def level_gece_vardiyasi():
    st.subheader("Bölüm 1: Gece Vardiyası")
    st.write("🌙 Gece saatlerinde koruma görevini üstlen.")
    if st.button("Saldır ⚔️"):
        st.session_state.enemy_health -= 25
        st.session_state.score += 15
    if st.button("Savun 🛡️"):
        st.session_state.health = min(100, st.session_state.health + 15)
    check_defeat()


def level_sorunlu_ogrenciler():
    st.subheader("Bölüm 2: Sorunlu Öğrenciler")
    st.write("👦👧 Ders sırasında dikkat dağınıklığını gider.")
    if st.button("Disiplin Uygula 👮‍♂️"):
        st.session_state.enemy_health -= 20
        st.session_state.score += 10
    if st.button("Mola Ver 🚶‍♂️"):
        st.session_state.health = min(100, st.session_state.health + 10)
    check_defeat()


def level_sorunlu_veliler():
    st.subheader("Bölüm 3: Sorunlu Veliler")
    st.write("🧔👩 Velilerin endişelerini yatıştır.")
    if st.button("Konuşma Yap 🗣️"):
        st.session_state.enemy_health -= 15
        st.session_state.score += 12
    if st.button("Empati Kur ❤️"):
        st.session_state.health = min(100, st.session_state.health + 12)
    check_defeat()


def level_fare_istilasi():
    st.subheader("Bölüm 4: Fare İstilası")
    st.write("🐭 Minik istilacılara karşı savun.")
    if st.button("Kovala 🏃‍♂️"):
        st.session_state.enemy_health -= 30
        st.session_state.score += 20
    if st.button("Kapan Kur 🪤"):
        st.session_state.health = min(100, st.session_state.health + 5)
    check_defeat()


def level_su_basmasi():
    st.subheader("Bölüm 5: Su Basması")
    st.write("💧 Suyu engelle.")
    if st.button("Pompa Çalıştır 🔧"):
        st.session_state.enemy_health -= 25
        st.session_state.score += 15
    if st.button("Baraj Kur 🧱"):
        st.session_state.health = min(100, st.session_state.health + 15)
    check_defeat()


def level_asansor_saldirisi():
    st.subheader("Bölüm 6: Asansör Saldırısı")
    st.write("🛗 Asansörü kontrol et ve durdur.")
    if st.button("Fren Bas 🛑"):
        st.session_state.enemy_health -= 20
        st.session_state.score += 18
    if st.button("Kablo Onar 🔧"):
        st.session_state.health = min(100, st.session_state.health + 10)
    check_defeat()


def level_lavabo_dusu():
    st.subheader("Bölüm 7: Lavabo Düşmesi")
    st.write("🚰 Lavabonun su basıncını dengele.")
    if st.button("Vanayı Kapat 🚰"):
        st.session_state.enemy_health -= 25
        st.session_state.score += 15
    if st.button("Boru Tak 📏"):
        st.session_state.health = min(100, st.session_state.health + 15)
    check_defeat()

# ----------------------
# Ana Döngü
# ----------------------
render_ui()

level = st.session_state.level
if level == 1:
    level_gece_vardiyasi()
elif level == 2:
    level_sorunlu_ogrenciler()
elif level == 3:
    level_sorunlu_veliler()
elif level == 4:
    level_fare_istilasi()
elif level == 5:
    level_su_basmasi()
elif level == 6:
    level_asansor_saldirisi()
elif level == 7:
    level_lavabo_dusu()
else:
    st.balloons()
    st.success("Tebrikler, tüm bölümleri tamamladın! Skorun: {}".format(st.session_state.score))

# ----------------------
# Asset Yükleme Notu
# ----------------------
# Her bölüm fonksiyonunun başında kendi asset'inizi
# st.image("assets/<level_name>.png") ile gösterebilirsiniz.

