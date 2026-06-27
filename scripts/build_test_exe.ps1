$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path -Parent $PSScriptRoot
Set-Location $ProjectRoot

.\.venv\Scripts\python -m pip install -r requirements-build.txt
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

.\.venv\Scripts\pyinstaller --clean --noconfirm cliniss_test.spec
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

Write-Host "Ready: dist\cliniss-tests.exe"
