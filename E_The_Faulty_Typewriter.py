t = int(input())

for _ in range(t):
    s = input()
    deleted = [False] * len(s)

    lower = []
    upper = []

    for i, c in enumerate(s):
        if c == 'b':
            if lower:
                deleted[lower.pop()] = True

        elif c == 'B':
            if upper:
                deleted[upper.pop()] = True

        elif c.islower():
            lower.append(i)

        elif c.isupper():
            upper.append(i)

    ans = []

    for i, c in enumerate(s):
        if c != 'b' and c != 'B' and not deleted[i]:
            ans.append(c)

    print(''.join(ans))