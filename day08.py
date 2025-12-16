import numpy as np
from itertools import product

def multi_table(n):
    mt = np.ones([n,n], dtype=int)
    mt[0,:] = range(1, n+1)
    mt[:,0] = range(1, n+1)
    for row,col in product(range(1,n), range(1,n)):
        mt[row,col] = mt[row,0] * mt[0,col]

    return int(sum(mt[-1,:])), int(sum(mt.flatten()))

def main():
    n = 3
    while True:
        bottom, total = multi_table(n)
        if total == 2025:
            print(n, bottom)
            break
        else:
            n += 1

main()
