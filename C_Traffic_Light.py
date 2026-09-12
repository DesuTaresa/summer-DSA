
for _ in range(int(input())):
    ls = input().split()
    n = int(ls[0])
    c =ls[1]
    s = input()

    if c == 'g':
        print(0)
    else:
        s2 = s + s
        mum = 0
        last_g = -1

        for i in range(2 * n - 1, -1, -1):
            if s2[i] == 'g':
                last_g = i
            elif s2[i] == c and i < n and last_g != -1:
                wait_t = last_g - i
                if wait_t >mum:
                    mum = wait_t

        print(mum)