import sys

def main():
    mapping = {
        "zero": "0",
        "two": "2",
        "four": "4",
        "six": "6",
        "nine": "9"
    }
    words = sorted(mapping.keys(), key=lambda x: -len(x))
    input = sys.stdin.read().split()
    T = int(input[0])
    cases = input[1:T+1]
    for s in cases:
        res = []
        i = 0
        n = len(s)
        while i < n:
            c = s[i]
            if c in {'0','2','4','6','9'}:
                res.append(c)
                i += 1
            else:
                matched = False
                for w in words:
                    lw = len(w)
                    if i + lw <= n and s[i:i+lw] == w:
                        res.append(mapping[w])
                        i += lw
                        matched = True
                        break
                if not matched:
                    i += 1
        print(''.join(res))

if __name__ == "__main__":
    main()

