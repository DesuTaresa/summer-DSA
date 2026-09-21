from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))

prefix = []
total = 0

for x in a:
    total += x
    prefix.append(total)

m = int(input())
queries = list(map(int, input().split()))

for q in queries:
    pile = bisect_left(prefix, q)
    print(pile + 1)