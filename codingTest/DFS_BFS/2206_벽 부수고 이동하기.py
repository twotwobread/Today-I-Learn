# 단순하게 생각해서 모든 1인 인덱스를 저장해놓고 하나씩 0으로 바꾸는 완전 탐색 방식 생각해보자
# 이때는 BFS 시간 복잡도가 O(N*M) 이고 최대 1의 개수가 대략 O(N*M) 이라서
# 최대 1000 ^ 4 의 복잡도가 나온다. -> 2초 안에 푸는 것은 불가능하다.
# 그래서 생각해봐야하는 것이 모든 벽을 부술 필요가 있을까?
# 없다. 경로 상의 유의미한 벽들만 부수면 된다.
# 최단 거리를 풀때 현재 인덱스까지의 거리를 저장할 것이다. 이때에 거리말고 부순 벽의 개수와 같은 상태가 같이 저장된다면
# 어떻게 라도 반례를 만들 수 있다고 한다. 무조건 거리 값만 와야한다.
# 그렇다면 상태는 어디에 표현을 해야 하는가? 우리가 dist[x] = 10 이라하면 시작노드부터 x까지 거리가 10이다.
# 이런 의미이다. 그렇다면 저기에서 상태는 어떤게 있는가? x까지 라는 놈이 상태인것이다. 시작노드에서 상태가 바뀌어 x까지 왔는데 여기의 최단 거리가 10이란 것이다.
# 그렇다면 우리가 이 문제에서 표현하고 싶은 상태는 무엇인가?? 시작노드에서 목표노드까지 벽을 한개 부수거나 안 부수거나 했을 때의 최단 거리
# 여기에서 상태는 무엇인가?? 목표노드, 벽 부숨의 유무 이다.
# 상태를 차원으로 표현을 했으니까 즉, 여기에선 부숨 유무에 대한 상태(차원)이 추가가 되어야한다는 것이다.
from collections import deque
def solution():
    q = deque()
    q.append((0, 0, 0))
    visited = [[[-1]*2 for _ in range(M)] for _ in range(N)]
    # 부숨의 유무까지 상태로 포함한 visited이다.
    visited[0][0][0] = 1
    while q:
        r, c, state = q.popleft()
        for i in range(4):
            nr, nc = r + dx[i], c + dy[i]
            if not(0<=nr<N and 0<=nc<M):
                continue
            if visited[nr][nc][state] != -1:
                continue
            if graph[nr][nc] == 0:
                visited[nr][nc][state] = visited[r][c][state] + 1
                q.append((nr, nc, state))
            else:
                if state == 0:
                    visited[nr][nc][not state] = visited[r][c][state] + 1
                    q.append((nr, nc, not state))
    # for i in range(N):
    #     for j in range(M):
    #         print(visited[i][j], end=" ")
    print(min(visited[N-1][M-1][0], visited[N-1][M-1][1]) if visited[N-1][M-1][0] != -1 and visited[N-1][M-1][1] != -1 else visited[N-1][M-1][1]+visited[N-1][M-1][0]+1)
if __name__ == "__main__":
    dx = (0, 1, 0, -1)
    dy = (1, 0, -1, 0)
    N, M = map(int, input().split())
    graph = [list(map(int, input())) for _ in range(N)]
    solution()
