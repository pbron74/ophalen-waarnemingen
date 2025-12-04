# config.py
import os
import sys

def resource_path(relative_path: str) -> str:
    """
    Geeft het absolute pad naar een resource in de PyInstaller bundel.
    Werkt zowel via Finder als via Terminal.
    """
    if getattr(sys, 'frozen', False):
        # macOS app-bundle: Resources directory
        base_dir = os.path.dirname(sys.executable)
        resources_dir = os.path.abspath(os.path.join(base_dir, '..', 'Resources'))
        return os.path.join(resources_dir, relative_path)
    else:
        # Normale Python run → map naast dit bestand
        base_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base_dir, relative_path)

def get_data_folder() -> str:
    """
    Map voor schrijfbare data.
    Probeert eerst Resources/data, valt terug naar Documents als dat read-only is.
    """
    if getattr(sys, 'frozen', False):
        base_dir = os.path.dirname(sys.executable)
        resources_dir = os.path.abspath(os.path.join(base_dir, '..', 'Resources'))
        map_pad = os.path.join(resources_dir, 'data')
    else:
        map_pad = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

    # Als Resources/data niet schrijfbaar is → fallback naar Documents
    if not os.access(map_pad, os.W_OK):
        home = os.path.expanduser("~")
        map_pad = os.path.join(home, "Documents", "AHlauncher", "data")
        os.makedirs(map_pad, exist_ok=True)

    return map_pad

# ✅ Gebruik voor lezen van gemeenten.json
GEMEENTEN_FILE = resource_path('data/gemeenten.json')

# ✅ Gebruik voor schrijven van nieuwe bestanden
DATA_DIR = get_data_folder()