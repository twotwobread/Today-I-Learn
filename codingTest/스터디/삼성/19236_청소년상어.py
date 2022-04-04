# file name : 19236_청소년상어.py
# author Lee Suyoung(2022-04-02)
# 4x4 크기의 공간이 있음. 각 칸은 (x,y)와 같이 표현. x = 행의 번호, y = 열의 번호
# 한 칸에는 물고기 한 마리 존재. 각 물고기는 번호와 방향을 가짐.
# 번호는 1보다 크거나 같고, 16보다 작거나 같은 자연수. 같은 번호를 갖는 경우는 없음.
# 방향은 8가지 (상하좌우, 대각선) 중 하나.
# 청소년 상어는 (0,0)에 있는 물고기를 먹고, (0,0)에 들어감.
# 상어의 방향은 (0,0)에 있던 물고기의 방향과 같음.
# 물고기는 번호가 작은 물고기부터 순서대로 이동. 물고기는 한 칸을 이동할 수 있고,
# 이동할 수 있는 칸은 빈칸과 다른 물고기가 있는 칸, 이동할 수 없는 칸은 상어가 있거나,
# 공간의 경계를 넘는 칸. 각 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계
# 회전시킴. 만약, 이동할 수 있는 칸이 없으면 이동하지 않음.
# 그 외의 경우에는 그 칸으로 이동을 한다. 물고기가 있는 칸으로 이동 시 위치를 서로 바꿈.
# 물고기의 이동이 모두 끝나면 상어가 이동한다. 상어는 방향에 있는 칸으로 이동할 수 있고
# 한 번에 여러 개의 칸을 이동할 수 있음. 상어가 물고기가 있는 칸으로 이동했다면,
# 그 칸에 있는 물고기를 먹고, 그 물고기의 방향을 가지게 됨. 이동하는 중에 지나가는 칸에
# 있는 물고기를 먹지 않음. 물고기가 없는 칸으로는 이동할 수 없음. 상어가 이동할 수 있는
# 칸이 없으면 공간에서 벗어나 집으로 감. 상어 이동 후 다시 물고기 이동.
#
# 첫째 줄, 4개의 줄 물고기 정보 (ai, bi) , ai = 물고기 번호, bi = 방향 ( bi <= 8)
# 1번부터 12시부터 반시계 방향의 방향을 의미.
#
# 상어가 먹을 수 있는 물고기 번호의 합의 최댓값을 출력한다.
#
# 시간 제한 : 1초(추가시간 없음), 메모리 제한 : 512MB

# 이거 백트래킹임.
# 모든 경우를 다 봐야하고 가지치기를 잘해야할 듯.
# 가지치기는 이동할 수 없는 경우 ( 경로에 물고기가 없거나 경로를 벗어나는 경우 )
# easy
import heapq
import copy

RESULT = []
DIRECT = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0,1), (-1, 1)]
MAX = -int(1e9)
def moveFish(fishNum, fishDirect):
    q = []
    for i in range(4):
        for j in range(4):
            if fishNum[i][j] != -2 and fishNum[i][j] != -1:
                heapq.heappush(q, (fishNum[i][j], fishDirect[i][j], i, j))

    while q:
        check = True
        num, direct, row, col = heapq.heappop(q)
        if fishNum[row][col] != num:
            for i in range(4):
                for j in range(4):
                    if fishNum[i][j] == num:
                        row, col = i, j
                        check = False
                        break
                if not check:
                    break
        for k in range(7):
            adj_row, adj_col = row + DIRECT[direct-1][0], col + DIRECT[direct-1][1]
            if 0 <= adj_row < 4 and 0 <= adj_col < 4 and fishNum[adj_row][adj_col] != -2:
                # 방향 바꾸기
                fishDirect[row][col], fishDirect[adj_row][adj_col] = fishDirect[adj_row][adj_col], direct
                # 물고기 번호 바꾸기
                fishNum[row][col], fishNum[adj_row][adj_col] = fishNum[adj_row][adj_col], num
                break
            else:
                direct = ((direct - 1) + 1) % 8 + 1

def dfs(fishNum, fishDirect, i, j):
    global RESULT, DIRECT, MAX

    fishNum[i][j] = -2 # 상어라는 말
    direct = DIRECT[fishDirect[i][j] - 1]
    moveFish(fishNum, fishDirect)

    if i+direct[0] < 0 or i+direct[0] >= 4 or j+direct[1] < 0 or j+direct[1] >= 4:
        temp = sum(RESULT)
        if MAX < temp:
            MAX = temp
        return

    count = 0
    fishNum[i][j] = -1  # 물고기가 먹혔다는 말
    for k in range(1, 4): # 상어의 이동
        adj_row = i + (k * direct[0])
        adj_col = j + (k * direct[1])
        if 0 <= adj_row < 4 and 0 <= adj_col < 4:
            if fishNum[adj_row][adj_col] != -1:
                RESULT.append(fishNum[adj_row][adj_col])
                fish = copy.deepcopy(fishNum)
                fish_direct = copy.deepcopy(fishDirect)
                dfs(fishNum, fishDirect, adj_row, adj_col)
                fishNum = copy.deepcopy(fish)
                fishDirect = copy.deepcopy(fish_direct)
                RESULT.pop()
            else:
                count += 1
        else:
            count += 1
    if count == 3:
        temp = sum(RESULT)
        if MAX < temp:
            MAX = temp
        return



def solution(info):
    global MAX
    fishNum = [info[i][0::2] for i in range(4)]
    fishDirect = [info[i][1::2] for i in range(4)]
    RESULT.append(fishNum[0][0])
    dfs(fishNum, fishDirect, 0, 0)
    return MAX



if __name__ == "__main__":
    # info 입력
    info = [list(map(int, input().split(" "))) for _ in range(4)]
    print(solution(info))
