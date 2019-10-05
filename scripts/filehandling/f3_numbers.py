# WAP to write numbers from 1-20 in separate lines in a file 'numbers.txt'

f = open('numbers.txt', 'a')

for i in range(1,21):
    print(i*10, file  = f)
    
f.close()