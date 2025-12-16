for n in range(100, 1000):
    if n + int(str(n)[::-1]) == 968:
        print(n)
        break
