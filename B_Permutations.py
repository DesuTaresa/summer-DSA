
from itertools import permutations

n, k = map(int, input().split())
nums = [input().strip() for _ in range(n)]

ans = float('inf')

for p in permutations(range(k)):
    values = []

    for num in nums:
        new_num = ""

        for i in p:
            new_num += num[i]

        values.append(int(new_num))

    diffs = max(values) - min(values)

    ans = min(ans, diffs)

print(ans)
