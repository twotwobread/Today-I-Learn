# 문제 유형 : 최단 거리 구하기
# 자료 구조 : 2차원 리스트 - 버스 정보 저장
#           1차원 리스트 - 최단 거리 정보
#           heapq - 최단 거리 노드 도출을 위함
def floyd_warshall():
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j: graph[i][j] = 0
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
def solution():
    floyd_warshall()
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] == INF: print(0, end=" ")
            else: print(graph[i][j], end=" ")
        print()

if __name__ == "__main__":
    INF = int(1e9)
    n = int(input())
    m = int(input())
    graph = [[INF]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        a, b, cost = map(int, input().split())
        graph[a][b] = min(graph[a][b], cost)
    solution()
