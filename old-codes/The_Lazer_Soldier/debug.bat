@echo off
title The Lazer Soldier -- By Ihsan -- DEBUG MODE

:main1

set /p lazerint="lazerInt: "
set /p dinamitint="dinamitInt: "

python main.py dbg_mode %lazerint% %dinamitint%
python3 main.py dbg_mode %lazerint% %dinamitint%
choice /c YT /m "\nRESTART?? "
goto main%ERRORLEVEL%

:main2

:main0