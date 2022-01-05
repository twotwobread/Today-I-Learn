# file name : 이코테_실전4_2.py
# 8x8 좌표 평면 상에서 이동
# 1. 수평으로 두칸 이동한 뒤에 수직으로 한 칸
# 2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸
# 나이트의 위치가 주어져ㅅ을 때 나이트가 이동할 수 있는 경우의 수 출력
# 행은 1-8, 열은 a-h
# author : Lee Suyoung (2022-01-05)

# 갈 수 있는 모든 경우의 수에 대한 좌표의 이동값을 만들고
# 그걸로 다 비교해보면 된다.

# 위치좌표 n을 입력하는 부분
n = input()

# 좌표에서 이동할 수 있는 모든 경우의 수 선언
move = [(2,1), (2,-1), (-2,1), (-2,-1), (1,-2), (-1,-2), (1,2), (-1,2)] # RD, RU, LD, LU, UR, UL, DR, DL 
# 모든 경우의 수를 다 확인하면서 갈 수 있는 위치 갯수 세기
cnt = 0
for m in move:
    row = ord(n[1]) + m[1]; col = ord(n[0]) + m[0]
    if row<ord('1') or row>ord('8') or col < ord('a') or col > ord('h'):
        #print("{}, {}, {}".format(m, chr(row),chr(col)))
        continue
    else:
        cnt += 1
print(cnt)
# 결과값 출력

###[ 제시된 예시 답안 ]###
n = input()
row = int(n[1])
column = int(ord(n[0])) - int(ord('a')) + 1

steps = [(2,1), (2,-1), (-2,1), (-2,-1), (1,-2), (-1,-2), (1,2), (-1,2)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if 1 <= next_row <= 8 and 1 <= next_column <=8:
        result += 1

print(result)
