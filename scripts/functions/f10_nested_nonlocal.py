x = 10
def funct():
    x = 100
    def inner1():
        x = -100
        def inner2():
            nonlocal x
            x = 10
            print('Inner2', x)
        inner2()
        print('Inner1:', x)
    inner1()
    print('funct ', x)

print(x)
funct()