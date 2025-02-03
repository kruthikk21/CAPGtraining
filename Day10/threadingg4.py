import queue
import threading
import time
def producer(q):
    for i in range(10):
        q.put(i)
        print(f"Produced {i}")
        q.put(None)
def consumer(q):
    while True:
        data=q.get()
        if data is None:
            break
        print(f"Consumed {data}")
        q.task_done()
        time.sleep(2)
q=queue.Queue()
producer_thread=threading.Thread(target=producer,args=(q,))
consumer_thread=threading.Thread(target=consumer,args=(q,))
producer_thread.start()
consumer_thread.start()
producer_thread.join()
consumer_thread.join()
print(q.qsize())
print("Exited")