# file name: 이코테_예제4_1.py
# N x N 크기의 정사각형 공간, 1x1 정사각형으로 나누어져 있음.
# 가장 왼쪽 위 좌표는 (1, 1), 가장 오른쪽 아래 좌표는 (N, N)
# A는 상, 하, 좌, 우 이동 가능, 시작 좌표는 (1, 1)
# N x N을 벗어나는 이동은 무시됨.
# author: Lee Suyoung (2021-01-04)


# n을 입력받는 부분
n = int(input())
# 움직임의 명령을입력 받는 부분
order = list(map(str, input().split()))

# L, R, U, D가 의미하는 움직임을 정의하는 부분
pos = [1, 1]
move = {'L':(0, -1), 'R':(0, 1), 'U':(-1, 0), 'D':(1, 0)} # 행과 열로 표시해서 x축으로 움질일 때 열이 바뀌는 것을 주의
# 시작좌표부터 들어온 order에 따라 좌표를 바꿔주는 부분
for o in order:
    #print(move[o])
    # 튜플끼리는 연산 불가능, 요소로 접근해야함.
    # 튜플은 입력, 수정, 삭제가 불가능하다 -> 주로 수정하면 안 되는 데이터셋에 사용한다.
    # pos는 수정을 해야 하기 때문에 리스트로 설정
    if pos[0] + move[o][0] < 1 or pos[0] + move[o][1] > n or pos[1] + move[o][1] < 1 or pos[1] + move[o][1] > n :
        continue
    else:
        pos[0] += move[o][0]; pos[1] += move[o][1]

print("{} {}".format(pos[0], pos[1]))

###[ 제안된 예시 답안 ]###
n = int(input())
x, y = 1, 1
plans = input().split()

# L,R,U,D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny >n:
        continue
    x, y = nx, ny
print(x, y)
