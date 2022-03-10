# file name : 14889_스타트와링크.py
# 축구는 평일 오후에 하고 의무 참석도 아님.
# 축구하려고 모인 사람은 N명 N은 짝수임.
# N/2명으로 이루어진 스트트팀과 링크 팀으로 사람을 나눠야함.
# Sij는 i번 사람과 j번 사람이 같은 팀에 속한 경우 팀에 더해지는 능력치임.
# 팀의 능력치는 팀에 속한 모든 쌍의 Sij의 합임.
# Sji와 Sij는 다를 수 있음.
# 팀의 능력치의 차이를 최소로 하려함
# 
# 4<=N<=20, N은 짝수.
# N개의 줄에 S
# Sii는 항상 0, 나머지 Sij는 1보다 크거나 같고 100보다 작거나 같은 정수.
#  
# 시간 제한 : 2초 | 메모리 제한 : 512MB | 
# author : Lee Suyoung(2022-03-10)

# n 입력
from collections import deque

result = deque()
MINVALUE = int(1e9)
SUM = 0
n = int(input())
# n개의 줄 s 정보 입력
graph = [list(map(int,input().split(" "))) for _ in range(n)]

def calculateSum(graph):
    global MINVALUE
    sum = 0
    for i in result:
        for j in result:
            sum += graph[i][j]
    other = []
    otherSum = 0
    for i in range(n):
        if i not in result:
            other.append(i)
    for i in other:
        for j in other:
            otherSum += graph[i][j]
    if MINVALUE > abs(sum - otherSum):
        MINVALUE = abs(sum - otherSum)
        
def dfs(graph, num):
    global MINVALUE
    if len(result) >= n/2:
        calculateSum(graph)
        return
    for i in range(num+1, n):
        result.append(i)
        dfs(graph, i)
        result.pop()

for i in range(n):
    result.append(i)
    dfs(graph, i)
    result.pop()
print(MINVALUE)

