import threading
import os

def fun():
    print("In fun")
    print(threading.current_thread().name)
    for i in range(5):
        print(i)
        
def mun():
    print("In mun")
    print(threading.current_thread().name)
    for i in range(5):
        print("In mun")
        
        
print(threading.current_thread().name)

thread1 = threading.Thread(target=fun)
thread2 = threading.Thread(target=mun)

thread1.start()
thread2.start()