# config.py
import os
import sys

def get_data_folder():
    if getattr(sys, 'frozen', False):
        # ✅ PyInstaller bundel: zoek in Contents/Resources
        base_dir = os.path.dirname(sys.executable)
        resources_dir = os.path.abspath(os.path.join(base_dir, '..', 'Resources'))
        map_pad = os.path.join(resources_dir, 'data')
    else:
        # ✅ Normale Python run → map naast dit bestand
        base_dir = os.path.dirname(os.path.abspath(__file__))
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

