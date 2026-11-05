
for _ in range(int(input())):
    s = input()
    if s[0] != s[-1]:
        s = s[-1] + s[1:]
    print(s)