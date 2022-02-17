# file name : 다익스트라_문제38.py
# 정확한 순위
# 선생님은 시험을 본 학생 N명의 성적을 분실하고, 성적을 비교한 결과의 일부만 가지고 있다.
# 학생 N명의 성적은 모두 다른데, 다음은 6명의 학생에 대하여 6번만 성적을 비교한 결과이다.
# 1번 < 5번, 3번 < 4번, 4번 < 2번, 4번 < 6번, 5번 < 2번, 5번 < 4번
# 2 <= N <= 500, 학생들의 수   2 <= M <= 10,000 성적을 비교한 횟수
# M개의 각 줄에는 두 학생의 성적을 비교한 결과를 나타내는 두양의 정수 a, b -> a < b라는 의미
# author : Lee Suyoung(2022-02-17)

# INF = int(1e9)

# #n,m 입력
# n, m = map(int, input().split())
# graph = [[INF]*(n+1) for _ in range(n+1)]

# for i in range(1, n+1):
#     graph[i][i] = 0

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a][b] = 1

# for k in range(1, n+1):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

# result=0
# for i in range(1, n+1):
#     cnt = 0
#     for j in range(1, n+1):
#         if i != j and (graph[i][j] != INF or graph[j][i] != INF):
#             cnt += 1
#     if cnt == n-1:
#         result+=1 
# print(result)

# 근데 O(N^3)인데 플루이드 시간 복잡도가 최대 500개의 노드가 있는데 이걸 쓰는게 가능한가?
# 노드별로 다익스트라 돌려보자.

import heapq

INF = int(1e9)
n,m = map(int, input().split(" "))
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split(" "))
    graph[a].append((b,1))

countList = [0] * (n+1)
for i in range(1, n+1): # 500
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0, i))
    distance[i] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        countList[now] += 1
        countList[i] += 1
        for adj in graph[now]:
            adjNode, adjDist = adj
            if distance[adjNode] > distance[now] + adjDist:
                distance[adjNode] = distance[now] + adjDist
                heapq.heappush(q, (distance[adjNode], adjNode))
result = 0
for i in range(1,n+1):
    if (countList[i]-1) == n:
        result += 1
print(result)

# 다익스트라 알고리즘 시간 복잡도가 O(ElogV) 이니까 
# 최대 10000 * log500 근데 이걸 모든 노드에 대해서 돌리니까 곱하기 500 -> 천만 정도 거기에 500을 더해서 고정도 나올 것 같다.
# 플루이드보다는 빠를것 같다.

