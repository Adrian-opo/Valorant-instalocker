import streamlit as st

# Configuração DEVE ser a primeira coisa
st.set_page_config(
    page_title="VALORANT Instalocker",
    page_icon="🎮",
    layout="wide"
)

# Inicialização do estado - forma mais robusta
def init_state():
    try:
        if not hasattr(st.session_state, 'initialized'):
            st.session_state.selected_agents = []
            st.session_state.is_running = False
            st.session_state.initialized = True
    except:
        pass

init_state()

# CSS
st.markdown("""
<style>
.stApp {
    background: #0f1923;
}
h1, h2, h3 {
    color: #ff4655 !important;
}
.agent-card {
    background: #1e2328;
    border: 2px solid #3a3f45;
    border-radius: 12px;
    padding: 15px;
    text-align: center;
}
.agent-card:hover {
    border-color: #ff4655;
}
.stButton>button {
    background: #ff4655;
    color: white;
    border: none;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

# Header
st.title("VALORANT INSTALOCKER")
st.write("Selecione seus agentes preferidos")

# Agentes
AGENTS = ["Jett", "Reyna", "Raze", "Phoenix", "Yoru", "Neon",
          "Brimstone", "Viper", "Omen", "Astra", "Harbor",
          "Sova", "Breach", "Skye", "KAY/O", "Fade", "Gekko",
          "Sage", "Cypher", "Killjoy", "Chamber", "Deadlock"]

# Usar checkbox simples em vez de session_state complexo
st.write("### Selecione os agentes:")
cols = st.columns(7)
selected = []

for idx, agent in enumerate(AGENTS):
    with cols[idx % 7]:
        if st.checkbox(agent, key=f"agent_{idx}"):
            selected.append(agent)

if selected:
    st.write(f"Agentes selecionados: {', '.join(selected)}")
    
    if st.button("🔒 LOCK NOW!", type="primary"):
        st.success(f"Tentando lockar: {selected[0]}")
else:
    st.info("Selecione pelo menos um agente")

st.write("---")
st.caption("VALORANT Instalocker v1.0")
