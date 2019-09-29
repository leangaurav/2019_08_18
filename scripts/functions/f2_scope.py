x = 100 # global
def funct():
    x = 10 # local 
    print('Function : ', x)

print(x)
funct()
print(x)