import streamlit as st

# ----------------------
# State Yönetimi
# ----------------------
if 'stage' not in st.session_state:
    st.session_state.stage = 'intro'
    st.session_state.player_health = 100
    st.session_state.enemy_health = 100
    st.session_state.score = 0

# ----------------------
# Yardımcı Fonksiyonlar
# ----------------------
def restart_game():
    st.session_state.stage = 'intro'
    st.session_state.player_health = 100
    st.session_state.enemy_health = 100
    st.session_state.score = 0


def next_stage():
    order = ['intro', 'gece_mail', 'ogrenciler', 'veliler', 'fare', 'su', 'asansor', 'lavabo', 'finished']
    idx = order.index(st.session_state.stage)
    st.session_state.stage = order[idx + 1]
    st.session_state.player_health = 100
    st.session_state.enemy_health = 100


def render_bars():
    st.progress(st.session_state.player_health / 100, text="Can")
    st.progress(st.session_state.enemy_health / 100, text="Düşman Can")

# ----------------------
# Uygulama Başlığı
# ----------------------
st.title("🌻 DİLAY'I KORU")
stage = st.session_state.stage

# ----------------------
# Intro
# ----------------------
if stage == 'intro':
    st.write("**Gece vardiyasına hoş geldiniz!**\n\nBu gece vardiyasını yenmek için yeterince cesur musun? 🤔")
    col1, col2 = st.columns(2)
    if col1.button("Evet, hazırım! 💪"):
        next_stage()
    if col2.button("Hayır, korkuyorum 😱"):
        st.error("Korkuya yenik düştün! Oyunu kaybettin. 😔")
        if st.button("Tekrar Dene"):
            restart_game()

# ----------------------
# Bölüm 1: Mail Saldırısı
# ----------------------
elif stage == 'gece_mail':
    st.subheader("Bölüm 1: Mail Saldırısı 📧👾")
    st.write("**Durum:** Dilay her gece vardiyasında maillerini kontrol eder ve aniden canavar bir 'Mail Saldırısı' başlatır!")
    render_bars()
    col1, col2 = st.columns(2)
    if col1.button("Spam Filtresi Etkinleştir 🛡️"):
        st.success("Spam filtresi canavarı durdurdu! 🎉")
        st.session_state.enemy_health = 0
        st.session_state.score += 20
    if col2.button("Mail Yaz 📝"):
        st.error("Yanlış seçim! Mail kaosa döndü, kaybettin. 💥")
        st.session_state.player_health = 0
    if st.session_state.enemy_health <= 0:
        next_stage()
    if st.session_state.player_health <= 0:
        if st.button("Yeniden Başla"):
            restart_game()

# ----------------------
# Bölüm 2: Sorunlu Öğrenciler
# ----------------------
elif stage == 'ogrenciler':
    st.subheader("Bölüm 2: Sorunlu Öğrenciler 👦👧")
    st.write("**Durum:** Ders sırasında sınıf karıştı! Sorunlu öğrenciler ne yaparsın?")
    render_bars()
    col1, col2 = st.columns(2)
    if col1.button("Disiplin Zili Çal 🔔"):
        st.success("Öğrenciler sustu, devam edebilirsin! 📚")
        st.session_state.enemy_health = 0
        st.session_state.score += 15
    if col2.button("Selfie Çek 🤳"):
        st.error("Selfie zamanı değil! Kaos büyüdü, kaybettin. 🤡")
        st.session_state.player_health = 0
    if st.session_state.enemy_health <= 0:
        next_stage()
    if st.session_state.player_health <= 0:
        if st.button("Yeniden Başla"):
            restart_game()

# ----------------------
# Bölüm 3: Sorunlu Veliler
# ----------------------
elif stage == 'veliler':
    st.subheader("Bölüm 3: Sorunlu Veliler 🧔👩")
    st.write("**Durum:** Veliler sınıfta toplandı, şikâyetler yağmur gibi! Ne yapacaksın?")
    render_bars()
    col1, col2 = st.columns(2)
    if col1.button("Çay Daveti 🫖"):
        st.success("Veliler sakinleşti, devam! ☕")
        st.session_state.enemy_health = 0
        st.session_state.score += 18
    if col2.button("Kalabalık Tweetle 🐦"):
        st.error("Tweet attın, sabah yazdıkların karşına çıktı, kaybettin. 😂")
        st.session_state.player_health = 0
    if st.session_state.enemy_health <= 0:
        next_stage()
    if st.session_state.player_health <= 0:
        if st.button("Yeniden Başla"):
            restart_game()

# ----------------------
# Bölüm 4: Fare İstilası
# ----------------------
elif stage == 'fare':
    st.subheader("Bölüm 4: Fare İstilası 🐭")
    st.write("**Durum:** Minik fareler saldırıya geçti! Ne yaparsın?")
    render_bars()
    col1, col2 = st.columns(2)
    if col1.button("Kedi Maması Koy 🥫"):
        st.success("Fareler kedi mamasına saldırdı, boşlandı! 🐱")
        st.session_state.enemy_health = 0
        st.session_state.score += 22
    if col2.button("Fare Kovala 🏃‍♂️"):
        st.error("Fareler çok hızlıydı, kaçtılar, kaybettin. 😵")
        st.session_state.player_health = 0
    if st.session_state.enemy_health <= 0:
        next_stage()
    if st.session_state.player_health <= 0:
        if st.button("Yeniden Başla"):
            restart_game()

# ----------------------
# Bölüm 5: Su Basması
# ----------------------
elif stage == 'su':
    st.subheader("Bölüm 5: Su Basması 💧")
    st.write("**Durum:** Su her tarafı kapladı! Hangi hamleyi yaparsın?")
    render_bars()
    col1, col2 = st.columns(2)
    if col1.button("Pompayı Çalıştır 🔧"):
        st.success("Pompa devreye girdi, su azaldı! 🚰")
        st.session_state.enemy_health = 0
        st.session_state.score += 17
    if col2.button("Deniz Bisikleti Kirala 🚲"):
        st.error("Deniz bisikletine binince su tuttu, kaybettin. 🤦‍♂️")
        st.session_state.player_health = 0
    if st.session_state.enemy_health <= 0:
        next_stage()
    if st.session_state.player_health <= 0:
        if st.button("Yeniden Başla"):
            restart_game()

# ----------------------
# Bölüm 6: Asansör Saldırısı
# ----------------------
elif stage == 'asansor':
    st.subheader("Bölüm 6: Asansör Saldırısı 🛗")
    st.write("**Durum:** Asansör kontrolden çıktı! Nasıl durduracaksın?")
    render_bars()
    col1, col2 = st.columns(2)
    if col1.button("Acil Fren 🛑"):
        st.success("Frenler tuttu, asansör durdu! 👍")
        st.session_state.enemy_health = 0
        st.session_state.score += 19
    if col2.button("Asansörde İn İn 🚶‍♀️"):
        st.error("Asansör boş, düşersin, kaybettin. 🩹")
        st.session_state.player_health = 0
    if st.session_state.enemy_health <= 0:
        next_stage()
    if st.session_state.player_health <= 0:
        if st.button("Yeniden Başla"):
            restart_game()

# ----------------------
# Bölüm 7: Lavabo Düşmesi
# ----------------------
elif stage == 'lavabo':
    st.subheader("Bölüm 7: Lavabo Düşmesi 🚰")
    st.write("**Durum:** Lavabo her an düşebilir! Hangi planı uygularsın?")
    render_bars()
    col1, col2 = st.columns(2)
    if col1.button("Kayışı Sıkıştır 🔩"):
        st.success("Lavabo güvenli, bölüm tamam! 🎉")
        st.session_state.enemy_health = 0
        st.session_state.score += 20
    if col2.button("Instagram Canlı Yayın 📱"):
        st.error("Canlı yayında lavabo düştü, kaybettin. 📉")
        st.session_state.player_health = 0
    if st.session_state.enemy_health <= 0:
        next_stage()
    if st.session_state.player_health <= 0:
        if st.button("Yeniden Başla"):
            restart_game()

# ----------------------
# Bitiş
# ----------------------
elif stage == 'finished':
    st.balloons()
    st.success(f"Tebrikler! Tüm bölümleri tamamladın. Skorun: {st.session_state.score} 🌟")
    if st.button("Yeniden Başla"):
        restart_game()
