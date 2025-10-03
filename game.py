import streamlit as st
import json
import streamlit.components.v1 as components

# --------------------------------
# İki Popup'ı sırayla (sadece 1 kez)
# --------------------------------
FIRST_POP = (
    "Kendini anlatmakta ne kadar zorlandığını bilmeseydim, çoktan gitmiştim. "
    "Her konuştuğunda susturulduğunu bilmeseydim, çoktan gitmiştim. "
    "Çocukken, yaralı başın bir kez okşansaydı… Çoktan gitmiştim. "
    "Sözlerinin yaralarından geldigini bilmeseydim… Çoktan gitmiştim. "
    "Oysa keşke yüreğimi teraziye vurabilsem; o zaman anlardın… "
    "Belki biraz huzur gerek, o çocuğun başını okşayabilmek için. "
    "Ben olmasam da… sen kuzey ışıklarında."
)

SECOND_POP = "🎮 Hoş geldin. (Bu metni dilediğin mesajla değiştir.)"

def show_welcome_once(messages, state_key="welcome_shown"):
    if not st.session_state.get(state_key):
        js = "<script>" + "".join([f"alert({json.dumps(m)});" for m in messages]) + "</script>"
        components.html(js, height=0)
        st.session_state[state_key] = True

show_welcome_once([FIRST_POP, SECOND_POP])

# ----------------------
# Game Selection
# ----------------------
if 'game_choice' not in st.session_state:
    st.session_state['game_choice'] = None

if st.session_state['game_choice'] is None:
    st.title("🌻 Hangi oyunu oynamak istersin?")
    c1, c2 = st.columns(2)
    if c1.button("📝 GECE VARDİYASI KAPIŞMASI"):
        st.session_state['game_choice'] = 'text'
    if c2.button("🏃‍♂️ GECE VARDİYASI MARATON KOŞUSU"):
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
  button { font-size:1.2rem; padding:0.5rem 1rem; margin:0.5rem; border:none;
             border-radius:8px; background:#2196F3; color:#fff; cursor:pointer; }
  canvas { background:#fafafa; display:block; margin:auto; }
</style>
</head>
<body>
<div id="startScreen">
  <div style="font-size:1.8rem; font-weight:bold;margin-bottom:0.5rem; text-align:center;">
    🌻 Ayçiçeğim Dilay, Gece Vardiyası ile Kapışıyor!
  </div>
  <div style="font-size:1.2rem; margin-bottom:1rem; text-align:center;">
    Engelleri Aş ve Savaş: DİLAY RACONNN
  </div>
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
let frame=0, speed=4, over=false;
const runner={x:50,y:150,vy:0,gravity:0.6,jump:-12,symbol:'🌻',w:40,h:40};
const icons=['📧','👻','☕️','🐭','💦','🚰'];
let obstacles=[];

document.getElementById('startBtn').onclick = ()=>{document.getElementById('startScreen').style.display='none'; loop();};
document.getElementById('restartBtn').onclick = ()=>location.reload();
canvas.addEventListener('keydown', e=>{}); // placeholder
// Jump controls
document.addEventListener('keydown', e=>{ if(e.code==='Space'&&runner.y===150) runner.vy=runner.jump; });
canvas.addEventListener('touchstart', ()=>{ if(runner.y===150) runner.vy=runner.jump; });
canvas.addEventListener('mousedown', ()=>{ if(runner.y===150) runner.vy=runner.jump; });

function loop(){
  frame++;
  ctx.clearRect(0,0,canvas.width,canvas.height);
  // ground
  ctx.fillStyle='#888'; ctx.fillRect(0,190,canvas.width,10);
  // runner
  runner.vy+=runner.gravity; runner.y=Math.min(150,runner.y+runner.vy);
  ctx.font='40px Arial'; ctx.fillText(runner.symbol,runner.x,runner.y);
  ctx.font='12px Arial'; ctx.fillText('DILAY',runner.x,runner.y-10);
  // spawn
  if(frame%80===0) obstacles.push({x:canvas.width,icon:icons[Math.floor(Math.random()*icons.length)]});
  // draw obstacles
  obstacles.forEach(ob=>{ ob.x-=speed; ctx.font='30px Arial'; ctx.fillText(ob.icon,ob.x,180);
    if(ob.x<runner.x+runner.w&&ob.x+30>runner.x&&runner.y>=150) over=true; });
  obstacles=obstacles.filter(o=>o.x>-50);
  // score
  ctx.fillStyle='#000'; ctx.font='20px Arial'; ctx.fillText('Skor: '+Math.floor(frame/10),canvas.width/2-40,30);
  // loop or over
  if(!over) requestAnimationFrame(loop); else document.getElementById('gameOverScreen').style.display='flex';
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
if 'stage' not in st.session_state:
    st.session_state.stage = 'intro'
    st.session_state.step = 0
    st.session_state.lives = 3
    st.session_state.answered = False
    st.session_state.score = 0

# ----------------------
# Global CSS for Text Adventure
# ----------------------
st.markdown("""
<style>
.game-title { font-size:48px; font-weight:bold; text-align:center; margin-top:20px; }
.lives-board { font-size:20px; text-align:center; margin-bottom:20px; }
.question-box { background:#f0f0f5; padding:20px; border-radius:10px; margin:20px auto; max-width:800px; }
.btn-option { width:45%; padding:15px; font-size:18px; margin:10px; border-radius:8px; }
.btn-next { background-color:#2196F3; color:white; width:200px; padding:12px; margin:20px auto; display:block; border:none; border-radius:8px; font-size:18px; }
</style>
""", unsafe_allow_html=True)

# ----------------------
# Event Data
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
        { 'q': "🐭 Fareler istilaya geçti! Ne yapacaksın?",
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
# Text Adventure Functions
# ----------------------
def restart(full=False):
    st.session_state.stage = 'intro'
    st.session_state.step = 0
    st.session_state.answered = False
    st.session_state.score = 0
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
# Text Adventure UI
# ----------------------
st.markdown('<div class="game-title">🌻 GECE VARDİYASI: GÖREV DİLAY\'I KORU</div>', unsafe_allow_html=True)
hearts = '❤️' * st.session_state.lives
st.markdown(f'<div class="lives-board">Can: {hearts}</div>', unsafe_allow_html=True)

if st.session_state.stage == 'intro':
    st.markdown('<div class="question-box">Gece vardiyasına hoş geldin! 🤔</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    if c1.button('💪 Evet, hazırım'): st.session_state.stage='gece_mail'
    if c2.button('😱 Hayır, korkuyorum'): 
        st.session_state.lives -=1
        if st.session_state.lives>0:
            st.error('Korkuya yenik düştün!')
            restart()
        else:
            st.error('❌ Oyun bitti!')
            if st.button('🔄 Yeniden Başla'): restart(full=True)
elif st.session_state.stage in events:
    ev = events[st.session_state.stage][st.session_state.step]
    st.markdown(f'<div class="question-box">{ev["q"]}</div>', unsafe_allow_html=True)
    o1,o2 = st.columns(2)
    if not st.session_state.answered:
        if o1.button(ev['ops'][0]):
            st.session_state.answered=True
            if ev['correct']==0: st.success('✅ Doğru seçim!'); advance()
            else: st.session_state.lives-=1; st.error('❌ Yanlış seçim!')
        if o2.button(ev['ops'][1]):
            st.session_state.answered=True
            if ev['correct']==1: st.success('✅ Doğru seçim!'); advance()
            else: st.session_state.lives-=1; st.error('❌ Yanlış seçim!')
    else:
        if st.button('▶️ İleri'): advance() if st.session_state.lives>0 else (st.error('❌ Can kalmadı!'))
elif st.session_state.stage=='finished':
    st.balloons(); st.success('🎉 Tüm bölümleri tamamladın!');
    if st.button('🔄 Yeniden Başla'): restart(full=True)
