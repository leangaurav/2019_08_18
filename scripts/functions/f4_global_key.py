x = 100 # global
def funct():
    global x
    x = 10 # local
    print('Function : ', x)

print(x)
funct()
print(x)