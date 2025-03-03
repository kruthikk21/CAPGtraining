import threading
import time
data=[
    list[range(20000)],
    list[range(20000,40000)]
    list[range(40000,50000)]

]
def processing(data):
    print(f"processing{data}")