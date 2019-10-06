# WAP to create a copy of file 'lines.txt' as 'lines_copy.txt' which changes all vowels to the number 0.

with open('lines.txt', 'r') as f1:
    with open('lines_copy.txt', 'w') as f2:
        for line in f1:
            for c in line:
                if c in 'aeiouAEIOU':
                    c = '0'
                f2.write(c)