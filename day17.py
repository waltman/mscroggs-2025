def xnor(x, y):
    return int(not(x^y))

def reduce_xnor(s):
    lst = [int(c) for c in s]
    while len(lst) > 1:
        tmp = []
        for i in range(len(lst)-1):
            tmp.append(xnor(lst[i],lst[i+1]))
        lst = tmp.copy()

    return lst[0]

num_bits = 10
cnt = 0
for n in range(0, 2**num_bits):
    bits = f'{n:0{num_bits}b}'
    if reduce_xnor(bits) == 1:
        cnt += 1

print(cnt)
