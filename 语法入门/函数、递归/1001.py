L, R = map(int, input().split())
cnt = 0
for num in range(L, R + 1):
    s = str(num)
    cnt += s.count('2')
print(cnt)
