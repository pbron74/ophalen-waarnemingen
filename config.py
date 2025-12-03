import os, sys

def get_data_folder():
    if hasattr(sys, '_MEIPASS'):
        base_dir = sys._MEIPASS
        # macOS bundel → Resources/data
        resources_dir = os.path.join(os.path.dirname(base_dir), "Resources", "data")
        if os.path.exists(resources_dir):
            return resources_dir
    elif getattr(sys, 'frozen', False):
        base_dir = os.path.dirname(sys.executable)
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_dir, "data")

DATA_DIR = get_data_folder()

