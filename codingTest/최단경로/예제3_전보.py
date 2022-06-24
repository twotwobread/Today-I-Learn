# 문제 유형 : 최단 거리 구하기
# 자료 구조 : 2차원 리스트 - 통로에 대한 정보
#           1차원 리스트 - 최단 거리 정보
#           heapq - 우선순위가 거리로 정렬된 queue를 얻기 위함.
# [아이디어]
# - c에서 최단 거리 리스트를 만들고 리스트 길이에서 INF인 개수를 빼면 도시 개수가 나옴.
# - 리스트 최대 원소 값을 도출하면 총 걸리는 시간임.
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
            adj_node, time = adj
            if distance[adj_node] > dist + time:
                distance[adj_node] = dist + time
                heapq.heappush(q, (distance[adj_node], adj_node))
    return distance
def solution():
    table = dijkstra(c)
    print(len(table)-table.count(INF)-1, end=" ")
    print(max(list(filter(lambda x:x != INF, table))))

if __name__ == "__main__":
    INF = int(1e9)
    n, m, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, t = map(int, input().split())
        graph[a].append((b, t))
    solution()
