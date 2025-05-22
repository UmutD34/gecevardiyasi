import streamlit as st

# ----------------------
# Global CSS
# ----------------------
st.markdown(
    """
    <style>
    .game-title { font-size:48px; font-weight:bold; text-align:center; }
    .score-board { font-size:20px; text-align:center; margin-bottom:20px; }
    .bars { display:flex; justify-content:space-around; margin:20px 0; }
    .bar-label { font-weight:bold; }
    .question-box { background:#f0f0f5; padding:20px; border-radius:10px; margin-bottom:20px; }
    .btn-option { width:100%; padding:15px 0; font-size:18px; margin:5px; border-radius:8px; }
    .btn-correct { background-color:#4CAF50; color:white; }
    .btn-wrong { background-color:#f44336; color:white; }
    .btn-next { background-color:#2196F3; color:white; width:200px; margin:20px auto; display:block; }
    </style>
    """, unsafe_allow_html=True)

# ----------------------
# State Yönetimi
# ----------------------
if 'stage' not in st.session_state:
    st.session_state.stage = 'intro'
    st.session_state.step = 0
    st.session_state.health = 100
    st.session_state.enemy = 100
    st.session_state.score = 0
    st.session_state.answered = False

# ----------------------
# Event Data
# ----------------------
events = {
    'gece_mail': [
        { 'q': "📧 Gelen kutusu patlamak üzere! İlk hamle?",
          'ops': ["🛡️ Spam filtresi", "📖 Hepsini oku"], 'correct':0, 'pts':10},
        { 'q': "🔄 CC: Herkes faciası başladı! Nasıl durdurursun?",
          'ops': ["🔇 Yanıtları kapat", "🏫 Cevabı okula gönder"], 'correct':0, 'pts':15},
        { 'q': "🚀 Son aşama: Mail saldırısına son hamle?",
          'ops': ["📂 Arşive at", "🗑️ Hemen sil"], 'correct':0, 'pts':20},
    ],
    # diğer bölümler benzer şekilde...
}
order = ['intro','gece_mail','finished']

# ----------------------
# Fonksiyonlar
# ----------------------
def restart():
    st.session_state.update({
        'stage':'intro','step':0,'health':100,'enemy':100,'score':0,'answered':False
    })


def advance():
    st.session_state.step += 1
    st.session_state.answered = False
    if st.session_state.step >= len(events[st.session_state.stage]):
        # sonraki bölüme
        idx = order.index(st.session_state.stage)
        st.session_state.stage = order[idx+1]
        st.session_state.step = 0

# ----------------------
# Layout
# ----------------------
st.markdown('<div class="game-title">🌻 DİLAY'I KORU</div>', unsafe_allow_html=True)
st.markdown(f'<div class="score-board">Skor: {st.session_state.score}</div>', unsafe_allow_html=True)

# Intro
if st.session_state.stage=='intro':
    st.markdown('<div class="question-box">Gece vardiyasına hoş geldin! 🤔</div>', unsafe_allow_html=True)
    c1,c2 = st.columns(2)
    if c1.button('💪 Evet, hazırım', key='intro_yes'):
        st.session_state.stage='gece_mail'
    if c2.button('😱 Hayır, korkuyorum', key='intro_no'):
        st.error('Korkuya yenik düştün!')
        if st.button('🔄 Tekrar Dene'):
            restart()

# Event Bölümü
elif st.session_state.stage in events:
    ev = events[st.session_state.stage][st.session_state.step]
    st.markdown(f'<div class="question-box">{ev["q"]}</div>', unsafe_allow_html=True)
    o1,o2 = st.columns(2)
    if not st.session_state.answered:
        if o1.button(ev['ops'][0], key=f'opt1_{st.session_state.step}'):
            st.session_state.answered = True
            if 0==ev['correct']:
                st.success('✅ Doğru!')
                st.session_state.score += ev['pts']
            else:
                st.error('❌ Yanlış!')
        if o2.button(ev['ops'][1], key=f'opt2_{st.session_state.step}'):
            st.session_state.answered = True
            if 1==ev['correct']:
                st.success('✅ Doğru!')
                st.session_state.score += ev['pts']
            else:
                st.error('❌ Yanlış!')
    else:
        if st.button('▶️ İleri', key=f'next_{st.session_state.step}'):
            advance()

# Finished
elif st.session_state.stage=='finished':
    st.balloons()
    st.success(f'Tebrikler! Skorun: {st.session_state.score} 🌟')
    if st.button('🔄 Yeniden Başla'):
        restart()
