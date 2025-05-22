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
order = ['intro','gece_mail','ogrenciler','veliler','fare','su','lavabo','finished']
