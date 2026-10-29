for _ in range(int(input())):
    n , s, x = map(int, input().split())
    ls = list(map(int, input().split()))
    d = sum(ls)
    if d>s:
        print("NO")
    elif d==s:
        print("YES")
    else:
        m = s-d
        if m%x==0:
            print("YES")
        else:
            print("NO")