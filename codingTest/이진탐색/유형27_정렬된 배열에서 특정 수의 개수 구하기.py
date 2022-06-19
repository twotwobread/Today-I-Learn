# < 정렬된 배열에서 특정 수의 개수 구하기 >
# 문제 유형 : 이분 탐색 -> 변형
# 자료 구조 : 튜플 - 수열 저장
#           변수 - 밑 index, 위 index
# [ 아이디어 ]
# - 내가 원하는 값과 같거나 큰 값들을 끝까지 밀어보기
# - 내가 원하는 값과 같거나 작은 값들을 끝까지 밀어보기
# - 인덱스 구해서 빼기

def upper_binarySearch(start, end, goal):
    while start < end:
        middle = (start + end + 1)//2
        if sequence[middle] > goal:
            end = middle - 1
        else:
            start = middle
    return start
def lower_binarySearch(start, end, goal):
    while start < end:
        middle = (start + end)//2
        if sequence[middle] < goal:
            start = middle + 1
        else:
            end = middle
    return end

def solution():
    u_index = upper_binarySearch(0, len(sequence)-1, x)
    l_index = lower_binarySearch(0, len(sequence)-1, x)
    if u_index == l_index:
        if sequence[u_index] != x:
            return -1
    return u_index - l_index + 1
if __name__ == "__main__":
    N, x = map(int, input().split())
    sequence = tuple(map(int, input().split()))
    result = solution()
    if result > 0:
        print(result)
    else:
        print(-1)
