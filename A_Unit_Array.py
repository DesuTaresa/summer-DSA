for _ in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))
    neg = ls.count(-1)
    ans = 0

    while neg > n // 2:
        neg -= 1
        ans += 1

    if neg % 2 == 1:
        ans += 1

    print(ans)
