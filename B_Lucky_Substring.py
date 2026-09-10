s = input().strip()

ans = ""
max_count = 0

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        sub = s[i:j]

        if all(c == '4' or c == '7' for c in sub):
            count = s.count(sub)

            if count > max_count or (count == max_count and (ans == "" or sub < ans)):
                max_count = count
                ans = sub

print(ans if ans else -1)