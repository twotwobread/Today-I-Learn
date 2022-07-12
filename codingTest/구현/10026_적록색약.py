# 문제 유형 : 구현
# 아이디어
# - 어짜피 최대 그리디의 크기는 100 x 100이다.
# - bfs를 이용하여 반복문으로 푸는 경우에 최대 반복횟수는 결국 10,000번 이다.
# - 그래서 적록색약인 사람이 볼때, 아닌 사람이 볼때 2번 반복해도 시간 초과는 없을 것이라 예상한다.
from collections import deque
def bfs(row, col):
    q = deque()
    q.append((row, col))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0 and colorDict[color[nx][ny]] == colorDict[color[x][y]]:
                visited[nx][ny] = 1
                q.append((nx, ny))

if __name__ == "__main__":
    dx = (0, 1, 0, -1)
    dy = (1, 0, -1, 0)
    n = int(input())
    colorDict = dict()
    color = [list(input()) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    colorDict['R'] = 0; colorDict['G'] = 1; colorDict['B'] = 2
    part = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                bfs(i, j)
                part += 1

    colorDict['G'] = 0
    visited = [[0] * n for _ in range(n)]
    blindPart = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                bfs(i, j)
                blindPart += 1
    print(part, blindPart)
