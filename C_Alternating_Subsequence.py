
for _ in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))

    ans = 0
    mx = ls[0]

    for i in range(1, n):
        if (ls[i] > 0 ) == (ls[i-1] > 0):
            mx = max(mx, ls[i])
        else:
            ans += mx
            mx = ls[i]

    ans += mx

    print(ans)
