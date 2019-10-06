# context manager
with open('lines.txt', 'r') as f:
    s = f.read() # read complete file data
    print(repr(s) )
    print("Before close ", f.closed)

print("After close ", f.closed)