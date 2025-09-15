@echo off
setlocal
cd /d "C:\Users\PCX\Desktop\sanalyzer"
call ".venv\Scripts\activate.bat"
REM Konsolsuz çalıştır: venv içindeki pythonw.exe ile gui.py
start "" ".\.venv\Scripts\pythonw.exe" "gui.py"
exit /b
