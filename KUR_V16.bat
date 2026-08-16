@echo off
setlocal
chcp 65001 >nul
title Gobekli Tepe v1.6 Kur

set "ROOT=%~dp0"
set "GAME=C:\Program Files (x86)\cs16v2017_oyunyoneticisi"
set "CSTRIKE=%GAME%\cstrike"

echo.
echo GOBEKLI TEPE v1.6 KURULUYOR...
echo.

if not exist "%ROOT%cstrike\maps\fy_gobeklitepe_v16.bsp" (
  echo HATA: Artifact klasor yapisi bozulmus.
  echo cstrike\maps\fy_gobeklitepe_v16.bsp bulunamadi.
  pause
  exit /b 1
)

if not exist "%CSTRIKE%" (
  echo HATA: CS yolu bulunamadi:
  echo %CSTRIKE%
  pause
  exit /b 2
)

if not exist "%CSTRIKE%\maps" mkdir "%CSTRIKE%\maps"
if not exist "%CSTRIKE%\gfx\env" mkdir "%CSTRIKE%\gfx\env"

copy /y "%ROOT%cstrike\maps\fy_gobeklitepe_v16.bsp" "%CSTRIKE%\maps\fy_gobeklitepe_v16.bsp"
copy /y "%ROOT%cstrike\maps\fy_gobeklitepe_v16.res" "%CSTRIKE%\maps\fy_gobeklitepe_v16.res"
copy /y "%ROOT%cstrike\gfx\env\gobekli16*.tga" "%CSTRIKE%\gfx\env\"

if errorlevel 1 (
  echo.
  echo Kopyalama engellendi.
  echo BAT dosyasina sag tiklayip YONETICI OLARAK CALISTIR.
  pause
  exit /b 3
)

echo.
echo BSP + RES + 6 SKYBOX DOSYASI KURULDU.
echo CS aciliyor...
start "" "%GAME%\hl.exe" -steam -game cstrike -console +map fy_gobeklitepe_v16
pause
