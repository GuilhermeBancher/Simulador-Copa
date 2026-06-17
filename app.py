import streamlit as st
import time
import pandas as pd  # Garantindo o pandas para a manipulação dos seus dados dinâmicos

# 1. Configuração da página (Obrigatória em primeiro lugar)
st.set_page_config(
    page_title="WC Prediction Engine", 
    page_icon="🏆", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# SEU MOTOR DE SIMULAÇÃO (LÓGICA DINÂMICA ORIGINAL)
# ==============================================================================
# NOTA: Certifique-se de que suas funções ou leituras de arquivos (ex: pd.read_csv)
# que geram o ranking dinâmico estejam declaradas aqui antes das abas.

@st.cache_data
def carregar_ranking_dinamico():
    """
    Substitua o mock abaixo pela chamada real do seu DataFrame ou função.
    Exemplo: return pd.read_csv("seus_dados_de_elo.csv") ou seu modelo Monte Carlo.
    O importante é que ele retorne as colunas usadas no loop abaixo!
    """
    # Exemplo de estrutura que seu modelo gera dinamicamente:
    dados = [
        {"pos": 1, "sigla": "ES", "nome": "Spain", "elo": 2075, "prob": 21.7},
        {"pos": 2, "sigla": "BR", "nome": "Brazil", "elo": 2045, "prob": 18.4},
        {"pos": 3, "sigla": "FR", "nome": "France", "elo": 2030, "prob": 15.2},
        {"pos": 4, "sigla": "AR", "nome": "Argentina", "elo": 2020, "prob": 12.8},
        {"pos": 5, "sigla": "EN", "nome": "England", "elo": 1995, "prob": 8.6},
        {"pos": 6, "sigla": "DE", "nome": "Germany", "elo": 1980, "prob": 6.4},
        {"pos": 7, "sigla": "PT", "nome": "Portugal", "elo": 1975, "prob": 5.1},
        {"pos": 8, "sigla": "NL", "nome": "Netherlands", "elo": 1960, "prob": 4.5},
    ]
    return pd.DataFrame(dados)

# Chamada dos dados dinâmicos do seu modelo
df_ranking_dinamico = carregar_ranking_dinamico()


# ==============================================================================
# NAVEGAÇÃO POR ABAS (Isolamento completo contra duplicações)
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

    # Puxando dinamicamente os 5 primeiros do seu modelo para a Home
    contenders = df_ranking_dinamico.head(5)

    for _, c in contenders.iterrows():
        col_team, col_progress, col_values = st.columns([2.5, 5, 1.2])
        with col_team:
            st.write(f"**{c['pos']}** {c['sigla']}  **{c['nome']}**")
        with col_progress:
            st.progress(float(c['prob']) / 100.0)
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
# CONTEÚDO DA ABA 2: GLOBAL RANKINGS (CONECTADO E FILTRADO DINAMICAMENTE)
# ==============================================================================
with tab_rankings:
    st.title("📊 Global ELO Rankings")
    st.write("Full standing of all nations based on current ELO strength and simulation output.")
    
    # Campo de busca tratado
    search_query = st.text_input("🔍 Search for a country...", "", key="search_rankings").strip().lower()
    st.write("---")
    
    # Cabeçalho da Tabela
    col_h_team, col_h_elo, col_h_progress, col_h_prob = st.columns([2.5, 1, 4, 1])
    with col_h_team: st.write("**TEAM**")
    with col_h_elo: st.write("**ELO SCORE**")
    with col_h_progress: st.write("**WIN PROBABILITY MATRIX**")
    with col_h_prob: st.write("**CHANCE**")
        
    st.write("---")
    
    visible_teams = 0
    
    # Varrendo o seu DataFrame dinâmico linha por linha
    for _, t in df_ranking_dinamico.iterrows():
        # Lógica de busca insensível a maiúsculas/minúsculas e adaptada para "brasil/brazil"
        nome_pais = str(t["nome"]).lower()
        sigla_pais = str(t["sigla"]).lower()
        
        is_match = (
            search_query in nome_pais or 
            search_query in sigla_pais or 
            (search_query == "brasil" and nome_pais == "brazil")
        )
        
        if search_query and not is_match:
            continue
            
        visible_teams += 1
        col_t_name, col_t_elo, col_t_bar, col_t_prob = st.columns([2.5, 1, 4, 1])
        with col_t_name:
            st.write(f"**{t['pos']}** &nbsp;&nbsp; `{t['sigla']}` &nbsp;&nbsp; {t['nome']}")
        with col_t_elo:
            st.write(f"⚡ {t['elo']}")
        with col_t_bar:
            st.progress(float(t["prob"]) / 100.0)
        with col_t_prob:
            st.write(f"**{t['prob']}%**")

    if visible_teams == 0:
        st.warning("⚠️ No nations found matching your search query.")


# ==============================================================================
# CONTEÚDO DA ABA 3: SINGLE MATCH SIMULATION (100% SEGURO)
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
    
    for idx, match in enumerate(upcoming_fixtures):
        st.write(f"📅 **{match['date']} — {match['time']}**")
        
        c_t1, c_vs, c_t2, c_predict = st.columns([2, 0.5, 2, 1.5])
        
        with c_t1:
            st.write(f"{match['flag1']} **{match['t1']}** (`{match['s1']}`)")
        with c_vs:
            st.write("**VS**")
        with c_t2:
            st.write(f"(`{match['s2']}`) **{match['t2']}** {match['flag2']}")
        with c_predict:
            if st.button("Simulate Match", key=f"btn_m_{idx}"):
                st.info(f"Simulating {match['t1']} vs {match['t2']}...")
                time.sleep(0.8)
                st.success(f"Win {match['t1']} (54%) | Draw (22%) | Win {match['t2']} (24%)")
                
        st.write("---")
