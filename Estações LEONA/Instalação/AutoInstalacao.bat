echo Pacote de instalacao Estacao LEONA

start /wait .\amcap.exe /S
start /wait .\arduino-1.8.2-windows.exe  /S
start /wait .\npp.7.4.2.Installer.x64  /S
start /wait .\ccsetup534.exe  /S
start /wait .\python-3.6.1-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

echo Fim da Instalação. Estação será reiniciada.

mkdir "%USERPROFILE%\Desktop\scripts"

copy "..\LEONA v3 Tornado\LEONA TORNADO v3.1\scripts" "%USERPROFILE%\Desktop\scripts"

mklink "C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\main.py" "%USERPROFILE%\Desktop\scripts\main.py"

shutdown.exe /r /t 00
