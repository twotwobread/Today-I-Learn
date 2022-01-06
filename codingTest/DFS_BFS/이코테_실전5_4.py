# file name : 이코테_실전5_2.py
# N x M 맵, 현재 위치 (1, 1) , 출구 (N, M)
# 괴물 : 0, 이동가능 : 1
# 최소 칸의 개수를 구해라. 시작 칸, 마지막 칸을 모두 포함.
# N, M ( 4 <= N, M <= 200 )
# author : Lee Suyoung (2022-01-06)

# 이 문제는 최소 거리를 구해야한다. DFS를 이용하면 어떻게든 출구까지 가는 여러 방안이 나올 수 있다.
# 하지만 최소거리가 아니다. 그래서 BFS를 이용해보자. 어떤 칸에 도착을 했는데 갈 곳이 없거나 최소거리가 아닌 경우 다른 노드를 생각
# 0과 1이랑 다르게 2로 내 이동 경로를 표시해보자.
from copy import deepcopy
from collections import deque
# bfs
def bfs(maze, route, row, col, before):
    global direction, n, m, queue
    if len(queue) <= 0 : # queue가 비면 끝낸다.
        return
    print(queue)# for test
    x = queue.pop(0) # 자기 자신을 큐에서 뺀다.
    print("pop info : ", x) # for test
    maze[row][col] = 0 # 방문한 노드 처리
    cnt = before + 1 # 이전 노드까지의 거리에서 자기자신을 더함.
    if route[row][col] > cnt or route[row][col] == 1: # 만약 현재 좌표까지의 거리가 모든 루트 중 최소일 경우
        route[row][col] = cnt
    for d in direction: # 북, 동, 남, 서 순으로 돌면서 확인
        nx = row + d[0]; ny = col + d[1]
        if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != 0:
            queue.append((nx, ny, cnt)) # 방문하지 않았고 괴물이 없고 맵을 넘어가지 않으면 큐에 push
    for q in queue:
        bfs(maze, route, q[0], q[1], q[2]) # 재귀 호출



# n, m 입력 및 필요한 변수 선언
n, m = map(int,input().split())
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)] # U, R, D, L (시계방향)
queue = list()
queue.append((0,0,0))
# 맵 상태 입력
maze = []; route = []
for i in range(n):
    maze.append(list(map(int, input()))) # 이렇게 쓰면 바로 int형으로 구할 수 있다.
#print(maze) # for test
route = deepcopy(maze) # 경로를 표시하기 위한 하나의 맵을 더 만듬 
bfs(maze, route, queue[0][0], queue[0][1], queue[0][2])
# 개수 출력
#print(route) # for test
print(route[n-1][m-1])





### [ 제시된 예시 답안 ] ###
n, m = map(int, input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def BFS(x,y):
    # 큐 구현을 위한 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    #큐가 빌 때까지 반복
    while queue:
        # 현재 위치를 pop
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i];
            if nx >= n or nx < 0 or ny >= m or ny < 0: # 맵 상을 벗어난 경우
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록 -> 거리의 크기가 항상 1이기에 먼저 도착하면 거리의 값이 낮을 수 밖에 없음.
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0,0))
