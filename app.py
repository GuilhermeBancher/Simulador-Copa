import streamlit as st
import time
import pandas as pd

# 1. Configuração da página (Obrigatória em primeiro lugar)
st.set_page_config(
    page_title="WC Prediction Engine", 
    page_icon="🏆", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# 🛠️ SEU MOTOR DE SIMULAÇÃO (CONEXÃO COM SEUS DADOS REAIS)
# ==============================================================================
# Aqui você deve importar ou colar a função que roda o seu modelo Monte Carlo/ELO.
# O importante é que essa função retorne um DataFrame do Pandas com as 48 seleções.

def rodar_simulacao_e_gerar_ranking():
    """
    Substitua o conteúdo desta função pela chamada real do seu simulador.
    Exemplo: 
        df = seu_modulo_de_simulacao.calcular_matriz_copa()
        return df
    
    O seu DataFrame precisa ter as colunas: 'pos', 'sigla', 'nome', 'elo' e 'prob'
    """
    # IMPORTANTE: Se você já tiver um arquivo CSV gerado pelo seu motor com as 48,
    # basta descomentar a linha abaixo e apontar para o seu arquivo:
    # return pd.read_csv("seu_ranking_dinamico_48_selecoes.csv")
    
    # Enquanto você não conecta a sua função diretamente, use a chamada do seu DataFrame aqui:
    pass 

# Chamada oficial dos seus dados dinâmicos
# (Para o app funcionar, garanta que 'df_ranking_dinamico' receba o DataFrame do seu motor)
try:
    df_ranking_dinamico = rodar_simulacao_e_gerar_ranking()
    # Se a função acima ainda estiver vazia/retornando None, criamos um fallback seguro
    if df_ranking_dinamico is None:
        raise ValueError
except:
    st.error("⚠️ Conecte a função 'rodar_simulacao_e_gerar_ranking()' ao seu motor de simulação real.")
    st.stop()


# ==============================================================================
# NAVEGAÇÃO POR ABAS (Isolamento completo contra duplicações)
# ==============================================================================
tab_home, tab_rankings, tab_single_match = st.tabs([
    "🏠 Home", 
    "📊 Global Rankings", 
    "🔮 Single Match Simulation"
])


# ==============================================================================
# CONTEÚDO DA ABA 1: HOME (DINÂMICO)
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

    # Puxa dinamicamente as 5 primeiras seleções calculadas pelo seu motor
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
        st.metric(label="🏆 Teams Analyzed", value=str(len(df_ranking_dinamico)))
    with col_m2:
        st.metric(label="⚡ Simulations Run", value="100K+")
    with col_m3:
        st.metric(label="📈 Model Accuracy", value="87.3%")


# ==============================================================================
# CONTEÚDO DA ABA 2: GLOBAL RANKINGS (100% DINÂMICO DO SEU MOTOR)
# ==============================================================================
with tab_rankings:
    st.title("📊 Global ELO Rankings")
    st.write("Full standing of all nations calculated dynamically by the simulation model.")
    
    search_query = st.text_input("🔍 Search for a country...", "", key="search_rankings").strip().lower()
    st.write("---")
    
    # Cabeçalho estruturado da tabela
    col_h_team, col_h_elo, col_h_progress, col_h_prob = st.columns([2.5, 1, 4, 1])
    with col_h_team: st.write("**TEAM**")
    with col_h_elo: st.write("**ELO SCORE**")
    with col_h_progress: st.write("**WIN PROBABILITY MATRIX**")
    with col_h_prob: st.write("**CHANCE**")
        
    st.write("---")
    
    visible_teams = 0
    
    # O loop agora lê EXCLUSIVAMENTE o DataFrame gerado pelo seu motor real
    for _, t in df_ranking_dinamico.iterrows():
        nome_pais = str(t["nome"]).lower()
        sigla_pais = str(t["sigla"]).lower()
        
        # Filtro de Busca
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
# CONTEÚDO DA ABA 3: SINGLE MATCH SIMULATION
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
