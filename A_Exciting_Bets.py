for _ in range(int(input())):
    a, b = map(int, input().split())
    if a==b:
        print(0, 0)
    else:
        d = abs(a-b)
        mov = min(a%d, d-a%d)
        print(d, mov)