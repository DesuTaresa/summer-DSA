
for _ in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))
    a = 0
    b = 0
    for i in range(n):
        if i % 2 != ls[i] % 2:
            if i % 2 == 0:
                a += 1
            else:
                b += 1
    if a == b:
        print(a)
    else:
        print(-1)