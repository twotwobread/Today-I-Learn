# file name : 9663_N-Queen.py
# N-Queen
# 크기가 NxN 체스판 위에 퀸 N개를 서로 공격할 수 없게 높는 문제.
# N이 입력되었을떄, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성.
# 
# 1 <= N <= 15
# 
# N개의 퀸이 서로 공격할 수 없게 놓는 경우의 수를 출력
#
# 시간 제한 : 10초 | 메모리 제한 : 128MB
# author : Lee Suyoung (20222-03-06)

# 일단 모든 경우를 다 찾아야함. DFS를 이용
# 일단 완전탐색을 해야겠지.
# 근데 퀸이 서로를 공격할 수 없어야하니까 퀸이 공격할 수 있는
# 범위가 존재한다는 것이고 이걸피해서 조지고 모든 경우라서
# 다른 경우가 나와야한다는 것인데
# 퀸 사기네 -> 상하좌우대각선 어디든 갈 수 있고 몇칸이든 이동가능
# 일단 dfs를 모든 칸에서 조져봐야하긴해
result = []
COUNT = 0
# n 입력
n = int(input())

def isRight(i,j,row,col):
    if i == row or j == col or (i-j)==(row-col):
        return False
    else:
        return True

def dfs(row, col):
    global COUNT
    if len(result) == n:
        COUNT += 1
        return
    for i in range(row+1, n):
        for j in range(n):
            if isRight(i, j, row, col):
                result.append((row, col))
                dfs(i,j)
                result.pop()

for i in range(n-1):
    for j in range(n):
        result.append((i,j))
        dfs(i,j)
print(COUNT)

# 수정 필요
# file name : 9663_N-Queen.py
# N-Queen
# 크기가 NxN 체스판 위에 퀸 N개를 서로 공격할 수 없게 높는 문제.
# N이 입력되었을떄, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성.
# 
# 1 <= N <= 15
# 
# N개의 퀸이 서로 공격할 수 없게 놓는 경우의 수를 출력
#
# 시간 제한 : 10초 | 메모리 제한 : 128MB
# author : Lee Suyoung (20222-03-06)

# 일단 모든 경우를 다 찾아야함. DFS를 이용
# 일단 완전탐색을 해야겠지.
# 근데 퀸이 서로를 공격할 수 없어야하니까 퀸이 공격할 수 있는
# 범위가 존재한다는 것이고 이걸피해서 조지고 모든 경우라서
# 다른 경우가 나와야한다는 것인데
# 퀸 사기네 -> 상하좌우대각선 어디든 갈 수 있고 몇칸이든 이동가능
# 일단 dfs를 모든 칸에서 조져봐야하긴해
from collections import deque
result = deque()
COUNT = 0
# n 입력
n = int(input())

def isRight(i, j):
    for x in range(len(result)):
        if j == result[x][1] or abs(i - result[x][0]) == abs(j - result[x][1]):
            return False
    return True

def dfs(row, col):
    global COUNT
    if row >= n:
        return
    if len(result) == n:
        COUNT += 1
        #print(result)
        return
    for j in range(n):
        if isRight(row+1, j):
            result.append((row+1, j))
            dfs(row+1,j)
            result.pop()

for i in range(n):
    result.append((0,i))
    dfs(0,i)
    result.pop()
print(COUNT)
