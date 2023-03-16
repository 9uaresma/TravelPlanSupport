@echo off
setlocal ENABLEDELAYEDEXPANSION
:: 環境変数 MyIP1, MyIP2, MyIP3... にIPアドレスを取得する

call :GET_IP_ADDRESSES

if defined MyIP1 nativefier "http://"%MyIP1%":3000" -n "TravelPlanSupport"

goto EOF


:GET_IP_ADDRESSES
set GET_IP_ADDRESSES_COUNT=1
for /f "usebackq delims=: tokens=2*" %%i in (`ipconfig.exe ^| findstr.exe /r /c:"IPv4 .*"`) do (
set MyIP=%%i
set MyIP!GET_IP_ADDRESSES_COUNT!=!MyIP: =!
set /a GET_IP_ADDRESSES_COUNT=!GET_IP_ADDRESSES_COUNT!+1
)
exit /b

:EOF