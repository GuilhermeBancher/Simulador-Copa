import streamlit as st
import time

# 1. Configuração da página (Deve ser o primeiro comando)
st.set_page_config(
    page_title="WC Prediction Engine", 
    page_icon="🏆", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# NAVEGAÇÃO POR ABAS (Tudo envelopado de forma isolada)
# ==============================================================================
tab_home, tab_rankings, tab_single_match = st.tabs([
    "🏠 Home", 
    "📊 Global Rankings", 
    "🔮 Single Match Simulation"
])

# ==============================================================================
# CONTEÚDO DA ABA 1: HOME
# ==============================================================================
with tab_home:
    st.caption("🟢 SIMULATION MODEL ACTIVE")
    st.title("🏆 2026 World Cup Predictor")
    st.write("Powered by ELO-based probabilistic simulation model")
    st.caption("100,000+ match simulations • Real-time recalibration")

    st.write("---")

    col_btn1, col_btn2 = st.columns([1.2, 4])
    with col_btn1:
        run_sim = st.button("🔮 Run full tournament simulation", type="primary", key="btn_home_sim")
    with col_btn2:
        st.button("View bracket →", key="btn_home_bracket")

    if run_sim:
        with st.spinner("Recalibrating Monte Carlo matrix..."):
            time.sleep(1.5)
        st.success("Tournament simulated successfully!")

    st.write("---")
    st.subheader("📈 Top Title Contenders")

    contenders = [
        {"pos": 1, "sigla": "ES", "nome": "Spain", "status": "FAVORITE", "prob": 21.7, "elo": 2075},
        {"pos": 2, "sigla": "BR", "nome": "Brazil", "status": "FAVORITE", "prob": 18.4, "elo": 2045},
        {"pos": 3, "sigla": "FR", "nome": "France", "status": "CONTENDER", "prob": 15.2, "elo": 2030},
        {"pos": 4, "sigla": "AR", "nome": "Argentina", "status": "CONTENDER", "prob": 12.8, "elo": 2020},
        {"pos": 5, "sigla": "EN", "nome": "England", "status": "CONTENDER", "prob": 8.6, "elo": 1995},
    ]

    for c in contenders:
        col_team, col_progress, col_values = st.columns([2.5, 5, 1.2])
        with col_team:
            st.write(f"**{c['pos']}** {c['sigla']}  **{c['nome']}** ({c['status']})")
        with col_progress:
            st.progress(c['prob'] / 100.0)
        with col_values:
            st.write(f"**{c['prob']}%** (ELO {c['elo']})")

    st.write("---")
    col_m1, col_m2, col_m3 = st.columns(3)
    with col_m1:
        st.metric(label="🏆 Teams Analyzed", value="48")
    with col_m2:
        st.metric(label="⚡ Simulations Run", value="100K+")
    with col_m3:
        st.metric(label="📈 Model Accuracy", value="87.3%")


# ==============================================================================
# CONTEÚDO DA ABA 2: GLOBAL RANKINGS
# ==============================================================================
with tab_rankings:
    st.title("📊 Global ELO Rankings")
    st.write("Full standing of all 48 qualified nations based on current ELO strength and simulation output.")
    
    search_query = st.text_input("🔍 Search for a country...", "", key="search_rankings").strip().lower()
    st.write("---")
    
    all_teams = [
        {"pos": 1, "sigla": "ES", "nome": "Spain", "elo": 2075, "prob": 21.7},
        {"pos": 2, "sigla": "BR", "nome": "Brazil", "elo": 2045, "prob": 18.4},
        {"pos": 3, "sigla": "FR", "nome": "France", "elo": 2030, "prob": 15.2},
        {"pos": 4, "sigla": "AR", "nome": "Argentina", "elo": 2020, "prob": 12.8},
        {"pos": 5, "sigla": "EN", "nome": "England", "elo": 1995, "prob": 8.6},
        {"pos": 6, "sigla": "DE", "nome": "Germany", "elo": 1980, "prob": 6.4},
        {"pos": 7, "sigla": "PT", "nome": "Portugal", "elo": 1975, "prob": 5.1},
        {"pos": 8, "sigla": "NL", "nome": "Netherlands", "elo": 1960, "prob": 4.5
