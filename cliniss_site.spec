# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path
import sys

from PyInstaller.utils.hooks import collect_submodules


project_root = Path.cwd()
sys.path.insert(0, str(project_root))

datas = [
    (str(project_root / 'static'), 'static'),
    (str(project_root / 'templates'), 'templates'),
]

hiddenimports = []
for package in ('config', 'core', 'pages', 'content', 'leads'):
    hiddenimports += collect_submodules(package)

a = Analysis(
    [str(project_root / 'scripts' / 'run_site_bundle.py')],
    pathex=[str(project_root)],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='cliniss-site',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
