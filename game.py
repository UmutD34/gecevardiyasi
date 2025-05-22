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
        'stage':'intro',
        'step':0,
        'lives':3,
        'answered':False,
        'score':0
    })

# DEBUG: uncomment to view state
# st.write(st.session_state)

# ----------------------
# Event Data
# ----------------------
events = {
    'gece_mail': [
        { 'q': "📧 Gece vardiyası baslarken gıcık bir mail ile karşılaştın, ne yapacaksın?",
          'ops': ["🛡️ Racon mail", "📖 Görmezden gel"], 'correct':0, 'pts':10, 'icon':'✉️'},
        { 'q': "🗑️ Mail spam klasörüne düştü, geri getirmek ister misin?",
          'ops': ["🔄 Geri alırım", "🚮 Sil"], 'correct':1, 'pts':12, 'icon':'🗳️'},
        { 'q': "🔄 Yazım yanlışı uyarısı, ne yapacaksın?",
          'ops': ["✍️ Düzenlerim", "🙉 Umursamam"], 'correct':0, 'pts':15, 'icon':'✍️'},
        { 'q': "📅 Maili 2050'ye erteledin, ne hissediyorsun?",
          'ops': ["😅 Panikteyim", "🚀 Geleceği kucakla"], 'correct':0, 'pts':18, 'icon':'🕒'},
        { 'q': "🚀 Kameralar bozuldu, ne yapacaksın?",
          'ops': ["🙏 Dua et", "🗑️ At"], 'correct':0, 'pts':20, 'icon':'📷'},
    ],
    'ogrenciler': [
        { 'q': "💳 Kartını unutan öğrenci, ne yapacaksın?",
          'ops': ["🔔 Kapıyı aç", "🎧 Dinlemem"], 'correct':0, 'pts':8, 'icon':'👩‍🎓'},
        { 'q': "👻 Hayalet gördüğünü iddia etti, ne yapacaksın?",
          'ops': ["🦹‍♂️ Maske tak", "🎤 Şarkı söylerim"], 'correct':1, 'pts':12, 'icon':'👻'},
        { 'q': "🎓 'Gecikmeyen ders' ister, ne yaparsın?",
          'ops': ["🏚️ Kabul ederim", "📕 Kitap öneririm"], 'correct':1, 'pts':10, 'icon':'🏚️'},
        { 'q': "🍕 Pizza vakti diyor, ne yanıt verirsin?",
          'ops': ["🍕 Ortaya pizza söyle","🚫 Diyetindeyim"], 'correct':0, 'pts':14, 'icon':'🍕'},
        { 'q': "🤖 Robot öğretmen ister diyor, cevap?",
          'ops': ["🤖 Tasarlarım", "😂 Ben yeterim"], 'correct':0, 'pts':16, 'icon':'🤖'},
    ],
    'veliler': [
        { 'q': "☕️ Veliler çay istiyor, ne önerirsin?",
          'ops': ["🍵 Papatya", "🥤 Enerji içeceği"], 'correct':0, 'pts':10, 'icon':'☕️'},
        { 'q': "📱 Sürekli arıyorlar, ne yapacaksın?",
          'ops': ["🔇 Sessize al", "✍️ Not alırım"], 'correct':1, 'pts':12, 'icon':'📱'},
        { 'q': "🎁 Papua Yeni Gine soruyor, ne önerirsin?",
          'ops': ["✈️ Tur paketi", "📺 Belgesel izle"], 'correct':1, 'pts':15, 'icon':'🎁'},
        { 'q': "📝 'Ölmez hoca' yazmışlar, ne dersin?",
          'ops': ["😂 Teşekkür ederim", "🤔 Düzeltirim"], 'correct':0, 'pts':13, 'icon':'📝'},
        { 'q': "🎓 Üniversite seçimi soruyorlar, ne önerirsin?",
          'ops': ["🎭 Sosyal Bilimler", "⚙️ Mühendislik"], 'correct':0, 'pts':17, 'icon':'🎓'},
    ],
    'fare': [
        { 'q': "🐭 Fare istilası başladı, ne yapacaksın?",
          'ops': ["🥫 Miyu çağır", "🔊 Kaval çal"], 'correct':0, 'pts':10, 'icon':'🐭'},
        { 'q': "💻 Fareler bilgisayara saldırıyor, ne yaparsın?",
          'ops': ["🪤 İzlerim", "💻 Onlara öğretirim"], 'correct':1, 'pts':12, 'icon':'💻'},
        { 'q': "📦 Fareler kutuda saklanıyor, ne yaparsın?",
          'ops': ["📦 Dokunurum", "🔍 Kontrol ederim"], 'correct':1, 'pts':14, 'icon':'📦'},
        { 'q': "🐈 Kedi mi çağırırsın?",
          'ops': ["🪤 Tuzak kur", "🐈 Kedi getir"], 'correct':1, 'pts':15, 'icon':'🐈'},
        { 'q': "🎶 Fareler dans etmek istiyor, izin ver?",
          'ops': ["🎶 Veririm", "🚫 Ders başlasın"], 'correct':0, 'pts':16, 'icon':'🎶'},
    ],
    'su': [
        { 'q': "🌊 Koridor suyla doldu, ne yaparsın?",
          'ops': ["🔧 Pompa", "🛶 Kano"], 'correct':0, 'pts':10, 'icon':'💧'},
        { 'q': "💦 Selfie mi vanayı kapatmalı mı?",
          'ops': ["🚰 Vanayı kapat", "🤳 Selfie"], 'correct':0, 'pts':12, 'icon':'🚰'},
        { 'q': "🪣 Kova mı yoksa havuz mu?",
          'ops': ["🪣 Kova", "🏊‍♂️ Havuz"], 'correct':1, 'pts':15, 'icon':'🪣'},
        { 'q': "🍹 Meyve suyu mu istersin?",
          'ops': ["🍹 Evet", "💧 Hayır"], 'correct':0, 'pts':14, 'icon':'🍹'},
        { 'q': "🎯 Fıskiye yapalım mı?",
          'ops': ["🎯 Evet", "🚫 Hayır"], 'correct':0, 'pts':16, 'icon':'🎯'},
    ],
    'lavabo': [
        { 'q': "🚰 Lavabo sallanıyor, ne yaparsın?",
          'ops': ["🔩 Sıkıştır", "📱 Oyna"], 'correct':0, 'pts':10, 'icon':'🚰'},
        { 'q': "📉 Titreşim devam ediyor, ne yaparsın?",
          'ops': ["🦵 Destek ekle", "🎈 Müziği aç"], 'correct':1, 'pts':12, 'icon':'📉'},
        { 'q': "🛠️ Lavabo patladı, ne yaparsın?",
          'ops': ["🔧 Boru bağla", "💃 Dans et"], 'correct':0, 'pts':15, 'icon':'💥'},
        { 'q': "🧸 Oyuncak koysak olur mu?",
          'ops': ["🧸 Evet","🚫 Hayır"], 'correct':1, 'pts':14, 'icon':'🧸'},
        { 'q': "🎉 Parti mi yapsak burada?",
          'ops': ["🎉 Evet","🛑 Hayır"], 'correct':0, 'pts':16, 'icon':'🎉'},
    ],
}
order = ['intro','gece_mail','ogrenciler','veliler','fare','su','lavabo','finished']

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
step_display = st.session_state.step+1 if st.session_state.stage in events else ''
total = len(events.get(st.session_state.stage, []))
status_html = f'<div class="status-board">'
status_html += f'<div class="section-indicator">{section} {step_display}/{total}</div>'
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
        st.session_state.stage='gece_mail'
    if c2.button('😱 Hayır, korkuyorum'):
        st.session_state.lives -=1
        if st.session_state.lives>0:
            st.warning('Korkuya yenik düştün!')
            restart()
        else:
            st.error('❌ Oyun bitti!')
            if st.button('🔄 Yeniden Başla'):
                restart(full=True)

# ----------------------
# Play Sections
# ----------------------
elif st.session_state.stage in events:
    ev = events[st.session_state.stage][st.session_state.step]
    # Shuffle options
    opts = [{'text':o, 'correct':(i==ev['correct'])} for i,o in enumerate(ev['ops'])]
    random.shuffle(opts)
    st.markdown(f'<div class="question-box">{ev["icon"]} {ev["q"]}</div>', unsafe_allow_html=True)
    o1,o2 = st.columns(2)
    if not st.session_state.answered:
        if o1.button(opts[0]['text']):
            st.session_state.answered=True
            if opts[0]['correct']:
                st.success('✅ Doğru seçim!')
                st.session_state.score+=ev['pts']
            else:
                st.session_state.lives-=1
                st.error('❌ Yanlış seçim!')
        if o2.button(opts[1]['text']):
            st.session_state.answered=True
            if opts[1]['correct']:
                st.success('✅ Doğru seçim!')
                st.session_state.score+=ev['pts']
            else:
                st.session_state.lives-=1
                st.error('❌ Yanlış seçim!')
    else:
        if st.button('▶️ İleri'):
            if st.session_state.lives>0:
                advance()
            else:
                st.error('CAN KALMADI')
                if st.button('🔄 Yeniden Başla'):
                    restart(full=True)

# ----------------------
# Finished
# ----------------------
elif st.session_state.stage=='finished':
    st.balloons()
    st.success('🎉 Tüm bölümleri tamamladın!')
    if st.button('🔄 Yeniden Başla'):
        restart(full=True)

# ----------------------
# HTML5 Infinite Runner (Sunflower Runner)
# ----------------------
import streamlit.components.v1 as components

# HTML5 canvas ile koşu oyunu: Ayçiçekli Runner
GAME_HTML = """<!DOCTYPE html>
<html lang=\"en\">
<head>
<meta charset=\"UTF-8\">
<title>Sunflower Runner</title>
<style>
  body { margin:0; overflow:hidden; }
  canvas { background:#fafafa; display:block; margin:auto; }
</style>
</head>
<body>
<canvas id=\"c\" width=\"800\" height=\"200\"></canvas>
<script>
const canvas = document.getElementById('c');
const ctx = canvas.getContext('2d');
let frame = 0;
let speed = 6;
let gameOver = false;

// Runner as sunflower image
const sun = new Image();
sun.src = 'https://i.imgur.com/QPdE3G3.png';
const runner = { x: 50, y: 150, vy: 0, gravity: 0.6, jump: -12, w: 40, h: 40 };

// Esprili metinler
const jokes = [
  "Spam mail geldi!",
  "Hayalet öğrenci... Boo!",
  "Sinirli veli kapıda!",
  "Fare partisi var!",
  "Su sel oldu!",
  "Lavabo temizlik zamanı!"
];

let obstacles = [];

// Zıplama kontrolü
document.addEventListener('keydown', e => { if(e.code==='Space' && runner.y===150) runner.vy = runner.jump; });

function loop() {
  frame++;
  ctx.clearRect(0,0,canvas.width,canvas.height);

  // Zemin
  ctx.fillStyle = '#888'; ctx.fillRect(0,190,canvas.width,10);

  // Runner fizik ve çizim (ayçiçeği zıplıyor)
  runner.vy += runner.gravity;
  runner.y = Math.min(150, runner.y + runner.vy);
  ctx.drawImage(sun, runner.x, runner.y-10, runner.w, runner.h);

  // Engel oluşturma
  if(frame % 80 === 0) {
    let text = jokes[Math.floor(Math.random()*jokes.length)];
    obstacles.push({ x: canvas.width, start: frame, text });
  }

  // Engelleri çiz ve çarpışma
  obstacles.forEach(ob => {
    ob.x -= speed;
    // Typewriter efekti
    let len = Math.min(ob.text.length, Math.floor((frame - ob.start)/10));
    let display = ob.text.substring(0, len);
    ctx.fillStyle = '#000';
    ctx.font = '20px Arial';
    ctx.fillText(display, ob.x, 180);
    // Çarpışma kontrolü
    if(ob.x < runner.x + runner.w && ob.x + 100 > runner.x && runner.y + runner.h >= 190) {
      gameOver = true;
    }
  });
  obstacles = obstacles.filter(o => o.x > -200);

  // Skor
  let score = Math.floor(frame/10);
  ctx.fillStyle = '#000';
  ctx.font = '20px Arial';
  ctx.fillText('Skor: ' + score, 650, 30);

  if(!gameOver) requestAnimationFrame(loop);
  else {
    ctx.fillStyle = 'rgba(0,0,0,0.5)';
    ctx.fillRect(0,0,canvas.width,canvas.height);
    ctx.fillStyle = '#fff';
    ctx.font = '30px Arial';
    ctx.fillText('Oyun Bitti! F5 ile yeniden', 260, 100);
  }
}
// Başlat
sun.onload = () => loop();
</script>
</body>
</html>"""

components.html(GAME_HTML, height=240)
