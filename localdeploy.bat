@echo off
rem obtaining addon name, the current directory name
for %%f in (%cd%) do set addon=%%~nxf
rem copying addon files to local nvda addon directory
robocopy /S addon %appdata%\nvda\addons\%addon%