
for _ in range(int(input())):
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        print(0)
    elif b <= a and (a - b) % 2 == 0:
        print(a)
    elif b <= a + 1 and (a - b) % 2 != 0:
        print(a + 1)
    else:
        print(-1)