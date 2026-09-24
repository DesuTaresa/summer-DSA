for _ in range(int(input())):
    a, b, n = map(int, input().split())
    
    ls= list(map(int, input().split()))

    ans = b

    for i in ls:
        ans += min(i, a - 1)

    print(ans)