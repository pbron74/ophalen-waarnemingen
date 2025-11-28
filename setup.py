from setuptools import setup

APP = ['main_menu.pyw']  # jouw hoofdscript
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'Aziatische Hoornaar.icns',
    'packages': [
        'tkinter',
        'logging',
        'clustering',
        'vallenplan',
        'scrape_en_exporteer'
    ],
    'resources': ['config.py'],  # bundel config mee
    'plist': {
        'CFBundleName': 'AHlauncher',
        'CFBundleShortVersionString': '0.1.0',
        'CFBundleVersion': '0.1.0',
        'CFBundleIdentifier': 'nl.paul.ahlauncher'
    }
}

setup(
    name='AHlauncher',
    version='0.1.0',
    description='Clustering GUI launcher for ecological fieldwork',
    author='Paul',
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
