for _ in range(int(input())):
    n, a, b = map(int, input().split())
    if n==a and n==b:
        print("Yes")
    elif a+b<=n-2:
        print("Yes")
    else:
        print("No")
