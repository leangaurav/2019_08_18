import threading
import time
a = []

def producer():
    print("Producer started")
    for i in range(10):
        print("producer produced", i)
        a.append(i)
        time.sleep(0.2)
        
    a.append(None)
    print("Producer ended")


def consumer():
    name = threading.current_thread().name
    print("Consumer start", name)
    while True:
        while len(a) == 0:
            pass
        data = a.pop()
        if data == None:
            a.append(None)
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
