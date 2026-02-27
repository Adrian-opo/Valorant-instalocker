import PyInstaller.__main__
import os
import sys

def build_exe():
    """Compila o app.py para executavel .exe"""
    
    print("VALORANT Instalocker - Build Script")
    print("=" * 50)
    
    # Opcoes do PyInstaller
    args = [
        'app.py',                           # Script principal
        '--name=ValorantInstalocker',       # Nome do executavel
        '--onefile',                        # Arquivo unico
        '--windowed',                       # Sem console (GUI)
        '--clean',                          # Limpa cache
        '--noconfirm',                      # Nao confirma overwrite
        
        # Oculta imports do Streamlit
        '--hidden-import=streamlit',
        '--hidden-import=streamlit.runtime.scriptrunner',
        '--hidden-import=streamlit.runtime',
        '--hidden-import=streamlit.runtime.secrets',
        '--hidden-import=streamlit.runtime.state',
        '--hidden-import=streamlit.runtime.uploaded_file_manager',
        '--hidden-import=streamlit.runtime.media_file_manager',
        '--hidden-import=streamlit.runtime.legacy_caching',
        '--hidden-import=streamlit.runtime.caching',
        '--hidden-import=streamlit.runtime.forward_msg_queue',
        '--hidden-import=streamlit.runtime.fragment',
        '--hidden-import=streamlit.runtime.memory_media_file_storage',
        '--hidden-import=streamlit.runtime.memory_uploaded_file_manager',
        '--hidden-import=streamlit.runtime.pages_manager',
        '--hidden-import=streamlit.runtime.runtime',
        '--hidden-import=streamlit.runtime.session_manager',
        '--hidden-import=streamlit.runtime.websocket_session_manager',
        '--hidden-import=streamlit.elements',
        '--hidden-import=streamlit.elements.lib',
        '--hidden-import=streamlit.elements.lib.policies',
        '--hidden-import=streamlit.elements.lib.column_types',
        '--hidden-import=streamlit.proto',
        '--hidden-import=streamlit.proto.RootContainer_pb2',
        '--hidden-import=streamlit.proto.BackMsg_pb2',
        '--hidden-import=streamlit.proto.Block_pb2',
        '--hidden-import=streamlit.proto.Arrow_pb2',
        '--hidden-import=streamlit.proto.ArrowNamedDataset_pb2',
        '--hidden-import=streamlit.proto.Balloons_pb2',
        '--hidden-import=streamlit.proto.Snow_pb2',
        '--hidden-import=altair',
        '--hidden-import=pandas',
        '--hidden-import=numpy',
        '--hidden-import=PIL',
        '--hidden-import=requests',
    ]
    
    print("\nIniciando build...")
    print("Isso pode levar alguns minutos...\n")
    
    try:
        PyInstaller.__main__.run(args)
        
        print("\n" + "=" * 50)
        print("BUILD CONCLUIDO!")
        print("=" * 50)
        print("\nExecutavel gerado em:")
        print("   dist/ValorantInstalocker.exe")
        print("\nComo usar:")
        print("   1. Va para a pasta 'dist/'")
        print("   2. Execute 'ValorantInstalocker.exe'")
        print("   3. O navegador abrira automaticamente")
        
    except Exception as e:
        print(f"\nErro no build: {e}")
        sys.exit(1)

if __name__ == "__main__":
    build_exe()
