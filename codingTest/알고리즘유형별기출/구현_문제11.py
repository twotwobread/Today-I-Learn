# file name : 구현_문제11.py
# 뱀
# 사과를 먹으면 뱀의 길이가 늘어난다. 벽에 부딪히면 게임이 끝난다.
# 게임은 NxN 정사각 보드 위에서 진행되고, 몇몇칸에는 사과가 놓여져 있다. 
# 게임을 시작할 때는 맨위 맨 좌측에 위치하고 뱀의 길이는 1이다. 뱀은 처음에 오른쪽을 향한다.
# 뱀은 매 초마다 이동을 하는데 규칙을 따른다.
#  1. 먼저 뱀은 몸길이를 늘려 머리를 다음 칸에 위치시킨다.
#  2. 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리를 움직이지 않는다.
#  3. 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
# 사과의 위치와 뱀의 이동 경로가 주어질때 이 게임이 몇 초에 끝나는지 계산하시오.
# 2 <= N <= 100, 보드 크기
# 0 <= K <= 100, 사과의 개수
# (행, 열) 로 사과의 위치를 알려줌. 사과의 위치는 모두 다르다. 1,1에는 사과가 없다.
# 1 <= L <= 100, 뱀의 방향 변환 횟수
# 정수 X와 문자 C로 이루어져 있고 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(L) 또는 오른쪽(D)으로 90도 방향 회전
# X는 10,000이하의 양의 정수이고 X가 증가하는 순으로 방향 정보가 주어진다.
# author : Lee Suyoung (2022-02-09)

# 이거 어렵구만
# 먼저 보드에 빈칸 = 0으로 표시를 하고 사과는 1로 표시를 하자. 그리고 뱀의 몸통의 위치를 2라고 표시를 해야할 것 같다.
# 그리고 이동을 하면서 2를 다시 0으로 바꾸고 이런 식으로
# 그리고 벽면은 out of range해서 끝나도록 만들어주자.
# 뱀이 지금 보고 있는 방향도 기억해둬야 할 것 같다.

import sys
from collections import deque
input = sys.stdin.readline

def OutOfRange(row, col, max_row, max_col):
    if row<=0 or row > max_row or col<=0 or col > max_col:
        return False
    return True

# n 입력 , 보드크기
n = int(input())
graph = [[0]*(n+1) for i in range(n+1)]
# K 입력, 사과의 개수
k = int(input())
# K개의 사과의 위치 정보 입력
apple = []
for i in range(k):
    row, col = map(int, input().split())
    graph[row][col] = 1 # 사과의 정보 그래프에 입력
# L 입력, 방향 변환 횟수
l = int(input())
# L개의 방향 변환 정보
spin = deque()
for i in range(l):
    time, direct = input().split()
    spin.append((int(time), direct))
# 방향과 이동을 위한 리스트
direction_name = ["R", "D", "L", "U"] # 상하좌우 이동을 나타냄.
direction_row = [0, 1, 0, -1]
direction_col = [1, 0, -1, 0]

# 현재 행, 열, 방향, 초
now_row, now_col = 1, 1
now_direction = "R"
second = 0
tail = deque()
while True:
    if not OutOfRange(now_row, now_col, n, n) or graph[now_row][now_col] == 2:
        break
    
    if graph[now_row][now_col] != 1:
        if len(tail) > 0:
            x, y = tail.popleft()
            graph[x][y] = 0
    graph[now_row][now_col] = 2 #현재의 위치도 뱀의 몸뚱아리로 만들기
    tail.append((now_row, now_col)) #꼬리 위치를 저장

    # 회전하는 부분
    if len(spin)>0 and second == spin[0][0]: 
        t, s = spin.popleft()
        if s == "L":
            direct_index = direction_name.index(now_direction)
            direct_index -= 1
            if direct_index == -1:
                direct_index = 3
            now_direction = direction_name[direct_index]
        elif s == "D":
            direct_index = direction_name.index(now_direction)
            direct_index += 1
            if direct_index == 4:
                direct_index = 0
            now_direction = direction_name[direct_index]
    direct_index = direction_name.index(now_direction)
    next_row, next_col = now_row+direction_row[direct_index], now_col+direction_col[direct_index]
    now_row, now_col = next_row, next_col
    second+=1

print(second)
