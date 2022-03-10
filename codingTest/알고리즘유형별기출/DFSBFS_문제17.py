# file name : DFSBFS_문제17.py
#
# 경쟁적 전염
# NxN 크기의 시험관 존재, 특정 위치에는 바이러스 존재.
# 바이러스의 종류는 1~K번까지 K가지 존재, 모든 바이러스는 이 중 하나에 속함.
# 1초마다 상,하,좌,우의 방향으로 증식, 매초 번호가 낮은 종류의 바이러스부터 증식
# 또한 증식 과정에서 특정한 칸에 이미 어떤 바이러스가 있다면
# 다른 바이러스는 들어갈 수 없음.
#
# 1 <= N <= 200, 1<= K <= 1,000
# N개의 줄 시험관의 정보
# S, X, Y 공백으로 구분하여 주어짐 ( S초 뒤에 X, Y에 존재하는 바이러스의 종류)
# author : Lee Suyoung(2022-03-10)

# 토마토 푼 것처럼 풀면 될듯.

# n, k 입력
from collections import deque
import heapq
n, k = map(int, input().split(" "))
# n개의 줄 시험관의 정보 입력
graph = [list(map(int,input().split(" "))) for _ in range(n)]
# s, x, y 입력
s, x, y = map(int, input().split(" "))

# 먼저 heapq를 이용해서 우선순위 바이러스로 담고 한 라운드에 있는 바이러스는
# 한라운드에 다 처리하는 방식으로 조지자
# 현재 바이러스 있는 시험관 담기
queue = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            queue.append((graph[i][j], i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(graph, queue, sec, goal):
    while queue:
        queue.sort()
        if sec == goal:
            break
        lenQueue = len(queue)
        for _ in range(lenQueue):
            virus, row, col = queue.pop(0)
            for j in range(4):
                adjRow, adjCol = row+dx[j], col+dy[j]
                if 0<=adjRow<n and 0<=adjCol<n and graph[adjRow][adjCol] == 0:
                    graph[adjRow][adjCol] = virus
                    queue.append((virus, adjRow, adjCol))
        sec += 1
bfs(graph, queue, 0, s)
print(graph[x-1][y-1])
