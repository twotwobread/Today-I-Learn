# # file name : 다이나믹_문제34.py
# #
# # 병사 배치하기
# # N명의 병사가 무작위로 나열
# # 각 병사는 특정한 값의 전투력 보유, 전투력 높은 병사가 앞쪽에 오도록 배치(내림차순)
# # 배치 과정에서 특정 위치에 있는 병사를 열외시키는 방법 이용
# # 남아 있는 병사의 수가 최대가 되도록 하려함.
# # 
# # 1 <= N <= 2,000
# # 각 병사의 전투력 , fight <= 10,000,000
# #
# # 남은 병사의 수가 최대이고 내림차순이 되는 열외시켜야 하는 병사의 수를 출력
# #
# # 풀이시간 : 40분 | 시간 제한 : 1초 | 메모리 제한 : 256MB |
# # author : Lee Suyoung (2022-03-13)

# # 두 가지 경우로 나눌 수 있지 않나
# # 하나는 앞의 놈을 제외, 하나는 뒤의 놈을 제외
# # 앞의 놈이 내보다 안큰 경우, 뒤의 놈이 내보다 안작은 경우
# # 재귀를 이용해서 앞뒤를 비교해서 제외하는 경우를 다 살펴보면 될꺼같은데

# #count = [INF]*n
# #kn = INF
# # def countNum(soldier, index, before, cnt):
# #     if index == len(soldier):
# #         count[index-1] = min(count[index-1], cnt)
# #         return
# #     countNum(soldier, index+1, before, cnt+1) # 자기 자신을 없앤 경우
# #     if before <= soldier[index]: # 이전 인덱스를 없앤 경우
# #         countNum(soldier, index+1, soldier[index], cnt+1)
# #     else: # 이전 인덱스를 살려둔 경우
# #         countNum(soldier, index+1, soldier[index], cnt)

# from collections import deque
# # n 입력
# n = int(input())
# INF = int(1e9)
# # 병사 정보 입력
# soldier = list(map(int, input().split(" ")))

# def countNumber():
#     queue = deque()
#     queue.append((INF, 0, 0))
#     count = INF
#     while queue:
#         length = len(queue)
#         for _ in range(length):
#             before, cnt, index = queue.popleft()
#             if index == len(soldier):
#                 count = min(count, cnt)
#             else:
#                 queue.append((before, cnt+1, index+1)) # 자기 자신을 없앤 부분
#                 if before <= soldier[index]:
#                     queue.append((soldier[index], cnt+1, index+1)) # 이전 부분을 없앤 부분
#                 else:
#                     queue.append((soldier[index], cnt, index+1)) # 이전 부분을 살린 부분
#     return count
# count = countNumber()
# print(count)

def binarySearch(power, left, right, goal):
    while left < right:
        mid = (left+right)//2
        midValue = power[mid]
        if goal < midValue:
            left = mid + 1
        else:
            right = mid
        #print(left, right)
    return right
# n 입력
n = int(input())
# power 입력
power = list(map(int, input().split(" ")))

L = [power[0]]
compare = 0
length = []
for p in power[1:]:
    #print("power = ", p)
    if L[compare] > p:
        L.append(p)
        compare = compare + 1
    else:
        L[binarySearch(L, 0, compare, p)] = p
    #print("compare = ", compare, "\nL = ", L)
    #print()

print(n-len(L))

# LIS를 이용하는 문제
# 처음엔 BFS를 이용하여 풀려고 하였으나 메모리 초과가 발생.
# DP 문제 중에 LIS, LCS는 많이 쓰인다.
# 잘 알고 있는 것이 좋을 듯 하다.
