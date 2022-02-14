# file name : DFSBFS_문제15.py
# 특정 거리의 도시 찾기
# 어떤 나라에 1 ~ N번까지 도시와 M개의 단방향 도로가 존재, 모든 도로의 거리는 1
# 이떄 특정 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시의 번호를 출력하는 프로그램 작성
# 출발 도시 X에서 출발 도시 X는 항상 0
# 2 <= N <= 300,000, 1 <= M <= 1,000,000, 1 <= K <= 300,000, 1 <= X <= N
# 위는 도시의 개수, 도로의 개수, 거리 정보 , 출발도시의 번호
# 둘째 줄 부터 M개 의 줄에 걸쳐 A, B ( 1 <= A,B <= N) 단, A와 B는 서로 다른 자연수
# 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력
# 존재하지 않을 경우 -1출력
# 풀이 시간 : 30분, 시간 제한 : 2초, 메모리 제한 : 256MB
# author : Lee Suyoung (2022-02-14)

from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

# n, m, k, x 입력
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
# 거리 정보 입력 M개
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
# 다익스트라 이용하자. 아래 알고리즘은 다익스트라라고 하기엔 노드 중 가장 짧은 distance를 생각하지 않아서 어려움이 있음.
# 이게 가능한 이유는 모든 거리가 1이라서 가능함.
def dijkstra(start):
    q = deque() # 거리가 전부 1이라서 heapq 쓰지 않고 이걸로 했음. 
    q.append(start) # heapq를 썼으면 더 줄일 수 있음. queue에 들어올때가 가장 작은 거리 값을 가지고 있기 때문에 맨밑에 반복문이 필요없음.
    distance[start] = 0
    while q: 
        now = q.popleft()
        for i in graph[now]:
            if distance[i] > distance[now] + 1:
                distance[i] = distance[now] + 1
                q.append(i)

dijkstra(x)
# 시간을 조금 더 줄이기 위해서 스트링을 이용해서 한번에 출력
result = ""
for i in range(1, n+1):
    if distance[i] == k:
        result += (str(i)+"\n")
if result == "":
    print("-1")
else:
    print(result)

# 1904ms 나옴.
