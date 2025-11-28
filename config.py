# config.py
import os, sys

def get_data_folder():
    # Als het een gebundelde executable is (PyInstaller)
    if getattr(sys, 'frozen', False):
        base_dir = os.path.dirname(sys.executable)
    else:
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

DATA_DIR = get_data_folder()