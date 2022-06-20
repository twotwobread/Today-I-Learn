# 문제 유형 : 백트래킹, DP
# 자료 구조 : 2차원 리스트 - 상담 일정표 저장
#           2차원 리스트 - DP 테이블
# [ 아이디어 ]
# - T + 일수 - 1의 날짜가 7을 안넘으면 내 날짜 이전꺼랑 더해서 비교
# - 맨 처음 날짜의 상담은 7을 넘는지 안넘는지만 비교

def solution():
    dp = [0]*(n+1)
    for i in range(1, n+1):
        t, p = consulting[i-1]
        if (t+i-1) <= n:
            dp[t+i-1] = max(dp[t+i-1], dp[i-1] + p)
        dp[i] = max(dp[i], dp[i-1])
    print(max(dp))



if __name__ == "__main__":
    n = int(input())
    consulting = [tuple(map(int, input().split())) for _ in range(n)]
    solution()
