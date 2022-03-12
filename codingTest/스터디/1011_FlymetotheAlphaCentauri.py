# file name : 1011_FlymetotheAlphaCentauri.py
#
# 공간이동 장치는 이동 거리를 급격하게 늘리면 심각한 결함이 발생
# 이전 작동시기에 k 광년을 이동했다 가정 시, k or k-1 or k+1 광년만 이동가능
# ex ) 첫 작동 시 1만을 이동 가능( 0, -은 의미가 없기 때문 )
# 1 광년 이동 후엔 0,1,2 광년을 이동 가능.
# 공간이동 장치 작동시 에너지 소모가 크기에 최소한의 작동 횟수로 이동 예정.
# y 지점에 도착해서도 공간 이동장치의 안정성을 위해 도착하기 바로 직전엔
# 이동거리 1 광년으로 움직일 예정
# 
# 테스트 케이스의 개수, T
# 현재 위치, 목표 위치 , 0 <= x < y < 2^31
#  
# 시간 제한 : 2초 | 메모리 제한 : 512MB |
# author : Lee Suyoung(2022-03-12)

# 이전에 1광년 이동하면 다음에는 최대 2광년 까지 이동가능하다는 의미구나
# 일단은 무조건 내가 도달할 목적지의 한칸 전으로 가는 걸 짜고 거기서 플러스 1을 무조건 하는
# 그런 느낌으로 가면 될듯
# x는 항상 y보다 작다고 하네

# # t 입력 ( 테케 개수 )
# t = int(input())
# for _ in range(t):
# # x, y 현재, 목표 위치 입력
#     x, y = map(int, input().split(" "))

#     x += 1
#     cnt = 1 
#     kn = 1
#     check = False
#     while True:
#         if x == (y-1):
#             break
#         if x == y :
#             check = True
#             break
#         else:
#             if (x+(kn+1)) <= (y-1):
#                 kn += 1
#                 x += kn
#                 cnt += 1
#             else:
#                 if (x+kn) <= (y-1):
#                     x += kn
#                     cnt += 1
#                 else:
#                     if (x+(kn-1)) <= (y-1):
#                         kn -= 1
#                         x += kn
#                         cnt += 1
#     if check:
#         print(cnt)
#     else:    
#         print(cnt+1)

#def dfs(index, goal, initial_x, cnt, kn):
#     if not isRange(index, goal, initial_x, kn):
#         return INF
#     if index == goal:
#         return cnt
#     return min(dfs(index+(kn-1), goal, initial_x, cnt+1, kn-1)
#     , dfs(index+kn, goal, initial_x, cnt+1, kn), dfs(index+(kn+1), goal, initial_x, cnt+1, kn+1))
# from collections import deque

# t = int(input())
# INF = int(1e9)

# def isRange(index, start, end, kn):
#     if start<=index<=end and kn > 0:
#         return True
#     else:
#         return False

# def bfs(queue, start, end):
#     graph = [INF] * (end+1)
#     while queue:
#         index, kn, cnt = queue.popleft()
#         graph[index] = min(graph[index], cnt)
#         array = [kn-1, kn, kn+1]
#         for i in array:
#             adjIndex = index + i
#             if isRange(adjIndex, start, end, i):
#                 queue.append((adjIndex, i, cnt+1))
#     return graph[end]


# for _ in range(t):
#     x, y = map(int, input().split(" "))
#     cnt = 1
#     queue = deque()
#     if (x - y) == 1:
#         print(cnt)
#         continue
#     queue.append((x+1, 1, cnt))
#     cnt = bfs(queue, x+1, y-1)
#     print(cnt+1)

from collections import deque

t = int(input())
INF = int(1e9)

def isRange(index, start, end, kn):
    if start<=index<=end and kn > 0:
        return True
    else:
        return False

def bfs(queue, start, end):
    result = INF
    while queue:
        length = len(queue)
        for i in range(length):
            index, kn, cnt = queue.popleft()
            if index == end and result > cnt:
                result = cnt
            for i in (kn-1, kn, kn+1):
                if isRange(index+i, start, end, i):
                    queue.append((index+i, i, cnt+1))
    return result

for _ in range(t):
    x, y = map(int, input().split(" "))
    cnt = 1
    if (x - y) == 1:
        print(cnt)
        continue
    cnt = bfs(deque([(x+1, 1, cnt)]), x+1, y-1)
    print(cnt+1)
    
# 처음엔 구현처럼 그냥 반복문을 이용하려 했는데 그럴 경우 내가 목표로 하는 값을
# 넘는 경우에 무한 반복이 발생하게 되니까 그걸 잡을 수 없음.
# dfs를 이용해야겠다 생각 -> 재귀를 이용하려 했음.
# 근데 일반적으로 테스트 서버에서 1000의 뎁스 이상으로 들어가면 recursion error를 발생시킴.
# 그래서 bfs를 이용하려 생각함.
# bfs를 이용하여 queue, graph를 이용해서 목표 인덱스에 값을 쓰려했는데 메모리 초과 발생.
# -> graph 대신 result 변수를 이용해서 minimum value를 반환 -> 그래도 메모리 초과 발생.
