from itertools import permutations

eq1 = lambda a, b, c: (a-b) / c == 1
eq2 = lambda a, b, c: (a*b) - c == 37
eq3 = lambda a, b, c: (a+b) + c == 17
eq4 = lambda a, b, c: (a/b) * c == 2
eq5 = lambda a, b, c: (a+b) / c == 1
eq6 = lambda a, b, c: (a*b) / c == 2

for arr in permutations(range(1,10)):
    if eq1(arr[0], arr[1], arr[2]) and \
       eq2(arr[3], arr[4], arr[5]) and \
       eq3(arr[6], arr[7], arr[8]) and \
       eq4(arr[0], arr[3], arr[6]) and \
       eq5(arr[1], arr[4], arr[7]) and \
       eq6(arr[2], arr[5], arr[8]):

       print(arr)
       print(arr[0] * arr[4] * arr[5])
