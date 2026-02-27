import os
import sys
import subprocess

def main():
    """Inicia o Streamlit como um processo separado"""
    
    # Pega o diretório onde o executável está
    if getattr(sys, 'frozen', False):
        # Se estiver rodando como EXE
        application_path = os.path.dirname(sys.executable)
    else:
        # Se estiver rodando como script
        application_path = os.path.dirname(os.path.abspath(__file__))
    
    # Caminho do app.py
    app_path = os.path.join(application_path, 'app.py')
    
    # Se app.py não existir, cria um simples
    if not os.path.exists(app_path):
        # Estamos rodando do EXE único, precisamos extrair
        import tempfile
        temp_dir = tempfile.mkdtemp()
        
        # Cria o app.py no temp
        app_content = '''import streamlit as st

st.set_page_config(page_title="VALORANT Instalocker", layout="wide")

st.title("VALORANT INSTALOCKER")
st.write("Escolha seu agente:")

agentes = ["Jett", "Reyna", "Raze", "Phoenix", "Brimstone", "Viper", "Omen", "Sage"]

for agente in agentes:
    if st.button(f"Selecionar {agente}"):
        st.success(f"Agente {agente} selecionado!")
'''
        app_path = os.path.join(temp_dir, 'app.py')
        with open(app_path, 'w') as f:
            f.write(app_content)
    
    # Comando para iniciar o Streamlit
    cmd = [
        sys.executable,
        '-m', 'streamlit',
        'run',
        app_path,
        '--server.headless', 'true',
        '--browser.serverAddress', 'localhost',
    ]
    
    print("Iniciando VALORANT Instalocker...")
    print(f"Abra o navegador em: http://localhost:8501")
    
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao iniciar: {e}")
        input("Pressione ENTER para sair...")
    except KeyboardInterrupt:
        print("\nEncerrando...")

if __name__ == "__main__":
    main()
