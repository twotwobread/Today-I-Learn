# file name : 15685_드래곤커브.py
# 드래곤 커브는 세가지 속성을 가짐
# 1. 시작 점
# 2. 시작 방향
# 3. 세대
# 0 세대 드래곤 커브는 길이가 1인 서분 (0,0)에서 시작방향이 오른쪽임.
# 1 세대 드래곤 커브는 0세대 커브를 끝 점 기준으로 시계 방향 90도 회전 후 드래곤 커브의 끝 점에 붙인 것.
# 2 세대 드래곤 커브도 같은 방식
# 즉, K(K>1)세대 드래곤 커브는 K-1 세대 드래곤 커브를 끝 점을 기준으로 90도 시계 방향 회전 시킨 후 끝 점에 붙인 것
# 100x100인 격자 위에 드래곤 커브가 N개 존재
# 이때, 크기가 1x1인 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 정사각형의 개수를 구하는 프로그램 작성.
# 격자의 좌표는 (x,y), 0<=x<=100, 0<=y<=100
#
# 드래곤 커브의 개수 (1<=N<=20)
# N개의 줄, 드래곤 커브의 정보, x,y,d,g ( x,y는 드래곤 커브의 시작 점, d는 시작 방향, g는 세대) ( 0<=x,y<=100, 0<=d<=3, 0<=g<=10 )
# 0 : x좌표가 증가하는 방향, 1: y좌표가 감소하는 방향, 2 : x좌표가 감소하는 방향, 3 : y좌표가 증가하는 방향

dx = (1, 0, -1, 0) # 오, 위, 좌, 아래
dy = (0, -1, 0, 1)
#direction = [(1,0,3,2), (2,3,0,1), (3,2,1,0), (0,1,2,3)]

def find_tangular(num, pos, check):
    x, y = pos
    if (x+1, y) in check[num+1:]

def solution(n, dragon):
    realPos=[]
    for curve in dragon:
        G_dragon = []
        x, y, d, g = curve

        # 0세대 좌표 넣기
        G_dragon.append([x, y, d])
        realPos.append((x, y))
        pos_x, pos_y = x+dx[d], y+dy[d]
        G_dragon.append([pos_x, pos_y, (d+1)%4])
        if 0<=pos_x<=100 and 0<=pos_y<=100:
            realPos.append((pos_x, pos_y))
    
        # 다음세대 좌표 넣기
        for i in range(g):
            temp = [] # 추가되는 좌표를 위함.
            x, y = G_dragon[-1][0], G_dragon[-1][1] # 끝점 좌표
            for j in range(len(G_dragon)-1, 0, -1): # 현재 좌표부터 최초 좌표 전까지
                direct = G_dragon[j][2]
                pos_x, pos_y = x+dx[direct], y+dy[direct]
                temp.append([pos_x, pos_y, (direct+1)%4])
                if 0<=pos_x<=100 and 0<=pos_y<=100:
                    realPos.append((pos_x, pos_y))
                x, y = pos_x, pos_y
            G_dragon.extend(temp)
    realPos = set(realPos) # 중복요소 제거
    #for i in range(len(realPos)):
    #    count = find_tangular(i, realPos[i], realPos)
    print(realPos)
    print(len(realPos))

    # 사각형 수 구하기.
    
    return 0

                
if __name__ == "__main__":
    # n 입력
    n = int(input())
    # 드래곤 커브 정보 입력
    dragon = [list(map(int, input().split(" "))) for _ in range(n)]
    result = solution(n ,dragon)
    print(result)
