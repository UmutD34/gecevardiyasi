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
# Olay Verisi (sorular, seçenekler, doğru indeks, puan)
# ----------------------
event_data = {
    'gece_mail': [
        { 'question': "Dilay'ın gelen kutusu patlamak üzere! İlk hamle? 📧",
          'options': ["Spam filtresi uygula 🛡️", "Hepsini oku 📖"], 'correct': 0, 'pts': 10 },
        { 'question': "CC: Herkes faciası başladı! Nasıl durdurursun? 🔄",
          'options': ["Yanıtları kapat🔇", "Cevabı okula gönder🏫"], 'correct': 0, 'pts': 15 },
        { 'question': "Son aşama: Mail saldırısına son hamle? 🚀",
          'options': ["Hepsini arşive at📂", "Hemen sil🗑️"], 'correct': 0, 'pts': 20 }
    ],
    'ogrenciler': [
        { 'question': "Öğrenciler dans etmeye başladı! Ne yaparsın? 💃🕺",
          'options': ["Zil çal🔔", "Onlara DJ ol🎧"], 'correct': 0, 'pts': 8 },
        { 'question': "Masadan hayalet sesleri geliyor! Ne yaparsın? 👻",
          'options': ["Maske tak🦹‍♂️", "Şarkı söyle🎤"], 'correct': 0, 'pts': 12 },
        { 'question': "Motivasyon konuşması yap! 🎓",
          'options': ["Konuşmayı başlat📢", "Selfie iste🤳"], 'correct': 0, 'pts': 15 }
    ],
    'veliler': [
        { 'question': "Veliler öğretmeni sorguluyor! İlk hamle? 🧔👩‍🦰",
          'options': ["Çay daveti ☕", "Sözlü sınav yap✏️"], 'correct': 0, 'pts': 10 },
        { 'question': "Veliler Whatsapp'ta grup kurdu! Ne yaparsın? 📱",
          'options': ["Sessize al🔇", "GIF gönder🎬"], 'correct': 0, 'pts': 12 },
        { 'question': "Son adım: Velilere hediye seç! 🎁",
          'options': ["Kalem seti al✏️", "Çiçek gönder🌸"], 'correct': 0, 'pts': 15 }
    ],
    'fare': [
        { 'question': "Fareler her yere yayıldı! İlk strateji? 🐭",
          'options': ["Kedi maması koy🥫", "Sesli kovala🔊"], 'correct': 0, 'pts': 10 },
        { 'question': "Fareler bilgisayara saldırıyor! Ne yaparsın? 💻",
          'options': ["Kapan kur🪤", "Ses aç🔊"], 'correct': 0, 'pts': 12 },
        { 'question': "Son adım: Fare tuzağı mı yoksa kedi çağır? 🐈",
          'options': ["Tuzak kur🪤", "Kedi ara📞"], 'correct': 0, 'pts': 15 }
    ],
    'su': [
        { 'question': "Koridorlar göle döndü! İlk hamle? 🌊",
          'options': ["Pompa çalıştır🔧", "Kano kirala🛶"], 'correct': 0, 'pts': 10 },
        { 'question': "Su basıncı tehlikeli! Ne yaparsın? 💥",
          'options': ["Vanayı kapat🚰", "Selfie çek🤳"], 'correct': 0, 'pts': 12 },
        { 'question': "Son adım: Havuz mu kovamı? 🪣",
          'options': ["Kova getir🪣", "Havuz kur🏊‍♂️"], 'correct': 0, 'pts': 15 }
    ],
    'asansor': [
        { 'question': "Asansör birden hızlandı! İlk hamle? 🚀",
          'options': ["Acil fren🛑", "Atla🦘"], 'correct': 0, 'pts': 10 },
        { 'question': "Kablo kopmak üzere! Ne yaparsın? 🛠️",
          'options': ["Kablo onar🔧", "Asansörde konuş🗣️"], 'correct': 0, 'pts': 12 },
        { 'question': "Son adım: Kat kontrol mü yoksa ip iniş? 🪜",
          'options': ["Kat şifresini gir🔢", "İple in🧗‍♂️"], 'correct': 0, 'pts': 15 }
    ],
    'lavabo': [
        { 'question': "Lavabo sabit durmuyor! İlk seçenek? 🚰",
          'options': ["Kayışı sıkıştır🔩", "Instagram canlı📱"], 'correct': 0, 'pts': 10 },
        { 'question': "Lavabo titreşim yapıyor! Ne yaparsın? 📉",
          'options': ["Destek ayağı ekle🦵", "Havaya kaldır🎈"], 'correct': 0, 'pts': 12 },
        { 'question': "Son adım: Su tahliyesi mi yoksa yerleştir? 🛠️",
          'options': ["Boru bağla🔧", "Dans et💃"], 'correct': 0, 'pts': 15 }
    ]
}

# ----------------------
# Yardımcı Fonksiyonlar
# ----------------------
def restart_game():
    st.session_state.stage = 'intro'
    st.session_state.section_step = 0
    st.session_state.player_health = 100
    st.session_state.enemy_health = 100
    st.session_state.score = 0
    st.session_state.ready_next = False


def next_event():
    st.session_state.section_step += 1
    st.session_state.player_health = 100
    st.session_state.enemy_health = 100
    st.session_state.ready_next = False
    # 3 adım sonra sonraki bölüme geç
    if st.session_state.section_step >= 3:
        order = ['intro','gece_mail','ogrenciler','veliler','fare','su','asansor','lavabo','finished']
        idx = order.index(st.session_state.stage)
        st.session_state.stage = order[idx+1]
        st.session_state.section_step = 0


def render_bars():
    st.progress(st.session_state.player_health/100, text="Can")
    st.progress(st.session_state.enemy_health/100, text="Düşman Can")

# ----------------------
# Ana Uygulama
# ----------------------
st.title("🌻 DİLAY'I KORU")
st.write(f"**Skor:** {st.session_state.score}")
st.write("---")
stage = st.session_state.stage

# Intro
if stage=='intro':
    st.write("**Gece vardiyasına hoş geldiniz!**\nBu gece vardiyasını yenmek için yeterince cesur musun? 🤔")
    c1,c2 = st.columns(2)
    if c1.button("Evet, hazırım! 💪"):
        st.session_state.stage='gece_mail'
        st.session_state.section_step=0
    if c2.button("Hayır, korkuyorum 😱"):
        st.error("Korkuya yenik düştün! Oyunu kaybettin. 😔")
        if st.button("Tekrar Dene"):
            restart_game()

# Bölüm Akışı
elif stage in event_data:
    render_bars()
    step = st.session_state.section_step
    events = event_data[stage]
    data = events[step]
    st.subheader(f"Bölüm {list(event_data.keys()).index(stage)+1}: {stage.replace('_',' ').title()} (Adım {step+1}/3)")
    st.write(data['question'])
    # Seçenekler
    choice = st.radio("Seçenekler:", data['options'], key=f"radio_{stage}_{step}")
    # Onayla ve İleri
    if not st.session_state.ready_next:
        if st.button("Onayla ✅", key=f"confirm_{stage}_{step}"):
            idx = data['options'].index(choice)
            if idx==data['correct']:
                st.success("Doğru seçim!")
                st.session_state.score += data['pts']
            else:
                st.error("Yanlış seçim, canın tükendi.")
                st.session_state.player_health = 0
            st.session_state.ready_next = True
    else:
        if st.button("İleri ▶️", key=f"next_{stage}_{step}"):
            next_event()

# Bitiş
elif stage=='finished':
    st.balloons()
    st.success(f"Tebrikler! Tüm bölümleri tamamladın. Skorun: {st.session_state.score} 🌟")
    if st.button("Yeniden Başla"): restart_game()

# Kaybetme Durumu
if st.session_state.player_health<=0:
    st.error("Kaybettin! 🙁")
    if st.button("Baştan Başla"): restart_game()
