n, m, a, b = map(int, input().split())

cost = (n // m) * min(m * a, b)
res = n % m

cost += min(res * a, b)

print(cost)