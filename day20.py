powers = set()
for n in range(2, 32):
    k = 2
    while True:
        if (power := n**k) >= 1000:
            break
        elif power >= 100:
            powers.add(power)
        k += 1

for power in powers:
    if power + 29 in powers:
        print(power, power+29)
