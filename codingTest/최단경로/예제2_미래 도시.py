# 1 -> X
# 양방향
# 1 -> K -> X
# 문제 유형 : 최단 거리 구하기
# 자료 구조 : 2차원 리스트 - 회사 간 도로 정보
#           1차원 리스트 - 최단 거리 정보
#           time 변수 - 최소 이동 시간
# < 아이디어 >
# - 1번에서 K번 까지의 최단 거리를 구하고 K번에서 X번까지의 최단 거리를 구해서 더함.
# - heapq 이용할 예정.

# [다익스트라를 이용하여 푼 형태]
# import heapq
# def dijkstra(start, end):
#     q = []
#     distance = [1e9] * (n + 1)
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#     while q:
#         dist, node = heapq.heappop(q)
#         if distance[node] < dist:
#             continue
#         for adj in graph[node]:
#             if distance[adj] > dist + 1:
#                 distance[adj] = dist + 1
#                 heapq.heappush(q, (distance[adj], adj))
#     return distance[end]
# def solution():
#     dist_1k = dijkstra(1, k)
#     dist_kx = dijkstra(k, x)
#     return dist_1k + dist_kx
#
# if __name__ == "__main__":
#     n, m = map(int, input().split())
#     graph = [[] for _ in range(n+1)]
#     for i in range(m):
#         a, b = map(int, input().split())
#         graph[a].append(b)
#         graph[b].append(a)
#     x, k = map(int, input().split())
#     print(solution()) if solution() < 1e9 else print(-1)

# [플루이드] 이용한 형태
def solution():
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph[1][k] + graph[k][x]

if __name__ == "__main__":
    INF = int(1e9)
    n, m = map(int, input().split())
    graph = [[INF]*(n+1) for _ in range(n+1)]
    for i in range(n+1): graph[i][i] = 0
    for i in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1
        graph[b][a] = 1
    x, k = map(int, input().split())
    print(solution()) if solution() < INF else print(-1)
