t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))

    a = [b[0]]
    for i in range(1, n):
        if b[i - 1] > b[i]:
            a.append(b[i])
        a.append(b[i])

    print(len(a))
    print(*a)