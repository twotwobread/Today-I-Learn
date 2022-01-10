# file name: 이코테_실전7_2.py
# 부품이 N개 존재 -> M개 종류 대량 구매
# M개의 부품이 존재하는지 확인
# 1<= N <= 1,000,000 , 1<= M <= 100,000
# author: Lee Suyoung (2022-01-10)

# 최대 100,000 종류를 확인해야하는데 1,000,000 번씩 돌수있다.
# 그럼 100,000,000,000 번의 탐색이 필요할 수 있네 -> 이진 탐색 사용

def binarySearch(data, start, end, target):
    if start>end:
        return None
    mid = (start+end)//2
    if data[mid]==target:
        return mid
    elif data[mid]<target:
        return binarySearch(data, mid+1, end, target)
    else:
        return binarySearch(data, start, mid-1, target)

import sys

# n 입력 
n = int(input())
# 가게 보유중인 부품 종류 리스트 입력 (sys 사용)
market = list(map(int, input().split()))
# m 입력
m = int(input())
# 손님이 요구하는 부품 종류 리스트 입력 (sys 사용)
customer = list(map(int, input().split()))

# 이진 탐색 사용 -> 가게 보유 부품 리스트 정렬 필요
market.sort()
for c in customer:
    result = binarySearch(market, 0, len(market)-1, c)
    if result == None:
        print("no", end=' ')
    else:
        print("yes", end=' ')

"""
이렇게 문제를 풀면 부품을 찾는 과정에서 최악의 경우 시간 복잡도 O(M x log N)의 연산이 필요하여 이론상 최대 약 200만번의 연산이 이루어진다고 분석 가능.
오히려 부품을 정렬하기 위해서 요구되는 시간 복잡도 O(N x log N)이 이론적으로 최대 약 2,000만으로 더욱 더 많은 연산이 필요한 것을 알 수 있음.
결과적으로 이진 탐색을 사용하는 문제 풀이 방법의 경우 시간 복잡도는 O((M + N) x log N)이다.
"""

#### [ 계수 정렬을 이용한 비교 ] ####
print()
# n 입력
n = int(input())
# 가게 부품 리스트 입력
all_kind = [0]*1000001
for i in input().split():
    all_kind[int(i)]+=1
# m 입력
m = int(input())
# 손님이 요구한 부품 종류 입력
customer = list(map(int, input().split()))
# 가게 부품 중 가장 큰 값을 이용해서 모든 종류 리스트 생성
# 반복을 통해 값을 모든 종류 리스트에 넣는다.
# 그리고 손님이 요구한 부품 종류의 인덱스에 0이 아니면 존재
for c in customer:
    # 0이면 없음.
    if all_kind[c] == 0:
        print("no", end=' ')
    else:
        print("yes", end=' ')


##### [ set을 이용한 풀이 ] #####
# 단순히 특정한 데이터가 존재하는지를 검사하기 때문에 효과적이다.
n = int(input())
array = set(map(int, input().split()))

m= int(input())
l = list(map(int, input().split()))

for i in l:
    if i in array:
        print("yes", end=" ")
    else:
        print("no", end=" ")
