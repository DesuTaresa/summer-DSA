n, t = map(int, input().split())
ls = list(map(int, input().split()))

l = 0
total = 0
ans = 0

for r in range(n):
    total += ls[r]

    while total > t:
        total -= ls[l]
        l += 1

    ans = max(ans, r - l + 1)

print(ans)