from queue import Queue
import threading

q = Queue()

def producer():
    print("Producer started")
    for i in range(10):
        print("producer produced", i)
        q.put(i)
        
    q.put(None)
    print("Producer ended")


def consumer():
    name = threading.current_thread().name
    print("Consumer start", name)
    while True:
        data = q.get() # waits/blocking call
        if data == None:
            q.put(None)
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

print("End of main", q.qsize())
