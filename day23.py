def sum_cube(n):
    return sum(int(c)**3 for c in str(n))

for n in range(100, 1000):
    if sum_cube(n) == n:
        print(n)
