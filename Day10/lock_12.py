import threading
import time
def task(lock):
    with lock:
        print("lock acquired")
        time.sleep(2)
        print("lock released")
lock=threading.Lock()
thread=[threading.Thread(target=task,args=(lock,))for _ in range(3))]
for t in thread:
    t.start()
for t in thread:
    t.join()
print("exited")

