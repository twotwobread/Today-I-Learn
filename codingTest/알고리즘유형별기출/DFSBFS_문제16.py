# file name : DFSBFS_문제16.py
# 연구소
# 크기가 NxM인 직사각형으로 나타내고 직사각형은 1x1 크기의 정사각형으로 나누어져 있다.
# 연구소는 빈칸, 벽으로 이루어져 있고, 벽은 칸 하나를 가득 차지한다.
# 일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈칸으로 모두 퍼져나갈 수 있다.
# 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.
# 0 = 빈칸, 1 = 벽, 2 = 바이러스
# 3 <= N,M <= 8 ( 세로크기(행), 가로 크기(열) )
# 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수입니다.
# 빈칸의 개수는 3개 이상입니다.
# author : Lee Suyoung (2022-02-08)

# 잠만 이거 조합이용봐야겠다.

def dfs(row, col, visited, sum):
    if row<0 or row>=n or col<0 or col>=m or graph[row][col] == 1 or visited[row][col] == True:
        return sum
    if graph[row][col] == 2:
        return -1
    elif graph[row][col] == 0:
        visited[row][col] = True
        direct1 = dfs(row+1, col, visited, sum+1)
        if direct1 == -1:
            return -1
        direct2 = dfs(row-1, col, visited, direct1)
        if direct2 == -1:
            return -1
        direct3 = dfs(row, col+1, visited, direct2)
        if direct3 == -1:
            return -1
        direct4 = dfs(row, col-1, visited, direct3)
        if direct4 == -1:
            return -1
        return direct4

from itertools import *
import sys
input = sys.stdin.readline
INF = int(1e9)

# n, m 입력
n, m = map(int, input().split())

# graph 정보 입력, 조합을 위한 빈칸 인덱스의 행, 열 찾기
graph = []
case = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 0:
            case.append((i,j))

_case = list(combinations(case, 3))
print(_case)
safeCount = 0

for c in _case:
    # 방문정보 확인하기 위한 2차원 리스트
    visited = [[False]*m for i in range(n)]
    temp=[]
    x, y, z = c 
    temp.append(graph[x[0]][x[1]])
    temp.append(graph[y[0]][y[1]])
    temp.append(graph[z[0]][z[1]])

    graph[x[0]][x[1]] = 1
    graph[y[0]][y[1]] = 1
    graph[z[0]][z[1]] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                num = dfs(i,j,visited, 0)
                if num == -1:
                    continue
                cnt += num
    if safeCount < cnt:
        best = c
        safeCount = cnt
    
    graph[x[0]][x[1]] = temp[0]
    graph[y[0]][y[1]] = temp[1]
    graph[z[0]][z[1]] = temp[2]
print(safeCount)
print(best)

## 아 조합이용하는 거 맞는거 같은데 dfs하는 부분을 다시 생각을 정리해서 풀어야할것 같다. ㅠㅠ
# 내일 다시 풀자 !!
