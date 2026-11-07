used = [False] * 9
path = []

def dfs():
    if len(path) == 8:
        print(' '.join(map(str, path)))
        return
    for i in range(1,9):
        if not used[i]:
            used[i] = True
            path.append(i)
            dfs()
            path.pop()
            used[i] = False
dfs()
