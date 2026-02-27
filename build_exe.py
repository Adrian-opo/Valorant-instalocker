import PyInstaller.__main__
import sys

def build_exe():
    print("VALORANT Instalocker - Build Script")
    print("=" * 50)
    
    args = [
        'main.py',                          # Entry point atualizado
        '--name=ValorantInstalocker',
        '--onefile',
        '--windowed',
        '--clean',
        '--noconfirm',
        
        # Inclui app.py como dado
        '--add-data=app.py;.',
        
        # Collect all
        '--collect-all', 'streamlit',
        '--collect-all', 'altair',
        '--collect-all', 'pandas',
        '--collect-all', 'numpy',
        '--collect-all', 'PIL',
        
        # Hidden imports
        '--hidden-import=importlib_metadata',
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
