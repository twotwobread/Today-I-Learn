# 문제 유형 : 최소 신장 트리
# 자료 구조 : 1차원 리스트 - 간선 정보
#           rt - 루트의 정보, 사이클을 찾기 위함.
#           minValue - 유지비 최솟값을 구하기 위함.
def find(rt, x):
    if rt[x] != x:
        rt[x] = find(rt, rt[x])
    return rt[x]
def union(rt, a, b):
    pA = find(rt, a)
    pB = find(rt, b)
    if pA > pB:
        rt[pA] = pB
    else:
        rt[pB] = pA
def solution():
    sumValue = 0
    max = -1
    for cost, a, b in edge:
        if find(rt, a) != find(rt, b):
            union(rt, a, b)
            sumValue += cost
            max = cost if max < cost else max
    return sumValue - max

if __name__ == "__main__":
    n, m = map(int, input().split())
    rt = list(map(int, range(n+1)))
    edge = []
    for _ in range(m):
        a, b, cost = map(int, input().split())
        edge.append((cost, a, b))
    edge.sort()
    print(solution())
