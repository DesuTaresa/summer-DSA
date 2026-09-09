import math
for _ in range(int(input())):
    n = int(input())

    squares = math.isqrt(n)
    cubes = round(n ** (1 / 3))

    while (cubes + 1) ** 3 <= n:
        cubes += 1
    while cubes ** 3 > n:
        cubes -= 1

    sixth = round(n ** (1 / 6))

    while (sixth + 1) ** 6 <= n:
        sixth += 1
    while sixth ** 6 > n:
        sixth -= 1

    print(squares + cubes - sixth)