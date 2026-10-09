
n, m, k = map(int, input().split())
a = [list(input().strip()) for _ in range(n)]

start = None

for i in range(n):
    for j in range(m):
        if a[i][j] == '.':
            start = (i, j)
            break
    if start is not None:
        break

stack = [start]
visited = set()
order = []

while stack:
    x, y = stack.pop()

    if (x, y) in visited:
        continue

    visited.add((x, y))
    order.append((x, y))

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == '.' and (nx, ny) not in visited:
                stack.append((nx, ny))

for i in range(len(order) - k, len(order)):
    x, y = order[i]
    a[x][y] = 'X'

for row in a:
    print(''.join(row))