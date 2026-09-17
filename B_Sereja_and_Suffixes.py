n, m = map(int, input().split())
ls = list(map(int, input().split()))

ans = [0] * n
s = set()

for i in range(n - 1, -1, -1):
    s.add(ls[i])
    ans[i] = len(s)

for _ in range(m):
    l = int(input())
    print(ans[l - 1])