x = 10
def funct():
    x = 100
    def inner1():
        x = 1000
        print('Inner1:', x)
    print(x)

print(x)
funct()