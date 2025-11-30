# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main_menu.pyw'],   # jouw hoofdscript
    pathex=[],
    binaries=[],
    datas=[
        ('config.py', '.'),                # bundel config.py mee
        ('data/*', 'data'),                # bundel data-map (leeg of gevuld)
        ('Aziatische Hoornaar.icns', '.'), # bundel macOS icoon
    ],
    hiddenimports=['tkinter', 'logging', 'clustering', 'vallenplan', 'scrape_en_exporteer'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
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
    console=False,   # False = GUI-only, geen terminalvenster
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

app = BUNDLE(
    coll,
    name='AHlauncher.app',
    icon='Aziatische Hoornaar.icns',
    bundle_identifier='nl.paul.ahlauncher',
    info_plist={
        'CFBundleName': 'AHlauncher',
        'CFBundleShortVersionString': '0.1.0',
        'CFBundleVersion': '0.1.0',
        'CFBundleIdentifier': 'nl.paul.ahlauncher',
    }
)