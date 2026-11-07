n, x = map(int, input().split())
x = str(x)
print(sum(str(i).count(x) for i in range(1, n + 1)))
