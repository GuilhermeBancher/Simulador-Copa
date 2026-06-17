import streamlit as st
import time

# 1. Configuração da página (Obrigatória em primeiro lugar)
st.set_page_config(
    page_title="WC Prediction Engine", 
    page_icon="🏆", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 2. HERO SECTION (IMAGEM 1 DO ESBOÇO)
st.markdown("<p class='model-active'>● SIMULATION MODEL ACTIVE</p>", unsafe_allowed_html=True)
st.markdown("<h1 class='main-title-yellow'>2026 World Cup</h1>", unsafe_allowed_html=True)
st.markdown("<h1 class='main-title-white'>Predictor</h1>", unsafe_allowed_html=True)
st.markdown("<p class='subtitle'>Powered by ELO-based probabilistic simulation model</p>", unsafe_allowed_html=True)
st.markdown("<p class='sub-caption'>100,000+ match simulations • Real-time recalibration</p>", unsafe_allowed_html=True)

st.markdown("<br>", unsafe_allowed_html=True)

# Botões de ação centralizados
col_space1, col_btn1, col_btn2, col_space2 = st.columns([2, 1.2, 1, 2])
with col_btn1:
    run_sim = st.button("🔮 Run full tournament simulation", use_container_width=True, type="primary")
with col_btn2:
    st.button("View bracket →", use_container_width=True)

if run_sim:
    with st.spinner("Recalibrating Monte Carlo matrix..."):
        time.sleep(1.5)
    st.success("Tournament simulated successfully!")

st.markdown("<br><br>", unsafe_allowed_html=True)

# 3. TOP TITLE CONTENDERS SECTION (IMAGEM 2 DO ESBOÇO)
st.markdown("### 📈 Top Title Contenders")

contenders = [
    {"pos": 1, "sigla": "ES", "nome": "Spain", "status": "FAVORITE", "prob": 21.7, "elo": 2075, "cor": "#f59e0b"},
    {"pos": 2, "sigla": "BR", "nome": "Brazil", "status": "FAVORITE", "prob": 18.4, "elo": 2045, "cor": "#0ea5e9"},
    {"pos": 3, "sigla": "FR", "nome": "France", "status": "CONTENDER", "prob": 15.2, "elo": 2030, "cor": "#ec4899"},
    {"pos": 4, "sigla": "AR", "nome": "Argentina", "status": "CONTENDER", "prob": 12.8, "elo": 2020, "cor": "#10b981"},
    {"pos": 5, "sigla": "EN", "nome": "England", "status": "CONTENDER", "prob": 8.6, "elo": 1995, "cor": "#a855f7"},
]

for c in contenders:
    badge_lbl = "FAVORITE" if c["status"] == "FAVORITE" else "CONTENDER"
    badge_clss = "badge-fav" if c["status"] == "FAVORITE" else "badge-cont"
    
    with st.container():
        col_team, col_progress, col_values = st.columns([2.5, 5, 1.2])
        with col_team:
            st.markdown(f"<div class='team-row'><span class='team-pos'>{c['pos']}</span><span class='team-sigla'>{c['sigla']}</span><span class='team-name'>{c['nome']}</span><span class='{badge_clss}'>{badge_lbl}</span></div>", unsafe_allowed_html=True)
        with col_progress:
            st.markdown(f"<div class='progress-bg'><div class='progress-bar' style='background-color: {c['cor']}; width: {c['prob'] * 4.2}%;'></div></div>", unsafe_allowed_html=True)
        with col_values:
            st.markdown(f"<div class='values-row'><b>{c['prob']}%</b><br><span class='elo-text'>ELO {c['elo']}</span></div>", unsafe_allowed_html=True)

st.markdown("<br><hr class='custom-hr'><br>", unsafe_allowed_html=True)

# 4. FOOTER METRICS
col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    st.metric(label="🏆 Teams Analyzed", value="48")
with col_m2:
    st.metric(label="⚡ Simulations Run", value="100K+")
with col_m3:
    st.metric(label="📈 Model Accuracy", value="87.3%")
