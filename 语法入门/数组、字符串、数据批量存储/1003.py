n, k, m = map(int, input().split())
pe = list(range(n))
pos = pe.index(k)

while len(pe) > 1:
    pos = (pos + m - 1) % len(pe)
    pe.pop(pos)

print(pe[0])
