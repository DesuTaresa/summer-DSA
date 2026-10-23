for _ in range(int(input())):
    n, k = map(int, input().split())
    if n==k:
        print(n*2)
    else:
        d=n-k
        print(2**(d+1)+(2*(k-1)))
