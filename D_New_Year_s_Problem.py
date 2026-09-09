

for _ in range(int(input())):
    li = input().strip()

    while li == "":
        li = input().strip()

    n, m = map(int, li.split())

    a = []

    for i in range(n):
        a.append(list(map(int, input().split())))

    low = 1
    high = 10**9
    ans = 0

    while low <= high:
        mid = (low + high) // 2

        covered = [0] * m
        good = False

        for i in range(n):
            cnt = 0

            for j in range(m):
                if a[i][j] >= mid:
                    covered[j] = 1
                    cnt += 1

            if cnt >= 2:
                good = True

        if good and sum(covered) == m:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    print(ans)