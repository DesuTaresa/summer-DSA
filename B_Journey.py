
for _ in range(int(input())):
    n, a, b, c = map(int, input().split())
    
    cycle_sum = a + b + c
    full_cyc = n // cycle_sum
    rem = n % cycle_sum
    
    days = full_cyc * 3
    
    if rem > 0:
        if rem <= a:
            days += 1
        elif rem <= a + b:
            days += 2
        else:
            days += 3
            
    print(days)