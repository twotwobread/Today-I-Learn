n, m = map(int, input().split(" "))

result = []

def dfs():
    if len(result) == m:
        print(str(" ".join(result)))
        return
    for i in range(1, n+1):
        if str(i) not in result:
            result.append(str(i))
            dfs()
            result.pop()
dfs()
