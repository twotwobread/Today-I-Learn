# 문제 유형 : 위상 정렬
# 자료 구조 : 2차원 배열 - 노드 연결 정보
from collections import deque
def solution():
    ranking = ""
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    for i in range(n):
        if len(q) == 0: # cycle
            print("IMPOSSIBLE")
            break
        if len(q) > 1: # 여러 경우
            print("?")
            break
        now = q.popleft()
        ranking += (str(now)+" ")
        for adj in range(len(graph[now])):
            if graph[now][adj]:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    q.append(adj)
    else:
        print(ranking)

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        n = int(input())
        graph = [[False]*(n+1) for _ in range(n+1)]
        indegree = [0]*(n+1)
        last = list(map(int, input().split()))
        for i in range(n):
            for j in range(i+1, n):
                graph[last[i]][last[j]] = True
                indegree[last[j]] += 1
        m = int(input())
        for _ in range(m):
            a, b = map(int, input().split())
            if graph[a][b]:
                graph[a][b] = False
                graph[b][a] = True
                indegree[a] += 1
                indegree[b] -= 1
            else:
                graph[a][b] = True
                graph[b][a] = False
                indegree[b] += 1
                indegree[a] -= 1
        solution()
