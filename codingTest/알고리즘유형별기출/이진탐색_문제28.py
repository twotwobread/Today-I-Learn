# file name : 문제28.py
# 고정점 찾기
# 고정점 : 수열의 원소 중에서 그 값이 인덱스와 동일한 원소를 의미
# 예를 들어 수열 a = {-15, -4, 2, 8, 13}이 있을 때 a[2] = 2이므로, 고정점은 2가 됩니다.
# 하나의 수열이 N개의 서로 다른 원소를 포함하고 있으며, 모든 원소가 오름차순으로 정렬되어 있습니다. 이때 이 수열에서 고정점이 있다면
# 고정점을 출력하는 프로그램을 작성하세요. 마약 고정점이 없다면 -1을 출력합니다.
# 단, 이문제는 시간 복잡도 O(log N)으로 알고리즘으 설계하지 않으면 '시간 초과' 판정을 받습니다.
# 1<=N<=1,000,000
# -10^9 <= 각 원소의 값 <= 10^9, N개의 원소가 정수 형태로 공백으로 구분되어 입력
# author: Lee Suyoung (2022-02-11)

# 일단 탐색에 관한 문제인 거 같고 근데 딱 고정된 무언가를 찾는게 아니라서 이진 탐색을 이용을 못할꺼 같은데
# 일단 그냥 순차 탐색으로 짜보자
# 근데 좀만 더 생각을 해보면 이진탐색을 할 수 있었지.
# 인덱스랑 인덱스 값을 비교하면서 정렬이 되어있으니까
# 인덱스보다 인덱스 값이 더 크다는 것은 더 큰 인덱스로 가도 똑같애 더 커
# 그니까 아래로 가야하고 인덱스보다 인덱스 값이 작다는 것은 밑으로 가도 똑같애 더 작어 그니까 위로 가야함.

# n 입력
n = int(input())
# n개의 수열 원소 입력
a = [0 for _ in range(n)]
a = list(map(int, input().split()))
# 이진탐색할 수 있겠다. 오우

def binarySearch(array):
    start = 0
    end = len(array) - 1
    result = -1
    while start<=end:
        mid = (end+start)//2 # 중간 인덱스
        if array[mid] == mid:
            result = mid
            break
        elif array[mid] < mid:
            start = mid + 1
        else:
            end = mid - 1
    return result

result=binarySearch(a)
print(result)


# check = False
# for i in range(n):
#     if a[i] == i:
#         check = True
#         print(a[i])
# if check == False:
#     print("-1")
