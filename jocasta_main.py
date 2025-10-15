from jocasta_voice import listen, speak
from jocasta_commands import execute

def run_once():
    speak("Halo, saya Jocasta. Siap membantu.", realistic=True)
    while True:
        cmd = listen()
        if "jocasta" in cmd:
            speak("Ya, saya di sini.", realistic=True)
            cmd2 = cmd.replace("jocasta", "").strip()
            execute(cmd2)
            break

if __name__ == "__main__":
    run_once()
