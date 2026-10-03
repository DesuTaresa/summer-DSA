for _ in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        if ls[i]%2 == ls[i+1]%2:
            ans += 1
    print(ans)