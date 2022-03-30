# file name : 14891_톱니바퀴.py
# 총 8개의 톱니를 가지고 있는 톱니바퀴 4개가 일렬로 놓여있음.
# 또 톱니는 N, S극 중 하나를 나타내고 있음. 톱니에는 번호가 매겨져있는데
# 가장 왼쪽부터 순차적으로 올라감.
# 이때, 톱니를 총 K번 회전시키려함. 톱니바퀴의 회전은 한 칸을 기준으로 함.
# 회전은 시계, 반시계 방향이 있음.
# 톱니 회전 시 회전시킬 톱니와 방향을 결정해야함. 서로 맞닿은 극에 따라
# 옆에 있는 톱니를 회전시킬 수 있고 회전시키지 않을 수 있음.
# 톱니 A가 회전할 때, 그옆에 있는 톱니 B와 맞닿은 톱니의 극이 다르면
# B는 A가 회전한 방향과 반대 방향으로 회전함.
# 초기 톱니 상태와 톱니를 회전시킨 방법이 주어 졌을 때, 최종 톱니의 상태를 구하시오.
#
# 1번 톱니 상태
# 2번 톱니 상태
# 3번 톱니 상태
# 4번 톱니 상태
# 상태는 8개의 정수로 이루어져 있고, 12시 방향부터 시계방향 순서대로 주어진다.
# N극은 0, S극은 1로 나타나있음.
# 5번째 줄, 회전 횟수 ( 1<=K<=100 )
# K개 줄, 회전시킨 방법, 각 방법은 두 개의 정수로 이루어져 있고
# 첫번째 정수는 회전시킨 톱니 번호, 두번째 정수는 방향 ( 1인 경우 시계 방향, -1인 경우 반시계 방향)
#
# K번 회전시킨 이후 네 톱니바퀴의 점수의 합을 출력
#   - 1번 톱니의 12방향이 N극이면 0점, S극이면 1점
#   - 2번 톱니의 12방향이 N극이면 0점, S극이면 2점
#   - 3번 톱니의 12방향이 N극이면 0점, S극이면 4점
#   - 4번 톱니의 12방향이 N극이면 0점, S극이면 8점
#
# 시간 제한 : 2초, 메모리 제한 : 512MB
# author : Lee Suyoung (2022-03-30)
# 극이 같으면 회전하지 않고 극이 다르면 반대 방향으로 회전
def caculatePoint(sawToothInfo):
    point = 1 if sawToothInfo[0][0]==1 else 0
    point += 2 if sawToothInfo[1][0]==1 else 0
    point += 4 if sawToothInfo[2][0]==1 else 0
    point += 8 if sawToothInfo[3][0]==1 else 0
    return point

def turnSawTooth(sawTooth, rotate):
    if rotate == 1:
        temp = [sawTooth.pop()]
        sawTooth = temp + sawTooth
    elif rotate == -1:
        temp = [sawTooth[0]]
        sawTooth = sawTooth[1:] + temp
    return sawTooth

def solution(num1SawTooth, num2SawTooth, num3SawTooth, num4SawTooth, rotateInfo):
    sawToothInfo = [num1SawTooth, num2SawTooth, num3SawTooth, num4SawTooth]
    for r in rotateInfo: # 처음 돌리는 놈.
        num, direct = r
        # 먼저 회전에 필요한 6개의 극 값을 받아놓자.
        # 인접 톱니 회전 정보를 위함
        #print(sawToothInfo[0][0], sawToothInfo[1][0], sawToothInfo[2][0], sawToothInfo[3][0])
        rotate = [0]*4
        rotate[num-1] = direct
        right = (num-1)
        while True: # 오른쪽 톱니들 돌리기
            if (right + 1) == 4:
                break
            if sawToothInfo[right][2] == sawToothInfo[right+1][6]:
                rotate[right+1] = 0
            else:
                if direct == 1:
                    rotate[right+1] = -1
                elif direct == -1:
                    rotate[right+1] = 1
                else:
                    rotate[right+1] = 0
            right += 1
            direct = rotate[right]
        left = (num-1)
        direct = rotate[left]
        while True: # 왼쪽 톱니들 돌리기
            if (left - 1) == -1:
                break
            if sawToothInfo[left][6] == sawToothInfo[left-1][2]:
                rotate[left-1] = 0
            else:
                if direct == 1:
                    rotate[left-1] = -1
                elif direct == -1:
                    rotate[left-1] = 1
                else:
                    rotate[left-1] = 0
            left -= 1
            direct = rotate[left]

        for i in range(4):
            sawToothInfo[i] = turnSawTooth(sawToothInfo[i], rotate[i])
    return caculatePoint(sawToothInfo)


if __name__ == "__main__":
    # 1번 톱니 상태
    num1SawTooth = list(map(int,input()))
    # 2번 톱니 상태
    num2SawTooth = list(map(int,input()))
    # 3번 톱니 상태
    num3SawTooth = list(map(int,input()))
    # 4번 톱니 상태
    num4SawTooth = list(map(int,input()))
    # 회전 횟수
    k = int(input())
    # 회전시킨 방법
    rotateInfo = [list(map(int, input().split(" "))) for _ in range(k)]
    print(solution(num1SawTooth, num2SawTooth, num3SawTooth, num4SawTooth, rotateInfo))
