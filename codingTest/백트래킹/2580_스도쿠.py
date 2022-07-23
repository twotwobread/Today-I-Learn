def find(row, col) -> None:
    findNum = [0]*10
    for r in range(N): # 세로
        if grid[r][col] != 0:
            findNum[grid[r][col]] = 1
    for c in range(M): # 가로
        if grid[row][c] != 0:
            findNum[grid[row][c]] = 1
    for i in isRange[row]:
        for j in isRange[col]:
            if grid[i][j] != 0:
                findNum[grid[i][j]] = 1
    for index, n in enumerate(findNum[1:]):
        if n == 0:
            numbers[(row, col)].append(index+1)
def isRight(temp, row, col):
    number = [0]*10
    for r in range(N):
        if temp[r][col] != 0:
            if number[temp[r][col]] == 1: return False
            else:
                number[temp[r][col]] = 1
    number = [0] * 10
    for c in range(M):
        if temp[row][c] != 0:
            if number[temp[row][c]] == 1: return False
            else:
                number[temp[row][c]] = 1
    number = [0] * 10
    for i in isRange[row]:
        for j in isRange[col]:
            if temp[i][j] != 0:
                if number[temp[i][j]] == 1: return False
                else:
                    number[temp[i][j]] = 1
    return True
def backTracking(arr, graph, number):
    if number == len(arr):
        for i in range(N):
            for j in range(M):
                print(graph[i][j], end=" ")
            print()
        return True
    row, col = arr[number]
    for n in numbers[(row, col)]:
        graph[row][col] = n
        if isRight(graph, row, col):
            #temp = [graph[i].copy() for i in range(N)]
            if backTracking(arr, graph, number+1): return True
        graph[row][col] = 0
    return False
if __name__ == "__main__":
    isRange = {0:(0,1,2), 1:(0,1,2), 2:(0,1,2), 3:(3,4,5), 4:(3,4,5), 5:(3,4,5), 6:(6,7,8), 7:(6,7,8), 8:(6,7,8)}
    N, M = 9, 9
    grid = [list(map(int, input().split())) for _ in range(N)]
    numbers = dict()
    blank = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 0:
                blank.append((i, j))
                numbers[(i, j)] = []
                find(i, j)
    backTracking(blank, grid, 0)
