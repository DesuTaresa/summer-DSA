t = int(input())
for _ in range(t):
    s = input()
    
    cnt0 = s.count('0')
    cnt1 = s.count('1')
    
    for ch in s:
        if ch == '0':
            if cnt1 == 0:
                break
            cnt1 -= 1
        else:
            if cnt0 == 0:
                break
            cnt0 -= 1
            
    print(cnt0 + cnt1)