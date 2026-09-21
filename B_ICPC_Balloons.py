for _ in range(int(input())):
    n = int(input())
    s = input()
    d = set(s)
    m = n - len(d)
    print(2*len(d)+m)