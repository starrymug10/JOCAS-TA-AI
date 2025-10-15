import threading
from jocasta_wake import WakeListener
from jocasta_main import run_once

def run_service():
    listener = WakeListener()
    while True:
        listener.listen()
        run_once()

if __name__ == "__main__":
    t = threading.Thread(target=run_service)
    t.start()
    t.join()
