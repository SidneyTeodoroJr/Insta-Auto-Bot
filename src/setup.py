import os
import sys
from cx_Freeze import setup, Executable

# Caminho para os assets (imagens)
assets_path = os.path.join("assets")

# Verificando o diretório correto para o sistema operacional
if sys.platform == "win32":
    # Diretório de arquivos adicionais no Windows
    include_files = [
        os.path.join("modules", "image_search.py"),  # Incluindo o módulo image_search.py
        assets_path,  # Incluindo os assets (imagens)
    ]
else:
    # Em outros sistemas operacionais, você pode querer ajustar os caminhos ou incluir outros arquivos
    include_files = [
        os.path.join("modules", "image_search.py"),
        assets_path,
    ]

# Configuração do executável (APP)
build_exe_options = {
    "packages": ["cv2", "pyautogui", "pynput", "cv2"],
    "include_files": include_files,  # Usando o caminho ajustado
}

# Configuração do setup
setup(
    name="InstaAutoBot",
    version="2.0",
    description="Automação que interage no Instagram de forma autônoma.",
    options={"build_exe": build_exe_options},
    executables=[Executable(
        os.path.join("main.py"), 
        base="Win32GUI",  # Para GUI no Windows
        target_name="InstaBot.exe",  # Nome do arquivo final
    )]
)