# WAF that takes a list and a number as argument and returns the index of that element in the list
# find([10,30,20,40], 30) -> 1
# find([10,30,20,40], 300) -> -1
# find([10,30,20,30], 30) -> 1

def find(seq, data):
    pos = -1
    
    idx = 0
    while idx < len(seq):
        if seq[idx] == data:
            pos = idx
            break
        idx += 1
            
    return pos

def find(seq, data):
    pos = -1
    
    for idx, val in enumerate(seq):
        if val == data:
            pos = idx
            break
    return pos

print(find([10,30,20,40], 30))
print(find([10,30,20,40], 300))
print(find([10,30,20,30], 30))        