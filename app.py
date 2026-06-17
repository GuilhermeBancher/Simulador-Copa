import streamlit as st
import time

# Configuração da página (Obrigatória em primeiro lugar)
st.set_page_config(
    page_title="WC Prediction Engine", 
    page_icon="🏆", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilização CSS Inteligente com o Troféu em Fade no Fundo do Site
st.markdown("""
    <style>
    /* Injeta o troféu da Copa do Mundo como marca d'água no fundo do app */
    .stApp {
        background-image: linear-gradient(rgba(11, 15, 25, 0.95), rgba(11, 15, 25, 0.95)), 
                          url('https://images.unsplash.com/photo-1508098682722-e99c43a406b2?q=80&w=1000&auto=format&fit=crop');
        background-size: cover;
        background-position: center top;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    
    /* Configuração de espaçamento e reset */
    .block-container { padding-top: 2rem; padding-bottom: 2rem; }
    
    /* Badges de Categoria (FAVORITE / CONTENDER) */
    .badge-favorite {
        background-color: rgba(234, 179, 8, 0.15);
        color: #eab308;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 0.7rem;
        font-weight: bold;
        text-transform: uppercase;
        border: 1px solid rgba(234, 179, 8, 0.3);
        margin-left: 10px;
    }
    .badge-contender {
        background-color: rgba(59, 130, 246, 0.15);
        color: #3b82f6;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 0.7rem;
        font-weight: bold;
        text-transform: uppercase;
        border: 1px solid rgba(59, 130, 246, 0.3);
        margin-left: 10px;
    }
    
    /* Customização das estatísticas do rodapé (Cards translúcidos para combinar com o fundo) */
    div[data-testid="stMetric"] {
        background-color: rgba(17, 24, 39, 0.7);
        backdrop-filter: blur(8px);
        border: 1px solid #1f2937;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
    }
    div[data-testid="stMetricLabel"] {
        color: #9ca3af !important;
        font-size: 0.85rem !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    div[data-testid="stMetricValue"] {
        color: #ffffff !important;
        font-size: 2.2rem !important;
        font-weight: 700 !important;
    }
    </style>
""", unsafe_allowed_html=True)

# ==============================================================================
# HERO SECTION (IMAGEM 1)
# ==============================================================================

# Status ativo em linha única segura
st.markdown("<p style='text-align: center; color: #10b981; font-weight: bold; letter-spacing: 0.1em; font-size: 0.85rem; margin-bottom: 0;'>🟢 SIMULATION MODEL ACTIVE</p>", unsafe_allowed_html=True)

# Títulos principais usando formatação linear anti-bugs
st.markdown("<h1 style='text-align: center; color: #facc15; font-size: 4rem; font-weight: 800; margin-bottom: 0; line-height: 1; font-family: sans-serif;'>2026 World Cup</h1>", unsafe_allowed_html=True)
st.markdown("<h1 style='text-align: center; color: #ffffff; font-size: 4rem; font-weight: 800; margin-top: 0; line-height: 1.1; font-family: sans-serif;'>Predictor</h1>", unsafe_allowed_html=True)
st.markdown("<p style='text-align: center; color: #9ca3af; font-size: 1.1rem; margin-top: 15px;'>Powered by ELO-based probabilistic simulation model</p>", unsafe_allowed_html=True)
st.markdown("<p style='text-align: center; color: #4b5563; font-size: 0.85rem; margin-top: -10px;'>100,000+ match simulations • Real-time recalibration</p>", unsafe_allowed_html=True)

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

# ==============================================================================
# TOP TITLE CONTENDERS SECTION (IMAGEM 2)
# ==============================================================================
st.markdown("### 📈 Top Title Contenders")

# Estrutura de dados das top 5 seleções
contenders = [
    {"pos": 1, "sigla": "ES", "nome": "Spain", "status": "FAVORITE", "prob": 21.7, "elo": 2075, "cor": "#f59e0b"},
    {"pos": 2, "sigla": "BR", "nome": "Brazil", "status": "FAVORITE", "prob": 18.4, "elo": 2045, "cor": "#0ea5e9"},
    {"pos": 3, "sigla": "FR", "nome": "France", "status": "CONTENDER", "prob": 15.2, "elo": 2030, "cor": "#ec4899"},
    {"pos": 4, "sigla": "AR", "nome": "Argentina", "status": "CONTENDER", "prob": 12.8, "elo": 2020, "cor": "#10b981"},
    {"pos": 5, "sigla": "EN", "nome": "England", "status": "CONTENDER", "prob": 8.6, "elo": 1995, "cor": "#a855f7"},
]

# Construção dos blocos horizontais lineares
for c in contenders:
    badge = "badge-favorite" if c["status"] == "FAVORITE" else "badge-contender"
    
    with st.container():
        col_team, col_progress, col_values = st.columns([2.5, 5, 1.2])
        
        with col_team:
            st.markdown(f"<div style='display: flex; align-items: center; margin-top: 8px;'><span style='color: #4b5563; font-weight: bold; width: 25px;'>{c['pos']}</span><span style='color: #ffffff; font-weight: bold; width: 35px; letter-spacing: 0.05em;'>{c['sigla']}</span><span style='color: #ffffff; font-weight: 600; margin-left: 5px;'>{c['nome']}</span><span class='{badge}'>{c['status']}</span></div>", unsafe_allowed_html=True)
            
        with col_progress:
            st.markdown(f"<div style='background-color: #1f2937; border-radius: 10px; height: 8px; width: 100%; margin-top: 18px;'><div style='background-color: {c['cor']}; height: 8px; border-radius: 10px; width: {c['prob'] * 4}%; max-width: 100%;'></div></div>", unsafe_allowed_html=True)
            
        with col_values:
            st.markdown(f"<div style='text-align: right; margin-top: 2px;'><span style='color: #ffffff; font-weight: bold; font-size: 1.1rem;'>{c['prob']}%</span><br><span style='color: #4b5563; font-size: 0.75rem; font-weight: bold;'>ELO <span style='color:#9ca3af;'>{c['elo']}</span></span></div>", unsafe_allowed_html=True)

st.markdown("<br><hr style='border-color: #1f2937;'><br>", unsafe_allowed_html=True)

# ==============================================================================
# FOOTER METRICS (RODAPÉ DA IMAGEM 2)
# ==============================================================================
col_m1, col_m2, col_m3 = st.columns(3)

with col_m1:
    st.metric(label="🏆 Teams Analyzed", value="48")
with col_m2:
    st.metric(label="⚡ Simulations Run", value="100K+")
with col_m3:
    st.metric(label="📈 Model Accuracy", value="87.3%")
