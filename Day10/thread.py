import threading
import time

def threadd():
    print("thread started")
    time.sleep(2)
    print("thread stopped")

threaddd1=threading.Thread(target=threadd)
threaddd1.start()
threaddd1.join()
print("exited")