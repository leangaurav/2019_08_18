with open('temp.txt', 'w') as f:
    f.write('abc')
    input('1')
    f.write('pqr')
    f.flush()
    input('2')
    f.write('xyz')
    input('3')