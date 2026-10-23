n = int(input())
v = list(map(int, input().split()))
u = sorted(v)

pref1 = [0] * (n + 1)
pref2 = [0] * (n + 1)

for i in range(n):
    pref1[i + 1] = pref1[i] + v[i]
    pref2[i + 1] = pref2[i] + u[i]

m = int(input())
for _ in range(m):
    t, l, r = map(int, input().split())
    if t == 1:
        print(pref1[r] - pref1[l - 1])
    else:
        print(pref2[r] - pref2[l - 1])