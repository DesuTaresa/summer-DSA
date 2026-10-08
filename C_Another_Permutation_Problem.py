for _ in range(int(input())):
    n = int(input())

    ans = 0

    for k in range(2, n + 1):
        ls = []

        for i in range(1, n + 1):
            ls.append(i)

        for i in range(k // 2):
            ls[n-k+i], ls[n-1-i] = ls[n-1-i], ls[n-k+i]

        tot_sum = 0
        cost_max = 0

        for j in range(n):
            tot_sum += ls[j] * (j + 1)
            cost_max = max(cost_max, ls[j] * (j + 1))

        ans = max(ans, tot_sum - cost_max)

    print(ans)