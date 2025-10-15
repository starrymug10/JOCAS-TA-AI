@echo off
title Installing JOCAS﻿TA AI
color 0a
echo ==============================================
echo         Installing JOCAS﻿TA - Hybrid AI
echo ==============================================
echo.

:: Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo Python belum terinstal. Membuka situs unduhan...
    start https://www.python.org/downloads/
    pause
    exit
)

echo Menginstal dependensi utama...
pip install --upgrade pip
pip install pyttsx3 SpeechRecognition pyautogui openai pyaudio requests playsound edge-tts pvporcupine

echo.
echo Instalasi selesai!
echo Menambahkan JOCAS﻿TA ke startup Windows...
copy "%~dp0\jocasta_service.py" "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\jocasta_service.py" >nul

echo Menjalankan JOCAS﻿TA untuk pertama kali...
python jocasta_service.py
pause
