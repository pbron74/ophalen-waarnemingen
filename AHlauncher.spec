# -*- mode: python ; coding: utf-8 -*-

import os
import selenium

block_cipher = None

# Selenium-pad detecteren
selenium_path = os.path.dirname(selenium.__file__)

a = Analysis(
    ['main_menu.pyw'],
    pathex=[],
    binaries=[],

    # 📦 Alle data-bestanden die mee moeten
    datas=[
        ('data/gemeenten.json', 'data'),
        ('AziatischeHoornaar.ico', '.'),
        ('config.py', '.'),
        (selenium_path, 'selenium'),
    ],

    # 🔧 Alle modules die PyInstaller moet bundelen
    hiddenimports=[
        'tkinter',
        'logging',

        # Scraping
        'scrape_en_exporteer',
        'scrape_en_exporteer.scraper',

        # Clustering
        'clustering',
        'clustering.clustering_logica',

        # Vallenplan
        'vallenplan',
        'vallenplan.vallenplan_logica',
    ],

    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='AHlauncher',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon='AziatischeHoornaar.ico'
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='AHlauncher'
)

