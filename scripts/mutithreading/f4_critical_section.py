import threading

lck  = threading.RLock()
counter = 0

def funct(n):
    global counter
    for i in range(n):
        lck.acquire()
        lck.acquire()
        counter += 1
        lck.release()
        lck.release()
        #print(threading.current_thread().name ,counter)
    
t1 = threading.Thread(target = funct, args = (100000,))
t2 = threading.Thread(target = funct, args = (100000,))

t1.start()
t2.start()

t1.join()
t2.join()

print(counter)