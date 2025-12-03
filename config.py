# config.py
import os, sys

def get_data_folder():
    """
    Bepaal een schrijfbare data-map voor AHlauncher.
    Werkt zowel in development als in gebundelde macOS/Windows builds.
    """
    if hasattr(sys, '_MEIPASS'):
        # ✅ PyInstaller runtime map (_internal)
        base_dir = sys._MEIPASS
    elif getattr(sys, 'frozen', False):
        # Gebundelde executable zonder _MEIPASS
        base_dir = os.path.dirname(sys.executable)
    else:
        # Gewone Python run of py2app
        base_dir = os.path.dirname(os.path.abspath(__file__))

    # Standaard data-map naast script/_MEIPASS
    map_pad = os.path.join(base_dir, "data")

    try:
        os.makedirs(map_pad, exist_ok=True)
    except PermissionError:
        # ✅ Fall-back naar Documents als installer-map read-only is
        home = os.path.expanduser("~")
        map_pad = os.path.join(home, "Documents", "AHlauncher", "data")
        os.makedirs(map_pad, exist_ok=True)

    return map_pad

# Globale variabele die je overal kunt importeren
DATA_DIR = get_data_folder()
