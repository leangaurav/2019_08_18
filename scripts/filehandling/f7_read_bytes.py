# context manager
with open('lines.txt', 'r') as f:
    print("Pointer: ", f.tell())
    s = f.read(10)
    print(repr(s) )
    print("Pointer: ", f.tell())
    s = f.read(10)
    print(repr(s) )
    print("Pointer: ", f.tell())