import streamlit as st
import random

# ----------------------
# Global CSS & Styling
# ----------------------
st.markdown(
    """
    <style>
    .game-title { font-size: calc(1.5rem + 1vw); font-weight:bold; text-align:center; margin-top:1rem; }
    .status-board { display:flex; justify-content:space-between; padding:0 2rem; font-size:1rem; margin-bottom:1rem; }
    .section-indicator, .lives-board, .score-board { flex:1; text-align:center; }
    .question-box { background:#f0f0f5; padding:1rem; border-radius:10px; margin:1rem auto; max-width:90%; }
    .btn-option { width:45%; padding:0.75rem; font-size:1rem; margin:0.5rem; border-radius:8px; transition:background 0.3s; }
    .btn-option:hover { background:#ddd; }
    .btn-next { background-color:#2196F3; color:white; width:200px; padding:0.75rem; margin:1rem auto; display:block; border:none; border-radius:8px; font-size:1rem; }
    img.icon { width:40px; vertical-align:middle; margin-right:0.5rem; }
    </style>
    """, unsafe_allow_html=True)

# ----------------------
# Initialize State
# ----------------------
if 'stage' not in st.session_state:
    st.session_state.update({
        'stage':'intro', 'step':0, 'lives':3, 'answered':False, 'score':0
    })

# ----------------------
# Event Data
# ----------------------
events = {
    'gece_mail': [
        { 'q': "📧 Gece vardiyası baslarken gıcık bir mail ile karşılaştın, ne yapacaksın?",
          'ops': ["🛡️ Dilay racon ile mail yazarım", "📖 Görmezden gelirim"], 'correct':0, 'pts':10, 'icon':'✉️'},
        { 'q': "🗑️ Mail spam klasörüne düştü, tekrar geri getirmek ister misin?",
          'ops': ["🔄 Geri alırım", "🚮 Kalmasın"], 'correct':1, 'pts':12, 'icon':'🗳️'},
        { 'q': "🔄 Yazım yanlışı uyarısı, ne yapacaksın?",
          'ops': ["✍️ Hemen düzenlerim", "🙉 Görmemezlikten gelirim"], 'correct':0, 'pts':15, 'icon':'✍️'},
        { 'q': "📅 Maili yanlışlıkla 2050'ye erteledin, ne hissediyorsun?",
          'ops': ["😅 Geri alırım", "🚀 Geleceğe yolculuk"], 'correct':0, 'pts':18, 'icon':'🕒'},
        { 'q': "🚀 Kameralar bozuldu, ne yapacaksın?",
          'ops': ["🙏 Dua et", "🗑️ Çöpe at"], 'correct':0, 'pts':20, 'icon':'📷'},
    ],
    'ogrenciler': [
        { 'q': "💳 Kartını unutan öğrenci, ne yapacaksın?",
          'ops': ["🔔 Raconla aç", "🎧 Dinlemem"], 'correct':0, 'pts':8, 'icon':'👩‍🎓'},
        { 'q': "👻 Hayalet gördüğünü iddia etti, ne yapacaksın?",
          'ops': ["🦹‍♂️ Maske tak ve kovala", "🎤 Beraber şarkı söylerim"], 'correct':1, 'pts':12, 'icon':'👻'},
        { 'q': "🎓 'Kütüphane gecekondusu' temalı ders isterim diyor, ne dersin?",
          'ops': ["🏚️ Tema uygundur", "📕 Kitap öneririm"], 'correct':1, 'pts':10, 'icon':'🏚️'},
        { 'q': "🍕 Öğrenci size pizza ikram etmek istiyor, kabul eder misin?",
          'ops': ["🍕 Afiyetle yerim", "🚫 Diyetim var"], 'correct':0, 'pts':14, 'icon':'🍕'},
        { 'q': "🤖 Öğrenci robot hoca isterim diyor, cevabın nedir?",
          'ops': ["🤖 Gelin robotu kodlayalım", "😂 Bana yeter derseniz"], 'correct':0, 'pts':16, 'icon':'🤖'},
    ],
    'veliler': [
        { 'q': "☕️ Veliler çay istiyor, ne önerirsin?",
          'ops': ["🍵 Papatya çayı","🥤 Enerji içeceği"], 'correct':0, 'pts':10, 'icon':'☕️'},
        { 'q': "📱 Sürekli arıyorlar, ne yapacaksın?",
          'ops': ["🔇 Sessize al","✍️ Not alıp sonra cevaplarım"], 'correct':1, 'pts':12, 'icon':'📱'},
        { 'q': "🎁 'Çocuğum papua yeni gine' diyorlar, ne önerirsin?",
          'ops': ["✈️ Tur paketi hazırla","📺 BBC belgesel izle"], 'correct':1, 'pts':15, 'icon':'🎁'},
        { 'q': "📝 Not kağıdına 'ölmez hoca' yazmışlar, ne düşünüyorsun?",
          'ops': ["😂 İltifat kabul","🤔 Düzeltme yap"], 'correct':0, 'pts':13, 'icon':'📝'},
        { 'q': "🎓 Veliler üniversite seçimini soruyor, ne önerirsin?",
          'ops': ["🎭 Sosyal bilimler","⚙️ Mühendislik"], 'correct':0, 'pts':17, 'icon':'🎓'},
    ],
    'fare': [
        { 'q': "🐭 Fare istilası başladı, ne yapacaksın?",
          'ops': ["🥫 Miyu çağır","🔊 Kaval çal"], 'correct':0, 'pts':10, 'icon':'🐭'},
        { 'q': "💻 Fareler bilgisayara saldırıyor, ne yapacaksın?",
          'ops': ["🪤 İzle","💻 Onlara bilgisayar öğret"], 'correct':1, 'pts':12, 'icon':'💻'},
        { 'q': "📦 Fareler kutuya saklanmış, ne yaparsın?",
          'ops': ["📦 Kutuya dokun","🔍 İçini kontrol et"], 'correct':1, 'pts':14, 'icon':'📦'},
        { 'q': "🐈 Kedi mi çağırırsın?",
          'ops': ["🪤 Tuzak kur","🐈 Kedi getir"], 'correct':1, 'pts':15, 'icon':'🐈'},
        { 'q': "🎶 Fareler dans etmek istiyor, izin verirsin?",
          'ops': ["🎶 Evet dans etsinler","🚫 Ders başlasın"], 'correct':0, 'pts':16, 'icon':'🎶'},
    ],
    'su': [
        { 'q': "🌊 Koridorlar suyla doldu, ne yapacaksın?",
          'ops': ["🔧 Pompa çalıştır","🛶 Kano kirala"], 'correct':0, 'pts':10, 'icon':'💧'},
        { 'q': "💦 Vanayı kapatmak mı yoksa selfie mi?",
          'ops': ["🚰 Vanayı kapat","🤳 Selfie çek"], 'correct':0, 'pts':12, 'icon':'🚰'},
        { 'q': "🪣 Kova mı yoksa havuz mu?",
          'ops': ["🪣 Kova getir","🏊‍♂️ Havuz kur"], 'correct':1, 'pts':15, 'icon':'🪣'},
        { 'q': "🍹 Su yerine meyve suyu mı?",
          'ops': ["🍹 Meyve suyu getir","💧 Su yeter"], 'correct':0, 'pts':14, 'icon':'🍹'},
        { 'q': "🎯 Su fıskıyesi yapalım mı?",
          'ops': ["🎯 Evet","🚫 Hayır"], 'correct':0, 'pts':16, 'icon':'🎯'},
    ],
    'lavabo': [
        { 'q': "🚰 Lavabo sallanıyor, ne yapacaksın?",
          'ops': ["🔩 Kayışı sıkıştır","📱 Oyna"], 'correct':0, 'pts':10, 'icon':'🚰'},
        { 'q': "📉 Lavabo titreşim yapıyor, ne yapacaksın?",
          'ops': ["🦵 Destek ayağı ekle","🎈 Müziği aç"], 'correct':1, 'pts':12, 'icon':'📉'},
        { 'q': "🛠️ Lavabo patladı, ne yapacaksın?",
          'ops': ["🔧 Boru bağla","💃 Dans et"], 'correct':0, 'pts':15, 'icon':'💥'},
        { 'q': "🧸 Lavaboya oyuncak mı ekleyelim?",
          'ops': ["🧸 Oyuncak bırak","🚫 Güvenlik öncelik"], 'correct':1, 'pts':14, 'icon':'🧸'},
        { 'q': "🎉 Lavaboyu parti alanına mı dönüştürelim?",
          'ops': ["🎉 Evet","🛑 Hayır"], 'correct':0, 'pts':16, 'icon':'🎉'},
    ],
}
order = ['intro','gece_mail','ogrenciler','veliler','fare','su','lavabo','finished']','gece_mail','ogrenciler','veliler','fare','su','lavabo','finished']

# ----------------------
# Game Functions
# ----------------------
def restart(full=False):
    st.session_state.update({'stage':'intro','step':0,'answered':False})
    if full: st.session_state.lives = 3

def advance():
    st.session_state.step += 1
    st.session_state.answered = False
    if st.session_state.step >= len(events[st.session_state.stage]):
        idx = order.index(st.session_state.stage)
        st.session_state.stage = order[idx+1]
        st.session_state.step = 0

# ----------------------
# Header & Status
# ----------------------
st.markdown('<div class="game-title">🌻 GECE VARDİYASI: GÖREV DİLAY\'I KORU</div>', unsafe_allow_html=True)
section = st.session_state.stage.replace('_',' ').title()
step = st.session_state.step + 1 if st.session_state.stage in events else ''
total = len(events.get(st.session_state.stage, []))
status_html = f'<div class="status-board">'
status_html += f'<div class="section-indicator">{section} {step}/{total}</div>'
status_html += f'<div class="lives-board">Can: {"❤️"*st.session_state.lives}</div>'
status_html += f'<div class="score-board">Puan: {st.session_state.score}</div></div>'
st.markdown(status_html, unsafe_allow_html=True)

# ----------------------
# Intro Section
# ----------------------
if st.session_state.stage == 'intro':
    st.markdown('<div class="question-box">Gece vardiyasına hoş geldin! 🤔</div>', unsafe_allow_html=True)
    c1,c2 = st.columns(2)
    if c1.button('💪 Evet, hazırım'):
        st.session_state.stage = 'gece_mail'
    if c2.button('😱 Hayır, korkuyorum'):
        st.session_state.lives -= 1
        if st.session_state.lives > 0:
            st.warning('Korkuya yenik düştün!')
            restart()
        else:
            st.error('❌ Oyun bitti!')
            if st.button('🔄 Yeniden Başla'):
                restart(full=True)

# ----------------------
# Play Sections with Randomized Options
# ----------------------
elif st.session_state.stage in events:
    ev = events[st.session_state.stage][st.session_state.step]
    # Prepare paired options and shuffle
    options = []
    for idx, opt_text in enumerate(ev['ops']):
        is_correct = (idx == ev['correct'])
        options.append({'text': opt_text, 'correct': is_correct})
    random.shuffle(options)

    st.markdown(f'<div class="question-box">{ev.get("icon","")} {ev["q"]}</div>', unsafe_allow_html=True)
    o1, o2 = st.columns(2)
    if not st.session_state.answered:
        if o1.button(options[0]['text']):
            st.session_state.answered = True
            if options[0]['correct']:
                st.success('✅ Doğru seçim!')
                st.session_state.score += ev['pts']
            else:
                st.session_state.lives -= 1
                st.error('❌ Yanlış seçim!')
        if o2.button(options[1]['text']):
            st.session_state.answered = True
            if options[1]['correct']:
                st.success('✅ Doğru seçim!')
                st.session_state.score += ev['pts']
            else:
                st.session_state.lives -= 1
                st.error('❌ Yanlış seçim!')
    else:
        if st.button('▶️ İleri'):
            if st.session_state.lives > 0:
                advance()
            else:
                st.error('❌ Can kalmadı!')
                if st.button('🔄 Yeniden Başla'):
                    restart(full=True)

# ----------------------
# Finished
# ----------------------
elif st.session_state.stage == 'finished':
    st.balloons()
    st.success('🎉 Tüm bölümleri tamamladın!')
    if st.button('🔄 Yeniden Başla'):
        restart(full=True)

# ----------------------
# HTML5 Mini Oyun (Flappy Dilay)
# ----------------------
import streamlit.components.v1 as components
GAME_HTML = """<!-- HTML5 Flappy Dilay code -->"""
components.html(GAME_HTML, height=650)
