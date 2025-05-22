import streamlit as st
import random

# ----------------------
# Initialize game choice state
# ----------------------
if 'game_choice' not in st.session_state:
    st.session_state['game_choice'] = None

# ----------------------
# Game Selection Screen
# ----------------------
if st.session_state['game_choice'] is None:
    st.title("🌻 Hangi oyunu oynamak istersin?")
    col1, col2 = st.columns(2)
    if col1.button("📝 GECE VARDİYASI KAPIŞMASI"):
        st.session_state['game_choice'] = 'text'
    if col2.button("🏃‍♂️ GECE VARDİYASI MARATON KOŞUSU"):
        st.session_state['game_choice'] = 'runner'
    st.stop()

# ----------------------
# Runner Game
# ----------------------
if st.session_state['game_choice'] == 'runner':
    import streamlit.components.v1 as components
    GAME_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Sunflower Runner</title>
<style>
  body { margin:0; overflow:hidden; font-family:Arial,sans-serif; }
  #startScreen, #gameOverScreen {
    position:absolute; top:0; left:0;
    width:100%; height:100%;
    background:rgba(255,255,255,0.9);
    display:flex; flex-direction:column; align-items:center; justify-content:center;
    z-index:2;
  }
  #gameOverScreen { display:none; }
  button {
    font-size:1.2rem; padding:0.5rem 1rem;
    margin:0.5rem; border:none;
    border-radius:8px; background:#2196F3; color:#fff;
    cursor:pointer;
  }
  canvas { background:#fafafa; display:block; margin:auto; z-index:1; }
</style>
</head>
<body>
<div id="startScreen">
  <div style="font-size:1.8rem; margin-bottom:1rem; text-align:center; font-weight:bold;">🌻 Ayçiçeğim Dilay Gece Vardiyası ile Kapışıyor!</div>
  <div style="font-size:1.2rem; margin-bottom:1rem; text-align:center;">Engelleri Aş ve Savaşı: DİLAY RACONNN</div>
  <button id="startBtn">OYUNA BAŞLA</button>
</div>
<canvas id="c" width="800" height="200"></canvas>
<div id="gameOverScreen">
  <div style="font-size:2rem; margin-bottom:1rem;">Oyun Bitti!</div>
  <button id="restartBtn">Yeniden Başla</button>
</div>
<script>
const canvas = document.getElementById('c');
const ctx = canvas.getContext('2d');
let frame = 0, speed = 4, over = false;
const runner = { x:50, y:150, vy:0, gravity:0.6, jump:-12, symbol:'🌻', w:40, h:40 };
const icons = ['📧','👻','☕️','🐭','💦','🚰'];  // olay temalı ikonlar
let obstacles = [];
document.getElementById('startBtn').onclick = () => { document.getElementById('startScreen').style.display = 'none'; loop(); };
document.getElementById('restartBtn').onclick = () => location.reload();
document.addEventListener('keydown', e => { if(e.code==='Space' && runner.y===150) runner.vy = runner.jump; });
canvas.addEventListener('touchstart', e => { if(runner.y===150) runner.vy = runner.jump; });
canvas.addEventListener('mousedown', e => { if(runner.y===150) runner.vy = runner.jump; });
function loop() {
  frame++; ctx.clearRect(0,0,canvas.width,canvas.height);
  ctx.fillStyle = '#888'; ctx.fillRect(0,190,canvas.width,10);
  runner.vy += runner.gravity; runner.y = Math.min(150, runner.y + runner.vy);
  ctx.font = '40px Arial'; ctx.fillText(runner.symbol, runner.x, runner.y);
  // Character name label\ n  ctx.font = '12px Arial'; ctx.fillText('DILAY', runner.x, runner.y - 10);
  if(frame % 80 === 0) { let icon = icons[Math.floor(Math.random()*icons.length)]; obstacles.push({ x:canvas.width, icon }); }
  obstacles.forEach(ob => { ob.x -= speed; ctx.font = '30px Arial'; ctx.fillText(ob.icon, ob.x, 180);
    if(ob.x < runner.x + runner.w && ob.x + 30 > runner.x && runner.y >= 150) over = true; });
  obstacles = obstacles.filter(o => o.x > -50);
  ctx.fillStyle = '#000'; ctx.font = '20px Arial'; ctx.fillText('Skor: ' + Math.floor(frame/10), 650, 30);
  if(!over) requestAnimationFrame(loop); else document.getElementById('gameOverScreen').style.display = 'flex';
}
</script>
</body>
</html>
"""
    components.html(GAME_HTML, height=240)
    st.stop()

# ----------------------
# Text Adventure Setup
# ----------------------
st.session_state.setdefault('stage','intro')
st.session_state.setdefault('step',0)
st.session_state.setdefault('lives',3)
st.session_state.setdefault('answered',False)
st.session_state.setdefault('score',0)

# Global CSS & Styling for Text Adventure
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
    </style>
    """, unsafe_allow_html=True)

# Event Data
# ----------------------

events = {
    'gece_mail': [
        { 'q': "📧 Gece vardiyası baslarken gıcık bir mail ile karşılaştın, ne yapacaksın?",
          'ops': ["🛡️ Dilay racon ile mail yazarım", "📖 Görmezden gelirim"], 'correct':0, 'pts':10},
        { 'q': "🗑️ Spam klasörüne düşen maili geri getirir misin?",
          'ops': ["🔄 Geri alırım", "🚮 Kalmasın"], 'correct':1, 'pts':12},
        { 'q': "🔄 Yazım yanlışı uyarısı çıktı, ne yaparsın?",
          'ops': ["✍️ Düzeltirim", "🙉 Hiç umursamam"], 'correct':0, 'pts':15},
    ],
    'ogrenciler': [
        { 'q': "💳 Kartını unutmuş öğrenci kapıda, ne yapacaksın?",
          'ops': ["🔔 Raconuyla açarım", "🎧 Duymuyorum"], 'correct':0, 'pts':8},
        { 'q': "👻 Hayalet görmüş diyor, tepkin ne olur?",
          'ops': ["🦹‍♂️ Maske takarım", "🎤 Şarkı söylerim"], 'correct':1, 'pts':12},
        { 'q': "🎓 İmza attırmamak için 'selfie' isterse?",
          'ops': ["🤳 Selfie istemem", "📢 Yurda geri sokarım"], 'correct':1, 'pts':15},
    ],
    'veliler': [
        { 'q': "☕️ Veliler çay istiyor, önerin?",
          'ops': ["🍵 Papatya çayı", "🥤 Enerji içeceği"], 'correct':0, 'pts':10},
        { 'q': "📱 Sürekli aranıyorsun, ne yaparsın?",
          'ops': ["🔇 Sessize alırım", "✍️ Not alırım"], 'correct':1, 'pts':12},
        { 'q': "🎁 'Papua Yeni Gine'de diyorlar, ne önerirsin?",
          'ops': ["✈️ Tur paketi", "📺 Belgesel izle"], 'correct':1, 'pts':15},
    ],
    'fare': [
        { 'q': "🐭 Fare istilası başladı, ne yaparsın?",
          'ops': ["🥫 Miyu çağırırım", "🔊 Kaval çalarım"], 'correct':0, 'pts':10},
        { 'q': "💻 Bilgisayara fareler saldırıyor, ne yaparsın?",
          'ops': ["🪤 Tuzak kurarım", "💻 Onlara kod öğretirim"], 'correct':1, 'pts':12},
        { 'q': "🐈 Kedi çağırmak mı istersin?",
          'ops': ["🐈 Çağırırım", "📞 Farelerle konuşurum"], 'correct':0, 'pts':15},
    ],
    'su': [
        { 'q': "🌊 Koridor suyla doldu, ne yaparsın?",
          'ops': ["🔧 Pompa çalıştırırım", "🛶 Kano kiralarım"], 'correct':0, 'pts':10},
        { 'q': "💦 Vanayı kapatmalı mısın?",
          'ops': ["🚰 Kapatırım", "🤳 Selfie çekerim"], 'correct':0, 'pts':12},
        { 'q': "🪣 Kova mı yoksa havuz mu?",
          'ops': ["🪣 Kova getiririm", "🏊‍♂️ Havuz kurarım"], 'correct':1, 'pts':15},
    ],
    'lavabo': [
        { 'q': "🚰 Lavabo sallanıyor, ne yaparsın?",
          'ops': ["🔩 Kayışı sıkıştırırım", "📱 Oynarım"], 'correct':0, 'pts':10},
        { 'q': "📉 Lavabo titreşim yapıyor, ne yaparsın?",
          'ops': ["🦵 Destek eklerim", "🎈 Müziği açarım"], 'correct':1, 'pts':12},
        { 'q': "🛠️ Lavabo patladı, ne yaparsın?",
          'ops': ["🔧 Boru bağlarım", "💃 Dans ederim"], 'correct':0, 'pts':15},
    ],
}

# ----------------------
# Text Adventure Functions
# ----------------------
def restart():
    st.session_state.update({'stage':'intro','step':0,'answered':False})

def advance():
    st.session_state.step += 1
    st.session_state.answered = False
    if st.session_state.step >= len(events[st.session_state.stage]):
        idx = list(events.keys()).index(st.session_state.stage)
        stages = list(events.keys()) + ['finished']
        st.session_state.stage = stages[idx+1]
        st.session_state.step = 0

# ----------------------
# Text Adventure UI
# ----------------------
st.markdown(f"<h1 class='game-title'>🌻 DİLAY'I KORU</h1>", unsafe_allow_html=True)
section = st.session_state.stage.replace('_',' ').title()
step_display = st.session_state.step+1 if st.session_state.stage in events else ''
total = len(events.get(st.session_state.stage, []))
st.markdown(f"<div class='status-board'><div class='section-indicator'>{section} {step_display}/{total}</div><div class='lives-board'>Can: {'❤️'*st.session_state.lives}</div><div class='score-board'>Puan: {st.session_state.score}</div></div>", unsafe_allow_html=True)

if st.session_state.stage == 'intro':
    st.markdown("<div class='question-box'>Gece vardiyasına hoş geldin! 🤔</div>", unsafe_allow_html=True)
    c1,c2 = st.columns(2)
    if c1.button('💪 Evet, hazırım'):
        st.session_state.stage = 'gece_mail'
    if c2.button('😱 Hayır, korkuyorum'):
        st.session_state.lives -= 1
        if st.session_state.lives > 0:
            st.error('Korkuya yenik düştün!')
            restart()
        else:
            st.error('❌ Oyun bitti!')
            if st.button('🔄 Yeniden Başla'):
                restart(); st.experimental_rerun()
elif st.session_state.stage in events:
    ev = events[st.session_state.stage][st.session_state.step]
    st.markdown(f"<div class='question-box'>{ev['q']}</div>", unsafe_allow_html=True)
    o1,o2 = st.columns(2)
    if not st.session_state.answered:
        if o1.button(ev['ops'][0]):
            st.session_state.answered = True
            if 0==ev['correct']:
                st.success('✅ Doğru seçim!')
                st.session_state.score += ev['pts']
            else:
                st.session_state.lives -= 1
                st.error('❌ Yanlış seçim!')
        if o2.button(ev['ops'][1]):
            st.session_state.answered = True
            if 1==ev['correct']:
                st.success('✅ Doğru seçim!')
                st.session_state.score += ev['pts']
            else:
                st.session_state.lives -= 1
                st.error('❌ Yanlış seçim!')
    else:
        if st.button('▶️ İleri'):
            if st.session_state.lives>0:
                advance()
            else:
                st.error('Can kalmadı!')
                if st.button('🔄 Yeniden Başla'):
                    restart(); st.experimental_rerun()
elif st.session_state.stage=='finished':
    st.balloons()
    st.success('🎉 Tüm bölümleri tamamladın!')
    if st.button('🔄 Yeniden Başla'):
        restart(); st.experimental_rerun()
