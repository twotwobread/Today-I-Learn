# file name : 20057_마법사상어와토네이도.py
# 크기 NxN인 격자로 나누어진 모래밭에서 연습
# 위치 (r,c)는 격자 r행 c열을 의미, A[r][c]는 (r,c)에 모래양을 의미
# 토네이도 시전 시 격자의 가운데 칸부터 토네이도의 이동이 시작.
# 토네이도는 한 번에 한 칸 이동.
# y에 있는 모래의 해당 비율 만큼 소수점 아래는 버림.
# a로 이동하는 모래의 양은 비율이 적혀있는 칸으로 이동하지 않은 남은 모래의 양과 같음
# 왼쪽이 아닌 다른 방향으로 이동 시, 그림을 해당 방향으로 돌리면 됨.
# 토네이도는 (1,1)까지 이동한 뒤 소멸. 모래가 격자의 밖으로 이동가능.
# 토네이도 소멸 시 격자 밖으로 나간 모래의 양을 구해보자.
#
# 첫째 줄, 격자 크기 3 <= N <= 499 ( 홀수 )
# 둘째 줄, N개의 줄, 각 칸의 모래의 정보 ( 0<=A[r][c]<=1,000)
# 가운데 칸에 있는 모래의 양은 0
#
# 격자 밖으로 나간 모래의 양 출력
#
# author : Lee Suyoung(2022-03-23)


# 토네이도의 무브를 구현하기 위해 왼,아래,오른쪽,위의 구성
# 거기에 움직임의 크기를 곱하여 이동.
# 이동 시, 모래가 가는 칸에 대한 정보도 미리 선언해놓으면 좋을 듯
# 격자를 나가면 해당 칸의 모래를 더해주는 형식으로 구현.
# 그리고 (1,1) 도착 시 종료.

dx = [0, 1, 0, -1] # 왼, 아래, 오른쪽, 위
dy = [-1, 0, 1, 0] # 그대로, 아래, 열과 행 교환 & 부호 교환, 부호만 교환, 열과 행만 교환
# 토네이도 이동 시 영향의 받는 칸 정보 ( 대칭되는 부분도 있으니까 생각해야함.)
sandMove = [((0,-2,5/100), (1,0,7/100),(1,-1,10/100),(1,1,1/100),(2,0,2/100),(-1,0,7/100),(-1,-1,10/100),(-1,1,1/100),(-2,0,2/100))
            , ((2,0,5/100), (0,1,7/100),(1,1,10/100),(-1,1,1/100),(0,2,2/100),(0,-1,7/100),(1,-1,10/100),(-1,-1,1/100),(0,-2,2/100))
            , ((0,2,5/100), (-1,0,7/100),(-1,1,10/100),(-1,-1,1/100),(-2,0,2/100), (1,0,7/100),(1,1,10/100),(1,-1,1/100),(2,0,2/100))
            , ((-2,0,5/100), (0,-1,7/100),(-1,-1,10/100),(1,-1,1/100),(0,-2,2/100),(0,1,7/100),(-1,1,10/100),(1,1,1/100),(0,2,2/100))]

def solution(n, A):
    OUT = 0
    x = n//2
    y = n//2
    direct = 0 # 방향
    move = 1 # 움직이는 칸의 크기
    while not (x == 0 and y == 0):
        #next_x = 0 if x + int(dx[direct]*move)<0 else x + int(dx[direct]*move)
        #next_y = 0 if y + int(dy[direct]*move)<0 else y + int(dy[direct]*move)
        next_sand = A[next_x][next_y]
        if direct == 0 or direct ==2:
            route = 
        for j in sandMove[direct]:
            amount = 0
            move_x, move_y, percent = j
            
            if 0<=next_x+move_x<n and 0<=next_y+move_y<n:
                sand = int(next_sand*percent)
                amount += sand
                A[next_x+move_x][next_y+move_y] += sand
            else:
                out = int(next_sand*percent)
                amount += out
                OUT += out
        if 0<=next_x+dx[direct]<n and 0<=next_y+dy[direct]<n:
            A[next_x+dx[direct]][next_y+dy[direct]] += (next_sand-amount)
        else:
            OUT += (next_sand-amount)
        A[next_x][next_y] -= next_sand
        if direct == 1 or direct == 3:
            move += 1
        print("(",x,",",y,")","->","(",next_x,",",next_y,")")
        for a in range(n):
            print(A[a])
        print()
        x = next_x
        y = next_y
        direct = (direct+1)%4
    return OUT


if __name__ == "__main__":
    # n 입력
    n = int(input())
    # 각 칸의 모래의 정보 입력
    A = [list(map(int,input().split(" "))) for _ in range(n)]
    result = solution(n, A)
    print(result)
  # 토네이도가 한칸씩 이동하면서 모래를 밀어내야 하는데 바로 건너뛰면서 생각을 해버림
  # 그 부분을 구현하면 됨.
