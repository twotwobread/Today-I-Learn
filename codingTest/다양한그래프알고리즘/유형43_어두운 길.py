# 문제 유형 : 최소비용 신장 트리
# 자료 구조 : 2차원 리스트 - 도로 정보
#           1차원 리스트 - 최소비용 도로 정보 가져오기 위함.
# [아이디어]
# - 절약할 수 있는 최대 금액이기 때문에 도로 정보 받을때 값을 다 더하고 최소비용 신장 트리를 만들어서 그 값을 빼면 나옴.
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
    newSumValue = 0
    for cost, a, b in edge:
        if find(rt, a) != find(rt, b):
            union(rt, a, b)
            newSumValue += cost
    print(sumValue - newSumValue)

if __name__ == "__main__":
    n, m = map(int, input().split())
    rt = list(map(int, range(n)))
    sumValue = 0
    edge = []
    for _ in range(m):
        x, y, z = map(int, input().split())
        sumValue += z
        edge.append((z, x, y))
    edge.sort()
    solution()

