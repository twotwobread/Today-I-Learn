# file name : 이코테_실전9_2.py
# 미래 도시
# 미래 도시는 1 ~ N번 도시까지의 회사가 있음. 
# 특정 회사끼리는 서로 도로를 통해 연결
# A는 현재 1번 회사에 위치해 있고, X번 회사에 방문해 물건을 판매하고자 한다.
# 연결된 2개의 회사는 양방향으로 이동할 수 있다.
# 도로로 연결되어있으면 1만큼의 시간으로 이동 가능하다.
# 또한 A는 소개팅에도 참석할 생각이다. 소개팅 상대는 K번 회사에 존재한다.
# A는 방문 판매하기 전에 K번 회사에 가서 커피를 마시고 X번 회사로 갈 생각이다. ( 1 -> K -> X )
# A는 가능한 가장 빠르게 이동하고 한다.
# A가 회사 사이를 이동하게 되는 최소 시간을 계산하는 프로그램을 작성하시오 ( 소개팅 상대와 커피 마시는 시간은 고려 X )
# 1 <= N, M <= 100 공백으로 구분 , 2 ~ M+1 번째 줄 연결된 회사의 번호가 공백으로 구분되어 주어짐.
# 1<=K<=100 X,K 공백으로 구분
# author : Lee Suyoung (2022-02-05)

# 플로이드 사용하면 좋을 듯 노드의 수도 적고 간선의 수도 적음.
# 그리고 1->K, K->X  이 두개의 이동 경로의 합을 구해야함.
# 양방향이기에 간선 정보 받아 값을 넣을 때 양방향으로 넣어줘야할듯.
# 잠만 근데 중요한게 여기에는 비용이 없음. 그래서 그냥 1을 넣어주면 될듯.

import sys
input = sys.stdin.readline
INF = int(1e9)

# n,m 입력
n, m = map(int, input().split())
# 필요한 리스트 초기화 및 간선 정보 입력
graph = [[INF]*(n+1) for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1 # 비용을 1로 넣어주는 모습
    graph[b][a] = 1 # 양방향 때문에

# X, K 정보 입력
x, k = map(int, input().split())

for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

result = graph[1][k] + graph[k][x]
if result >= INF:
    print("-1")
else:
    print(result)

# 제시된 답안과 똑같음
# 해당 문제는 전형적인 플로이드 워셜 알고리즘 문제이다. 현재 문제에서 N의 범위가 100 이하로 매우 한정적이다. 따라서 플로이드 워셜 알고리즘을 이용해도 빠르게
# 풀 수 있기 때문에, 구현이 간단한 플로이드 워셜 알고리즘을 이용하는 것이 유리하다. 이 문제의 핵심 아이디어는 1번 노드에서 K를 거쳐 X로 가는 최단 거리라는 
# 점이다. 최단 거리 문제는 그림으로 먼저 그려보는 것도 좋은 방법이다.
