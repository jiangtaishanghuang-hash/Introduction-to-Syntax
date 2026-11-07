def main():
    import sys
    data = list(map(int, sys.stdin.readline().split()))
    cnt = data[:10]

    odd = 0
    mid = ''
    for i in range(10):
        if cnt[i] % 2 == 1:
            odd += 1
            mid = str(i)
            cnt[i] -= 1
    if odd > 1:
        print(-1)
        return

    left = []
    for i in range(1, 10):
        take = cnt[i] // 2
        left.append(str(i) * take)
    take0 = cnt[0] // 2
    left.append('0' * take0)
    left = ''.join(left)

    if left == '':
        if mid != '':
            print(mid)
        else:
            print(-1)
        return

    ans = left + mid + left[::-1]
    print(ans)

if __name__ == "__main__":
    main()
