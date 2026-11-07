import sys


def main():
    data = sys.stdin.read().split()
    ptr = 0
    n = int(data[ptr])
    ptr += 1
    k = int(data[ptr])
    ptr += 1

    A = list(map(int, data[ptr:ptr + n]))
    ptr += n
    B = list(map(int, data[ptr:ptr + n]))
    ptr += n

    sumB = sum(B)
    diff = [A[i] - B[i] for i in range(n)]
    diff.sort(reverse=True)

    add = sum(diff[:k])
    print(sumB + add)


if __name__ == "__main__":
    main()
