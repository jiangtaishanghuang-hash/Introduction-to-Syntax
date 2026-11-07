cycle = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,
         14,13,12,11,10,9,8,7,6,5,4,3,2,1]

n = int(input())
a = list(map(int, input().split()))

next_values = []
for i in range(30):
    ok = True
    for j in range(n):
        pos = (i + j) % 30
        if cycle[pos] != a[j]:
            ok = False
            break
    if ok:
        last_pos = (i + n - 1) % 30
        nxt_pos = (last_pos + 1) % 30
        next_values.append(cycle[nxt_pos])

unique = list(set(next_values))
if len(unique) != 1:
    print(-1)
else:
    last = a[-1]
    nv = unique[0]
    if nv > last:
        print("UP")
    else:
        print("DOWN")
