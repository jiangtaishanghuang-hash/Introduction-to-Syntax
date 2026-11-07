def main():
    skip = [[0]*10 for _ in range(10)]
    skip[1][3] = skip[3][1] = 2
    skip[1][7] = skip[7][1] = 4
    skip[1][9] = skip[9][1] = 5
    skip[2][8] = skip[8][2] = 5
    skip[3][7] = skip[7][3] = 5
    skip[3][9] = skip[9][3] = 6
    skip[4][6] = skip[6][4] = 5
    skip[7][9] = skip[9][7] = 8

    import sys
    for line in sys.stdin:
        s = line.strip()
        if not s:
            continue
        used = [False] * 10
        ok = True
        for idx in range(len(s)):
            cur = int(s[idx])
            if used[cur]:
                ok = False
                break
            used[cur] = True
            if idx == 0:
                continue
            prev = int(s[idx-1])
            mid = skip[prev][cur]
            if mid != 0 and not used[mid]:
                ok = False
                break
        print("YES" if ok else "NO")

if __name__ == "__main__":
    main()
