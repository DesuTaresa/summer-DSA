k = int(input())
ls = list(map(int, input().split()))
ls.sort()
if k ==0:
    print(0)
elif sum(ls)<k:
    print(-1)
else:
    d = 0
    counter = 0
    i = 11
    while d<k:
        d += ls[i]
        counter += 1
        i -= 1
    print(counter)
    
    
