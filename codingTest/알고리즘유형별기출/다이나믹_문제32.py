# file name : 다이나믹_문제32.py
# 정수 삼각형
# 선택된 수는 대각선 왼쪽 혹은 오른쪽만 선택가능
# 선택된 수의 합이 최대가 되는 경로를 구하시오.
# 1 <= n <= 500
# 둘째줄 부터 정수 주어짐.
# 풀이 시간 : 30분, 시간 제한 : 2초, 메모리 제한 : 128MB
# author : Lee Suyoung (2022-02-28)

# 그냥 맨 밑에 부터 올라가면서 왼쪽 오른쪽 비교만 하면 됨.
# 이거 트리처럼 접근하면 되겠네 
# 왼쪽 자식 인덱스는 ,,,  안되네 아쉽네.
# 그냥 1, 2, 3, 4 이런식으로 증가하는 느낌이네 오른쪽은 2,3,4,5 ,,,
# 근데 2차원 배열을 이용한다하면 같은 인덱스 다음 인덱스 이렇게 생각.
# 2차원 배열을 이용하기엔 너무 느릴꺼 같다는 생각.

import sys
input = sys.stdin.readline

# n 입력
n = int(input())
# 삼각형 정수 입력
triangle = []
for _ in range(n):
    array = list(map(int, input().split(" ")))
    triangle.extend(array) # 1차원 배열로 만들기 위함.
sumMax = []
for _ in range(len(triangle)):
    sumMax.append(0)
# 현재 인덱스에서 왼쪽 자식, 오른쪽 자식 더해서 비교해서 해당 인덱스 값을 바꾸고 마지막 인덱스는 안들려도 됨.
sumMax[0] = triangle[0]
plus = 2
count = 0
for i in range(len(triangle)-n):
    if count == (plus-1):
        count = 0
        plus += 1
    sumMax[i+(plus-1)] = max(sumMax[i+(plus-1)], sumMax[i]+triangle[i+(plus-1)]) # 왼쪽 자식
    sumMax[i+plus] = max(sumMax[i+plus], sumMax[i]+triangle[i+plus]) # 오른쪽 자식
    count += 1
# 마지막 로우의 인덱스들 중에서 가장 높은 값 추출
print(max(sumMax[len(triangle)-n:len(triangle)]))
 
