f = open('lines.txt', 'r')

s = f.read() # read complete file data

print(repr(s) )

print("Before close ", f.closed)
f.close()
print("After close ", f.closed)