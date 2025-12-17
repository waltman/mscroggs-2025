def addup(start, n):
    s1 = sum(range(start, start+n))
    s2 = sum(range(start+n, start+n*2))
    return s2-s1

DIFF = 203401

for n in range(100, 1000):
    res = addup(0, n)
    if res == DIFF:
        print(n)
