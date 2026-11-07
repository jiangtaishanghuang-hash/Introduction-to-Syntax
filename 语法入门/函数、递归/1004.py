def sum_digit(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s

x, y = map(int, input().split())
count = 0
for num in range(x, y + 1):
    if sum_digit(num) % 5 == 0:
        count += 1
print(count)
