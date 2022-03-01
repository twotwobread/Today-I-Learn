# file name : 그래프이론_문제43.py
#
# N개의 집, M개의 도로로 구성
# 각 집은 0 ~ N-1번까지의 번호로 구분
# 모든 도로 가로등 구비 -> 특정 도로의 가로등을 하루 동안 켜기 위한 비용 == 해당 도로의 길이
# 일부 가로등을 비활성화하되, 마을에 있는 임의의 두 집에 대하여 가로등이 켜진 도로만으로도 오갈 수 있도록 만들자.
# 최대한 많은 비용을을 절약하고자 하는데 일부 가로등을 비활성화 했을때 절약할 수 있는 최대 금액을 출력하는 프로그램 작성.
#
# 집의수  1 <= N <= 200,000 , 도로의 수  N-1 <= M <= 200,000
# M개의 줄 , 각 도로에 대한 정보 X, Y, Z 공백 구분 ( 0<= X, Y < N )
# X, Y 사이에 양방향 도로가 있고 그 길이가 Z라는 의미, X와 Y는 같은 경우가 없고 모든 도로의 길이 합은 2^31보다 작음.
# 풀이 시간 : 40분 | 시간 제한 : 1초 | 메모리 제한 : 128MB
# author : Lee Suyoung(2022-03-01)

# 최소 신장 트리 인가 그느낌.

# 필요한 함수
def FindParent(x, parent):
    if parent[x] != x:
        parent[x] = FindParent(parent[x], parent)
    return parent[x]
def UnionParent(a, b, parent):
    a = FindParent(a, parent)
    b = FindParent(b, parent)
    if (a < b):
        parent[b] = a
    else:
        parent[a] = b

# n, m 입력
n, m = map(int, input().split(" "))
# 필요한 변수, 리스트 선언 및 초기화
parent = [[0] for _ in range(n)]
for i in range(n):
    parent[i] = i
edge = []
# m개 줄, 도로에 대한 정보
sum = 0
for _ in range(m):
    x, y, z = map(int, input().split(" "))
    edge.append((z,x,y))
    sum += z

edge.sort()
result = 0
for e in edge:
    z, x, y = e
    if FindParent(x, parent) != FindParent(y, parent):
        UnionParent(x, y, parent)
        result += z

print(sum - result)
