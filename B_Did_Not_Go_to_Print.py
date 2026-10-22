
for _ in range(int(input())):
    n = int(input())
    ls = input()

    li = []
    printed = set()

    for i in range(n):
        if ls[i] == "1":
            li.append(i + 1)

        elif ls[i] == "2":
            if li:
                printed.add(li.pop())
            else:
                printed.add(i + 1)

        elif ls[i] == "3":
            printed.add(i + 1)

    not_printed = []

    for i in range(1, n + 1):
        if i not in printed:
            not_printed.append(i)

    print(len(not_printed))
    print(*not_printed)

