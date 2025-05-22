import streamlit as st

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
# Debug View
# ----------------------
# Uncomment to see state for debugging
# st.write(st.session_state)

# ----------------------
# Event Data (Fixed Content)
# ----------------------
events = {
    'gece_mail': [
        { 'q': "📧 Gece vardiyası baslarken gıcık bir mail ile karşılaştın, ne yapacaksın?",
          'ops': ["🛡️ Dilay racon ile mail yazarım", "📖 Görmezden gelirim"], 'correct':0, 'pts':10, 'icon':'✉️'},
        { 'q': "🔄 Yazım yanlışı uyarısı, ne yapacaksın?",
          'ops': ["🔇 Bilgisayarı camdan at", "🏫 Masanın altına gir"], 'correct':0, 'pts':15, 'icon':'✍️'},
        { 'q': "🚀 Kameralar bozuldu, ne yapacaksın?",
          'ops': ["🙏 Dua et", "🗑️ Çöpe at"], 'correct':0, 'pts':20, 'icon':'📷'},
    ],
    'ogrenciler': [
        { 'q': "💳 Kartını unutan öğrenci, ne yapacaksın?",
          'ops': ["🔔 Raconla aç", "🎧 Dinlemem"], 'correct':0, 'pts':8, 'icon':'👩‍🎓'},
        { 'q': "👻 Hayalet gördüğünü iddia etti, ne yapacaksın?",
          'ops': ["🦹‍♂️ Maske tak","🎤 Şarkı söyle"], 'correct':0, 'pts':12, 'icon':'👻'},
        { 'q': "🎓 Gece dışarı çıkmak isterken imza atmam dedi, ne yapacaksın?",
          'ops': ["📢 Yurda geri sok","🤳 Reels izle"], 'correct':0, 'pts':15, 'icon':'✍️'},
    ],
    'veliler': [
        { 'q': "☕️ Veliler çay istiyor, ne önerirsin?",
          'ops': ["Çay tavaiye et","Numara yap"], 'correct':0, 'pts':10, 'icon':'☕️'},
        { 'q': "📱 Sürekli arıyorlar, ne yapacaksın?",
          'ops': ["🔇 Sessize al","🎬 GIF gönder"], 'correct':0, 'pts':12, 'icon':'📱'},
        { 'q': "🎁 Papua Yeni Gine soruyor, ne önerirsin?",
          'ops': ["Bilet al","Papatya çayı"], 'correct':0, 'pts':15, 'icon':'🎁'},
    ],
    'fare': [
        { 'q': "🐭 Fare istilası başladı, ne yapacaksın?",
          'ops': ["🥫 Miyu çağır","🔊 Kaval çal"], 'correct':0, 'pts':10, 'icon':'🐭'},
        { 'q': "💻 Fareler bilgisayara saldırıyor, ne yapacaksın?",
          'ops': ["🪤 İzle","🔊 Kov"], 'correct':0, 'pts':12, 'icon':'💻'},
        { 'q': "🐈 Fareler kaçıyor, ne yapacaksın?",
          'ops': ["🪤 Tuzak kur","📞 Fareleri ara"], 'correct':0, 'pts':15, 'icon':'🐈'},
    ],
    'su': [
        { 'q': "🌊 Koridorlar suyla doldu, ne yapacaksın?",
          'ops': ["🔧 Pompa çalıştır","🛶 Kano kirala"], 'correct':0, 'pts':10, 'icon':'💧'},
        { 'q': "💦 Vanayı kapatmak mı yoksa selfie mi?",
          'ops': ["🚰 Vanayı kapat","🤳 Selfie çek"], 'correct':0, 'pts':12, 'icon':'🚰'},
        { 'q': "🪣 Kova mı yoksa havuz mu?",
          'ops': ["🪣 Kova getir","🏊‍♂️ Havuz kur"], 'correct':0, 'pts':15, 'icon':'🪣'},
    ],
    'lavabo': [
        { 'q': "🚰 Lavabo sallanıyor, ne yapacaksın?",
          'ops': ["🔩 Kayışı sıkıştır","📱 Oyna"], 'correct':0, 'pts':10, 'icon':'🚰'},
        { 'q': "📉 Lavabo titreşim yapıyor, ne yapacaksın?",
          'ops': ["🦵 Destek ayağı","🎈 Müziği aç"], 'correct':0, 'pts':12, 'icon':'📉'},
        { 'q': "🛠️ Lavabo patladı, ne yapacaksın?",
          'ops': ["🔧 Boru bağla","💃 Dans et"], 'correct':0, 'pts':15, 'icon':'💥'},
    ],
}
order = ['intro','gece_mail','ogrenciler','veliler','fare','su','lavabo','finished']

# ----------------------
# Game Functions
# ----------------------
def restart(full=False):
    st.session_state.update({ 'stage':'intro', 'step':0, 'answered':False })
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
# Section indicator, Lives, Score
section = st.session_state.stage.replace('_',' ').title()
step = st.session_state.step + 1 if st.session_state.stage in events else ''
total = len(events.get(st.session_state.stage, []))
status = st.markdown(f'<div class="status-board"><div class="section-indicator">{section} {step}/{total}</div><div class="lives-board">Can: {"❤️"*st.session_state.lives}</div><div class="score-board">Puan: {st.session_state.score}</div></div>', unsafe_allow_html=True)

# ----------------------
# Intro
# ----------------------
if st.session_state.stage == 'intro':
    st.markdown('<div class="question-box">Gece vardiyasına hoş geldin! 🤔</div>', unsafe_allow_html=True)
    c1,c2 = st.columns(2)
    if c1.button('💪 Evet, hazırım'):
        st.session_state.stage = 'gece_mail'
    if c2.button('😱 Hayır, korkuyorum'):
        st.session_state.lives -=1
        if st.session_state.lives>0:
            st.warning(f'Korkuya yenik düştün!')
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
    st.markdown(f'<div class="question-box">{ev["icon"]} {ev["q"]}</div>', unsafe_allow_html=True)
    o1,o2 = st.columns(2)
    if not st.session_state.answered:
        if o1.button(ev['ops'][0]):
            st.session_state.answered = True
            if 0==ev['correct']:
                st.success('✅ Doğru seçim!')
                st.session_state.score += ev['pts']
            else:
                st.session_state.lives -=1
                st.error('❌ Yanlış seçim!')
        if o2.button(ev['ops'][1]):
            st.session_state.answered = True
            if 1==ev['correct']:
                st.success('✅ Doğru seçim!')
                st.session_state.score += ev['pts']
            else:
                st.session_state.lives -=1
                st.error('❌ Yanlış seçim!')
    else:
        if st.button('▶️ İleri'):
            if st.session_state.lives>0:
                advance()
            else:
                st.error('❌ Can kalmadı!')
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
# HTML5 Mini Oyun (Flappy Dilay)
# ----------------------
import streamlit.components.v1 as components

GAME_HTML = """
<!DOCTYPE html>
<html lang=\"en\">
<head><meta charset=\"UTF-8\"><title>Flappy Dilay</title>
<style>body{margin:0;overflow:hidden}canvas{background:#70c5ce;display:block;margin:auto}</style>
</head><body>
<canvas id=\"c\" width=\"400\" height=\"600\"></canvas>
<script>
const cv=document.getElementById('c'),ctx=cv.getContext('2d');let f=0,bx=50,by=150,bv=0,ps=[],sc=0;const g=0.4,fl=-8,pg=150;
document.addEventListener('keydown',e=>{if(e.code==='Space')bv=fl;});
function L(){f++;ctx.fillStyle='#70c5ce';ctx.fillRect(0,0,400,600);
 if(f%100===0){let y=50+Math.random()*(600-pg-100);ps.push({x:400,yn:y,ys:y+pg});}
 ps.forEach(p=>{ctx.fillStyle='#228B22';ctx.fillRect(p.x,p.yn-400,50,400);ctx.fillRect(p.x,p.ys,50,400);p.x-=2;
 if(bx>p.x&&bx< p.x+50&&(by<p.yn||by>p.ys))return GO();if(p.x===bx)sc++;});ps=ps.filter(p=>p.x> -50);
 bv+=g;by+=bv;ctx.fillStyle='#FFD700';ctx.beginPath();ctx.arc(bx,by,20,0,2*Math.PI);ctx.fill();
 if(by>600||by<0)return GO();ctx.fillStyle='#fff';ctx.font='30px Arial';ctx.fillText(sc,180,50);
 requestAnimationFrame(L);}function GO(){ctx.fillStyle='rgba(0,0,0,0.5)';ctx.fillRect(0,0,400,600);
 ctx.fillStyle='#fff';ctx.font='30px Arial';ctx.fillText('Oyun Bitti!',100,280);ctx.font='20px Arial';ctx.fillText('Yenile: F5',130,320);}L();
</script>
</body></html>
"""

components.html(GAME_HTML, height=650)
