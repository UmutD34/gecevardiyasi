import streamlit as st

# ----------------------
# State Yönetimi
# ----------------------
if 'stage' not in st.session_state:
    st.session_state.stage = 'intro'
    st.session_state.section_step = 0
    st.session_state.player_health = 100
    st.session_state.enemy_health = 100
    st.session_state.score = 0
    st.session_state.ready_next = False

# ----------------------
# Yardımcı Fonksiyonlar
# ----------------------
def restart_game():
    for key in ['stage','section_step','player_health','enemy_health','score','ready_next']:
        st.session_state[key] = 0 if key=='section_step' else (False if key=='ready_next' else 100 if 'health' in key else 0)
    st.session_state.stage = 'intro'
    st.session_state.player_health = 100
    st.session_state.enemy_health = 100
    st.session_state.score = 0
    st.session_state.ready_next = False


def next_event():
    st.session_state.section_step += 1
    st.session_state.player_health = 100
    st.session_state.enemy_health = 100
    st.session_state.ready_next = False
    # 3 macera sonra sonraki bölüme geç
    if st.session_state.section_step >= 3:
        order = ['intro','gece_mail','ogrenciler','veliler','fare','su','asansor','lavabo','finished']
        idx = order.index(st.session_state.stage)
        st.session_state.stage = order[idx+1]
        st.session_state.section_step = 0


def render_bars():
    st.progress(st.session_state.player_health / 100, text="Can")
    st.progress(st.session_state.enemy_health / 100, text="Düşman Can")

# ----------------------
# Başlık ve skor
# ----------------------
st.title("🌻 DİLAY'I KORU")
st.write(f"**Skor:** {st.session_state.score}")
st.write("---")
stage = st.session_state.stage

# ----------------------
# Intro
# ----------------------
if stage == 'intro':
    st.write("**Gece vardiyasına hoş geldiniz!**\nBu gece vardiyasını yenmek için yeterince cesur musun? 🤔")
    c1,c2 = st.columns(2)
    if c1.button("Evet, hazırım! 💪"):
        st.session_state.stage='gece_mail';st.session_state.section_step=0
    if c2.button("Hayır, korkuyorum 😱"):
        st.error("Korkuya yenik düştün! Oyunu kaybettin. 😔")
        if st.button("Tekrar Dene"):
            restart_game()

# ----------------------
# Bölümler
# ----------------------
else:
    render_bars()
    step = st.session_state.section_step

    def process_choice(correct, pts):
        if correct:
            st.success("Doğru seçim!")
            st.session_state.score += pts
        else:
            st.error("Yanlış seçim, canın tükendi.")
            st.session_state.player_health = 0
        st.session_state.ready_next = True

    def show_next():
        if st.button("İleri ▶️"):
            next_event()

    # Ortak akış: henüz seçim yapılmamışsa seçenekleri göster, yapıldıysa ileri butonunu göster
    if stage=='gece_mail':
        st.subheader(f"Bölüm 1: Mail Saldırısı (Adım {step+1}/3)")
        if not st.session_state.ready_next:
            if step==0:
                st.write("Dilay'ın gelen kutusu patlamak üzere! İlk hamle? 📧")
                c1,c2=st.columns(2)
                if c1.button("Spam filtresi uygula 🛡️"): process_choice(True,10)
                if c2.button("Hepsini oku 📖"): process_choice(False,0)
            elif step==1:
                st.write("CC: Herkes faciası başladı! Nasıl durdurursun? 🔄")
                c1,c2=st.columns(2)
                if c1.button("Yanıtları kapat🔇"): process_choice(True,15)
                if c2.button("Cevabı okula gönder🏫"): process_choice(False,0)
            else:
                st.write("Son aşama: Mail saldırısına son hamle? 🚀")
                c1,c2=st.columns(2)
                if c1.button("Hepsini arşive at📂"): process_choice(True,20)
                if c2.button("Hemen sil🗑️"): process_choice(False,0)
        else:
            show_next()

    elif stage=='ogrenciler':
        st.subheader(f"Bölüm 2: Sorunlu Öğrenciler (Adım {step+1}/3)")
        if not st.session_state.ready_next:
            if step==0:
                st.write("Öğrenciler dersin ortasında dans etmeye başladı! 💃🕺")
                c1,c2=st.columns(2)
                if c1.button("Zil çal🔔"): process_choice(True,8)
                if c2.button("Onlara DJ ol🎧"): process_choice(False,0)
            elif step==1:
                st.write("Masadan hayalet sesleri geliyor! 👻")
                c1,c2=st.columns(2)
                if c1.button("Maske tak🦹‍♂️"): process_choice(True,12)
                if c2.button("Şarkı söyle🎤"): process_choice(False,0)
            else:
                st.write("Motivasyon konuşması yap! 🎓")
                c1,c2=st.columns(2)
                if c1.button("Konuşmayı başlat📢"): process_choice(True,15)
                if c2.button("Selfie iste🤳"): process_choice(False,0)
        else:
            show_next()

    # ... Her bölüm için aynı mantıkla devam ettirin ...

    # Bitiş
    if stage=='finished':
        st.balloons(); st.success(f"Tebrikler! Skorun: {st.session_state.score} 🌟")
        if st.button("Yeniden Başla"): restart_game()

    # Kaybetme Durumu
    if st.session_state.player_health<=0:
        st.error("Kaybettin! 🙁")
        if st.button("Baştan Başla"): restart_game()
