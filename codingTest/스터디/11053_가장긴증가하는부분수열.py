# file name : 11053_가장긴증가하는부분수열.py
# 
# A = {10,20,10,30,20,50}
# 길이는 4이고 {10,20,30,50}
# 
# 수열의 크기, 1 <= N <= 1,000
# 수열 A, 1 <= Aj <= 1,000
# 시간 제한 : 1초 | 메모리 제한 : 256MB |
# author : Lee Suyoung ( 2022-03-15 )


# LIS로 짜면 될듯
# 이분 탐색을 짜주고 만약 나보다 이전 값보다 크면 그냥 넣고
# 크지 않으면 이분 탐색으로 위치 찾고 넣고 !!

# n 입력
n = int(input())
# 수열 A 입력
A = list(map(int, input().split(" ")))
# 수열을 넣기 위한 리스트 선언
L = [A[0]]
compare = 0

def binarySearch(list, left, right, goal):
    while left < right:
        mid = (left+right)//2
        if goal > list[mid]:
            left = mid + 1
        else:
            right = mid
    return right

for a in A[1:]:
    if L[compare] < a:
        L.append(a)
        compare += 1
    else:
        L[binarySearch(L, 0, len(L)-1, a)] = a
print(len(L))

# 기본적인 간단한 LIS 문제
