from cx_Freeze import setup, Executable, sys

# Lista de archivos adicionales (ejemplo: imágenes, fuentes, etc.)
# Si no tienes archivos adicionales, simplemente deja la lista vacía.

additional_files = [
    ("static/icon.ico", "static/icon.ico"),
    # (".env", ".env"),
]  # ruta original del archivo y ruta en la distribución final

build_options = {
    "packages": [
        "cryptography",
    ],  # Puedes añadir paquetes adicionales que no sean detectados automáticamente
    "excludes": [],  # Puedes excluir paquetes que no desees incluir
    "include_files": additional_files,
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

shortcut_table = [
    (
        "DesktopShortcut",  # Shortcut
        "DesktopFolder",  # Directory_
        "Malo Malísimo",  # Name
        "TARGETDIR",  # Component_
        "[TARGETDIR]\main.exe",  # Target
        None,  # Arguments
        None,  # Description
        None,  # Hotkey
        None,  # Icon
        None,  # IconIndex
        None,  # ShowCmd
        "TARGETDIR",  # WkDir
    )
]
msi_data = {"Shortcut": shortcut_table}
bdist_msi_options = {"data": msi_data}

setup(
    name="Malo Malisimo",
    version="1.0",
    author="David Castagneto Aguirre",
    description="Ransomware for beginners",
    options={
        "build_exe": build_options,
        "bdist_msi": bdist_msi_options,
    },
    executables=[
        Executable(script="main.py", base=base, icon="static/icon.ico")
    ],  # Punto de entrada de tu aplicación
)
