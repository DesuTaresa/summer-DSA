for _ in range(int(input())):
    a, b = map(int, input().split())
    ans = min(a, b, (a+b)//4)
    print(ans)