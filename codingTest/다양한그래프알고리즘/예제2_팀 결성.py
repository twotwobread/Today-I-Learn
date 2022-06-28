# 문제 유형 : 서로소 집합 찾기
# 자료 구조 : 2차원 리스트 - 팀 합치기 정보를 저장.
#           1차원 배열 - 노드별 루트 노드 정보 저장.
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]
def union(parent, a, b):
    pA = find(parent, a)
    pB = find(parent, b)
    if pA > pB:
        parent[pA] = pB
    else:
        parent[pB] = pA

if __name__ == "__main__":
    n, m = map(int, input().split())
    rt = list(map(int, range(n+1)))
    for _ in range(m):
        check, a, b = map(int, input().split())
        if check:
            if find(rt, a) == find(rt, b):
                print("YES")
            else:
                print("NO")
        else:
            union(rt, a, b)
