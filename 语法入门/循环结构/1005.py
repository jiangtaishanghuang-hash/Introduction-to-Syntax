while True:
    try:
        n = int(input())
        for i in range(1, n + 2):
            print(" " * (2 * n - 2 * i + 2), end="")
            print("*" * i, end="")
            print()
        for i in range(n, 0, -1):
            print(" " * (2 * n - 2 * i + 2), end="")
            print("*" * i, end="")
            print()

    except:
        break
