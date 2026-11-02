
for i in range(int(input())):
    m, k = map(int, input().split())
    ls = list(map(int,input().split()))
    ls.sort()
    l=0
    r=1
    d =1
    while r<m:
        if abs(ls[r]-ls[r-1])<=k:
            res =r-l+1
            d= max(d,res)
            r+=1
        else:
            l=r
            r=l+1
    print(len(ls)-d)