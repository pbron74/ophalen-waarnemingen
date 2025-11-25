from setuptools import setup

APP = ['main_menu.py']  # hoofdscript
DATA_FILES = [('_internal', ['_internal/*'])]  # bundel interne map
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icon.icns',  # optioneel icoon voor macOS
    'packages': ['tkinter', 'logging']  # voeg gebruikte modules toe
}

setup(
    app=APP,
    name='AHlauncher',  # naam van de app
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
