# file name : 이코테_실전9_3.py
# 전보
# 어떤 나라에는 N개의 도시가 있고 각 도시는 보내자 하는 메시지가 있는 경우, 다른 도시로 전보를 보내 메시지를 전송할 수 있다.
# 하지만 X라는 도시에서 Y라는 도시로 전보를 보내고자 한다면, 도시 X에서 Y로 향하는 통로가 설치되어 있어야 한다.
# 예를 들어, X에서 Y로 향하는 통로는 있는데 Y에서 X로 향하는 통로가 없다면 전보를 보낼 수 없다. 또한 통로를 거쳐 메시지를 보낼 땐 일정 시간이 소요된다.
# C라는 도시에서 최대한 많은 도시로 메시지를 보내고자 한다.
# 각 도시의 번호와 통로가 설치되어 있는 정보가 주어졌을 때, 도시 C에서 보낸 메시지를 받게 되는 도시의 개수는 총 몇 개이며
# 도시들이 모두 메시지를 받는 데까지 걸리는 시간은 얼마인지 계산하는 프로그램 작성
# 1 <= N <= 30,000, 1<=M<=200,000, 1<=C<=N 공백으로 구분
# 1<=X, Y<=N, 1<=Z<=1,000 
# author : Lee Suyoung (2022-02-05)

# 일단 무조건 다익스트라를 이용해야 함. 플로이드는 너무 노드가 많다.
# 내 생각엔 다익스트라를 구현하고 함수를 사용할 때 모든 C에서 모든 노드로 뿌리면 될듯
# distance 봤을 때, INF 면 도달못하는거네 그냥
# 총 걸리는 시간은 가장 큰 시간을 하면 되겟다.

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

# n, m, c 입력 ( 노드 개수, 간선 개수, start)
n, m, c = map(int, input().split())

# graph 초기화 및 간선 정보 입력
graph = [[] for _ in range(n+1)]

for _ in range(m):
    # x,y,z 입력 ( 간선 정보, cost)
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

# distance 초기화
distance = [INF] * (n+1)

def dijkstra(start):
    q=[]
    distance[start] = 0
    heapq.heappush(q, (distance[start], start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

dijkstra(c)

count = 0
max_value = -1
for i in range(1, n+1):
    dist = distance[i]
    if dist==0 or dist==INF:
        continue
    count+=1
    if max_value < dist:
        max_value = dist

print(count, max_value)

### [ 제시된 답안 ] ###
# 마지막 출력부분만 다름.
# 이게 훨씬 파이썬을 잘이용한 것 같다.
# 그리고 자기 자신만 빼면 되는 걸 나 처럼하면 조건문이 길어져서 더 깔끔하지 못하다.
# 그리고 비교문을 할때 비교 대상의 위치를 한쪽으로 고정해야 코드를 읽을 때 더 잘읽히는 것 같다.
count = 0
max_value = 0
for d in distance:
    if d != INF:
        count += 1
        max_value = max(max_value, d)
    
print(count-1, max_value)
