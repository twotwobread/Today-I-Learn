# file name : 7569_토마토.py
#
# 토마토를 격자 모양 상자의 칸에 하나씩 넣고 수직으로 쌓아 보관.
# 창고에 보관되는 토마토는 익은 것도 있지만 안익은 것도 존재
# 익지 않은 토마토는 익은 토마토의 영향으로 익는다. 인접한 토마토는 익는다. ( 왼,오,앞,뒤,위,아래 )
# 토마토가 혼자 익는 경우는 없다. 며칠이 지나면 창고의 토마토가 다 익는지 '최소일수'를 알고 싶다.
# 상자의 일부에는 토마토가 들어있지 않을 수 있다.
#
# 상자의 가로 칸 수  ( 2 <= M <= 100 ), 세로 칸 수 ( 2 <= N <= 100), 쌓아지는 상자 수 ( 2 <= H <= 100 ) 
# 둘째 줄부터는 가장 밑의 상자부터 가장 위의 상자까지에 저장된 토마토들의 정보가 주어짐.
# 즉, 둘째 줄부터 N개의 줄에는 하나의 상자에 담긴 토마토의 정보가 주어짐.
# 정수 -1 : 토마토 없는 칸 , 정수 0 : 익지 않은 토마토, 정수 1 : 익은 토마토.
# N개의 줄이 이렇게 H번 반복해서 주어짐. ( 무조건 토마토가 하나 이상 있는 경우만 주어짐. )
# 저장될 때부터 모든 토마토가 익어있다면 0, 토마토가 모두 익지 못하는 상황이라면 -1 출력
#
# 시간 제한 : 1초 | 메모리 제한 : 256MB | 
# author : Lee SUyoung(2022-03-03)

# bfs, 큐를 이용

from collections import deque
# m, n, h 입력
m, n, h = map(int, input().split(" "))
# 상자에 담긴 토마토의 정보 ( N개의 줄이 H번 반복되며 들어옴. 처음이 맨 밑에 층)
boxStack = []
for i in range(h): # h개의 층의 박스를 입력
    boxStack.append([list(map(int, input().split(" "))) for _ in range(n)])

# 익은 토마토를 전부 큐에 삽입. ( 익은 토마토 인접 토마토들이 다 같이 익어가야하기 때문. )
ripeTomato = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if boxStack[i][j][k] == 1:
                ripeTomato.append((i, j, k))

# 토마토가 다 익히기 위한 bfs 알고리즘
dh = [1, -1, 0, 0, 0, 0] # 상, 하, 우, 좌, 앞, 뒤
dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
def bfs(ripeTomato, boxStack):
    while ripeTomato:
        height, row , col = ripeTomato.popleft()
        for i in range(6):
            adjHeight, adjRow, adjCol = height+dh[i], row+dx[i], col+dy[i]
            if 0<=adjHeight<h and 0<=adjRow<n and 0<=adjCol<m and boxStack[adjHeight][adjRow][adjCol] == 0:
                # 범위안에 존재하고 익지 않은 토마토를 발견했을떄
                boxStack[adjHeight][adjRow][adjCol] = boxStack[height][row][col] + 1
                ripeTomato.append((adjHeight, adjRow, adjCol))

bfs(ripeTomato, boxStack) # 토마토 익히기

# 최소일수 구하기
zeroCheck = False
result = 0
for i in range(h):
    for j in boxStack[i]:
        if 0 in j:
            zeroCheck = True
            break
        result = max(result, max(j))

if zeroCheck:
    print("-1")
else:
    print(result-1)
