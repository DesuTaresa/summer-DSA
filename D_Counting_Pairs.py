
t = int(input())
def count_pairs(a, limit):
    left = 0
    right = len(a) - 1
    count = 0

    while left < right:
        if a[left] + a[right] <= limit:
            count += right - left
            left += 1
        else:
            right -= 1

    return count


for _ in range(t):
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))

    total = sum(a)
    a.sort()

    high = total - x
    low = total - y

    answer = count_pairs(a, high) - count_pairs(a, low - 1)

    print(answer)

