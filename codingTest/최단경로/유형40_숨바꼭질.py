# 문제 유형: 최단 거리 찾기
# 자료 구조 : 2차원 배열 - 노드 간 연결 정보
#           1차원 배열 - 최단 거리 정보
#           heapq - 최단 거리 노드 도출
import heapq
def dijkstra(start):
    distance = [INF]*(n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for adj in graph[node]:
            cost = dist + 1
            if distance[adj] > cost:
                distance[adj] = cost
                heapq.heappush(q, (cost, adj))
    return distance
def solution():
    dist = dijkstra(1)
    maxValue = max(dist[1:])
    print(dist.index(maxValue), maxValue, dist.count(maxValue))

if __name__ == "__main__":
    INF = int(1e9)
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    solution()
