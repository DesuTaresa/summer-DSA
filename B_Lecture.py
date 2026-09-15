n, m = map(int, input().split())

words = {}

for _ in range(m):
    a, b = input().split()
    words[a] = b

lec = input().split()

for i in lec:
    b = words[i]

    if len(b) < len(i):
        print(b, end=" ")
    else:
        print(i, end=" ")