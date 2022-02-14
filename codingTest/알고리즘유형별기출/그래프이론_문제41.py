# file name : 그래프이론_문제41.py
# author : Lee Suyoung(2022-02-14)
# N개의 줄에 걸쳐 NxN 행렬을 통해 두 여행지가 서로 연결되어 있는지의 여부가 주어짐.
# 여행지의 번호들이 주어지며 공백으로 구분

# 여행지의 번호들의 부모가 다 같으면 여행 계획이 가능함.
import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# n, m 입력 , 여행지의 수와 여행 계획에 속한 도시의 수
n, m = map(int, input().split())
parent = [0]*(n)
for i in range(n):
    parent[i] = i
# 연결 여부 입력
graph = [[0]*(n) for _ in range(n)] # 연결되어 있는 지 확인하기 위한 그래프
for i in range(n):
    array = list(map(int, input().split()))
    graph[i] = array
    for j in range(n):
        if graph[i][j] == 1:
            union_parent(parent, i, j) # 서로소 union 시행
# 여행 계획 입력
plan = list(map(int, input().split()))
# 여행 계획 가능한지 find_parent 실행
check = "YES"
for i in plan[1:]:
    if find_parent(parent, plan[0]) == find_parent(parent, i):
        continue
    else:
        check="NO"
        break
print(check)
        
