# context manager
with open('lines.txt', 'r') as f:
    print("Pointer: ", f.tell())
    
    s = f.read(10)
    
    while s:
        print(repr(s) )
        s = f.read(10)
    
    f.seek(0)
    print("Reading again: " , f.read(10))