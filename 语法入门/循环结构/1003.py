import string
ch = input().strip()
n = ord(ch) - ord('A') + 1
for i in range(1 , n+1):
    left = "".join(string.ascii_uppercase[k] for k in range(i))
    right = left[-2::-1]
    print(" " * (n - i) + left + right)
