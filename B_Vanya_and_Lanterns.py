n, l = map(int, input().split())
ls = list(map(int, input().split()))

ls.sort()

ans = max(ls[0], l - ls[-1])

for i in range(1, n):
    gap = ls[i] - ls[i - 1]
    ans = max(ans, gap / 2)

print(f"{ans:.10f}")