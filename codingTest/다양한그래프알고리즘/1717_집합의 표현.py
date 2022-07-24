def isParent(x):
    tmp = x
    while tmp != parent[tmp]:
        tmp = parent[tmp]
    parent[x] = tmp
    return parent[x]
def merge(a, b):
    a = isParent(a)
    b = isParent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

if __name__ == "__main__":
    N, M = map(int, input().split())
    parent = [i for i in range(N + 1)]
    for m in range(M):
        method, a, b = map(int, input().split())
        if method:
            if isParent(a) == isParent(b):
                print("YES")
            else:
                print("NO")
        else:
            merge(a, b)
