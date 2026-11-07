def is_leap(y):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        return True
    return False

def get_day(y, m):
    day_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    if m == 2 and is_leap(y):
        return 29
    return day_list[m-1]

import sys
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    y, m, x = map(int, line.split())
    target = str(x)
    cnt = 0
    maxd = get_day(y, m)
    for d in range(1, maxd+1):
        s = f"{y:04d}-{m:02d}-{d:02d}"
        cnt += s.count(target)
    print(cnt)
