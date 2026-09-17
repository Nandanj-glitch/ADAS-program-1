@echo off
cd /d "%~dp0"
C:\Python314\python.exe -m pip install -r requirements.txt
C:\Python314\python.exe headlight_detection.py
pause
