for _ in range(int(input())):
    n, k, x = map(int, input().split())
    ls = []
    for i in range(1, k + 1):
        ls.append(i)
    ls.remove(x)

    li = []

    if 1 in ls:
        for i in range(n):
            li.append(1)
        print("YES")
        print(len(li))
        print(*li)

    elif 2 in ls and n % 2 == 0:
        d = n // 2
        for i in range(d):
            li.append(2)
        print("YES")
        print(len(li))
        print(*li)

    elif 2 in ls and 3 in ls and n >= 3:
        li.append(3)
        rem = n - 3
        d = rem // 2
        for i in range(d):
            li.append(2)
        print("YES")
        print(len(li))
        print(*li)

    else:
        print("NO")