import streamlit as st
import time

# 1. Configuração da página (Obrigatória em primeiro lugar)
st.set_page_config(
    page_title="WC Prediction Engine", 
    page_icon="🏆", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# 2. HERO SECTION (IMAGEM 1 DO ESBOÇO - USANDO APENAS COMANDOS NATIVOS)
st.caption("🟢 SIMULATION MODEL ACTIVE")
st.title("🏆 2026 World Cup Predictor")
st.write("Powered by ELO-based probabilistic simulation model")
st.caption("100,000+ match simulations • Real-time recalibration")

st.write("---")

# Botões de ação centralizados usando colunas nativas
col_space1, col_btn1, col_btn2, col_space2 = st.columns([2, 1.2, 1, 2])
with col_btn1:
    run_sim = st.button("🔮 Run full tournament simulation", use_container_width=True, type="primary")
with col_btn2:
    st.button("View bracket →", use_container_width=True)

if run_sim:
    with st.spinner("Recalibrating Monte Carlo matrix..."):
        time.sleep(1.5)
    st.success("Tournament simulated successfully!")

st.write("---")

# 3. TOP TITLE CONTENDERS SECTION (IMAGEM 2 DO ESBOÇO)
st.subheader("📈 Top Title Contenders")

contenders = [
    {"pos": 1, "sigla": "ES", "nome": "Spain", "status": "FAVORITE", "prob": 21.7, "elo": 2075},
    {"pos": 2, "sigla": "BR", "nome": "Brazil", "status": "FAVORITE", "prob": 18.4, "elo": 2045},
    {"pos": 3, "sigla": "FR", "nome": "France", "status": "CONTENDER", "prob": 15.2, "elo": 2030},
    {"pos": 4, "sigla": "AR", "nome": "Argentina", "status": "CONTENDER", "prob": 12.8, "elo": 2020},
    {"pos": 5, "sigla": "EN", "nome": "England", "status": "CONTENDER", "prob": 8.6, "elo": 1995},
]

# Renderização usando colunas e elementos 100% nativos
for c in contenders:
    col_team, col_progress, col_values = st.columns([2.5, 5, 1.2])
    with col_team:
        st.write(f"**{c['pos']}** {c['sigla']}  **{c['nome']}** ({c['status']})")
    with col_progress:
        # Barra de progresso nativa do Streamlit
        st.progress(c['prob'] / 100.0)
    with col_values:
        st.write(f"**{c['prob']}%** (ELO {c['elo']})")

st.write("---")

# 4. FOOTER METRICS
col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    st.metric(label="🏆 Teams Analyzed", value="48")
with col_m2:
    st.metric(label="⚡ Simulations Run", value="100K+")
with col_m3:
    st.metric(label="📈 Model Accuracy", value="87.3%")
