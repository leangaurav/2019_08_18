f = open('name.txt', 'w')
print(f)
print(dir(f))

for i in range(10):
    print('Gaurav', file = f)
    
f.close()