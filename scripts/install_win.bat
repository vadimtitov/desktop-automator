ECHO OFF
title Desktop Automator Installer
echo Installing Desktop Automator ...
python -m pip install pyinstaller
python -m pip install -r requirements.txt
pyinstaller --name desktop-automator --onefile src\desktopautomator\__main__.py
PAUSE
