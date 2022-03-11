n, m = map(int, input().split(" "))

result = []
whole = []

def dfs(i):
    if len(result) == m: 
        print(str(" ".join(result)))
        return
    for i in range(i, n+1):
        result.append(str(i))
        dfs(i)
        result.pop()
for i in range(1, n+1):
    result.append(str(i))
    dfs(i)
    result.pop()
