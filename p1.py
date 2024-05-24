import threading
import os
for a in range(10):
    print(a)
    
print(os.getpid())
print(os.getcwd())
print(os.getppid())

print(threading.current_thread().name)
 