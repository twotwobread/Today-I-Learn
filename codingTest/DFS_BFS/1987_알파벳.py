# R, C
# 1,1 시작
# 지금까지 지나온 알파벳과 달라야함.
def dfs(n, m, cnt, cmpStr):
    next = cnt + 1
    for i in range(4):
        nr, nc = n+dx[i], m+dy[i]
        if 0<=nr<r and 0<=nc<c and not graph[nr][nc] in cmpStr:
            cnt = max(cnt, dfs(nr, nc, next, cmpStr+graph[nr][nc]))
    return cnt
def solution():
    return dfs(0, 0, 1, graph[0][0])
if __name__ == "__main__":
    dx = (0, 1, 0, -1)
    dy = (1, 0, -1, 0)
    r, c = map(int, input().split())
    graph = [list(input()) for _ in range(r)]
    print(solution())

# 이해가 안되는게 시간을 줄일려고 dict() 이용해서 검색 시간을 O(len(tbl)) -> O(1)로 바꿨는데 시간 초과가 난다.
# 그 이유를 잘 모르겠다.
def dfs(n, m, cnt, tbl):
    next = cnt + 1
    for i in range(4):
        nr, nc = n+dx[i], m+dy[i]
        if 0<=nr<r and 0<=nc<c and not tbl.get(graph[nr][nc], 0):
            tbl[graph[nr][nc]] = 1
            cnt = max(cnt, dfs(nr, nc, next, tbl))
            del(tbl[graph[nr][nc]])
    return cnt
def solution():
    table = dict()
    table[graph[0][0]] = 1
    return dfs(0, 0, 1, table)
if __name__ == "__main__":
    dx = (0, 1, 0, -1)
    dy = (1, 0, -1, 0)
    r, c = map(int, input().split())
    graph = [list(input()) for _ in range(r)]
    print(solution())
    
