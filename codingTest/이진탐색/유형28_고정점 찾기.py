# 문제 유형 : 이분 탐색 -> 변형
# 자료 구조 : 튜플 - 수열 저장
# [ 아이디어 ]
# - 해당 인덱스에 들어있는 값이 실제 인덱스보다 작다면 더 커져야함, 오름차순 이기 때문에
# - 반대로 실제 인덱스보다 값이 더 크다면 작아져야함.

def solution(start, end):
    while start <= end:
        middle = (start + end)//2
        if sequence[middle] == middle:
            return print(middle)
        elif sequence[middle] < middle:
            start = middle + 1
        else:
            end = middle - 1
    print(-1)

if __name__ == "__main__":
    n = int(input())
    sequence = tuple(map(int, input().split()))
    solution(0, len(sequence) - 1)
