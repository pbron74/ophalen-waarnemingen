from setuptools import setup

APP = ['main_menu.py']  # jouw hoofdscript
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'Aziatische Hoornaar.icns',
    'packages': [
        'tkinter',
        'logging',
        'clustering',
        'vallenplan',
        'scrape_en_exporteer'
    ]
}

setup(
    app=APP,
    name='AHlauncher',
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
