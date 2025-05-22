import streamlit as st

# ----------------------
# Global CSS
# ----------------------
st.markdown(
    """
    <style>
    .game-title { font-size:48px; font-weight:bold; text-align:center; margin-top:20px; }
    .lives-board { font-size:20px; text-align:center; margin-bottom:10px; }
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
    st.session_state.lives = 3
    st.session_state.answered = False

# ----------------------
# Event Data (İçerik asla değiştirilmeyecek)
# ----------------------
events = {
    'gece_mail': [
        { 'q': "📧 Gece vardiyasi baslarken gıcık bir mail ile karşılaştın ne yapacaksın ?",
          'ops': ["🛡️ Dilay racon ile mail yazarım ", "📖 Görmezden gelirim"], 'correct':0, 'pts':10},
        { 'q': "🔄 Mailini atarken otomatik düzeltme ile yazım yanlışı yaptın ne yapacaksın",
          'ops': ["🔇 Bilgisayarı camdan at", "🏫 Masanın altına gir"], 'correct':0, 'pts':15},
        { 'q': "🚀 Kameralar bozuldu ne yapacaksın",
          'ops': ["📂 Kameraların açılması icin dua et", "🗑️ Kameraları Çöpe at"], 'correct':0, 'pts':20},
    ],
    'ogrenciler': [
        { 'q': "💃🕺 Öğrenciler kartını unutmuş ne yapacaksın",
          'ops': ["🔔 Bir daha unutma raconuyla kapıyı aç", "🎧 Kulaklık tak ve duyma"], 'correct':0, 'pts':8},
        { 'q': "👻 Öğrenci gece hayalet gördügünü söyledi ne yapacaksın",
          'ops': ["🦹‍♂️ Maske tak ve ondan uzaklaş", "🎤 Şarkı söyle"], 'correct':0, 'pts':12},
        { 'q': "🎓 Öğrenci gece 3 de dışarı cıkmak isterken imza atmayacagım dedi ne yapacaksın.",
          'ops': ["📢 Öğrenciyi yurda geri sok", "🤳 reels izle"], 'correct':0, 'pts':15},
    ],
    'veliler': [
        { 'q': "🧔👩 Veliler şikayet ediyor! İlk hamle?",
          'ops': ["☕ Çay içmelerini tavsiye et", "✏️ Hat düştü numarası yap"], 'correct':0, 'pts':10},
        { 'q': "📱 Veliler sürekli arıyor ne yapacaksın",
          'ops': ["🔇 Sessize al", "🎬 Komik GIF gönder"], 'correct':0, 'pts':12},
        { 'q': "🎁 Veliler cocugum papua yeni gine ye gittigini bana haber vermedi nerede diye soruyor ne yapacaksın",
          'ops': ["✏️ Velilere Papua Yeni Gine bileti al", "🌸 Papatya çayı öner"], 'correct':0, 'pts':15},
    ],
    'fare': [
        { 'q': "🐭 Fareler istilaya geçti! Ne yaparsın?",
          'ops': ["🥫 Miyu çagır", "🔊 Kaval çal"], 'correct':0, 'pts':10},
        { 'q': "💻 Fareler bilgisayara saldırıyor!",
          'ops': ["🪤 Keyifle izle", "🔊 Onları kov"], 'correct':0, 'pts':12},
        { 'q': "🐈 Fareler kaçıyor",
          'ops': ["🪤 Tuzak kur", "📞 Telefonu farelere at"], 'correct':0, 'pts':15},
    ],
    'su': [
        { 'q': "🌊 Koridorları su bastı",
          'ops': ["🔧 Pompa çalıştır", "🛶 Kano kirala"], 'correct':0, 'pts':10},
        { 'q': "💥 Su basıncı tehlikeli!",
          'ops': ["🚰 Vanayı kapat", "🤳 Selfie çek"], 'correct':0, 'pts':12},
        { 'q': "🪣 Tüm oda su doldu",
          'ops': ["🪣 Kova getir", "🏊‍♂️ Havuz kur da yüzelim"], 'correct':0, 'pts':15},
    ],
    'lavabo': [
        { 'q': "🚰 Lavabo sallanıyor! İlk hareket?",
          'ops': ["🔩 Kayışı sıkıştır", "📱 gecevardiyasi oyununu oyna"], 'correct':0, 'pts':10},
        { 'q': "📉 Lavabo titreşim yapıyor!",
          'ops': ["🦵 Destek ayağı ekle", "🎈 Salla salla  salla salla titreeee müzigi dinle "], 'correct':0, 'pts':12},
        { 'q': "🛠️ Lavabo patladı Su tahliyesi mi yoksa montaj?",
          'ops': ["🔧 Boru bağla", "💃 Dans et"], 'correct':0, 'pts':15},
    ],
}
order = ['intro','gece_mail','ogrenciler','veliler','fare','su','lavabo','finished']

# ----------------------
# Fonksiyonlar
# ----------------------
def restart(full=False):
    st.session_state.stage = 'intro'
    st.session_state.step = 0
    st.session_state.answered = False
    if full:
        st.session_state.lives = 3


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
st.markdown('<div class="game-title">🌻 GECE VARDİYASI: GÖREV DİLAY\'I KORU</div>', unsafe_allow_html=True)
st.markdown(f'<div class="lives-board">Kalan Can: {st.session_state.lives}</div>', unsafe_allow_html=True)

# Intro
if st.session_state.stage=='intro':
    st.markdown('<div class="question-box">Gece vardiyasına hoş geldin! 🤔</div>', unsafe_allow_html=True)
    c1,c2 = st.columns(2)
    if c1.button('💪 Evet, hazırım', key='intro_yes'):
        st.session_state.stage='gece_mail'
        st.session_state.step = 0
    if c2.button('😱 Hayır, korkuyorum', key='intro_no'):
        st.session_state.lives -= 1
        if st.session_state.lives > 0:
            st.error(f'Korkuya yenik düştün! Kalan can: {st.session_state.lives}')
            restart()
            st.stop()
        else:
            st.error('❌ Oyun bitti! Can hakkın tükendi.')
            if st.button('🔄 Yeniden Başla'):
                restart(full=True)
            st.stop()

# Oyun Bölümleri
elif st.session_state.stage in events:
    ev = events[st.session_state.stage][st.session_state.step]
    st.markdown(f'<div class="question-box">{ev["q"]}</div>', unsafe_allow_html=True)
    o1,o2 = st.columns(2)
    if not st.session_state.answered:
        if o1.button(ev['ops'][0], key=f'opt1_{st.session_state.stage}_{st.session_state.step}'):
            st.session_state.answered = True
            if 0 == ev['correct']:
                st.success('✅ Doğru seçim!')
                advance()
            else:
                st.session_state.lives -= 1
                if st.session_state.lives > 0:
                    st.error(f'❌ Yanlış seçim! Kalan can: {st.session_state.lives}')
                    restart()
                    st.stop()
                else:
                    st.error('❌ Oyun bitti! Can hakkın tükendi.')
                    if st.button('🔄 Yeniden Başla'):
                        restart(full=True)
                    st.stop()
        if o2.button(ev['ops'][1], key=f'opt2_{st.session_state.stage}_{st.session_state.step}'):
            st.session_state.answered = True
            if 1 == ev['correct']:
                st.success('✅ Doğru seçim!')
                advance()
            else:
                st.session_state.lives -= 1
                if st.session_state.lives > 0:
                    st.error(f'❌ Yanlış seçim! Kalan can: {st.session_state.lives}')
                    restart()
                    st.stop()
                else:
                    st.error('❌ Oyun bitti! Can hakkın tükendi.')
                    if st.button('🔄 Yeniden Başla'):
                        restart(full=True)
                    st.stop()

# Bitti
elif st.session_state.stage=='finished':
    st.balloons()
    st.success('🎉 Tüm bölümleri başarıyla tamamladın!')
    if st.button('🔄 Yeniden Başla'):
        restart(full=True)
