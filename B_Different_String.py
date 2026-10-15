for _ in range(int(input())):
    s = input()
    if len(set(s))==1:
        print("NO")
    else:
        m = ""
        for i in range(1,len(s)+1):
            if s[i ] != s[i-1]:
                m += s[i]
                m += s[i-1]
                break
        for j in s:
            if j!=m[0] or j!=m[1]:
                m += j
            
        print("YES")
        print(m)