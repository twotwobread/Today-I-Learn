# 문제 유형 : 최소비용 신장 트리 (ElogE)
# [아이디어]
# - x, y, z축으로 한번씩 정렬하면 3*(N-1)개의 간선만 생각하면 된다.
# - 3개의 축을 다 따로 분리해서 생각하는 것이다. 정렬을 하게 되면 바로 옆에 있는 노드가 그 축에서 가장 가까운 노드들이 된다.
# - 그렇기 때문에 그 축에서의 최소 간선들 (N-1)개가 되는 것이다.
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
    for cost, a, b in edge:
        if find(rt, a) != find(rt, b):
            union(rt, a, b)
            sumValue += cost
    print(sumValue)

if __name__ == "__main__":
    n = int(input())
    planet = [list(map(int, input().split()))+[i,] for i in range(n)]
    rt = list(map(int, range(n)))
    edge = []
    for i in range(3):
        temp = sorted(planet, key=lambda x: x[i])
        for j in range(1, n):
            edge.append((abs(temp[j-1][i] - temp[j][i]), temp[j-1][3], temp[j][3]))
    edge.sort()
    solution()

