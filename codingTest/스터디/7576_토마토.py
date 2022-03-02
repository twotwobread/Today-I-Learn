# file name : 7576_토마토.py
#
# 창고 토마토 중에는 잘 익은 것도 있고 안익은 것도 있음.
# 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은
# 익은 토마토의 영향을 받아 익게 된다. 인접한 토마토는 상하좌우를 의미.
# 대각선은 영향이 없고 혼자 저절로 익는 경우는 없다고 가정.
# 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 최소 일수를 알고 싶음.
# 단, 상자의 일부 칸에는 토마토가 없을 수도 있다.
#
# 2 <= M, N <= 1,000  상자의 가로 칸수, 세로 칸수
# N개의 줄에 상자에 담긴 토마토의 정보
# 1 : 익은 토마토, 0 : 익지 않은 토마토, -1 : 토마토가 없는 칸
# 토마토가 하나 이상 있는 경우만 입력으로 주어짐.
# 저장될 때부터 모든 토마토가 익어있으면 0을 출력, 토마토가 모두 익을 수 없으면 -1을 출력.
#
# 시간 제한 : 1초 | 메모리 제한 : 256MB | 
# author : Lee Suyoung (2022-03-02)

# 중요한게 일 수를 세는 방법이 빡씰꺼 같은데
# -1을 토마토가 없으니까 -1을 만나거나 범위를 넘는 경우 글로는 더 못가는 거지.
# bfs 써야하는 거 아님? 1인 익은 토마토를 찾고 거기서 부터 출발 
# 인접한 거 넣으면서 다음꺼 넣을때 1증가
# 그리고 하나 들어가서 다 찾았고 -1이나 범위 벗어나서 끝났으면 다른 1 찾는데
# 일수를 더하는게 아니라 더 큰걸 출력해야함.
# 일단 0, -1을 출력하는 상황은 예외니까 빼놓고 다른걸 먼저 구현하자.

from collections import deque

dx = [1, 0, -1, 0] # 아래, 오른쪽, 위, 왼쪽
dy = [0, 1, 0, -1]
def bfs(graph, visited, queue):
    result = 0
    while queue:
        date, nowRow, nowCol = queue.popleft()
        visited[nowRow][nowCol] = True
        if result < date:
            result = date
        for i in range(4):
            adjRow = nowRow+dx[i]
            adjCol = nowCol+dy[i]
            if adjRow >= 0 and adjRow < n and adjCol >= 0 and adjCol < m and graph[adjRow][adjCol] == 0 and not visited[adjRow][adjCol]: # 인접한 곳이 범위안에 있고 방문하지 않았으며 익지 않은 토마토가 있으면
                queue.append((date+1, adjRow, adjCol))
                graph[adjRow][adjCol] = 1
    return result

# m, n 입력
m, n = map(int, input().split(" "))
# n개 줄, 상자에 담긴 토마토 정보
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split(" "))))

visited = [[False]*m for _ in range(n)]
result = 0
queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            queue.append((0, i, j)) # 동시에 익히기 위해서 처음에 익은 토마토 큐에 담기

result = bfs(graph, visited, queue)

check = False
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            check = True
            break

if check:
    print(-1)
else:
    print(result)


# 와 동시에 익히는 건 생각을 못했네
# 동시에 익히는 것은 어떤 방식을 이용해야 할까.
# 맨처음에 1인 놈을 다 찾아서 큐에 넣어놓고 그 상태에서 큐를 빼면서 진행하는 건 어떰?
# 시간이 2초가 걸림,,, 맞았습니다 뜨긴했는데,,, 스터디때 질문 조져야겠구만유
