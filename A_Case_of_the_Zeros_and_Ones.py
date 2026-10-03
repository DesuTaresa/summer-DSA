n = int(input())
s = input()

zero = s.count("0")
one = s.count("1")

print(n - 2 * min(zero, one))