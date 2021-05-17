@echo off
title The Lazer Soldier -- By Ihsan

:main1
cls
python main.py
cls
echo Mau Main Lagi?
choice /c YT /m "Tulis Y untuk ya, atau T untuk tidak"
goto main%ERRORLEVEL%

:main2

:main0