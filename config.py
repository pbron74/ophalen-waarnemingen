import os
import sys

def get_data_folder():
    """
    Bepaal een schrijfbare data-map voor AHlauncher.
    Werkt zowel in development als in gebundelde macOS/Windows builds.
    """
    if getattr(sys, 'frozen', False):
        # PyInstaller bundel
        base_dir = os.path.dirname(sys.executable)
    elif hasattr(sys, '_MEIPASS'):
        # PyInstaller tijdelijke map
        base_dir = sys._MEIPASS
    else:
        # py2app bundel of gewone Python run
        base_dir = os.path.dirname(os.path.abspath(__file__))

    # Standaard data-map naast script/exe
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
