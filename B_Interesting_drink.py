from bisect import bisect_right

n = int(input())
prices = sorted(map(int, input().split()))

q = int(input())

for _ in range(q):
    m = int(input())
    print(bisect_right(prices, m))