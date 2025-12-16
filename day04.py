found = []
for n in range(250):
    if (val := sum(range(n, n+4))) < 100:
        continue
    elif val >= 1000:
        break
    else:
        found.append(val)

print(sum(found) / len(found))
