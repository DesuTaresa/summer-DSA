n, t = map(int, input().split())
ls = list(map(int, input().split()))

curr = 1

while curr < t:
    curr += ls[curr - 1]

if curr == t:
    print("YES")
else:
    print("NO")