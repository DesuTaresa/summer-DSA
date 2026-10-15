
n, k = map(int, input().split())
ls = list(map(int, input().split()))

ls.sort()

if k == 0:
    if ls[0] > 1:
        print(1)
    else:
        print(-1)
elif k == n:
    print(ls[n - 1])
else:
    x = ls[k - 1]
    if x < ls[k]:
        print(x)
    else:
        print(-1)
