t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    odd = 0
    mod0 = 0
    mod2 = 0

    for x in a:
        if x % 2 == 1:
            odd += 1
        elif x % 4 == 0:
            mod0 += 1
        else:
            mod2 += 1

    print(max(odd, mod0, mod2))