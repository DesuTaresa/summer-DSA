n = int(input())
ls = [4,7,44,47,77,44,474,477,744,747,777]
if n in ls or n%4== 0 or n%7== 0 or n%47==0 or n%44==0 or n%77==0 or n%74==0 or n%444==0 or n%474==0 or n%477==0:
    print("YES")
else:
    print("NO")