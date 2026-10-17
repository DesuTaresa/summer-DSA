
a, b = map(int, input().split())

if b == 0:
    if a == 1:
        print(0, 0)
    else:
        print(-1, -1)
elif b > 9 * a:
    print(-1, -1)
else:
    s = b
    smallest = ""
    largest = ""

    for i in range(a):
        for d in range(10):
            if (i > 0 or d > 0) and 0 <= s - d <= 9 * (a - i - 1):
                smallest += str(d)
                s -= d
                break

    s = b
    for i in range(a):
        d = min(9, s)
        largest += str(d)
        s -= d

    print(smallest, largest)
