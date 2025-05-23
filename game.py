import streamlit as st
import random, json, os, streamlit.components.v1 as components

# ----------------------
# Utilities for persistent scores
# ----------------------
SCORE_FILE = "scores.json"

def save_score_file(name, score):
    scores = load_score_file()
    scores.append({"isim": name, "skor": score})
    with open(SCORE_FILE, "w", encoding="utf-8") as f:
        json.dump(scores, f, ensure_ascii=False)

def load_score_file():
    if os.path.exists(SCORE_FILE):
        try:
            with open(SCORE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except: pass
    return []

# ----------------------
# One‑time welcome popup
# ----------------------
if 'welcome_shown' not in st.session_state:
    components.html("<script>alert('🌻 Sultanlar sultanı Dilay Sultan için gece vardiyasi oyunları serisi');</script>", height=0)
    st.session_state.welcome_shown = True

# ----------------------
# Game choice screen
# ----------------------
if 'game_choice' not in st.session_state:
    st.session_state.game_choice = None

if st.session_state.game_choice is None:
    st.title("🌻 Hangi oyunu oynamak istersin?")
    col1, col2 = st.columns(2)
    if col1.button("📝 GECE VARDİYASI KAPIŞMASI"):
        st.session_state.game_choice = 'text'
    if col2.button("🏃‍♂️ GECE VARDİYASI MARATON KOŞUSU"):
        st.session_state.game_choice = 'runner'
    st.stop()

# ----------------------
# Runner Game
# ----------------------
if st.session_state['game_choice'] == 'runner':
    import time
    st.session_state.setdefault('scores', [])
    diff = st.selectbox("Zorluk seviyesi", ["Kolay", "Orta", "Zor"], index=1)
    diff_base = {"Kolay":3, "Orta":4, "Zor":5}[diff]
    diff_spawn = {"Kolay":100, "Orta":80, "Zor":60}[diff]

 GAME_HTML = f'''
<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><title>Sunflower Runner</title>
<style>body{{margin:0;overflow:hidden;font-family:Arial}}canvas{{background:#fafafa;display:block;margin:auto}}
#start,#over{{position:absolute;top:0;left:0;width:100%;height:100%;background:rgba(255,255,255,.9);display:flex;flex-direction:column;align-items:center;justify-content:center;z-index:2}}
#over{{display:none}}button{{padding:.6rem 1.2rem;font-size:1.1rem;border:none;border-radius:8px;background:#2196F3;color:#fff;cursor:pointer}}</style></head>
<body>
<div id="start"><h2>🌻 Ayçiçeğim Dilay Gece Vardiyası ile Kapışıyor!</h2><p>Zorluk: <b>{diff}</b></p><button onclick="start()">OYUNA BAŞLA</button></div>
<canvas id="c" width="800" height="200"></canvas>
<div id="score" style="text-align:center;font-size:20px">Skor: 0</div>
<div id="over"><h2>Oyun Bitti!</h2><p id="msg"></p><input id="name" placeholder="Adını gir"><button onclick="save()">Skoru Kaydet</button></div>
<script>
const c=document.getElementById('c'),x=c.getContext('2d');let f=0,over=false;
const base={diff_base};const spawnInt={diff_spawn};
const r={{x:50,y:150,vy:0,g:0.6,j:-12,s:'🌻',w:40}};const ic=['✉️','👻','☕️','🐭','💦','🚰'];let obs=[];
function start(){{document.getElementById('start').style.display='none';loop();}}
function loop(){{f++;const speed=base+Math.floor(f/500);x.clearRect(0,0,800,200);x.fillStyle='#888';x.fillRect(0,190,800,10);
 r.vy+=r.g;r.y=Math.min(150,r.y+r.vy);x.font='40px Arial';x.fillText(r.s,r.x,r.y);
 if(f%spawnInt===0)obs.push({{x:800,ic:ic[Math.random()*ic.length|0]}});
 obs.forEach(o=>{{o.x-=speed;x.font='30px Arial';x.fillText(o.ic,o.x,180);if(o.x<r.x+r.w&&o.x+30>r.x&&r.y>=150)over=true;}});
 obs=obs.filter(o=>o.x>-50);document.getElementById('score').innerText='Skor: '+Math.floor(f/10);
 if(!over)requestAnimationFrame(loop);else{{document.getElementById('over').style.display='flex';document.getElementById('msg').innerText='Skorun: '+Math.floor(f/10);}}
}}
function save(){{const isim=document.getElementById('name').value||'İsimsiz';const s=parseInt(document.getElementById('msg').innerText.replace(/\D/g,''));window.parent.postMessage({{player:isim,score:s}},'*');document.body.innerHTML='<h2>Kaydedildi!</h2>';}}
document.addEventListener('keydown',e=>{{if(e.code==='Space'&&r.y===150)r.vy=r.j;}});c.addEventListener('mousedown',()=>{{if(r.y===150)r.vy=r.j;}});c.addEventListener('touchstart',()=>{{if(r.y===150)r.vy=r.j;}});
</script></body></html>
'''


    data = components.html(GAME_HTML, height=350, scrolling=False, key='runner')
    if isinstance(data, dict) and 'score' in data:
        st.session_state.scores.append({'isim': data['player'], 'skor': data['score']})
        save_score_file(data['player'], data['score'])
        st.success(f"🏅 {data['player']} skoru {data['score']} kaydedildi! ⭐ Zorluk: {diff}")

    if st.button("🏆 Skor Tablosu"):
        all_scores = load_score_file() + st.session_state.scores
        uniq = [dict(t) for t in {tuple(d.items()) for d in all_scores}]
        uniq_sorted = sorted(uniq, key=lambda x: x['skor'], reverse=True)
        for i,e in enumerate(uniq_sorted):
            medal = '🏆' if i==0 else '🥈' if i==1 else '🥉' if i==2 else ''
            st.write(f"{medal} {e['isim']} - {e['skor']}")

    st.stop()

    
  
