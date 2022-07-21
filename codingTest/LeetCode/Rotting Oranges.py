# 0 = 빈 셀, 1 = 신선한 오렌지, 2 = 썩은 오렌지
# 문제에선 M x N 그리드가 주어진다. 해당 그리드의 각 인덱스엔 위의 세 종류 중 하나의 오렌지가 담겨있는데 모든 썩은 오렌지들은 매분 인접 4방향에 위치한 신선한 오렌지를 썩게 만든다.
# 이 때, 모든 셀에 신선한 오렌지가 없을때까지 걸리는 최소 시간을 구하여라
# 해당 문제에선 격자가 주어진다. 그래서 격자형 그래프를 이용해보자. 그래프는 노드와 간선의 정보를 저장하고 있는 자료 구조이다. 이 문제에선 오렌지가 들어있는 인덱스를 노드로 생각할 수 있고 인접하다는 것을 간선으로 볼 수 있다. 그렇게 된다면 인접한 오렌지들끼린 모두 양방향으로 연결된 격자형 그래프가 되는 것이다.
# 해당 문제에서 원하는 것은 그래프 상에 신선한 오렌지 = 1이 없게 만드는 것이다. 없게 만들었을때 최소 시간이 걸리게 하고 싶은 것이다.
# 어떻게 할 수 있을까? 그렇게 하기 위해선 모든 노드를 탐색해야 하기 때문에 그래프 탐색 알고리즘인 BFS, DFS를 떠올릴 수 있다. BFS와 DFS 알고리즘 모두 시간, 공간 복잡도가 O(V+E)로 동일하다. 하지만 문제에선 썩은 오렌지가 매분 주위에 있는 신선한 오렌지를 썩게 만든다고 했다. 그 말은 모든 썩은 오렌지가 한꺼번에 퍼져나가야한다는 것이다. 이를 위해선 BFS를 이용해 주위의 오렌지를 같이 썩게 만들어야지 DFS를 이용하여 하나의 오렌지의 주위를 먼저 다 퍼트리고 다음 오렌지를 퍼트리면 안된다.
# m, n은 모두 최대 10 이기 때문에 최대 O(10*10)으로 표현 할 수 있다. 원하는 시간 내에 문제를 해결할 수 있다.
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def bfs(n,m,q):
            dx = (0, 1, 0, -1)
            dy = (1, 0, -1, 0)
            maxValue = 0
            while q:
                row, col, time = q.popleft()
                maxValue = max(maxValue, time)
                for i in range(4):
                    nr, nc = row + dx[i], col + dy[i]
                    if not(0<=nr<n and 0<=nc<m): continue
                    if grid[nr][nc] != 1: continue
                    q.append((nr, nc, time+1))
                    grid[nr][nc] = 2
            return maxValue
        
        # 먼저 썩은 오렌지를 다 담는다.
        q = deque()
        n = len(grid); m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2: 
                    q.append((i, j, 0)) # 썩은 시간을 표현하기 위해서 0으로 표현하였다.
        
        result = bfs(n, m, q)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return result
