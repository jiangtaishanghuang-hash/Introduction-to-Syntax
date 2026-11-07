a, b = map(int, input().split())
print(a, b)
if a < b:
    print("<\n")
elif a == b:
    print("=\n")
else:
    print(">\n")
