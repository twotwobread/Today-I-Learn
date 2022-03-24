# file name : 20055_컨베이어벨트위의로봇.py
# 길이가 N인 컨베이어 벨트가 있고, 길이가 2N인 벨트가 이 컨베이어 벨트를
# 위아래로 감싸며 돌고있음. 벨트는 길이 1 간격으로 2N개의 칸으로 나뉘어져
# 있으며, 각 칸에는 1-2N까지의 번호가 매겨져 있다.
# 서클러 형태이고 i번 칸의 내구도는 Ai이다. 1번칸 : 올리는 위치,
# N번칸: 내리는 위치. 컨베이어 벨트에 박스 모양 로봇을 하나씩 올리려 함.
# 로봇은 올리는 위치에만 올릴 수 있음. 언제든지 로봇이 내리는 위치에 도달하면
# 그 즉시 내림. 로봇은 컨베이어 벨트 위에서 스스로 이동할 수 있음.
# 로봇을 올리는 위치에 올리거나 로봇이 어떤 칸으로 이동하면 그 칸의 내구도는 1만큼 감소.
# 컨베이어 벨트를 이용해 로봇들을 건너편으로 옮기려 함. 
# 로봇을 옮기는 과정
# 1. 벨트가 각 칸위에 있는 로봇과 함께 한 칸 회전한다.
# 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 이동할 수 
# 있으면 이동. 만약 이동 할 수 없으면 가만히 있음
#     1. 로봇이 이동하기 위해선 이동하려는 칸에 로봇이 없으며, 내구도가 1이상
#        남아 있어야함.
# 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올림.
# 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정 종료.
# 5. 위과정 반복
# 종료되었을 때 몇 번째 단계가 진행 중이었는지 구해보자.
# 처음 수행되는 단계는 1번째 단계이다.
#
# 첫쨰 줄, N, K , 2<=N<=100, 1<=K<=2N
# 둘쨰 줄, 내구도 정보 A, 1<=A<=1,000
# 시간제한 : 1초, 메모리 제한 : 512MB
# author : Lee Suyoung(2022-03-24)

# 위에 과정 그대로 구현하면 될 듯
def moveBelt(n, A, robot):
    # 컨베이어 위치 바꾸는 부분
    index = -1
    temp = A.pop()
    A.insert(0, temp)
    # 로봇 올라간 위치도 바꿔야함.
    for r in range(len(robot)):
        move = (robot[r]+1)%(2*n)
        robot[r] = move
        if move == (n-1):
            index = r
    if index != -1:
        robot.pop(index)
    return A

def solution(n, k, A):
    durNum = 0 # 내구도 0인 칸 개수
    robot = [] # 로봇이 어디 올라가있는지, 올라간 순서 확인
    level = 0
    while durNum < k: # 4. 내구도 개수가 k개가 되면 종료
        level += 1
        # 1.컨베이어 돌리기
        A = moveBelt(n, A, robot)
        # 2.가장 먼저 올라간 로봇부터 이동하기
        index = -1
        for r in range(len(robot)):
            move = (robot[r]+1)%(2*n)
            if not move in robot and A[move] > 0: # 로봇이 없고 내구도가 0 이상
                robot[r] = move
                A[move] -= 1
                if move == (n-1):
                    index = r
                if A[move] == 0:
                    durNum += 1
        if index != -1:
            robot.pop(index)
        # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올린다.
        if A[0] > 0:
            if robot and 0 in robot: # 그리고 0번째 칸에 로봇이 존재하면 안올린다.
                continue
            robot.append(0)
            A[0] -= 1
            if A[0] == 0:
                durNum += 1
    return level
        


if __name__ == "__main__":
    # n, k 입력
    n, k = map(int, input().split(" "))
    # A, 내구도 정보 입력
    A = list(map(int,input().split(" ")))
    result = solution(n,k,A)
    print(result)
