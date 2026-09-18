n = int(input())

par = []

for i in range(n):
    par.append(int(input()))
ans = 0
for i in range(n):
    curr = i
    depth = 1
    while par[curr] != -1:
        curr = par[curr] - 1
        depth += 1

    ans = max(ans, depth)

print(ans)