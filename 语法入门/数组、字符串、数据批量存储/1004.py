L, M = map(int, input().split())
qujian = []
for _ in range(M):
    l, r = map(int, input().split())
    qujian.append( (l, r) )

qujian.sort()

wa_diao = 0
now_l, now_r = qujian[0]
for l, r in qujian[1:]:
    if l <= now_r:
        now_r = max(now_r, r)
    else:
        wa_diao += now_r - now_l + 1
        now_l, now_r = l, r
wa_diao += now_r - now_l + 1

zong = L + 1
shengxia = zong - wa_diao
print(shengxia)
