
n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

if k == 0:
    if a[0] > 1:
        print(1)
    else:
        print(-1)
elif k == n:
    print(a[n - 1])
else:
    x = a[k - 1]
    if x < a[k]:
        print(x)
    else:
        print(-1)
