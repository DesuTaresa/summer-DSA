s = input()
m = int(input())

n = len(s)
pref = [0] * n

for i in range(1, n):
    pref[i] = pref[i - 1] + (1 if s[i - 1] == s[i] else 0)

for _ in range(m):
    l, r = map(int, input().split())
    print(pref[r - 1] - pref[l - 1])