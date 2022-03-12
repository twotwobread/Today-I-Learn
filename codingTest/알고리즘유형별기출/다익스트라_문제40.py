# file name : 다익스트라_문제40.py
# 숨바꼭질
# 술래로부터 잡히지 않도록 숨을 곳을 찾는 중
# 동빈이는 1~N번까지의 헛간 중 하나를 골라 숨을 수 있음.
# 술래는 항상 1번 헛간에서 출발하고 전체 맵에는 총 M개의 양방향 통로 존재
# 하나의 통로는 서로 다른 두 헛간을 연결, 전체 헛간은 어떤 헛간에서 다른 어떤 헛간이든 도달 가능
# 1번 헛간으로부터 최단 거리가 가장 먼 헛간이 가장 안전하다고 판단하고 있음. 
# 최단 거리의 의미는 지나야 하는 길의 최소 개수
# 동빈이가 숨을 헛간의 번호를 출력
# 
# 2 <= N <= 20,000, 1 <= M <= 50,000 
# M개의 줄, 서로 연결된 두 헛간의 번호 , 1 <= A,B <= N
# 
# 거리가 같은 헛간이 여러 개면 가장 작은 헛간 번호를 출력
# 숨어야 하는 헛간 번호, 헛간까지 거리, 같은 거리를 갖는 헛간 개수
# 
# 풀이 시간 : 40분 | 시간 제한 : 1초 | 메모리 제한 : 128MB |
# author : Lee Suyoung(2022-03-12)

import heapq
# n, m 입력
INF = int(1e9)

n, m = map(int, input().split(" "))
# 연결된 헛간 정보 ( M개의 줄 )
graph = [[] for _ in range(n+1)]
distance = [[INF, i] for i in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split(" "))
    graph[a].append(b)
    graph[b].append(a)

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start][0] = 0
    while queue:
        dist, index = heapq.heappop(queue)
        if distance[index][0] < dist:
            continue
        for adj in graph[index]:
            if distance[adj][0] > dist+1:
                distance[adj][0] = dist+1
                heapq.heappush(queue, (distance[adj][0], adj))
    
dijkstra(1)
distance = sorted(distance, key=lambda x: (-x[0], x[1]))
sum = 0
value = distance[1][0]
print("before:",distance)
for i in distance: # 이 부분을 줄일 수 있는 방법있으면 최선일듯
    if value == i[0]:
        sum+=1
print("after:", distance)
print(graph)
print(distance[1][1], distance[1][0], sum)
