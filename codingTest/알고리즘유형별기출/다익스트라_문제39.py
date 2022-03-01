# file name : 다익스트라_문제39.py
# 
# 화성 탐사
# 화성은 에너지 공급원 찾기가 힘듬. 그래서 항상 죄적의 경로를 찾도록 개발
# 기계가 존재하는 공간은 N x N, 각각의 칸을 지나기 위한 비용이 존재.
# [0][0]에서 [N-1][N-1] 위치로 이동하는 최소 비용을 출력하는 프로그램 작성
# 특정 위치에서 상하좌우 인접한 곳으로 1칸씩 이동 가능.
#
# 테스트 케이스의 수  1 <= T <= 10
# 매 테스트 케이스의 첫째 줄, 탐사 공간의 크기  2 <= N <= 125
# N개의 줄에 걸쳐 공백으로 구분되는 각 칸의 비용  0 <= 각 칸의 비용 <= 9
# 풀이 시간 : 40분 | 시간 제한 : 1초 | 메모리 제한 : 128MB |
# author : Lee Suyoung (2022-03-01)

import heapq

# t 입력
t = int(input())
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 반복문 돌면서 n 입력
for _ in range(t):
    n = int(input())
    # 반복문 돌면서 각 칸의 비용 입력
    graph = []
    distance = [[INF]*n for _ in range(n)]
    for _ in range(n):
        graph.append(list(map(int, input().split(" "))))
    # 최소 비용 찾기
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = graph[0][0]
    while q:
        dist, x, y = heapq.heappop(q)
        if dist > distance[x][y]:
            continue
        for i in range(4):
            a, b = x+dx[i], y+dy[i]
            if a < 0 or a >= n or b < 0 or b >= n:
                continue
            if distance[a][b] > dist + graph[a][b]:
                distance[a][b] = dist + graph[a][b]
                heapq.heappush(q, (distance[a][b], a, b))
    print(distance[n-1][n-1])


