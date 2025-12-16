def all_different(n):
    seen = dict()
    for c in str(n):
        if c in seen:
            return 0
        else:
            seen[c] = 1

    return 1

def main():
    cnt = sum(all_different(n) for n in range(100, 1000))
    print(cnt)

main()
