n = int(input())
a = list(map(int, input().split()))

ones = sum(a)

current = 1 if a[0] == 0 else -1
best = current

for i in range(1, n):
    if a[i] == 0:
        value = 1
    else:
        value = -1

    current = max(value, current + value)
    best = max(best, current)

print(ones + best)