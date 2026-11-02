
for _ in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))

    for i in range(n):
        indx = i + 1
        val = ls[i]
        while indx % 2 == 0:
            indx //= 2
        while val % 2 == 0:
            val //= 2
        if indx != val:
            print("NO")
            break
    else:
        print("YES")
