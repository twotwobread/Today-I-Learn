import heapq

def isParent(x):
    if parent[x] != x:
        parent[x] = isParent(parent[x])
    return parent[x]
def merge(a, b):
    a = isParent(a)
    b = isParent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

if __name__ == "__main__":
    V, E = map(int, input().split())
    q = []
    parent = [i for i in range(V+1)]
    for _ in range(E):
        a, b, c = map(int, input().split())
        heapq.heappush(q, (c, a, b))
    sumValue = 0
    while len(q) > 0:
        c, a, b = heapq.heappop(q)
        if isParent(a) != isParent(b):
            sumValue += c
            merge(a, b)
    print(sumValue)
