# file name : 이코테_실전10_2.py
# 팀 결성 
# 학생들에게 0 ~ N번까지 번호 부여함.
# 처음에는 모든 학생이 서로 다른 팀으로 구분 -> N+1개의 팀 존재
# 팀 합치기 연산과 같은 팀 여부 확인 연산을 선생이 사용가능
# 선생이 M개의 연산을 수행 가능할때, 같은 팀 여부 확인 연산에 대한 연산 결과를 출력하는 프로그램을 작성
# 1 <= N, M <= 100,000
# 팀 합치기 = 0, a, b / a와 b 팀합치기 , 같은 팀 확인 = 1, a, b/ a와 b 같은 팀 여부 확인
# a와 b는 N 이하의 양의 정수
# author : Lee Suyoung (2022-02-06)

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

def find_team(parent, a, b):
    if find_parent(parent, a) == find_parent(parent, b):
        print("YES")
    else:
        print("NO")


n, m = map(int, input().split())
parent = [0] * (n+1)
result=[]

for i in range(n+1):
    parent[i] = i

for _ in range(m):
    type, a, b = map(int, input().split())
    if type == 0:
        union_parent(parent, a, b)
    elif type == 1:
        find_team(parent, a, b)


# 제시된 답안과 같음.
# 전형적인 서로소 집합 알고리즘 문제로 N과 M의 범위가 모두 최대 100,000이라서 경로 압축 방식의 서로소 집합 자료구조를 이용하여 시간 복잡도를 개선해야한다.
