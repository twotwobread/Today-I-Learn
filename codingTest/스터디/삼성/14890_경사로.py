# file name: 14890_경사로.py
# NxN 지도 존재, 각 칸에 그 곳의 높이가 적혀져있다.
# 이 지도에서 지나갈 수 있는 길이 몇 개 있는지 알아보려함.
# 길이란 한 행 또는 한 열 전부를 나타내며, 한쪽 끝에서 다른 쪽 끝까지 지나가는 것.
# 길을 지나갈려면 길에 속한 모든 칸의 높이가 같아야함.
# 혹은 경사로를 놓아서 지나갈 수 있는 길을 만들 수 있음.
# 경사로의 높이는 항상 1이고 길이는 L임.(개수는 부족할 일 없음.)
# 경사로는 낮은 칸과 높은 칸을 연결하고, 아래의 조건을 만족해야함.
#   - 경사로는 낮은 칸에 놓으며, L개의 연속된 칸에 경사로의 바닥이 모두 접해야함.
#   - 낮은 칸과 높은 칸의 높이 카이는 1이어야함.
#   - 경사로를 놓을 낮은 칸의 높이는 모두 같아야 하고, L개의 연속되어 있어야함.
# 아래의 경우에는 경사로를 놓을 수 없음.
#   - 경사로를 놓은 곳에 또 경사로를 놓는 경우
#   - 낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우
#   - 낮은 지점의 칸의 높이가 모두 같지 않거나, L개의 칸이 연속되지 않는 경우
#   - 경사로를 놓다가 범위를 벗어나는 경우
#
# 2<=N<=100, 1<=L<=N
# 지도 정보, 각 칸의 높이는 10보다 작거나 같은 자연수
#
# 길의 개수 출력
#
# 시간제한 : 2초, 메모리 제한 : 512MB
# author : Lee Suyoung(2022-03-29)

# 지금 그냥 graph만 돌리는데
# zip 이용해서 행, 열 바꾼 graph도 같이 돌려야 더 빠를 꺼임
# 해당 포문에서 동시에 처리해줘야함.

def solution(n, l, graph):
    # 열로 이루어진 길을 위해서
    rotateGraph = list(zip(*graph))
    rotateCnt = 0
    cnt =0
    for i in range(n):
        # 행부분 지나갈 수 있는지 확인.
        standard = graph[i][0]
        runway = [0]*n
        check = True
        for j in range(1, n):
            if standard != graph[i][j]:
                if standard-graph[i][j]==1: # 앞에가 한칸 높은 경우
                    for a in range(l): # l 길이만큼
                        if (j+a)>=n or graph[i][j+a] != graph[i][j] or runway[j+a] == 1: # 낮은 구간과 높이가 같고 경사로가 없다면
                            check = False
                            break
                    if not check:
                        break
                    for a in range(l): # l 길이만큼
                        runway[j+a] = 1 # 경사로 놓기  
                elif standard-graph[i][j]==-1: # 뒤에가 한칸 높은 경우
                    for a in range(1, l+1):
                        if (j-a)<0 or graph[i][j-a] != graph[i][j-1] or runway[j-a] == 1: # 낮은 구간과 높이가 같고 경사로가 없다면
                            check = False
                            break
                    if not check:
                        break
                    for a in range(1, l+1): # l 길이만큼
                        runway[j-a] = 1 # 경사로 놓기
                else:
                    check = False
                    break # 이 행은 지나갈 수 없음.
                standard = graph[i][j]
        if check:
            cnt += 1
        # 열부분 지나갈 수 있는지 확인.
        rotateCheck = True
        rotateRunway = [0]*n
        rotateStandard = rotateGraph[i][0]
        for j in range(n):
            if rotateStandard != rotateGraph[i][j]:
                if rotateStandard-rotateGraph[i][j]==1: # 앞에가 한칸 높은 경우
                    for a in range(l): # l 길이만큼
                         if (j+a>=n) or rotateGraph[i][j+a] != rotateGraph[i][j] or rotateRunway[j+a] == 1: # 낮은 구간과 높이가 같고 경사로가 없다면
                            rotateCheck = False
                            break
                    if not rotateCheck:
                        break
                    for a in range(l): # l 길이만큼
                        rotateRunway[j+a] = 1 # 경사로 놓기
					  
                elif rotateStandard-rotateGraph[i][j]==-1: # 뒤에가 한칸 높은 경우
                    for a in range(1, l+1):
                        if (j-a<0) or rotateGraph[i][j-a] != rotateGraph[i][j-1] or rotateRunway[j-a] == 1: # 낮은 구간과 높이가 같고 경사로가 없다면
                            rotateCheck = False
                            break
                    if not rotateCheck:
                        break
                    for a in range(1, l+1): # l 길이만큼
                        rotateRunway[j-a] = 1 # 경사로 놓기 
                else:
                    rotateCheck = False
                    break # 이 행은 지나갈 수 없음.
                rotateStandard = rotateGraph[i][j]
        if rotateCheck:
            rotateCnt += 1
    return cnt+rotateCnt
		
if __name__ == "__main__":
    # n, l 입력
    n, l = map(int, input().split(" "))
    # 지도 정보 입력
    graph = [list(map(int, input().split(" "))) for _ in range(n)]
    print(solution(n, l, graph))
