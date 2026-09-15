
for _ in range(int(input())):
    n, k = map(int, input().split())
    ls = list(map(int, input().split()))

    ans = k

    for i in ls:
        if i % k == 0:
            ans = 0
        else:
            ans = min(ans, k - i % k)

    if k == 4:
        even = 0

        for x in ls:
            if x % 2 == 0:
                even += 1

        if even >= 2:
            ans = 0
        elif even == 1:
            ans = min(ans, 1)
        else:
            ans = min(ans, 2)

    print(ans)