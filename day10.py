from math import sqrt

def odd_factors(n):
    root = int(sqrt(n))
    for i in range(1, root+1, 2):
        if n % i == 0:
            yield i
            x = n // i
            if x % 2 == 1 and x != root:
                yield x

print(len(list(odd_factors(2025))))
for n in range(100, 1000):
    if len(list(odd_factors(n))) == 16:
        print(n)
        break
    
