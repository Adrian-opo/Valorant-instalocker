import PyInstaller.__main__
import sys

def build_exe():
    print("VALORANT Instalocker - Build Script")
    print("=" * 50)
    
    args = [
        'app.py',
        '--name=ValorantInstalocker',
        '--onefile',
        '--windowed',
        '--clean',
        '--noconfirm',
        
        # Collect all streamlit
        '--collect-all', 'streamlit',
        '--collect-all', 'altair',
        '--collect-all', 'pandas',
        '--collect-all', 'numpy',
        '--collect-all', 'PIL',
        
        # Hidden imports
        '--hidden-import=importlib_metadata',
        '--hidden-import=streamlit.version',
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
        '--hidden-import=altair',
        '--hidden-import=pandas',
        '--hidden-import=numpy',
        '--hidden-import=PIL',
        '--hidden-import=requests',
        '--hidden-import=toml',
    ]
    
    print("\nIniciando build...")
    print("Isso pode levar alguns minutos...\n")
    
    try:
        PyInstaller.__main__.run(args)
        print("\nBUILD CONCLUIDO!")
        print("=" * 50)
        print("\nExecutavel: dist/ValorantInstalocker.exe")
        
    except Exception as e:
        print(f"\nErro: {e}")
        sys.exit(1)

if __name__ == "__main__":
    build_exe()
