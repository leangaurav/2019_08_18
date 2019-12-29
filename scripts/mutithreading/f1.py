import threading

print(dir(threading))

print(threading.current_thread())

def print_nums():
    for i in range(100):
        print(i)