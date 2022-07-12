# 문제 유형 : BFS
# 아이디어
# - 사과 썪어가는 문제랑 같음.
# - 0에서의 최소거리를 구하는 문제이기 때문에 모든 0이 동시에 퍼져나가야 최소거리를 구할 수 있음.
# - 먼저 큐에 0인 인덱스 정보를 담아놓고 bfs를 통해서 거리를 구해나가야함.
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def bfs(mat, visited, q):
            while q:
                x, y= q.popleft()
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0<=nx<len(mat) and 0<=ny<len(mat[x]) and visited[nx][ny] == -1:
                        q.append((nx, ny))
                        visited[nx][ny] = visited[x][y]+1
    
        q = deque()
        dx = (0, 1, 0, -1)
        dy = (1, 0, -1, 0)
        visited = [[-1]*len(mat[i]) for i in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    q.append((i, j))
                    visited[i][j] = 0
        bfs(mat, visited, q)
        return visited
                
