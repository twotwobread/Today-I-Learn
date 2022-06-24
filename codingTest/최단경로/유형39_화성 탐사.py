# 문제 유형 : 최단 거리 찾기
# 일반적으로 최단 거리 찾기 할때 지금까지는 노드의 연결 정보를 받았는데
# 이 문제는 2차원 배열로 준다.
# 생각해보면 그냥 모든 인덱스가 전부 노드인것이고 상,하,좌,우 인덱스와
# 양방향으로 연결된 노드들이라고 생각하면 된다.
# 그래서 똑같이 하는데 인접 노드는 상, 하, 좌, 우의 노드들이라고 생각하고
# 거기에 대해서 최단 거리를 구하면 된다.

import heapq
def solution():
    dist = [[INF]*n for _ in range(n)]
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    dist[0][0] = graph[0][0]
    while q:
        distance, x, y = heapq.heappop(q)
        if dist[x][y] < distance:
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                cost = distance + graph[nx][ny]
                if dist[nx][ny] > cost:
                    dist[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))
    print(dist[n-1][n-1])

if __name__ == "__main__":
    INF = int(1e9)
    dx = (0, -1, 0, 1)
    dy = (-1, 0, 1, 0)
    T = int(input())
    for _ in range(T):
        n = int(input())
        graph = [list(map(int, input().split())) for _ in range(n)]
        solution()
#
# 3
# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 답 : 20
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 답 : 19
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4
# 답 : 36
