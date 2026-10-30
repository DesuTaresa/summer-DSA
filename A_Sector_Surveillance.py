
for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()

    res = 0

    for i in range(0, n, k):
        if '0' not in s[i:i+k]:
            res += 1

    print(res)
