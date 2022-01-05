# file name : 이코테_실전4_3.py
# N x M 크기 직사각형, 육지 or 바다, 캐릭터는 동서남북 중 한 곳을 바라본다.
# A = 북쪽으로부터 떨어진 칸 수, B = 서쪽으로부터 떨어진 칸 수
# 바다로 된 공간은 갈 수 없음.
# 1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향 부터 차례대로 갈 곳을 정함.
# 2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다.
#    왼쪽으로 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
# 3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어있는 칸인 경우에는 바라보는 방향을 유지한 채로 한칸 뒤로 가고 1단계로 돌아간다.
#    단, 이때 뒤쪽 방향이 바다면 움직임을 멈춤.
# 3 <= n, m <=50, 0: 북, 1:동, 2: 남, 3:서 / 0:육지, 1:바다 
# author : Lee Suyoung (2022-01-05)

# n,m을 입력
n, m = map(int, input().split())
# 위치 좌표, 바라보는 방향 입력
a, b, d = map(int, input().split())
# 맵의 데이터 입력
Map=[]
for i in range(n):
    temp = list(map(int, input().split()))
    Map.append(temp)
# 북 동 남 서에 관하여 선언
turn = [(-1,0), (0,1), (1,0), (0, -1)]
# 현재 바로보는 위치에서 왼쪽부터 돌면서 갈 곳을 확인
cnt = 0
while True:
    # 방문한 위치를 바다와 구분하기 위해서 2로 저장
    if Map[a][b] == 0:
        Map[a][b] = 2
        cnt += 1
    #print("현재 pos : {}, {}, {}".format(a,b,cnt))
    temp_d = d
    stop = 0
    for i in range(4):
        temp_d -= 1 # turn left
        if temp_d<0 :
            temp_d += len(turn)
        row = a + turn[temp_d][0]; col = b + turn[temp_d][1]
        if (0 <= row < n and 0 <= col < m) and Map[row][col]==0:
            a = row; b = col;
            d = temp_d
            break
        else:
            stop += 1
    # 동서남북 들리지 않은 곳이 없다
    if stop == 4:
        back = d - 2
        if back<0 :
            back += len(turn)
        back_row = a + turn[back][0]; back_col = b + turn[back][1]
        if Map[back_row][back_col] == 1:
            break
        else:
            a = back_row; b = back_row 

print(cnt)

###[ 제시한 예시 답안 ]###
n, m = map(int, input().split())

d = [[0] * m for _ in range(n)] # 방문한 위치를 저장하기 위함.
x, y, direction = map(int, input().split())
d[x][y]=1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x  + dx[direction]
    ny = y  + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx; y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx; y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

print(count)
