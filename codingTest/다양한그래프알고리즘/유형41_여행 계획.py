# 문제 유형 : 서로소 집합
# 자료 구조 : 1차원 배열 - 루트 노드 정보
#           2차원 배열 - 여행지 정보
# [ 아이디어 ]
# - 서로소 집합을 이용하여 도로의 정보와 같이 집합을 구성하고 루트 노드가 같으면 갈 수 있는 것이고
#   같지 않으면 갈 수 없다.
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
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 and find(rt, i) != find(rt, j):
                union(rt, i, j)
    check = find(rt, plan[0])
    for p in plan[1:]:
        if check != find(rt, p):
            break
    else:
        return print("YES")
    return print("NO")

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    plan = list(map(int, input().split()))
    rt = list(map(int, range(n)))
    solution()
