import streamlit as st

# Configuração inicial obrigatória
st.set_page_config(page_title="Copa 2026", page_icon="🏆")

# Título na tela
st.title("🏆 2026 World Cup Predictor")
st.subheader("O app está funcionando oficialmente!")
st.write("Se você está vendo isso, o bug foi derrotado!")

st.markdown("---")

# Cards simples de teste
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Simulações", value="100K+")
with col2:
    st.metric(label="Status", value="Online")
