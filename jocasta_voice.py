import speech_recognition as sr
import pyttsx3
import asyncio
import edge_tts
import playsound

engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text, realistic=False):
    print(f"JOCAS﻿TA: {text}")
    if realistic:
        voice = "id-ID-ArdiNeural"
        asyncio.run(edge_tts.Communicate(text, voice=voice).save("temp.mp3"))
        playsound.playsound("temp.mp3")
    else:
        engine.say(text)
        engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Mendengarkan...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language='id-ID').lower()
        print("🗣️ Kamu:", command)
        return command
    except:
        return ""
