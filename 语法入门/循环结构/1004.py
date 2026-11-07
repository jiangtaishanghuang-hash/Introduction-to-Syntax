T = int(input())
for _ in range(T):
    n = int(input())
    mid = n//2
    for i in range(n):
        st = 2 * (mid - abs(i - mid)) + 1
        sp = abs(i - mid)
        print(" " * sp + "*" * st)
