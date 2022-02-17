# file name : 이진탐색_문제27.py
# 정렬된 배열에서 특정 수의 개수 구하기
# N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있다. 이떄 이 수열에서 x가 등장하는 횟수를 계산하세요
# 이 문제는 O(logN)으로 알고리즘을 설계하지 않으면 시간초과 판정을 받음.
# 1 <= N <= 1,000,000 , -10^9 <= x <= 10^9
# N개의 원소가 정수 형태로 공백으로 구분되어 입력
#  author : Lee Suyoung(2022-02-17)

# 일단 중요한게 계수정렬을 사용할 수 없네.
# 범위가 너무 쓰렉바다.
# 그럼 일단 bisect 이용해서 풀어보자.


from bisect import *

n, x = map(int, input().split())
data = list(map(int, input().split()))

left = bisect_left(data, x)
right = bisect_right(data, x)

if left == right:
	print(-1)
else:
	print(right-left)

### [ 제시된 답안 ] ###
# bisect를 쓰지 않고 x에 해당하는 값의 처음 인덱스와 마지막 인덱스를 찾아
# 갯수를 확인할 것이다. 그러기 위해서는 두개의 이진 탐색 함수가 필요하다.
# 첫번째 인덱스를 찾는 이진 탐색 함수와 마지막 인덱스를 찾는 이진 탐색함수


def first(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    # 해당 값을 가지는 원소 중 가장 왼쪽에 있는 경우에만 인덱스 반환
    if (mid == 0 or target > array[mid-1]) and array[mid] == target: # 찾는 타겟과 같고 인덱스가 0이거나 하나 작은 인덱스보다 값이 크다 (해당값의 첫시작 인덱스)
        return mid
    elif array[mid] >= target:
        return first(array, target, start, mid-1)
    elif array[mid] < target:
        return first(array, target, mid+1, end)
def last(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if (mid == (n-1) or target < array[mid+1]) and target == array[mid]:
        return mid
    elif array[mid] >= target:
        return last(array, target, start, mid-1)
    elif array[mid] < target:
        return last(array, target, mid+1, end)
# 정렬된 수열에서 값이 x인 원소의 개수를 세는 메서드
def count_by_value(array, x):
    # 데이터의 개수
    n = len(array)

    # x가 처음 등장한 인덱스 계산
    a = first(array, x, 0, n-1)

    if a == None:
        return 0
    b = last(array, x, 0, n-1)

    return b-a+1


n, x = map(int, input().split())
array = list(map(int, input().split()))
#값이 x인 데이터의 개수 계산
count = count_by_value(array, x)

if count == 0:
    print(-1)
else:
    print(count)
