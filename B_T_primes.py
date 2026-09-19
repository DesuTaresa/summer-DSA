import math

LIMIT = 10**6
is_prime = [True] * (LIMIT + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(LIMIT**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, LIMIT + 1, i):
            is_prime[j] = False

n = int(input())
num = list(map(int, input().split()))

for x in num:
    root = math.isqrt(x)
    if root * root == x and is_prime[root]:
        print("YES")
    else:
        print("NO")