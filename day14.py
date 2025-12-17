from itertools import groupby
from operator import itemgetter

def has_odd_run(s):
    lst = [int(c) for c in s]
    for k,v in groupby(enumerate(lst),key=itemgetter(1)):
        if k:
            v = list(v)
            if (v[-1][0] - v[0][0]) % 2 == 0:
                return True
    return False

num_bits = 11
cnt = 0
for n in range(0, 2**num_bits):
    bits = f'{n:0{num_bits}b}'
    if not has_odd_run(bits):
        cnt += 1

print(cnt)

