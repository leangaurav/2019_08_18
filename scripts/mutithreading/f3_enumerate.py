import threading

def print_nums(name):
    for i in range(100):
        print(name,":", i)
        
t1 = threading.Thread(target = print_nums, args = ("t1",))
t2 = threading.Thread(target = print_nums, args = ("t2",))

print(t1.name)
print(t2.name)
print(threading.current_thread().name)

t1.start()
t2.start()

#t1.join()
#t2.join()

for t in threading.enumerate():
    if t.name != "MainThread":
        t.join()

print("End")