# -*- mode: python ; coding: utf-8 -*-

import os
import selenium

block_cipher = None

selenium_path = os.path.dirname(selenium.__file__)

a = Analysis(
    ['main_menu.pyw'],
    pathex=[],
    binaries=[],
    datas=[
        ('data/gemeenten.json', 'data'),
        ('Aziatische Hoornaar.ico', '.'),
        ('config.py', '.'),
        (selenium_path, 'selenium'),
    ],
    hiddenimports=[
        'tkinter',
        'logging',
        'scrape_en_exporteer',
        'clustering',
        'vallenplan',
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
    icon='Aziatische Hoornaar.ico'
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

