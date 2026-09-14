
for _ in range(int(input())):
    n = int(input())
    s = input()

    ans = 1
    count = 1

    for i in range(1, n):
        if s[i] == s[i - 1]:
            count += 1
        else:
            count = 1

        ans = max(ans, count)

    print(ans + 1)

