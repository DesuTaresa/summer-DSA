
for _ in range(int(input())):
    n = int(input())
    s = input()
    a = 0
    res = 0
    for i in s:
        if i == '(':
            a += 1
        else:
            a -= 1

        if a < 0:
            res += 1
            a = 0

    print(res)