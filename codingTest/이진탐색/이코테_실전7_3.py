# file name: 이코테_실전7_3.py
# 절단기에 높이 H로 지정하면 줄지어진 떡이 한 번에 절단됨. 높이가 H보다 길면 잘리고 짧으면 잘리지 않는다.
# 손님은 이 잘린 떡의 길이 만큼을 들고간다.
# 손님이 왔을 때 요청한 떡의 길이가 M일 때 "적어도" M만큼의 떡을 얻기 위한 절단기에 설정할 높이의 최댓값을 구해라.
# 1 <= N <= 1,000,000, 1 <= M <=2,000,000,000, 0 <= 높이 <= 1,000,000,000
# 시간 제한: 2초, 메모리 제한: 128MB
# author: Lee Suyoung (2022-01-10)

# 계수 정렬을 이용하고 이진 탐색도 조져야할꺼 같다.
# 계수 정렬을 이용해서 줄지어진 떡을 다 넣고 그걸 줄지어진 놈의 중간부터 자르면서 이진 탐색을 조지는 겨
# 결국은 자를 수 있는 길이는 0 ~ 줄지어진 놈의 최대 길이 까지니까 이렇게 조져보자.
# 계수 정렬없이 그냥 이진 탐색만 써서 해도 될꺼 같은데 계수 정렬을 쓸곳이 없음.
# 아래처럼 풀면 적어도가 성립되지 않음.
# def binarySearch(l, start, end, target):
#     if start>end:
#         return None
#     mid = (start+end)//2
#     slice_sum = 0
#     for i in l:
#         temp = i - mid
#         if temp < 0:
#             temp = 0
#         slice_sum += temp

#     if target==slice_sum:
#         return mid
#     elif target < slice_sum:
#         return binarySearch(l, start, mid-1, target)
#     else:
#         return binarySearch(l, mid+1, end, target)


# import sys

# # n, m 입력
# n, m = int(input().split())
# # 줄지어진 떡의 길이 입력 (길이 최대 10억)
# length = list(map(int, sys.stdin.readline().rstrip().split()))
# # 줄지어진 떡의 길이 중 max 만큼의 리스트 생성
# result = binarySearch(length, 1, max(length), m)
# if result == None:
#     print("잘못된 입력값입니다.")
# else:
#     print(result)


###### [ 적어도가 성립하기 위해서 ] ######
import sys
# 시간적 여유가 없기에 함수 오버헤드를 막기 위해서 반복문을 사용하는 것이 좋을 것 같다. 
def binarySearch_2(l, arr, start, end, target):
    if start>end:
        return None
    mid = (start + end)//2
    slice_sum=0
    for i in l:
        temp = i - mid
        if temp < 0:
            temp = 0
        slice_sum += temp
    arr.append((mid, slice_sum))

    # 이진 탐색에서 적어도라는 말이 들어갔기에 같은 경우와 넘치는 경우를 묶을 수 있다.
    if target==slice_sum: # 같은 경우
        return mid
    elif target < slice_sum: # 넘치는 경우
        return binarySearch_2(l, arr, mid+1, end, target)
    else: # 부족한 경우
        return binarySearch_2(l, arr, start, mid-1, target)

n, m = map(int, input().split())
# 미리 array를 못만듬 10억개라서 너무 크다.
length = list(map(int, sys.stdin.readline().rstrip().split()))
array = []

result = binarySearch_2(length, array, 1, max(length), m)

# 여기서 시간초과가 날 것이다.
if result == None:
    at_least = min([a for a in array if m < a[1]], key=lambda l: l[1])
    print(at_least[0])
else:
    print(result)

"""
전형적인 파라메트릭 서치 유형의 문제이다.
파라메트릭 서치는 최적화 문제를 결정 문제(예 or 아니오로 답하는 문제)로 바꾸어 해결하는 기법이다.
'원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제'에 주로 파라메트릭 서치를 이용한다. 예를 들어 가장 큰 값을 찾으라는 최적화 문제라면
이진 탐색으로 결정 문제를 해결하면서 좁혀갈 수 있다. 코테나 프로그래밍 대회에서는 보통 파라메트릭 서치 유형은 이진 탐색을 이용하여 해결한다.
이 문제의 풀이 아이디어는 의외로 간단한데 적절한 높이를 찾을 때까지 절단기의 높이 H를 반복하여 조정하는 것이다.
그래서 '현재 이 높이로 자르면 조건을 만족할 수 있는가?'를 확인 후에 조건의 만족 여부에 따라서 탐색 범위를 좁혀갈 수 있다. 범위를 좁힐때 이진 탐색의 원리 이용한다.
절단기의 높이는 1부터 10억까지의 정수 중 하나이다. 그럼 이진 탐색을 떠올려야한다. 겁나 크니까. 높이 H를 이진 탐색으로 찾으면 대략 31번 만에 경우의 수를 모두 고려할 수 있다.
이때 떡의 개수가 100만개니까 최대 3000만번의 연산으로 가능하다. 시간 제한이 2초라서 아슬아슬하게 시간 초과 없이 정답 판정을 받을 것이다.
"""
# 일단 시간적 여유가 부족하기에 재귀를 빼고 반복문으로 구현할 예정
# 내가 짠 코드는 시간 초과가 날 것이다. 마지막에 다시 비교하기 때문이다.
#### [제시된 답안] ####

n, m = map(int, input().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))

#이진 탐색 반복
result = 0
start = 1; end=max(array)
while start<=end:
    mid = (start+end)//2
    slice_sum = 0
    for a in array:
        # 잘랐을 때 떡의 양 계산
        if a > mid:
            slice_sum += (a-mid)
    #자른 떡의 양이 부족한 경우
    if slice_sum < m:
        # 더 많이 잘라야 하니까 더 짧아져야함.
        end = mid-1
    #자른 떡의 양이 딱 맞거나 충분한 경우
    else:
        # 이부분이 적어도를 성립한다. 적어도라는 의미는 딱 맞거나 넘치는 경우를 의미하니까 이처럼 하나로 묶을 수 있다.
        # 그래서 mid == slice_sum인 조건문이 필요가 없다. 이러한 사고를 하는 것이 중요할 것 같다.
        result = mid # 결국 가장 가까운데 충분한 경우가 됨.
        start = mid+1

print(result)
