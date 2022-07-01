# 문제 유형 : 구현
# [아이디어]
# - 0 ~ (n-1) 격자를 이용.
# - 변수이용해서 초를 센다.
# - 최대 10,000초 까지 가능.
# - deque 이용해서 몸통 넣기.
from collections import deque
def outOfRange(nr, nc):
    if 0<=nr<n and 0<=nc<n:
        return True
    else:
        return False
def solution():
    time = 0
    row, col = 0, 0
    body = deque()
    body.append((0,0))
    direction = 0
    while True:
        if len(move) > 0 and move[0][0] == time:
            nd = move.popleft()[1]
            direction = (direction+1)%4 if nd == 'D' else (direction-1)%4
        nr, nc = row + dx[direction], col + dy[direction]
        if (nr, nc) in body or not outOfRange(nr, nc):
            print(time+1)
            break
        body.append((nr, nc))
        if graph[nr][nc] == 1:
            graph[nr][nc] = 0
        else:
            body.popleft()
        row, col = nr, nc
        time += 1

if __name__ == "__main__":
    dx = (0, 1, 0, -1)
    dy = (1, 0, -1, 0)
    n = int(input())
    graph = [[0]*n for _ in range(n)]
    m = int(input())
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x-1][y-1] = 1
    z = int(input())
    move = deque()
    for _ in range(z):
        time, direct = input().split()
        move.append((int(time), direct))
    solution()
