
for _ in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))
    
    if ls[0] == ls[-1]:
        print("NO")
    else:
        print("YES")
        res = [ls[-1]] + ls[:-1]
        print(*res)