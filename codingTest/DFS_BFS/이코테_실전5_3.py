# file name : 이코테_실전5_1.py
# N x M 얼음 틀, 구멍 0, 칸막이 1
# 구멍끼리 상, 하, 좌, 우 붙어있으면 연결되어 있음.
#  총 아이스크림의 개수는?
# 1 <= N, M <= 1,000
# author

# 0인 걸 찾으면 주변에 0을 다 찾아 방문하면 그놈을 1로 바꿔도 될 듯
# 그리고 내가 주변이 다 1이다. 그러면 카운트를 하나 증가 시켜 그리고 또 0을 찾아 이거 반복

# 함수 내부에서는 현재 좌표 방문 처리
def dfs(graph, row, col):
    if row < 0 or row >= n or col < 0 or col >= m or graph[row][col] == '1':
        return
    graph[row][col] = '1'
    dfs(graph, row+1, col)
    dfs(graph, row, col+1)
    dfs(graph, row-1, col)
    dfs(graph, row, col+1)

# n, m 입력
n, m = map(int, input().split())
# 얼음틀 형태 입력
ice_map = []
for i in range(n):
    ice_map.append(list(input()))

#print(ice_map)
# 0인 부분 찾아서 거기 좌표 넣으면서 함수 실행
cnt = 0
for i in range(n):
    for j in range(m):
        if ice_map[i][j]=='0':
            dfs(ice_map, i, j)
            cnt += 1    

print(cnt)


