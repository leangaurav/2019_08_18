x = 10
def funct():
    x = 100
    def inner1():
        nonlocal x
        #x = 1000
        print('Inner1:', x)
    inner1()
    print('funct ', x)

print(x)
funct()