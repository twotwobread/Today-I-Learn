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
# 2초, 512MB
# author : Lee Suyoung (2022-02-08)

# 이거 조합이용봐야겠다.    

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

def dfs(graph, row, col, visited, sum, virusCheck):
    if row<0 or row>=n or col<0 or col>=m or graph[row][col]==1:
        return virusCheck, sum
    if not visited[row][col]:
        if graph[row][col] == 2:
            virusCheck = True
        visited[row][col] = True
        sum += 1
        virusCheck, sum = dfs(graph, row+1, col, visited, sum, virusCheck)
        virusCheck, sum = dfs(graph, row, col+1, visited, sum, virusCheck)
        virusCheck, sum = dfs(graph, row-1, col, visited, sum, virusCheck)
        virusCheck, sum = dfs(graph, row, col-1, visited, sum, virusCheck)
        return virusCheck, sum
    return virusCheck, sum
        
# 모든 조합 만들기
_case = list(combinations(case, 3))
safeCount = 0
for c in _case: # 조합의 모든 경우 수 
    # 방문정보 확인하기 위한 2차원 리스트
    visited = [[False]*m for i in range(n)] #
    temp = []
    x, y, z = c
    temp.append(graph[x[0]][x[1]])
    temp.append(graph[y[0]][y[1]])
    temp.append(graph[z[0]][z[1]])

    graph[x[0]][x[1]] = 1
    graph[y[0]][y[1]] = 1
    graph[z[0]][z[1]] = 1
    
    tempCount = 0
    for row in range(n):
        for col in range(m):
            virusCheck = False
            sum = 0
            if graph[row][col] == 0 and not visited[row][col]:
                virusCheck, sum = dfs(graph, row, col, visited, 0, virusCheck)
                if virusCheck == True:
                    continue
                tempCount += sum

    if safeCount < tempCount:
        safeCount = tempCount
        bestPoint =  c

    graph[x[0]][x[1]] = temp[0]
    graph[y[0]][y[1]] = temp[1]
    graph[z[0]][z[1]] = temp[2]

print(safeCount)


## 아 조합이용하는 거 맞는거 같은데 dfs하는 부분을 다시 생각을 정리해서 풀어야할것 같다. ㅠㅠ
# 내일 다시 풀자 !!
# 2022-02-09 풀었다. 조합을 이용해서 3개 아무거나 뽑아서 그중 가장 작은 값을 출력한다.
# 2를 만나면 이제 virusCheck를 True로 바꾸어 더하지 않도록 만들었다.
# 원래 deepcopy를 이용해서 graph를 계속 복사하면서 돌렸는데 그렇게 하면 시간이 더 오래걸릴것이라
# 예상하여 graph의 값을 계속바꾸면서 반복했다.
# 근데 이게 2초인데 시간이 3680ms = 3.68초가 걸렸다. 근데 통과가 되었다.
# 일단 계산을 해보면 최대 8x8의 판이고 2를 최저로 2개 그거말고 다 빈칸이라 가정.
# 62개 중에서 3개를 뽑아야한다 => 37,820개의 가짓수가 있다. 이걸 하나할때마다. for문은 64번이 돌고
# 거기에 dfs가 최대한 들어간다면 61번이라고 생각-> 재귀라서 다시 나온다. 122번
# 대략적으로 122x1+61*37,820 = 2,420,480 + 122 정도인데 재귀의 오버헤드가 굉장히 많이 잡아먹는 것 같다.
 
