import threading

lck  = threading.RLock()
counter = 0

def funct(n):
    global counter
    for i in range(n):
        with lck:
            counter += 1
        
t1 = threading.Thread(target = funct, args = (100000,))
t2 = threading.Thread(target = funct, args = (100000,))

t1.start()
t2.start()

t1.join()
t2.join()

print(counter)