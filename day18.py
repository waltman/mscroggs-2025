from math import comb

MAX = 14
day18 = sum(comb(MAX-n, n-1) for n in range(1,MAX+1))
print(day18)
