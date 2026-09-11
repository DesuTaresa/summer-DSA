
for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()

    w = s[:k].count('W')
    ans = w

    for i in range(k, n):
        if s[i] == 'W':
            w += 1
        if s[i - k] == 'W':
            w -= 1

        ans = min(ans, w)

    print(ans)