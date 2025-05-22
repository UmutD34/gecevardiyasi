import streamlit as st, random, streamlit.components.v1 as components

# -------- Welcome once ----------
if 'welcome_shown' not in st.session_state:
    components.html("<script>alert('🌻 Hoş geldiniz! Gece Vardiyasına Hazır mısın, Dilay?');</script>", height=0)
    st.session_state.welcome_shown=True

# -------- Game choice ----------
st.session_state.setdefault('game_choice', None)
if st.session_state.game_choice is None:
    st.title("🌻 Hangi oyunu oynamak istersin?")
    col1,col2=st.columns(2)
    if col1.button("📝 GECE VARDİYASI KAPIŞMASI"): st.session_state.game_choice='text'
    if col2.button("🏃‍♂️ GECE VARDİYASI MARATON KOŞUSU"): st.session_state.game_choice='runner'
    st.stop()

# ========= RUNNER =========
if st.session_state.game_choice == 'runner':
    st.session_state.setdefault("scores", [])

    # --- HTML5 Runner ---
    GAME_HTML = """
    <!DOCTYPE html><html><head><meta charset='utf-8'>
    <style>
      body{margin:0;overflow:hidden;font-family:Arial}
      canvas{background:#fafafa;display:block;margin:auto}
      #score{position:absolute;top:10px;width:100%;text-align:center;font-size:20px}
      #screen,#gameOver{position:absolute;top:0;left:0;width:100%;height:100%;
        background:rgba(255,255,255,.9);display:flex;flex-direction:column;
        align-items:center;justify-content:center;z-index:2}
      #gameOver{display:none}
      button{font-size:1.2rem;padding:.5rem 1rem;border:none;border-radius:8px;background:#2196F3;color:#fff}
    </style></head><body>
    <div id=screen><h2>🌻 Ayçiçeğim Dilay Gece Vardiyası ile Kapışıyor!</h2>
      <p>Engelleri Aş ve Savaşı: <b>DİLAY RACONNN</b></p>
      <button onclick="start()">OYUNA BAŞLA</button></div>
    <canvas id=c width=800 height=200></canvas><div id=score>Skor: 0</div>
    <div id=gameOver><h2>Oyun Bitti!</h2></div>
    <script>
    const c=document.getElementById('c'),ctx=c.getContext('2d');
    let f=0,over=false;
    const r={x:50,y:150,vy:0,g:0.6,j:-12,s:'🌻',w:40};
    const icons=['✉️','👻','☕️','🐭','💦','🚰'];let obs=[];
    function start(){document.getElementById('screen').style.display='none';loop();}
    document.addEventListener('keydown',e=>{if(e.code==='Space'&&r.y===150)r.vy=r.j;});
    c.addEventListener('mousedown',()=>{if(r.y===150)r.vy=r.j;});
    c.addEventListener('touchstart',()=>{if(r.y===150)r.vy=r.j;});
    function loop(){
      f++;const speed=4+Math.floor(f/500);
      ctx.clearRect(0,0,800,200);ctx.fillStyle='#888';ctx.fillRect(0,190,800,10);
      r.vy+=r.g;r.y=Math.min(150,r.y+r.vy);
      ctx.font='40px Arial';ctx.fillText(r.s,r.x,r.y);
      if(f%(Math.max(30,80-Math.floor(f/1000)))===0)
          obs.push({x:800,ic:icons[Math.random()*icons.length|0]});
      obs.forEach(o=>{o.x-=speed;ctx.font='30px Arial';ctx.fillText(o.ic,o.x,180);
        if(o.x<r.x+40&&o.x+30>r.x&&r.y>=150)over=true;});
      obs=obs.filter(o=>o.x>-50);
      document.getElementById('score').innerText='Skor: '+Math.floor(f/10);
      if(!over)requestAnimationFrame(loop);
      else{
        const s=Math.floor(f/10);
        const p=prompt('Oyun bitti! Skorunuz: '+s+'\\nİsminiz?');
        window.parent.postMessage({player:p||'Anonim',score:s},'*');
        document.getElementById('gameOver').style.display='flex';
      }}
    </script></body></html>"""
    res = components.html(GAME_HTML, height=300, scrolling=False, return_value=True)

    # --- Skor kaydet ---
    if isinstance(res, dict) and 'score' in res:
        st.session_state.scores.append({'isim': res['player'], 'skor': res['score']})
        st.success(f"🏅 {res['player']} skoru {res['score']} kaydedildi!")

    # --- Skor Tablosu ---
    if st.button("🏆 Skor Tablosu"):
        for i, e in enumerate(sorted(st.session_state.scores, key=lambda x:x['skor'], reverse=True)):
            medal = '🏆' if i==0 else '🥈' if i==1 else '🥉' if i==2 else ''
            st.write(f\"{medal} {e['isim']} - {e['skor']}\")
    st.stop()

# ========= TEXT ADVENTURE =========
# --- State
st.session_state.setdefault('stage','intro');st.session_state.setdefault('step',0)
st.session_state.setdefault('lives',3);st.session_state.setdefault('answered',False)
st.session_state.setdefault('score',0)

# --- Event data (kısaltılmış – orijinal sorular aynı)
events={ 'gece_mail':[{'q':'📧 Mail sorusu','ops':['Doğru','Yanlış'],'correct':0,'pts':10}], }
order=list(events)+['finished']

# --- Helpers
def restart(full=False): st.session_state.update(stage='intro',step=0,answered=False,
    lives=3 if full else st.session_state.lives,score=0)
def advance():
    st.session_state.step+=1;st.session_state.answered=False
    if st.session_state.step>=len(events[st.session_state.stage]):
        st.session_state.stage=order[order.index(st.session_state.stage)+1]
        st.session_state.step=0

# --- UI
st.markdown('<h1 class=\"game-title\">🌻 DİLAY\'I KORU</h1>',unsafe_allow_html=True)
st.markdown(f\"<div class='lives-board'>Can: {'❤️'*st.session_state.lives}</div>\",unsafe_allow_html=True)

if st.session_state.stage=='intro':
    st.markdown('<div class=\"question-box\">Gece vardiyasına hoş geldin!</div>',unsafe_allow_html=True)
    if st.button('Başla'): st.session_state.stage='gece_mail'
elif st.session_state.stage in events:
    ev=events[st.session_state.stage][st.session_state.step]
    st.markdown(f\"<div class='question-box'>{ev['q']}</div>\",unsafe_allow_html=True)
    if st.button(ev['ops'][0]): st.session_state.answered=True; st.session_state.score+=ev['pts']; advance()
    if st.button(ev['ops'][1]): st.session_state.lives-=1; st.session_state.answered=True; advance() if st.session_state.lives>0 else st.error('Oyun bitti!')
elif st.session_state.stage=='finished':
    st.balloons();st.success('Tüm bölümler tamam!')
