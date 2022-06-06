# < 효율적인 화폐 구성 >
# 문제 유형 : DP
# 자료 구조 : 1차원 리스트 - DP 테이블
#           dict - 코인의 정보를 저장, 코인의 값이 비연속적이라 이런식으로 표현.
# [ 아이디어 ]
# - 현재 값에서 코인 값을 뺸 경우, 값이 존재하면 거기 값 + 1 해서 비교 때리기.

def solution():
    for i in range(1, m+1):
        for j in range(1, n+1):
            if (i-coin[j]) > 0 and dp[i-coin[j]] != 10001:
                dp[i] = min(dp[i], dp[i-coin[j]] + 1)
    if dp[m] == maxValue:
        print(-1)
    else:
        print(dp[m])

if __name__ == "__main__":
    n, m = map(int, input().split())
    maxValue = 10001
    dp = [maxValue] * maxValue
    coin = dict()
    for i in range(1, n+1):
        num = int(input())
        coin[i] = num
        dp[num] = 1
    solution()
