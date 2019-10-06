with open('lines.txt', 'r') as f:
    s = f.read(10)

    print(f.tell())
    f.read(5)
    print(f.tell())