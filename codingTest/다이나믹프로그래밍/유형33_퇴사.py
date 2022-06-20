# 문제 유형 : 최장 증가 수열 (LCS)
# 자료 구조 : 1차원 리스트 - 수열을 담기 위함.
# [ 아이디어 ]
# - 병사가 있는 자리마다 LCS의 길이를 계속 구해서 마지막까지 처리.

def binarySearch(array, start, end, goal):
    while start < end:
        mid = (start + end)//2
        if array[mid] > goal:
            start = mid + 1
        else:
            end = mid
    return end

def solution():
    dp = [sequence[0]]
    for i in range(1, n):
        if dp[-1] > sequence[i]:
            dp.append(sequence[i])
        else:
            index = binarySearch(dp, 0, len(dp) - 1, sequence[i])
            dp[index] = sequence[i]
    print(n - len(dp))
    print(dp)
    # for i in range(n):
    #     dp[i] = 1
    #     for j in range(i):
    #         if sequence[i] < sequence[j]:
    #             dp[i] = max(dp[i], dp[j] + 1)
    # print(n - max(dp))

if __name__ =="__main__":
    n = int(input())
    sequence = tuple(map(int, input().split()))
    dp = [0]*len(sequence)
    solution()
