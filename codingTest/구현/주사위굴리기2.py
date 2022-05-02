# nxn 격자
# 파이어볼 m개 발사, 각자 위치에서 대기중 그 후 이동
# 파이어볼 정보 : (r,c), m 질량, d 방향, s 속도
# 파이어볼 방향은 8개의 칸의 방향을 의미
# ↑ ↗ → ↘ ↓ ↙ ← ↖ ( 0 ~ 7 )
# 1. 파이어볼 자신의 방향으로 이동 ( 1번 열, 행과 n번 열, 행 붙어있음)
# 2. 이동 후, 2개 이상의 파이볼은 하나로 합쳐지고 4개로 나누어지는데
# 질량 = (질량합)/5, 속력 = (속력합)/(볼개수), 방향 = 모두 홀/짝수 (0,2,4,6), 이외 (1,3,5,7)
# 3. 질량 0인 파이어볼은 소멸
# K번 명령 후, 남아있는 파이어볼 질량의 합 구하기
# 격자 최대 50x50
# K 최대 1000
# 처음 볼 개수 최대 2500개
# 질량 최대 1000, 속도 최대 1000

# 일단 무조건 시뮬레이션
# 이동할때, 데이터를 빼고 넣고 어떻게 할지 고려
# 파이어볼이 있는 곳을 합치고 나눌때 데이터를 전부 없애고 다시 만들어야하는데 이걸 생각해야함.
# 내가 생각할 때, 무조건 파이볼 나누고 합칠때 새로운 행렬을 만들어서 옮기는게 좋을꺼 같음.
# 아니면 클리어를 하고 거기에 다시 넣던가.
# defaultdict 써보자. -> 여러개의 값이 들어갈 수 있는데. 그걸 방향 별로 나눠서 인덱스에 넣고
# 그 인덱스를 튜플로 딕셔너리에 넣어서 해당 값을 넣자. -> 이건 안됨. 어떤게 자기 정보인지
# 모르잖아.
# (r,c), m, s, d 이렇게 정보가 있는데
# 그러면 (r,c,d,m) 이걸로 저장을 하고 m이 같으면 어짜피 상관 없기 때문에
# 이렇게 표현 하는 게 좋을듯.
# defaultdict로도 가능 그이유는 어짜피 이동후에는 뭉쳐져있는 애들을 똑같은 질량, 속도로
# 방향만 바꿔서 쪼개기 때문에 이 정보가 누구껀지 판단하지 않아도 괜찮음
# 그래서 가능함. 그리고 리스트를 이용한 것보다 빠름.

from collections import defaultdict

# 이동하는 함수
def move(n, fireGraph, new):
    dx = (-1, -1, 0, 1, 1, 1, 0, -1) # ↑ ↗ → ↘ ↓ ↙ ← ↖ ( 0 ~ 7 )
    dy = (0, 1, 1, 1, 0, -1, -1, -1) # 1, 3, 5, 7
    for i in range(n):
        for j in range(n):
            for f in fireGraph[i][j]:
                m, s, d = f
                next_row = (i + dx[d] * s) % n
                next_col = (j + dy[d] * s) % n
                new[next_row][next_col].append([m, s, d])

def oddEvenCheck(check):
    even = False; odd = False
    for c in check:
        if c%2==0:
            even = True
        else:
            odd = True
    if even and odd:
        return False
    else:
        return True

# 합치기 & 나누기 함수
def mergeDivide(n, newGraph):
    for i in range(n):
        for j in range(n):
            if len(newGraph[i][j]) > 1: # 파이어볼 1개 이상인 경우
                length = len(newGraph[i][j])
                newWeight = 0; newSpeed = 0
                check = []
                for k in newGraph[i][j]:
                    newWeight += k[0]
                    newSpeed += k[1]
                    check.append(k[2])
                newGraph[i][j].clear()
                newWeight = newWeight//5
                newSpeed = newSpeed//length
                if newWeight > 0:
                    if oddEvenCheck(check):
                        for t in range(4):
                            newGraph[i][j].append([newWeight, newSpeed, t*2])
                    else :
                        for f in range(4):
                            newGraph[i][j].append([newWeight, newSpeed, f*2+1])

def solution(n, m, k, fireInfo):
    # graph 만들기
    fireGraph = [[[] for _ in range(n)] for _ in range(n)]
    for f in fireInfo:
        r, c, m, s, d = f
        fireGraph[r-1][c-1].append([m, s, d])
    for _ in range(k): # k번 명령
        # 1. 이동
        new = [[[] for _ in range(n)] for _ in range(n)] # 이동을 마친 그래프
        move(n, fireGraph, new)
        # 2. 합치기 & 나누기 + 소멸이 될수도 있음.
        mergeDivide(n, new)
        # 새로운 그래프 복사
        sumValue = 0
        for r in range(n):
            for c in range(n):
                fireGraph[r][c].clear()
                for d in new[r][c]:
                    sumValue += d[0]
                    fireGraph[r][c].append(d)
    return sumValue

if __name__ == "__main__":
    n, m, k = map(int, input().split(" "))
    fireInfo = [list(map(int, input().split(" "))) for _ in range(m)]
    print(solution(n, m, k, fireInfo))
