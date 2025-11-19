from setuptools import setup

APP = ['meldingen_per_gemeente_distibutie.pyw']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': None,  # Voeg hier een .icns-bestand toe als je een app-icoon wilt
    'packages': ['tkinter', 'datetime', 'openpyxl', 'selenium', 'pandas', 're', 'glob'],
    'includes': ['xml.etree.ElementTree'],
    'plist': {
        'CFBundleName': 'Meldingen_per_gemeente',
        'CFBundleShortVersionString': '1.0.0',
        'CFBundleIdentifier': 'nl.Paul_Bron.meldingen_per_gemeente',
        'NSHighResolutionCapable': True
    }
}

setup(
    app=APP,
    name='Meldingen_per_gemeente',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)