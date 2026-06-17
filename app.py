import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
import random
import time

# 1. Configuração da Página do Streamlit
st.set_page_config(
    page_title="2026 World Cup Predictor", 
    page_icon="🏆", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# 🧠 CORAÇÃO DO SEU MOTOR (MIGRADOS DO SEU SIMULADOR_TORNEIO.PY / SIMULADOR_JOGOS.PY)
# ==============================================================================

HOSTS = ["United States", "Mexico", "Canada"]
MEDIA_GOLS = 2.6

# Seus grupos oficiais da Copa do Mundo 2026
GRUPOS = {
    "A": ["Czechia", "Mexico", "South Korea", "South Africa"], 
    "B": ["Canada", "Switzerland", "Qatar", "Bosnia and Herzegovina"],
    "C": ["Scotland", "Morocco", "Haiti", "Brazil"],
    "D": ["United States", "Australia", "Turkey", "Paraguay"],
    "E": ["Germany", "Côte d'Ivoire", "Curaçao", "Ecuador"],
    "F": ["Sweden", "Japan", "Netherlands", "Tunisia"],
    "G": ["New Zealand", "Iran", "Belgium", "Egypt"],
    "H": ["Uruguay", "Spain", "Saudi Arabia", "Cabo Verde"],
    "I": ["France", "Norway", "Iraq", "Senegal"],
    "J": ["Argentina", "Austria", "Algeria", "Jordan"],
    "K": ["Portugal", "DR Congo", "Uzbekistan", "Colombia"],
    "L": ["England", "Croatia", "Ghana", "Panama"]
}


# Criando um set para isolar apenas as 48 seleções dos seus grupos
SELECOES_COPA = set()
for times in GRUPOS.values():
    SELECOES_COPA.update(times)

# Carregamento do seu arquivo Elo real com Fallback seguro de diretórios
@st.cache_data
def carregar_dados_elo():
    try:
        df = pd.read_csv("outputs/elo_ranking.csv")
    except FileNotFoundError:
        try:
            df = pd.read_csv("elo_ranking.csv")
        except FileNotFoundError:
            st.error("⚠️ Arquivo 'elo_ranking.csv' não encontrado no repositório!")
            st.stop()
            
    ratings_dict = dict(zip(df["team"], df["elo"]))
    return ratings_dict, df

ratings, df_ranking_completo = carregar_dados_elo()

# Suas funções originais de cálculo probabilístico de Poisson
def calcular_expectativa(elo_a, elo_b):
    return 1 / (1 + 10 ** ((elo_b - elo_a) / 400))

def jogar_partida(time_a, time_b, mata_mata=False):
    elo_a = ratings.get(time_a, 1500)
    elo_b = ratings.get(time_b, 1500)
    
    # Bônus de país sede do seu modelo (+100 ELO)
    if time_a in HOSTS: elo_a += 100
    if time_b in HOSTS: elo_b += 100
    
    exp_a = calcular_expectativa(elo_a, elo_b)
    exp_b = calcular_expectativa(elo_b, elo_a)
    
    lambda_a = exp_a * MEDIA_GOLS
    lambda_b = exp_b * MEDIA_GOLS
    
    gols_a = np.random.poisson(lambda_a)
    gols_b = np.random.poisson(lambda_b)
    
    if mata_mata and gols_a == gols_b:
        # Desempate por pênalti probabilístico baseado na expectativa de força
        vencedor = time_a if random.random() < exp_a else time_b
        return vencedor
    
    return gols_a, gols_b

# Sua lógica completa de simulação da árvore oficial da FIFA (Monte Carlo)
def simular_uma_copa_do_mundo():
    classificados_grupos = []
    terceiros_lugares = []
    
    for grupo, times in GRUPOS.items():
        pontos = Counter()
        saldo = Counter()
        gols_pro = Counter()
        
        for i in range(4):
            for j in range(i + 1, 4):
                t1, t2 = times[i], times[j]
                g1, g2 = jogar_partida(t1, t2, mata_mata=False)
                gols_pro[t1] += g1
                gols_pro[t2] += g2
                saldo[t1] += (g1 - g2)
                saldo[t2] += (g2 - g1)
                
                if g1 > g2: pontos[t1] += 3
                elif g2 > g1: pontos[t2] += 3
                else:
                    pontos[t1] += 1
                    pontos[t2] += 1
                    
        ranking_grupo = sorted(times, key=lambda x: (pontos[x], saldo[x], gols_pro[x]), reverse=True)
        classificados_grupos.extend(ranking_grupo[:2])
        terceiros_lugares.append((ranking_grupo[2], pontos[ranking_grupo[2]], saldo[ranking_grupo[2]], gols_pro[ranking_grupo[2]]))
        
    melhores_terceiros = sorted(terceiros_lugares, key=lambda x: (x[1], x[2], x[3]), reverse=True)[:8]
    vencedores_32 = classificados_grupos + [t[0] for t in melhores_terceiros]
    random.shuffle(vencedores_32)
    
    # Mata-Mata (Simulação em cascata até a grande final)
    vencedores_16 = [jogar_partida(vencedores_32[i], vencedores_32[i+1], mata_mata=True) for i in range(0, 32, 2)]
    vencedores_8 = [jogar_partida(vencedores_16[i], vencedores_16[i+1], mata_mata=True) for i in range(0, 16, 2)]
    vencedores_4 = [jogar_partida(vencedores_8[i], vencedores_8[i+1], mata_mata=True) for i in range(0, 8, 2)]
    finalistas = [jogar_partida(vencedores_4[i], vencedores_4[i+1], mata_mata=True) for i in range(0, 4, 2)]
    
    campeao = jogar_partida(finalistas[0], finalistas[1], mata_mata=True)
    return campeao

# Executor de Simulações em Lote para extrair probabilidades probabilísticas reais
@st.cache_data(show_spinner=False)
def rodar_simulacoes_lote(n_simulacoes=2000):
    contagem_campeoes = Counter()
    for _ in range(n_simulacoes):
        campeao = simular_uma_copa_do_mundo()
        contagem_campeoes[campeao] += 1
        
    # Inicializa todas as 48 seleções com pelo menos 0 vitórias caso não ganhem nenhuma
    dados_probabilidades = {}
    for selecao in SELECOES_COPA:
        vitorias = contagem_campeoes.get(selecao, 0)
        # Probabilidade real: (vitorias / total) * 100
        dados_probabilidades[selecao] = (vitorias / n_simulacoes) * 100
        
    return dados_probabilidades

# Se o usuário clicar em recalibrar com lote maior, salvamos no estado da sessão (st.session_state)
if "n_sim_executadas" not in st.session_state:
    st.session_state["n_sim_executadas"] = 2000
    st.session_state["dict_probs"] = rodar_simulacoes_lote(2000)


# ==============================================================================
# 🗂️ NAVEGAÇÃO POR ABAS
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
    st.caption(f"Active dataset: {st.session_state['n_sim_executadas']:,} match simulations • Real-time Monte Carlo matrix")

    st.write("---")

    col_btn1, col_btn2 = st.columns([1.5, 4])
    with col_btn1:
        run_sim = st.button("🔮 Run full tournament simulation", type="primary", key="btn_home_sim")
    with col_btn2:
        st.caption("Click to trigger a massive 10,000 tournament Monte Carlo loop and recalculate all vectors.")

    if run_sim:
        with st.spinner("Running 10,000 simulations through official FIFA tree... This might take a few seconds."):
            # Roda um lote de precisão maior e atualiza o estado dinâmico da aplicação
            novas_probs = rodar_simulacoes_lote(n_simulacoes=10000)
            st.session_state["n_sim_executadas"] = 10000
            st.session_state["dict_probs"] = novas_probs
        st.success("🎯 Projections recalibrated! Probabilities updated via Monte Carlo matrix.")
        st.rerun()

    st.write("---")
    st.subheader("📈 Top Title Contenders (Monte Carlo Real Output)")

    # Monta o DataFrame unificado com os dados ELO e injeta as probabilidades reais obtidas das simulações
    df_home = df_ranking_completo[df_ranking_completo["team"].isin(SELECOES_COPA)].copy()
    df_home["prob"] = df_home["team"].map(st.session_state["dict_probs"])
    df_home = df_home.sort_values(by=["prob", "elo"], ascending=[False, False]).reset_index(drop=True)
    
    # Exibe as 5 seleções com maiores chances reais de erguer a taça nas simulações
    contenders = df_home.head(5)
    siglas_home = {"Argentina": "AR", "France": "FR", "England": "EN", "Spain": "ES", "Germany": "DE", "Brazil": "BR", "Portugal": "PT", "Belgium": "BE"}

    for idx, c in contenders.iterrows():
        col_team, col_progress, col_values = st.columns([2.5, 5, 1.2])
        sigla = siglas_home.get(c['team'], "FC")
        prob_atual = float(c['prob'])
        
        with col_team:
            st.write(f"**{idx+1}** &nbsp;&nbsp; `{sigla}` &nbsp;&nbsp; **{c['team']}**")
        with col_progress:
            st.progress(prob_atual / 100.0 if prob_atual > 0 else 0.0)
        with col_values:
            st.write(f"**{prob_atual:.2f}%** ({int(c['elo'])} pts)")

    st.write("---")
    col_m1, col_m2, col_m3 = st.columns(3)
    with col_m1:
        st.metric(label="🏆 Teams Analyzed", value=f"{len(SELECOES_COPA)} (World Cup Only)")
    with col_m2:
        st.metric(label="⚡ Active Simulated Tournaments", value=f"{st.session_state['n_sim_executadas']:,}")
    with col_m3:
        # Soma de verificação para provar matematicamente que fecha em 100.0%
        soma_validada = sum(st.session_state["dict_probs"].values())
        st.metric(label="📊 Matrix Probability Sum", value=f"{soma_validada:.1f}%")


# ==============================================================================
# CONTEÚDO DA ABA 2: GLOBAL RANKINGS (ORDENADO E CALCULADO VIA SIMULAÇÃO)
# ==============================================================================
with tab_rankings:
    st.title("📊 Global ELO Rankings & Title Odds")
    st.write("Full standing of the 48 qualified nations. Odds are mapped directly from champion frequencies.")
    
    search_query = st.text_input("🔍 Search for a country...", "", key="search_rankings").strip().lower()
    st.write("---")
    
    col_h_team, col_h_elo, col_h_progress, col_h_prob = st.columns([2.5, 1, 4, 1])
    with col_h_team: st.write("**TEAM**")
    with col_h_elo: st.write("**ELO SCORE**")
    with col_h_progress: st.write("**WIN PROBABILITY MATRIX**")
    with col_h_prob: st.write("**CHANCE**")
        
    st.write("---")
    
    # Prepara o DataFrame completo filtrado para a tabela principal de visualização
    df_rankings_completo = df_ranking_completo[df_ranking_completo["team"].isin(SELECOES_COPA)].copy()
    df_rankings_completo["prob"] = df_rankings_completo["team"].map(st.session_state["dict_probs"])
    
    # Ordena estritamente por força de ELO para refletir o ranking dinâmico de qualidade técnica real
    df_rankings_completo = df_rankings_completo.sort_values("elo", ascending=False).reset_index(drop=True)
    
    visible_teams = 0
    posicao_ranking = 1
    
    for _, row in df_rankings_completo.iterrows():
        nome_time = str(row["team"])
        nome_comparar = nome_time.lower()
        
        # Filtro de Busca tolerante a maiúsculas/minúsculas e adaptação Brasil/Brazil
        is_match = (
            search_query in nome_comparar or 
            (search_query == "brasil" and nome_comparar == "brazil")
        )
        
        if search_query and not is_match:
            posicao_ranking += 1
            continue
            
        visible_teams += 1
        elo_valor = float(row["elo"])
        prob_campeao = float(row["prob"])
        
        col_t_name, col_t_elo, col_t_bar, col_t_prob = st.columns([2.5, 1, 4, 1])
        with col_t_name:
            st.write(f"**{posicao_ranking}** &nbsp;&nbsp; {nome_time}")
        with col_t_elo:
            st.write(f"⚡ {elo_valor:.1f}")
        with col_t_bar:
            # A barra de progresso agora reflete com precisão cirúrgica a chance matemática da seleção ganhar a copa
            st.progress(prob_campeao / 100.0 if prob_campeao > 0 else 0.0)
        with col_t_prob:
            st.write(f"**{prob_campeao:.2f}%**")
            
        posicao_ranking += 1

    if visible_teams == 0:
        st.warning("⚠️ No nations found matching your search query within the 48 World Cup teams.")


# ==============================================================================
# CONTEÚDO DA ABA 3: SINGLE MATCH SIMULATION (INTEGRADO AO SEU POISSON MATEMÁTICO)
# ==============================================================================
with tab_single_match:
    st.title("🔮 Single Match Prediction")
    st.write("Upcoming key fixtures. Run instantaneous ELO probabilistic simulations using your Python Poisson engine.")
    
    st.write("---")
    
    upcoming_fixtures = [
        {"date": "June 18, 2026", "t1": "Brazil", "flag1": "🇧🇷", "t2": "Germany", "flag2": "🇩🇪", "time": "16:00 UTC"},
        {"date": "June 19, 2026", "t1": "Spain", "flag1": "🇪🇸", "t2": "Morocco", "flag2": "🇲🇦", "time": "19:00 UTC"},
        {"date": "June 20, 2026", "t1": "Argentina", "flag1": "🇦🇷", "t2": "France", "flag2": "🇫🇷", "time": "13:00 UTC"},
    ]
    
    for idx, match in enumerate(upcoming_fixtures):
        st.write(f"📅 **{match['date']} — {match['time']}**")
        
        c_t1, c_vs, c_t2, c_predict = st.columns([2, 0.5, 2, 1.5])
        
        with c_t1:
            st.write(f"{match['flag1']} **{match['t1']}** (Elo {ratings.get(match['t1'], 1500):.1f})")
        with c_vs:
            st.write("**VS**")
        with c_t2:
            st.write(f"**{match['t2']}** (Elo {ratings.get(match['t2'], 1500):.1f}) {match['flag2']}")
        with c_predict:
            if st.button("Simulate Match", key=f"btn_m_{idx}"):
                vitorias_t1 = 0
                vitorias_t2 = 0
                empates = 0
                
                # Executa 1.000 simulações rápidas usando sua função jogar_partida() do Poisson em tempo real
                for _ in range(1000):
                    g_a, g_b = jogar_partida(match['t1'], match['t2'], mata_mata=False)
                    if g_a > g_b: vitorias_t1 += 1
                    elif g_b > g_a: vitorias_t2 += 1
                    else: empates += 1
                
                st.success(f"🔮 Probabilidades: {match['t1']} {vitorias_t1/10:.1f}% | Empate {empates/10:.1f}% | {match['t2']} {vitorias_t2/10:.1f}%")
                
        st.write("---")
