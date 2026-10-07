
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if all(x == 0 for x in a):
        print(0)

    elif n % 2 == 0:
        print(2)
        print(1, n)
        print(1, n)

    else:
        print(4)
        print(1, n - 1)
        print(1, n - 1)
        print(2, n)
        print(2, n)

