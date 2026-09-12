import math
for _ in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))
    sam = sum(ls)
    if math.sqrt(sam).is_integer()== True:
        print("YES")
    else:
        print("NO")
  
