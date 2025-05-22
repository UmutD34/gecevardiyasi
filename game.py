import streamlit as st

# ----------------------
# Global CSS
# ----------------------
st.markdown(
    """
    <style>
    .game-title { font-size:48px; font-weight:bold; text-align:center; margin-top:20px; }
    .score-board { font-size:20px; text-align:center; margin-bottom:10px; }
    .bars { display:flex; justify-content:space-around; margin:10px 0; }
    .bar { width:45%; }
    .question-box { background:#f0f0f5; padding:20px; border-radius:10px; margin:20px auto; max-width:800px; }
    .btn-option { width:45%; padding:15px; font-size:18px; margin:10px; border-radius:8px; }
    .btn-next { background-color:#2196F3; color:white; width:200px; padding:12px; margin:20px auto; display:block; border:none; border-radius:8px; font-size:18px; }
    </style>
    """, unsafe_allow_html=True)

# ----------------------
# State Yönetimi
# ----------------------
if 'stage' not in st.session_state:
    st.session_state.stage = 'intro'
    st.session_state.step = 0
    st.session_state.health = 100
    st.session_state.enemy = 100
    st.session_state.score = 0
    st.session_state.answered = False

# ----------------------
# Event Data
# ----------------------
events = {
    'gece_mail': [
        { 'q': "📧 Gelen kutusu patlamak üzere! İlk hamle?",
          'ops': ["🛡️ Spam filtresi", "📖 Hepsini oku"], 'correct':0, 'pts':10},
        { 'q': "🔄 CC: Herkes faciası başladı! Nasıl durdurursun?",
          'ops': ["🔇 Yanıtları kapat", "🏫 Cevabı okula gönder"], 'correct':0, 'pts':15},
        { 'q': "🚀 Son aşama: Mail saldırısına son hamle?",
          'ops': ["📂 Arşive at", "🗑️ Hemen sil"], 'correct':0, 'pts':20},
    ],
    'ogrenciler': [
        { 'q': "💃🕺 Öğrenciler dans ediyor! Ne yaparsın?",
          'ops': ["🔔 Zil çal", "🎧 DJ ol"], 'correct':0, 'pts':8},
        { 'q': "👻 Masadan hayalet sesleri geliyor! Ne yaparsın?",
          'ops': ["🦹‍♂️ Maske tak", "🎤 Şarkı söyle"], 'correct':0, 'pts':12},
        { 'q': "🎓 Son adım: Motivasyon konuşması yap",
          'ops': ["📢 Başlat", "🤳 Selfie iste"], 'correct':0, 'pts':15},
    ],
    'veliler': [
        { 'q': "🧔👩 Veliler şikayet ediyor! İlk hamle?",
          'ops': ["☕ Çay daveti", "✏️ Sözlü sınav"], 'correct':0, 'pts':10},
        { 'q': "📱 Veliler WhatsApp'ta grup kurdu!",
          'ops': ["🔇 Sessize al", "🎬 GIF gönder"], 'correct':0, 'pts':12},
        { 'q': "🎁 Hediye seçme zamanı!",
          'ops': ["✏️ Kalem seti", "🌸 Çiçek"], 'correct':0, 'pts':15},
    ],
    'fare': [
        { 'q': "🐭 Fareler istilaya geçti! Ne yaparsın?",
          'ops': ["🥫 Kedi maması", "🔊 Sesle kovala"], 'correct':0, 'pts':10},
        { 'q': "💻 Fareler bilgisayara saldırıyor!",
          'ops': ["🪤 Kapan kur", "🔊 Ses aç"], 'correct':0, 'pts':12},
        { 'q': "🐈 Kedi çağır mı yoksa tuzak mı?",
          'ops': ["🪤 Tuzak kur", "📞 Kedi ara"], 'correct':0, 'pts':15},
    ],
    'su': [
        { 'q': "🌊 Koridorlar göle döndü! İlk hamle?",
          'ops': ["🔧 Pompa çalıştır", "🛶 Kano kirala"], 'correct':0, 'pts':10},
        { 'q': "💥 Su basıncı tehlikeli!",
          'ops': ["🚰 Vanayı kapat", "🤳 Selfie çek"], 'correct':0, 'pts':12},
        { 'q': "🪣 Havuz mu kovamı?",
          'ops': ["🪣 Kova getir", "🏊‍♂️ Havuz kur"], 'correct':0, 'pts':15},
    ],
    'asansor': [
        { 'q': "🚀 Asansör hızlandı! İlk hamle?",
          'ops': ["🛑 Acil fren", "🦘 Atla"], 'correct':0, 'pts':10},
        { 'q': "🛠️ Kablo kopmak üzere!",
          'ops': ["🔧 Kablo onar", "🗣️ Asansörle konuş"], 'correct':0, 'pts':12},
        { 'q': "🪜 Son adım: Kat şifresi mi vs. ip iniş?",
          'ops': ["🔢 Kat şifresi gir", "🧗‍♂️ İple in"], 'correct':0, 'pts':15},
    ],
    'lavabo': [
        { 'q': "🚰 Lavabo sallanıyor! İlk hareket?",
          'ops': ["🔩 Kayışı sıkıştır", "📱 Canlı yayın"], 'correct':0, 'pts':10},
        { 'q': "📉 Lavabo titreşim yapıyor!",
          'ops': ["🦵 Destek ayağı ekle", "🎈 Havaya kaldır"], 'correct':0, 'pts':12},
        { 'q': "🛠️ Su tahliyesi mi yoksa montaj?",
          'ops': ["🔧 Boru bağla", "💃 Dans et"], 'correct':0, 'pts':15},
    ],
}
order = ['intro','gece_mail','ogrenciler','veliler','fare','su','asansor','lavabo','finished']

# ----------------------
# Fonksiyonlar
# ----------------------
def restart():
    st.session_state.update({'stage':'intro','step':0,'health':100,'enemy':100,'score':0,'answered':False})

def advance():
    st.session_state.step += 1
    st.session_state.answered = False
    if st.session_state.step >= len(events[st.session_state.stage]):
        idx = order.index(st.session_state.stage)
        st.session_state.stage = order[idx+1]
        st.session_state.step = 0

# ----------------------
# Layout
# ----------------------
st.markdown('<div class="game-title">🌻 DİLAY\'I KORU</div>', unsafe_allow_html=True)
st.markdown(f'<div class="score-board">Skor: {st.session_state.score}</div>', unsafe_allow_html=True)

# Intro
if st.session_state.stage=='intro':
    st.markdown('<div class="question-box">Gece vardiyasına hoş geldin! 🤔</div>', unsafe_allow_html=True)
    c1,c2 = st.columns(2)
    if c1.button('💪 Evet, hazırım', key='intro_yes'):
        st.session_state.stage='gece_mail'
        st.session_state.step = 0
    if c2.button('😱 Hayır, korkuyorum', key='intro_no'):
        st.error('Korkuya yenik düştün!')
        if st.button('🔄 Tekrar Dene'):
            restart()

# Oyun Bölümleri
elif st.session_state.stage in events:
    ev = events[st.session_state.stage][st.session_state.step]
    st.markdown(f'<div class="question-box">{ev["q"]}</div>', unsafe_allow_html=True)
    o1,o2 = st.columns(2)
    if not st.session_state.answered:
        if o1.button(ev['ops'][0], key=f'opt1_{st.session_state.stage}_{st.session_state.step}'):
            st.session_state.answered = True
            if 0==ev['correct']:
                st.success('✅ Doğru seçim!')
                st.session_state.score += ev['pts']
            else:
                st.error('❌ Yanlış seçim!')
        if o2.button(ev['ops'][1], key=f'opt2_{st.session_state.stage}_{st.session_state.step}'):
            st.session_state.answered = True
            if 1==ev['correct']:
                st.success('✅ Doğru seçim!')
                st.session_state.score += ev['pts']
            else:
                st.error('❌ Yanlış seçim!')
    else:
        if st.button('▶️ İleri', key=f'next_{st.session_state.stage}_{st.session_state.step}'):
            advance()

# Bitti
elif st.session_state.stage=='finished':
    st.balloons()
    st.success(f'Tebrikler! Tüm bölümleri tamamladın. Skor: {st.session_state.score} 🌟')
    if st.button('🔄 Yeniden Başla'):
        restart()
