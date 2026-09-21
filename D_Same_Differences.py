
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    count = {}
    ans = 0

    for i in range(n):
        x = a[i] - (i + 1)

        if x in count:
            ans += count[x]

        count[x] = count.get(x, 0) + 1

    print(ans)