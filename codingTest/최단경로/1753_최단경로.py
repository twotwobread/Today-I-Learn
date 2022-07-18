# 주어진 시작점에서 다른 모든 정점으로의 최단 경로
# 모든 간선의 가중치는 10 이하의 자연수

# 1<=V<-20,000, 1<=E<=300,000
# ElogV 느낌으로다가 하면 될듯.
import heapq
def dijkstra(start):
    distance = [INF]*(v+1)
    q = []
    heapq.heappush(q, (0, start)) 
    distance[start] = 0
    while q:
        dist, index = heapq.heappop(q)
        if dist > distance[index]:
            continue
        for adjIndex, adjDist in graph[index]:
            if distance[adjIndex] > dist + adjDist:
                distance[adjIndex] = dist + adjDist
                heapq.heappush(q, (distance[adjIndex], adjIndex))
    return distance

if __name__ == "__main__":
    INF = int(1e9)
    v, e = map(int, input().split())
    start = int(input())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        u,v_v,w = map(int, input().split())
        graph[u].append((v_v,w))
    result = dijkstra(start)
    for i, value in enumerate(result[1:]):
            if value != INF: print(value)
            else: print('INF')

