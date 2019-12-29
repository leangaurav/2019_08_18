import threading

def print_nums(name):
    for i in range(100):
        print(name,":", i)
        
t1 = threading.Thread(target = print_nums, args = ("t1",))
t2 = threading.Thread(target = print_nums, args = ("t2",))

t1.start()
t2.start()

print("End")