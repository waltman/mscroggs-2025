from itertools import permutations

best = 1000
for p in permutations('1234567'):
    x = int(''.join(p[0:3]))
    y = int(''.join(p[3:6]))
    z = int(p[6])
    if x + y + z == 1000:
        if (largest := max(x,y)) < best:
            best = largest

print(best)



