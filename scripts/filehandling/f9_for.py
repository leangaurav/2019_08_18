# context manager
with open('lines.txt', 'r') as f:
    print(dir(f))
    
    for data in f:
        print('Data:', data)