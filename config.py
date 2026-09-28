import os
import sys

def resource_path(relative_path: str) -> str:
    """
    Geeft het absolute pad naar een resource in een PyInstaller bundel.
    Werkt op Windows, macOS en tijdens development.
    """
    # PyInstaller bundel
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)

    # Normale Python run
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, relative_path)


def get_data_folder() -> str:
    """
    Map voor schrijfbare data.
    In PyInstaller: gebruik lokale data-map naast de EXE.
    In development: gebruik ./data
    """
    if hasattr(sys, '_MEIPASS'):
        # Schrijfbare map naast de EXE
        exe_dir = os.path.dirname(sys.executable)
        data_dir = os.path.join(exe_dir, "data")
        os.makedirs(data_dir, exist_ok=True)
        return data_dir

    # Development mode
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
    os.makedirs(data_dir, exist_ok=True)
    return data_dir


# JSON-bestand lezen
GEMEENTEN_FILE = resource_path('data/gemeenten.json')

# Schrijfbare map
DATA_DIR = get_data_folder()
