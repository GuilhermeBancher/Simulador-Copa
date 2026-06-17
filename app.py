import streamlit as st
import time

# 1. Configuração da página (Obrigatória em primeiro lugar)
st.set_page_config(
    page_title="WC Prediction Engine", 
    page_icon="🏆", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# ESTRUTURA CRUCIAL DAS ABAS (Tudo precisa rodar dentro dos blocos 'with')
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

    # Botões internos da aba Home para não duplicar
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
# CONTEÚDO DA ABA 3: SINGLE MATCH SIMULATION (ETAPA 3)
# ==============================================================================
with tab_single_match:
    st.title("🔮 Single Match Prediction")
    st.write("Upcoming fixtures for the next 3 days. Run instantaneous ELO probabilistic simulations.")
    
    st.write("---")
    
    # Mock dos jogos dos próximos 3 dias (Futuramente conectados com a API externa)
    upcoming_fixtures = [
        {"date": "June 18, 2026", "t1": "Brazil", "s1": "BR", "t2": "Germany", "s2": "DE", "time": "16:00 UTC"},
        {"date": "June 19, 2026", "t1": "Spain", "s1": "ES", "t2": "Morocco", "s2": "MA", "time": "19:00 UTC"},
        {"date": "June 20, 2026", "t1": "Argentina", "s1": "AR", "t2": "France", "s2": "FR", "time": "13:00 UTC"},
    ]
    
    # Construção dos blocos de confronto idênticos ao esboço
    for idx, match in enumerate(upcoming_fixtures):
        st.subheader(f"📅 {match['date']} — {match['time']}")
        
        # Grid do confronto: Time 1 | Versus | Time 2 | Botão de Calcular
        c_t1, c_vs, c_t2, c_predict = st.columns([2, 0.5, 2, 1.5])
        
        with c_t1:
            st.markdown(f"<div style='text-align: right; font-size: 1.2rem; padding-top: 5px;'><b>{match['t1']}</b> `{match['s1']}`</div>", unsafe_allowed_html=True)
        with c_vs:
            st.markdown("<div style='text-align: center; color: #4b5563; font-weight: bold; font-size: 1.1rem; padding-top: 5px;'>VS</div>", unsafe_allowed_html=True)
        with c_t2:
            st.markdown(f"<div style='text-align: left; font-size: 1.2rem; padding-top: 5px;'>`{match['s2']}` <b>{match['t2']}</b></div>", unsafe_allowed_html=True)
        with c_predict:
            # Botão individual para cada partida usando chaves (keys) dinâmicas para o Streamlit não bugar
            if st.button(f"Simulate Match {idx+1}", key=f"btn_match_{idx}"):
                st.info(f"Simulating {match['t1']} vs {match['t2']}...")
                time.sleep(0.8)
                # Exibe um resultado de teste na tela
                st.success(f"Prediction complete: Win {match['t1']} (54%) | Draw (22%) | Win {match['t2']} (24%)")
                
        st.write("---")
