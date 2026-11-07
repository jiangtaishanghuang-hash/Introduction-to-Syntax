n = int(input())
c = 1
for i in range(1, n + 1):
    row = []
    for _ in range(i):
        row.append(f"{c:4d}")
        c += 1
    print("".join(row))
