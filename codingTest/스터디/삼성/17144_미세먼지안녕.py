# file name : 17144_미세먼지안녕.py
# 공기청정기의 선능을 테스트하기 위해 구사과는 집을 크기가 RxC인 격자판으로 표현
# 각 칸 (r,c)에 있는 미세먼지의 양을 실시간으로 모니터링하는 시스템을 개발
# 공기청정기는 항상 1번 열에 설치되어 있고, 크기는 두행을 차지.
# 공기청정기가 설치되어 있지 않은 칸에 미세먼지가 있고 미세먼지 양은 Ar,c
# 1초 동안 아래 적힌 일이 순서대로 일어남.
# 1. 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
#   - (r,c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
#   - 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않음.
#   - 확산되는 양은 Ar,c/5이고 소수점은 버림.
# 2. 공기청정기가 작동
#   - 공기청정기에서 바람이 나옴.
#   - 위쪽 공기청정기 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기 바람은 시계방향으로 순환
#   - 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동
#   - 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화.
# 
# R,C,T ( 6<=R,C<=50, 1<=T<=1,000 )
# R개 줄, (-1<=Ar,c<=1,000), 공기청정기가 설치된 곳은 Ar,c = -1이고 나머지 값은 미세먼지의 양이다.
# -1은 2번 위아래로 붙어져 있고, 가장 윗행, 아랫 행과 두칸이상 떨어져있다.
#
# T초가 지난 후 구사과 방에 남아있는 미세먼지의 양을 출력.
#
# 시간제한 : 1초, 메모리 제한 : 512MB
# author : Lee Suyoung(2022-03-27)

# 일단 미세먼지의 확산은 deque에 담아서 처리하는게 맞는 것 같음.
# 동시에 일어나야해서
# 공기 순환은 공기청정기와 같은 행에 있으면 오른쪽으로 무조건 흘러 가면되고
# 맨위 행이나 맨 아래 행에 있으면 왼쪽으로 가고
# 공기청정기와 같은 열에 있으면 위쪽은 아래로, 아래쪽은 위로 가면된다.
from collections import deque

def solution(r,c,t,A):
    dusk = deque()
    muchine = [] # 먼저 들어가는 놈이 위쪽이고 나중에 아래쪽
    for i in range(r):
        for j in range(c):
            if A[i][j] == -1:
                muchine.append((i,j))
            elif A[i][j] != 0:
                dusk.append((i,j,A[i][j])) # 행, 열, 먼지양
    
    time = 0
    dx = (1,-1,0,0)
    dy = (0,0,1,-1)
    while time < t: # t초 후 종료
        time += 1
        # 1. 미세먼지가 확산. 확산은 모든 칸에서 동시에 일어남.
        while dusk: 
            row, col, amount = dusk.popleft()
            diffu = amount//5 
            for i in range(4):
                adj_x, adj_y = row+dx[i], col+dy[i]
                if 0<=adj_x<r and 0<=adj_y<c and A[adj_x][adj_y] != -1:
                    A[adj_x][adj_y] += diffu
                    A[row][col] -= diffu
        # print()
        # print(t, "초 전의 상태 : ")  
        # for i in range(r):
        #     for j in range(c):
        #         print(A[i][j], end=" ")
        #     print()
        # print()
        # # 2. 공기청정기 작동.
        count = 0
        check = [-1,-1]
        temp = -1
        for i in range(r):
            for j in range(c):
                value = -1
                if check[0] != -1 and check[1] != -1 and i == check[0] and j == check[1]:
                    check[0] = -1
                    check[1] = -1
                    continue
                if temp != -1:
                    if temp[0] == i and temp[1] == j:
                        value = temp[2]
                        temp = -1
                if A[i][j] != 0 and A[i][j] != -1:
                    if value == -1:
                        count += A[i][j]
                    # 위쪽 혹은 아래쪽 공기청정기랑 행이 같은 경우
                    if (i == muchine[0][0] or i == muchine[1][0]) and j != (c-1):
                        next_x, next_y = i, j+1
                        if A[next_x][next_y] == 0:
                            check[0] = next_x
                            check[1] = next_y
                        
                    # 맨 위 행이거나 맨 아래 행인 경우
                    elif (i == (r-1) or i == 0) and j != muchine[0][1]: 
                        next_x, next_y = i, j-1
                        
                    # 공기청정기랑 열이 같고 위쪽 행일 때
                    elif j == muchine[0][1] and i < muchine[0][0]:
                        next_x, next_y = i+1, j
                        if A[next_x][next_y] == 0:
                            check[0] = next_x
                            check[1] = next_y
                        
                    # 공기청정기랑 열이 같고 아래쪽 행일 때
                    elif j == muchine[1][1] and i > muchine[1][0]:
                        next_x, next_y = i-1, j
                        
                    # 열이 마지막 열이고 위쪽 행일 때
                    elif j == (c-1) and i <= muchine[0][0] and i != 0:
                        next_x, next_y = i-1, j
                        
                    # 열이 마지막 열이고 아래쪽 행일 때
                    elif j == (c-1) and i >= muchine[1][0] and i != (r-1):
                        next_x, next_y = i+1, j
                        if A[next_x][next_y] == 0:
                            check[0] = next_x
                            check[1] = next_y
                    else: # 아무것도 아닌 경우.
                        dusk.append((i,j, A[i][j]))
                        
                    if 0<=next_x<r and 0<=next_y<c:
                        if A[next_x][next_y] == -1:
                            if value == -1:
                                count -= A[i][j]
                                A[i][j] = 0
                            else:
                                pass
                            next_x, next_y = -1, -1
                            continue

                        if A[next_x][next_y] != 0:
                            temp = (next_x, next_y, A[next_x][next_y])
                        if value != -1:
                            A[next_x][next_y] = value
                            dusk.append((next_x, next_y, value))
                            count += value
                        else:
                            A[next_x][next_y] = A[i][j]
                            dusk.append((next_x, next_y, A[i][j]))
                            A[i][j] = 0
                        next_x, next_y = -1, -1 
        # print(dusk)
        # print()
        # print(t, "초 후의 상태 : ")  
        # for i in range(r):
        #     for j in range(c):
        #         print(A[i][j], end=" ")
        #     print()
        # print()
    sibal = 0
    for i in range(r):
        for j in range(c):
            if A[i][j] != -1:
                sibal += A[i][j]
    #print("sibal = ", sibal)
    return count

if __name__ == "__main__":
    # r,c,t 입력
    r,c,t = map(int, input().split(" "))
    # 미세먼저 정보, A 입력
    A = [list(map(int, input().split(" "))) for _ in range(r)]
    result = solution(r,c,t,A)
    print(result)
