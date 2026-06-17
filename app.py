import streamlit as st

# Configuração da página (obrigatória em primeiro lugar)
st.set_page_config(page_title="WC Prediction Engine", page_icon="🏆", layout="wide")

# Cabeçalho do Painel
st.markdown("<p style='text-align: center; color: #34d399; font-weight: bold; margin-bottom: 0;'>● SIMULATION MODEL ACTIVE</p>", unsafe_allowed_html=True)
st.markdown("<h1 style='text-align: center; color: #facc15; font-size: 3rem; margin-bottom: 0; font-family: sans-serif;'>2026 World Cup</h1>", unsafe_allowed_html=True)
st.markdown("<h1 style='text-align: center; color: #111827; font-size: 3rem; margin-top: 0; font-family: sans-serif;'>Predictor</h1>", unsafe_allowed_html=True)
st.markdown("<p style='text-align: center; color: #4b5563;'>Powered by ELO-based probabilistic simulation model</p>", unsafe_allowed_html=True)

# Botão de Simulação
col_b1, col_b2, col_b3 = st.columns([2, 1, 2])
with col_b2:
    st.button("▶ Run full tournament simulation", use_container_width=True)

st.write("---")
st.subheader("📈 Top Title Contenders")

# Dados das seleções favoritas
contenders = [
    {"pos": 1, "sigla": "ES", "nome": "Spain", "prob": 21.7, "elo": 2075, "cor": "#ef4444"},
    {"pos": 2, "sigla": "BR", "nome": "Brazil", "prob": 18.4, "elo": 2045, "cor": "#eab308"},
    {"pos": 3, "sigla": "FR", "nome": "France", "prob": 15.2, "elo": 2030, "cor": "#3b82f6"},
    {"pos": 4, "sigla": "AR", "nome": "Argentina", "prob": 12.8, "elo": 2020, "cor": "#06b6d4"},
    {"pos": 5, "sigla": "EN", "nome": "England", "prob": 8.6, "elo": 1995, "cor": "#a855f7"},
]

# Renderização das barras horizontais do seu protótipo
for c in contenders:
    col_info, col_bar, col_num = st.columns([2, 5, 1])
    with col_info:
        st.markdown(f"<div style='margin-top: 5px;'><b>{c['pos']}</b> &nbsp;&nbsp; <span style='color:#6b7280;'>{c['sigla']}</span> &nbsp;&nbsp; <b>{c['nome']}</b></div>", unsafe_allowed_html=True)
    with col_bar:
        # Barra customizada usando HTML puro para ficar igual ao seu design
        st.markdown(f"""
            <div style='background-color: #e5e7eb; border-radius: 10px; height: 16px; width: 100%; margin-top: 8px;'>
                <div style='background-color: {c["cor"]}; height: 16px; border-radius: 10px; width: {c["prob"] * 4}%;'></div>
            </div>
        """, unsafe_allowed_html=True)
    with col_num:
        st.markdown(f"<div style='text-align: right;'><b>{c['prob']}%</b><br><span style='font-size: 0.75rem; color:#9ca3af;'>ELO {c['elo']}</span></div>", unsafe_allowed_html=True)

st.write("---")

# Cards de Estatísticas no Rodapé
c1, c2, c3 = st.columns(3)
with c1:
    st.metric(label="🏆 Teams Analyzed", value="48")
with c2:
    st.metric(label="⚡ Simulations Run", value="100K+")
with c3:
    st.metric(label="📈 Model Accuracy", value="87.3%")
