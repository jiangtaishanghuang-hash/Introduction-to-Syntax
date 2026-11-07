import sys

def main():
    s = sys.stdin.read()
    n = len(s)
    res = []
    i = 0
    in_str = False
    while i < n:
        if not in_str:
            if i+1 < n and s[i] == '/' and s[i+1] == '*':
                j = i + 2
                found = False
                while j < n:
                    if s[j] == '*' and j+1 < n and s[j+1] == '/':
                        i = j + 2
                        found = True
                        break
                    j += 1
                if not found:
                    res.append('/')
                    i += 1
            else:
                c = s[i]
                res.append(c)
                if c == '"':
                    in_str = True
                i += 1
        else:
            c = s[i]
            res.append(c)
            if c == '\\':
                i += 1
                if i < n:
                    res.append(s[i])
            elif c == '"':
                in_str = False
            i += 1
    sys.stdout.write(''.join(res))

if __name__ == "__main__":
    main()
