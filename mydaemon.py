import time
import threading
import logging

logging.basicConfig(level=logging.INFO)

def daemon_task():
    while True:
        logging.info("Daemon is doing its job...")
        time.sleep(10)

def start_daemon():
    thread = threading.Thread(target=daemon_task, daemon=True)
    thread.start()
    logging.info("Daemon started in background.")

if __name__ == "__main__":
    start_daemon()
    while True:
        time.sleep(1)  # keep the main thread alive
