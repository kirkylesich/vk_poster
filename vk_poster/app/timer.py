import time
from main import start


def start_timer():
    while True:
        start()
        time.sleep(30 * 60)


start_timer()
