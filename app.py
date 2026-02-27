import streamlit as st
import requests
import json
import os
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="VALORANT Instalocker",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inicialização do session_state (DEVE vir antes de qualquer uso)
if 'selected_agents' not in st.session_state:
    st.session_state.selected_agents = []

if 'is_running' not in st.session_state:
    st.session_state.is_running = False

# CSS customizado para estilo VALORANT
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;600;700&display=swap');
    
    * {
        font-family: 'Rajdhani', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #0f1419 0%, #1a1f2e 50%, #0f1419 100%);
    }
    
    .stApp {
        background: #0f1923;
    }
    
    h1, h2, h3 {
        color: #ff4655 !important;
        font-weight: 700 !important;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    .agent-card {
        background: linear-gradient(145deg, #1e2328 0%, #2a2f35 100%);
        border: 2px solid #3a3f45;
        border-radius: 12px;
        padding: 15px;
        text-align: center;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .agent-card:hover {
        border-color: #ff4655;
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(255, 70, 85, 0.3);
    }
    
    .agent-card.selected {
        border-color: #ff4655;
        background: linear-gradient(145deg, #2a1f1f 0%, #3a2a2a 100%);
        box-shadow: 0 0 20px rgba(255, 70, 85, 0.5);
    }
    
    .agent-name {
        color: #fff;
        font-size: 14px;
        font-weight: 600;
        margin-top: 10px;
        text-transform: uppercase;
    }
    
    .agent-role {
        color: #8b9bb4;
        font-size: 11px;
        text-transform: uppercase;
    }
    
    .stButton>button {
        background: linear-gradient(90deg, #ff4655 0%, #ff6b7a 100%);
        color: white;
        border: none;
        padding: 15px 40px;
        font-size: 18px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 2px;
        border-radius: 8px;
        width: 100%;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 10px 30px rgba(255, 70, 85, 0.4);
    }
    
    .stButton>button:disabled {
        background: #3a3f45;
        color: #666;
        cursor: not-allowed;
        transform: none;
        box-shadow: none;
    }
    
    .sidebar .sidebar-content {
        background: #1e2328;
    }
    
    .status-online {
        color: #00ff88;
        font-weight: 700;
    }
    
    .status-offline {
        color: #ff4655;
        font-weight: 700;
    }
    
    .duelist { border-top: 3px solid #ff4655; }
    .controller { border-top: 3px solid #8b5cf6; }
    .initiator { border-top: 3px solid #f59e0b; }
    .sentinel { border-top: 3px solid #10b981; }
    
    .valorant-header {
        text-align: center;
        padding: 20px 0;
        margin-bottom: 30px;
        border-bottom: 2px solid #ff4655;
    }
    
    .valorant-header h1 {
        font-size: 48px !important;
        margin: 0;
        text-shadow: 0 0 20px rgba(255, 70, 85, 0.5);
    }
    
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #0f1419;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #3a3f45;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #ff4655;
    }
    </style>
    """, unsafe_allow_html=True)

# Dados dos agentes
AGENTS = {
    "Jett": {"role": "Duelist", "color": "#ff4655"},
    "Reyna": {"role": "Duelist", "color": "#ff4655"},
    "Raze": {"role": "Duelist", "color": "#ff4655"},
    "Phoenix": {"role": "Duelist", "color": "#ff4655"},
    "Yoru": {"role": "Duelist", "color": "#ff4655"},
    "Neon": {"role": "Duelist", "color": "#ff4655"},
    "Brimstone": {"role": "Controller", "color": "#8b5cf6"},
    "Viper": {"role": "Controller", "color": "#8b5cf6"},
    "Omen": {"role": "Controller", "color": "#8b5cf6"},
    "Astra": {"role": "Controller", "color": "#8b5cf6"},
    "Harbor": {"role": "Controller", "color": "#8b5cf6"},
    "Sova": {"role": "Initiator", "color": "#f59e0b"},
    "Breach": {"role": "Initiator", "color": "#f59e0b"},
    "Skye": {"role": "Initiator", "color": "#f59e0b"},
    "KAY/O": {"role": "Initiator", "color": "#f59e0b"},
    "Fade": {"role": "Initiator", "color": "#f59e0b"},
    "Gekko": {"role": "Initiator", "color": "#f59e0b"},
    "Sage": {"role": "Sentinel", "color": "#10b981"},
    "Cypher": {"role": "Sentinel", "color": "#10b981"},
    "Killjoy": {"role": "Sentinel", "color": "#10b981"},
    "Chamber": {"role": "Sentinel", "color": "#10b981"},
    "Deadlock": {"role": "Sentinel", "color": "#10b981"},
}

def get_agent_image_url(agent_name):
    uuids = {
        "Jett": "add6443a-41bd-e414-f6ad-e58d267f4e95",
        "Reyna": "a3bfb853-43b2-7238-a4f1-ad90e9e46bcc",
        "Raze": "f94c3b30-42be-e959-889c-5aa313dba261",
        "Phoenix": "eb93336a-449b-9c1b-0a54-a891f7921d69",
        "Yoru": "7f94d92c-4234-0a36-9646-3a87eb8b5c89",
        "Neon": "bb2a4828-46eb-8cd1-e765-15848195d751",
        "Brimstone": "9f0d8ba9-4140-b941-57d3-a7ad57c6b417",
        "Viper": "707eab51-4836-f488-046a-cda6bf494859",
        "Omen": "8e253930-4c05-31dd-1b6c-968525494517",
        "Astra": "41fb69c1-4189-7b37-f117-bcaf1e96f1bf",
        "Harbor": "95b78ed7-4637-86d9-7e41-71ba8c293152",
        "Sova": "320b2a48-4d9b-a075-30f1-1f93a9b638fa",
        "Breach": "5f8d3a7f-467b-97f3-062c-13acf203c006",
        "Skye": "6f2a04ca-43e0-be17-7f36-b3908627744d",
        "KAY/O": "601dbbe7-43ce-be57-2a40-4abd24953621",
        "Fade": "dade69b4-4f1a-ab8f-6b5a-9e3e8b7c2c1f",
        "Gekko": "e370fa57-4757-3604-3648-499e1f642d3f",
        "Sage": "569fdd95-4d10-43ab-ca70-79becc718b46",
        "Cypher": "117ed9e3-49f3-6512-3ccf-0cada7e3823b",
        "Killjoy": "1e58de9c-4950-5125-93e9-a0aee9f98746",
        "Chamber": "22697a3d-45bf-8dd7-4fec-84a9e28c69d7",
        "Deadlock": "cc8b64c8-4b25-4ff9-6e7f-3f8e9d2c1a5b",
    }
    uuid = uuids.get(agent_name, "")
    return f"https://media.valorant-api.com/agents/{uuid}/displayicon.png"

# Inicialização
load_css()

# Header
st.markdown("""
<div class="valorant-header">
    <h1>VALORANT INSTALOCKER</h1>
    <p>Selecione seus agentes preferidos e deixe o instalocker fazer o resto</p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### ⚙️ Configurações")
    
    delay = st.slider(
        "⏱️ Delay (ms)",
        min_value=0,
        max_value=500,
        value=100,
        step=10
    )
    
    st.markdown("### 🎮 Modo")
    mode = st.radio(
        "",
        ["🔒 Insta-Lock", "👆 Pick Only", "🎯 Smart"]
    )

# Main content
tabs = st.tabs(["🎮 Agentes", "⚡ Quick Lock", "📊 Estatísticas"])

with tabs[0]:
    st.markdown("### Selecione seus agentes preferidos")
    
    roles = ["Duelist", "Controller", "Initiator", "Sentinel"]
    
    for role in roles:
        st.markdown(f"#### {role}")
        agents_in_role = [(name, data) for name, data in AGENTS.items() if data["role"] == role]
        
        cols = st.columns(5)
        for idx, (agent_name, agent_data) in enumerate(agents_in_role):
            with cols[idx % 5]:
                is_selected = agent_name in st.session_state.selected_agents
                
                card_html = f"""
                <div class="agent-card {role.lower()} {'selected' if is_selected else ''}">
                    <img src="{get_agent_image_url(agent_name)}" 
                         style="width: 60px; height: 60px; object-fit: contain;"
                         onerror="this.style.display='none'">
                    <div class="agent-name" style="font-size: 12px;">{agent_name}</div>
                </div>
                """
                st.markdown(card_html, unsafe_allow_html=True)
                
                if st.button(
                    "✓" if is_selected else "+", 
                    key=f"btn_{agent_name}",
                    help=f"{'Remover' if is_selected else 'Adicionar'} {agent_name}"
                ):
                    if is_selected:
                        st.session_state.selected_agents.remove(agent_name)
                    else:
                        st.session_state.selected_agents.append(agent_name)
                    st.rerun()
    
    if st.session_state.selected_agents:
        st.markdown("### 📋 Ordem de Prioridade")
        for idx, agent in enumerate(st.session_state.selected_agents, 1):
            st.markdown(f"**#{idx}** {agent} - {AGENTS[agent]['role']}")

with tabs[1]:
    st.markdown("### ⚡ Quick Lock")
    
    if st.session_state.selected_agents:
        if st.button("🔒 LOCK NOW!", type="primary", use_container_width=True):
            st.success("Tentando lockar...")
    else:
        st.warning("Selecione agentes primeiro!")

with tabs[2]:
    st.markdown("### 📊 Estatísticas")
    st.info("Em breve...")

# Footer
st.markdown("""
<div style="text-align: center; padding: 20px; color: #8b9bb4; font-size: 12px; margin-top: 40px;">
    VALORANT Instalocker GUI v1.0
</div>
""", unsafe_allow_html=True)
