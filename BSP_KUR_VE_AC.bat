@echo off
setlocal
chcp 65001 >nul
title Gobekli Tepe BSP Kur

set "BSP=%~dp0fy_gobeklitepe_v12.bsp"
set "CSTRIKE=C:\Program Files (x86)\cs16v2017_oyunyoneticisi\cstrike"
set "HLROOT=C:\Program Files (x86)\cs16v2017_oyunyoneticisi"

echo.
echo GOBEKLI TEPE - HAZIR BSP KURULUMU
echo.

if not exist "%BSP%" (
    echo HATA: fy_gobeklitepe_v12.bsp bu BAT dosyasiyla ayni klasorde degil.
    echo GitHub Actions'tan indirdigin artifact ZIP'ini ac ve BSP'yi buraya koy.
    pause
    exit /b 1
)

if not exist "%CSTRIKE%\maps" (
    echo HATA: CS maps klasoru bulunamadi:
    echo %CSTRIKE%\maps
    pause
    exit /b 2
)

copy /y "%BSP%" "%CSTRIKE%\maps\fy_gobeklitepe_v12.bsp"
if errorlevel 1 (
    echo.
    echo Kopyalama basarisiz. BAT dosyasina sag tiklayip
    echo "Yonetici olarak calistir" ile tekrar dene.
    pause
    exit /b 3
)

echo.
echo Harita kuruldu:
echo %CSTRIKE%\maps\fy_gobeklitepe_v12.bsp
echo.

if exist "%HLROOT%\hl.exe" (
    start "" "%HLROOT%\hl.exe" -steam -game cstrike -console +map fy_gobeklitepe_v12
) else (
    echo CS'yi ac ve konsola:
    echo map fy_gobeklitepe_v12
)
pause
