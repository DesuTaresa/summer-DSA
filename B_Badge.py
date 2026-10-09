
n = int(input())
a = list(map(int, input().split()))

for i in range(1, n + 1):
    x = i
    visited = [False] * (n + 1)

    while not visited[x]:
        visited[x] = True
        x = a[x - 1]

    print(x, end=" ")