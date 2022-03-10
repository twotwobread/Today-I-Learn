# file name : 1182_부분수열의합.py
# 
# N개의 정수로 이루어진 수열이 있을 떄, 크기가 양수인 부분수열 중에서 
# 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하시오.
# 
# 정수의 개수 1<=N<=20, 정수의 합 |S| <= 1,000,000
# 정수의 절댓값은 100,000을 넘지 않음.
#
# 시간 제한 : 2초 | 메모리 제한 : 256MB |
# author : Lee Suyoug(2022-03-10)

from collections import deque
result = deque()
COUNT = 0
# 정수의 개수, 정수의 합 입력
n, s = map(int, input().split(" "))
# 각 정수 정보 입력
number = list(map(int, input().split(" ")))

def dfs(start, goal):
    global COUNT
    if sum(result) == goal and len(result) > 0:
        COUNT += 1
        #print(result)
    for i in range(start+1, n):
        result.append(number[i])
        dfs(i, goal)
        result.pop()
dfs(-1, s)
print(COUNT)

