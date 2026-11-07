import sys

def main():
    n, t = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()

    if '.' in s:
        a, b = s.split('.')
    else:
        a = s
        b = ''
    a = list(a)
    b = list(b)

    while t > 0:
        p = -1
        for i in range(len(b)):
            if int(b[i]) >= 5:
                p = i
                break
        if p == -1:
            break
        t -= 1
        carry = 1

        pos = p - 1
        while carry and pos >= 0:
            num = int(b[pos]) + carry
            if num >= 10:
                b[pos] = str(num - 10)
                carry = 1
            else:
                b[pos] = str(num)
                carry = 0
            pos -= 1

        if carry:
            idx = len(a) - 1
            while carry and idx >= 0:
                num = int(a[idx]) + carry
                if num >= 10:
                    a[idx] = str(num - 10)
                    carry = 1
                else:
                    a[idx] = str(num)
                    carry = 0
                idx -= 1
            if carry:
                a.insert(0, '1')
        b = b[:p]

    A = ''.join(a)
    B = ''.join(b).rstrip('0')
    if B == '':
        print(A)
    else:
        print(f"{A}.{B}")

if __name__ == "__main__":
    main()
