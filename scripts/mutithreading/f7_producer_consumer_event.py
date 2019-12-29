import threading
import time

a = []

lck = threading.Lock()
evt = threading.Event()

def producer():
    print("Producer started")
    for i in range(10):
        print("producer produced", i)
        a.append(i)
        evt.set()
        time.sleep(0.2)
        
    a.append(None)
    evt.set()
    print("Producer ended")


def consumer():
    name = threading.current_thread().name
    print("Consumer start", name)
    while True:
        with lck:
            if len(a) == 0:
                evt.wait() # blocking call
                evt.clear()

        data = a.pop()
        if data == None:
            a.append(None)
            evt.set()
            break
        print("Consumer", name, data)
    print("Consumer End", name)
    
t1 = threading.Thread(target = producer)
t2 = threading.Thread(target = consumer)
t3 = threading.Thread(target = consumer)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("End of main", a)
