n = int(input())
sushi = list(map(int, input().split()))

ans = 0
prev = 0
curr = 1

for i in range(1, n):
    if sushi[i] == sushi[i - 1]:
        curr += 1
    else:
        ans = max(ans, 2 * min(prev, curr))
        prev = curr
        curr = 1

ans = max(ans, 2 * min(prev, curr))

print(ans)