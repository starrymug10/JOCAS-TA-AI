import os
import datetime
from jocasta_voice import speak

def execute(command):
    if "buka youtube" in command:
        speak("Baik, membuka YouTube.", realistic=True)
        os.system("start https://youtube.com")

    elif "jam berapa" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"Sekarang pukul {now}", realistic=True)

    elif "matikan komputer" in command:
        speak("Baik, mematikan sistem.", realistic=True)
        os.system("shutdown /s /t 5")

    elif "terima kasih" in command:
        speak("Sama-sama, senang membantu.", realistic=True)

    else:
        speak("Saya belum mengerti perintah itu, tapi saya akan belajar.", realistic=True)
