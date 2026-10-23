for _ in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))

    li = []
    for i in ls:
        li.append(n + 1 - i)

    print(*li)