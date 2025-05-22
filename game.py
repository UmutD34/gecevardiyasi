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
    if col1.button("📝 Metin Macerası"):
        st.session_state['game_choice'] = 'text'
    if col2.button("🏃‍♂️ Koşu Oyunu"):
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
  <div style="font-size:2rem; margin-bottom:1rem;">🌻 GECE VARDİYASI KOŞUCUSU</div>
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
const icons = ['✉️','👻','☕️','🐭','💧','🚰','🔔','🎁','🪤','🎉'];
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
# (unchanged events dict here)

# Game functions and text adventure logic...
# ...
