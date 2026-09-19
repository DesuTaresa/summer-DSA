n, k = map(int, input().split())
left_min = 240 - k
ans = 0

for i in range(1, n + 1):
    if left_min >= 5 * i:
        left_min -= 5 * i
        ans += 1
    else:
        break

print(ans)