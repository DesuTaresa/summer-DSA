
for _ in range(int(input())):
    s = input()
    if len(s)%2==1:
        print("NO")
    else:
        d = len(s)//2
        if s[:d]==s[d:]:
            print("YES")
        else:
            print("NO")