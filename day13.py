from math import prod

for a1 in range(100, 1000):
    a2 = a1 * 2
    a3 = int(prod(int(c) for c in str(a1)))
    d1a = (a1 // 100) * 10 + a2 // 100
    d3 = (a1 % 10) * 100 + (a2 % 10) * 10 + (a3 % 10)

    d1b = int(sum(int(c) for c in str(a1)))
    if d1a == d1b and (d3 % 101) == 0:
        print(a1)
        print(a2)
        print(f' {a3}')
        print()

