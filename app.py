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



#Etapa 2

import streamlit as st
import time

# 1. Configuração da página
st.set_page_config(
    page_title="WC Prediction Engine", 
    page_icon="🏆", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# CRIAÇÃO DAS ABAS DE NAVEGAÇÃO SUPERIOR
# ==============================================================================
tab_home, tab_rankings = st.tabs(["🏠 Home", "📊 Global Rankings"])

# ==============================================================================
# CONTEÚDO DA ABA 1: HOME (ETAPA 1)
# ==============================================================================
with tab_home:
    st.caption("🟢 SIMULATION MODEL ACTIVE")
    st.title("🏆 2026 World Cup Predictor")
    st.write("Powered by ELO-based probabilistic simulation model")
    st.caption("100,000+ match simulations • Real-time recalibration")

    st.write("---")

    col_btn1, col_btn2 = st.columns([1, 4])
    with col_btn1:
        run_sim = st.button("🔮 Run full simulation", type="primary", key="btn_home_sim")
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
# CONTEÚDO DA ABA 2: GLOBAL RANKINGS (ETAPA 2)
# ==============================================================================
with tab_rankings:
    st.title("📊 Global ELO Rankings")
    st.write("Full standing of all 48 qualified nations based on current ELO strength and simulation output.")
    
    # Campo de busca para filtrar seleções (idêntico à lógica de usabilidade profissional)
    search_query = st.text_input("🔍 Search for a country...", "").strip().lower()
    
    st.write("---")
    
    # Base de dados simulada contendo as seleções (Exemplo expandido para demonstrar a rolagem)
    all_teams = [
        {"pos": 1, "sigla": "ES", "nome": "Spain", "elo": 2075, "prob": 21.7},
        {"pos": 2, "sigla": "BR", "nome": "Brazil", "elo": 2045, "prob": 18.4},
        {"pos": 3, "sigla": "FR", "nome": "France", "elo": 2030, "prob": 15.2},
        {"pos": 4, "sigla": "AR", "nome": "Argentina", "elo": 2020, "prob": 12.8},
        {"pos": 5, "sigla": "EN", "nome": "England", "elo": 1995, "prob": 8.6},
        {"pos": 6, "sigla": "DE", "nome": "Germany", "elo": 1980, "prob": 6.4},
        {"pos": 7, "sigla": "PT", "nome": "Portugal", "elo": 1975, "prob": 5.1},
        {"pos": 8, "sigla": "NL", "nome": "Netherlands", "elo": 1960, "prob": 4.5},
        {"pos": 9, "sigla": "IT", "nome": "Italy", "elo": 1950, "prob": 3.8},
        {"pos": 10, "sigla": "UY", "nome": "Uruguay", "elo": 1942, "prob": 3.2},
        {"pos": 11, "sigla": "BE", "nome": "Belgium", "elo": 1930, "prob": 2.9},
        {"pos": 12, "sigla": "HR", "nome": "Croatia", "elo": 1915, "prob": 2.1},
        {"pos": 13, "sigla": "US", "nome": "United States", "elo": 1890, "prob": 1.8},
        {"pos": 14, "sigla": "MX", "nome": "Mexico", "elo": 1875, "prob": 1.5},
        {"pos": 15, "sigla": "MA", "nome": "Morocco", "elo": 1870, "prob": 1.4},
        {"pos": 16, "sigla": "JP", "nome": "Japan", "elo": 1865, "prob": 1.2},
        # Nota: Futuramente, esse array será preenchido lendo um arquivo CSV com as 48 seleções!
    ]
    
    # Cabeçalho da Tabela de Rankings
    col_h_team, col_h_elo, col_h_progress, col_h_prob = st.columns([2.5, 1, 4, 1])
    with col_h_team:
        st.write("**TEAM**")
    with col_h_elo:
        st.write("**ELO SCORE**")
    with col_h_progress:
        st.write("**WIN PROBABILITY MATRIX**")
    with col_h_prob:
        st.write("**CHANCE**")
        
    st.write("---")
    
    # Loop para renderizar as linhas do ranking aplicando o filtro de busca
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
            # Renderiza a barra de progresso correspondente à probabilidade do time
            st.progress(t["prob"] / 100.0)
        with col_t_prob:
            st.write(f"**{t['prob']}%**")

    if visible_teams == 0:
        st.warning("No countries found matching your search criteria.")
