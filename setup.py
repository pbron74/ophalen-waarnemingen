from setuptools import setup

APP = ['AHlauncher.py']  # jouw main script
DATA_FILES = [('_internal', ['_internal/*'])]  # bundel interne map
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icon.icns',  # optioneel
    'packages': ['tkinter', 'logging']  # voeg gebruikte modules toe
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
