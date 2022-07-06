# M x N
# 그냥 bfs로 조지면 될듯

from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        visited = [[0]*n for _ in range(m)]
        dx = (0, 1, 0, -1)
        dy = (1, 0, -1, 0)
        q = deque()
        q.append((sr, sc, image[sr][sc]))
        visited[sr][sc] = 1
        image[sr][sc] = color
        while q:
            r, c, nowColor = q.popleft()
            for i in range(4):
                nr, nc = r + dx[i], c + dy[i]
                if 0<=nr<m and 0<=nc<n and image[nr][nc] == nowColor and visited[nr][nc] != 1:
                    image[nr][nc] = color
                    visited[nr][nc] = 1
                    q.append((nr, nc, nowColor))
        return image
