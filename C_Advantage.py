for _ in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))
    li = sorted(ls, reverse=True)
    mx = li[0]
    mn = li[1]
   
    ld = []
    for i in range(n):
        if ls[i] == mx:
            ld.append(ls[i]-mn)
        else:
            ld.append(ls[i]-mx)
    print(*ld)
    
        

    