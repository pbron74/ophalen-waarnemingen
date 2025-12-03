# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main_menu.pyw'],   # hoofdscript
    pathex=[],
    binaries=[],
    datas=[
        # Bundel config.py mee (optioneel, meestal niet nodig omdat het al in de exe zit)
        ('config.py', '.'),

        # macOS icoon
        ('Aziatische Hoornaar.icns', '.'),

        # Gemeenten.json expliciet in Resources/data
        ('data/gemeenten.json', 'Resources/data'),
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
    console=False,  # windowed
    icon='Aziatische Hoornaar.icns'
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
