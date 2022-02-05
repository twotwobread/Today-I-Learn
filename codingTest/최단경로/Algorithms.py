#간단한 다익스트라 알고리즘 소스코드

from dis import dis
import sys
input = sys.stdin.readline
INF = int(1e9) # 10억으로 무한을 의미하는 값 선언.

# 노드 개수, 간선 개수 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
# 인접 노드 리스트
graph = [[] for i in range(n+1)]
# 방문한 적 있는지를 체크하기 위한 리스트
visited = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a,b,c = map(int, input().split()) # a번 노드에서 b번 노드로 가는 비용이 c라는 의미.
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환.
def get_smallest_node():
    min_value = INF
    index=0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]: # min_value보다 작고 방문한적 없으면
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1] # 아까 간선의 정보를 얻은 것을 바탕으로 시작노드의 인접한 노드의 최단 거리에 비용을 넣는 과정
    # 시작 노드를 제외한 전체 n-1 개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]: 
            cost = distance[now] + j[1] # 현재 노드까지의 거리 플러스 인접한 노드까지의 거리 => 인접한 노드의 거리
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]: # 현재 인접한 노드까지의 거리, 아직 나오지 않은 경우엔 INF를 이용하여 굉장히 큰 값일 것이다.
                distance[j[0]] = cost

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 거리의 경우
    else:
        print(distance[i])

# 시간 복잡도: O(V^2)이다, 총 O(V)에 걸쳐서 최단 거리가 가장 짧은 노드를 매번 선형 탐색해야 하고, 현재 노드와 연결된 노드를 매번 일일이 확인하기 때문이다.
# 따라서 코딩 테스트의 최단 경로 문제에서 전체 노드의 개수가 5,000개 이하라면 일반적으로 이 코드로 문제를 풀 수 있다. 하지만 10,000개를 넘어가는 문제라면
# 이 코드로 해결하긴 어렵다. 노드의 개수 및 간선의 개수가 많을 때는 이어서 설명할 '개선된 다익스트라 알고리즘'을 사용해야 한다.

# 개선된 다익스트라 알고리즘
# 시간 복잡도 최악의 경우에도 O(ElogV)를 보장하여 해결할 수 있다. - E는 간선의 개수(Edge), V는 노드의 개수(Vertex)
# 간단한 알고리즘은 최단 거리가 가장 짧은 노드를 찾기 위해서, 매번 최단 거리 테이블을 선형적으로 탐색해야 했다. 이 과정에서만 O(V) 만큼 시간이 걸렸다.
# 하지만 최단 거리가 가장 짧은 노드를 단순히 선형적으로 찾는 것이 아니라 더 빠르게 찾을 수 있다면 시간 복잡도가 줄을 것이다.
# 간단한 다익스트라 알고리즘에서 사용했던 get_smallest_noe()라는 함수와 visited라는 리스트도 필요없을 것이다.
# heapq라는 자료구조를 사용함으로써 필요가 없다.

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 받기
start = int(input())
# 각 노드의 인접노드를 위한 리스트 만들기
graph = [[] for i in range(n+1)]
# 최단 거리 테이블 만들기
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(n+1):
    a,b,c = map(int, input().split())#간단한 다익스트라 알고리즘 소스코드

from dis import dis
import sys
input = sys.stdin.readline
INF = int(1e9) # 10억으로 무한을 의미하는 값 선언.

# 노드 개수, 간선 개수 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
# 인접 노드 리스트
graph = [[] for i in range(n+1)]
# 방문한 적 있는지를 체크하기 위한 리스트
visited = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a,b,c = map(int, input().split()) # a번 노드에서 b번 노드로 가는 비용이 c라는 의미.
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환.
def get_smallest_node():
    min_value = INF
    index=0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]: # min_value보다 작고 방문한적 없으면
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1] # 아까 간선의 정보를 얻은 것을 바탕으로 시작노드의 인접한 노드의 최단 거리에 비용을 넣는 과정
    # 시작 노드를 제외한 전체 n-1 개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]: 
            cost = distance[now] + j[1] # 현재 노드까지의 거리 플러스 인접한 노드까지의 거리 => 인접한 노드의 거리
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]: # 현재 인접한 노드까지의 거리, 아직 나오지 않은 경우엔 INF를 이용하여 굉장히 큰 값일 것이다.
                distance[j[0]] = cost

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 거리의 경우
    else:
        print(distance[i])

# 시간 복잡도: O(V^2)이다, 총 O(V)에 걸쳐서 최단 거리가 가장 짧은 노드를 매번 선형 탐색해야 하고, 현재 노드와 연결된 노드를 매번 일일이 확인하기 때문이다.
# 따라서 코딩 테스트의 최단 경로 문제에서 전체 노드의 개수가 5,000개 이하라면 일반적으로 이 코드로 문제를 풀 수 있다. 하지만 10,000개를 넘어가는 문제라면
# 이 코드로 해결하긴 어렵다. 노드의 개수 및 간선의 개수가 많을 때는 이어서 설명할 '개선된 다익스트라 알고리즘'을 사용해야 한다.

# 개선된 다익스트라 알고리즘
# 시간 복잡도 최악의 경우에도 O(ElogV)를 보장하여 해결할 수 있다. - E는 간선의 개수(Edge), V는 노드의 개수(Vertex)
# 간단한 알고리즘은 최단 거리가 가장 짧은 노드를 찾기 위해서, 매번 최단 거리 테이블을 선형적으로 탐색해야 했다. 이 과정에서만 O(V) 만큼 시간이 걸렸다.
# 하지만 최단 거리가 가장 짧은 노드를 단순히 선형적으로 찾는 것이 아니라 더 빠르게 찾을 수 있다면 시간 복잡도가 줄을 것이다.
# 간단한 다익스트라 알고리즘에서 사용했던 get_smallest_noe()라는 함수와 visited라는 리스트도 필요없을 것이다.
# heapq라는 자료구조를 사용함으로써 필요가 없다.

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 받기
start = int(input())
# 각 노드의 인접노드를 위한 리스트 만들기
graph = [[] for i in range(n+1)]
# 최단 거리 테이블 만들기
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = [] # 우선순위 큐를 위한 리스트
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: #큐가 비어있지 않으면
        dist, now = heapq.heappop(q) # 우선순위 큐이기에 가장 우선순위가 낮은 ( 가장 최단 거리가 짧은 ) 노드에 대한 정보 꺼내기
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시 ( 맞네 인접한 노드가 겹칠 수 있으니까 )
        if distance[now] < dist: # 아까 말했던게 다익스트라는 한번 처리되면 그 이하로 최단 거리가 줄지 않기 때문에 이런 조건으로 확인가능.
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])


# 플루이드 워셜 알고리즘
INF = int(1e9)

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())

# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n+1) for i in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용을 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INFINITY")
        else:
            print(graph[a][b], end=" ")
    print()


    graph[a].append((b,c))

def dijkstra(start):
    q = [] # 우선순위 큐를 위한 리스트
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: #큐가 비어있지 않으면
        dist, now = heapq.heappop(q) # 우선순위 큐이기에 가장 우선순위가 낮은 ( 가장 최단 거리가 짧은 ) 노드에 대한 정보 꺼내기
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시 ( 맞네 인접한 노드가 겹칠 수 있으니까 )
        if distance[now] < dist: # 아까 말했던게 다익스트라는 한번 처리되면 그 이하로 최단 거리가 줄지 않기 때문에 이런 조건으로 확인가능.
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])


# 플루이드 워셜 알고리즘
INF = int(1e9)

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())

# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n+1) for i in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용을 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INFINITY")
        else:
            print(graph[a][b], end=" ")
    print()

