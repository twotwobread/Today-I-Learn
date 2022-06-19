# < 떡볶이 떡 만들기 >
# 유형 : 이분 탐색 -> 변형
# 자료구조 : 튜플 - 떡 길이 저장
# [ 아이디어 ]
# - 이분 탐색을 조금 변형해서 중간값을 이용해 떡을 잘라보고 M과 같거나 이상이면 end = middle을 이용.
# - M보다 작으면 start = middle + 1을 이용.

def solution(start, end, goal):
    while start < end:
        middle = (start + end + 1) // 2
        sliceSum = 0
        for i in range(n):
            if rice[i] > middle:
                sliceSum += (rice[i] - middle)
        if sliceSum < goal:
            end = middle - 1
        else:
            start = middle
    return start

if __name__ == "__main__":
    n, m = map(int, input().split())
    rice = tuple(map(int, input().split()))
    print(solution(0, max(rice), m))
