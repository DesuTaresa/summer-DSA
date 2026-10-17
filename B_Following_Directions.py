for _ in range(int(input())):
    n = int(input())
    s = input()
    a = 0
    r = 0
    for i in range(n):
        if s[i]=="U":
            a += 1
            if a==1 and r ==1:
                print("YES")
                break
        elif s[i]=="R":
            r += 1
            if a==1 and r==1:
                print("YES")
                break
        elif s[i]=="D":
            a -= 1
            if a==1 and r==1:
                print("YES")
                break
        elif s[i]=="L":
            r -= 1
            if a==1 and r==1:
                print("YES")
                break
    else:
        print("NO")

