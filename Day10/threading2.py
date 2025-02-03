import threading
import time
def print_numbers():
    for i in range(1,6):
        print(i)
        time.sleep(4)
thread1=threading.Thread(target=print_numbers)
thread1.start()

def print_even():
    for i in range(1,50):
        if i%2==0:
            print("Even",i)
            time.sleep(2)
thread2=threading.Thread(target=print_even)
thread2.start()
thread2.join()
thread1.join()

print("exited")