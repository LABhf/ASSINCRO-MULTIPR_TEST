
#  ASSINCRO-MULTIPR_TEST
# this should be a way to multi process exec

import time
import threading

def delay(a):
    time.sleep(a)

def do():
    print("Seconnd Thread executed!")
    for i in range(0, 100):
        print("2 thread counts, ",i)
        delay(0.01)

def main():
    our_thread = threading.Thread(target=do, name="SecondThread Dudee!")
    our_thread.start()

    print(threading.active_count())
    print(threading.enumerate())

    delay(0.5)

    print(threading.active_count())

    for i in range(0, 100):
        print("main thread counts slower...", i)
        delay(0.05)

    print(threading.active_count())
    print(threading.enumerate())

    print("Main final")


if (__name__ == "__main__"):
    main()
