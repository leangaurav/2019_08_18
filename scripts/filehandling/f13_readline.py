with open('lines.txt', 'r') as f:
    s = f.readline()

    while s:
        print(s)
        s = f.readline()
        