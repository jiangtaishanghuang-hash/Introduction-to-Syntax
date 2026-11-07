T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    diff = max(arr) - min(arr)
    mean = sum(arr)/n
    var = sum((x-mean)**2 for x in arr)/n
    print(f"{diff} {var:.3f}")
