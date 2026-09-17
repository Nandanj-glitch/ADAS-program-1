@echo off
setlocal
cd /d "%~dp0"
where code >nul 2>nul
if errorlevel 1 (
    echo VS Code command "code" was not found.
    echo Open VS Code and install/enable the "code" command, then run this file again.
    pause
    exit /b 1
)
code "ADAS-PROGRAM6-Finished.ipynb"
