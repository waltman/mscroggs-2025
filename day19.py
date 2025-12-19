from itertools import permutations
from math import sqrt

squares = {n**2 for n in range(int(sqrt(123)), int(sqrt(987))+1)}

for p in permutations(range(1,10), 3):
    if (val := int(''.join(str(n) for n in p))) in squares:
        print(val)


