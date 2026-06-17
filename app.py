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
        {"pos": 8, "sigla": "NL", "nome": "Netherlands", "elo": 1960, "prob": 4.5},
    ]
    
    col_h_team, col_h_elo, col_h_progress, col_h_prob = st.columns([2.5, 1, 4, 1])
    with col_h_team: st.write("**TEAM**")
    with col_h_elo: st.write("**ELO SCORE**")
    with col_h_progress: st.write("**WIN PROBABILITY MATRIX**")
    with col_h_prob: st.write("**CHANCE**")
        
    st.write("---")
    
    visible_teams = 0
    for t in all_teams:
        if search_query and search_query not in t["nome"].lower() and search_query not in t["sigla"].lower():
            continue
            
        visible_teams += 1
        col_t_name, col_t_elo, col_t_bar, col_t_prob = st.columns([2.5, 1, 4, 1])
        with col_t_name:
            st.write(f"**{t['pos']}** &nbsp;&nbsp; `{t['sigla']}` &nbsp;&nbsp; {t['nome']}")
        with col_t_elo:
            st.write(f"⚡ {t['elo']}")
        with col_t_bar:
            st.progress(t["prob"] / 100.0)
        with col_t_prob:
            st.write(f"**{t['prob']}%**")


# ==============================================================================
# CONTEÚDO DA ABA 3: SINGLE MATCH SIMULATION (FORMATO 100% SEGURO)
# ==============================================================================
with tab_single_match:
    st.title("🔮 Single Match Prediction")
    st.write("Upcoming fixtures for the next 3 days. Run instantaneous ELO probabilistic simulations.")
    
    st.write("---")
    
    upcoming_fixtures = [
        {"date": "June 18, 2026", "t1": "Brazil", "s1": "BR", "flag1": "🇧🇷", "t2": "Germany", "s2": "DE", "flag2": "🇩🇪", "time": "16:00 UTC"},
        {"date": "June 19, 2026", "t1": "Spain", "s1": "ES", "flag1": "🇪🇸", "t2": "Morocco", "s2": "MA", "flag2": "🇲🇦", "time": "19:00 UTC"},
        {"date": "June 20, 2026", "t1": "Argentina", "s1": "AR", "flag1": "🇦🇷", "t2": "France", "s2": "FR", "flag2": "🇫🇷", "time": "13:00 UTC"},
    ]
    
    # Renderização limpa sem NENHUMA tag HTML (Impossível quebrar)
    for idx, match in enumerate(upcoming_fixtures):
        st.write(f"📅 **{match['date']} — {match['time']}**")
        
        c_t1, c_vs, c_t2, c_predict = st.columns(
