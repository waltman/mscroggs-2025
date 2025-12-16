from math import prod

for n in range(1000):
    prod_dig = prod(int(c) for c in str(n))
    if n == 4 * prod_dig:
        print(n)
