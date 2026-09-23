lines = iter(open(0))

first = next(lines, None)
if first:
    t = int(first)
    for _ in range(t):
        n, L, k = map(int, next(lines).split())
        
        max_dist = 0
        for _ in range(n):
            x, y = map(int, next(lines).split())
            d2 = x * x + y * y
            if d2 > max_dist:
                max_dist = d2
        
        r = int(max_dist ** 0.5)
        if r * r < max_dist:
            r += 1
            
        if r <= L:
            print(0)
            continue
            
        ans = 10**9
        for d in range(32):
            need = (r + (1 << d) - 1) >> d
            if need <= L:
                ops = d
            else:
                add = (need - L + k - 1) // k
                ops = d + add
            if ops < ans:
                ans = ops
                
        print(ans)