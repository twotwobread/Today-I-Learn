# x가 3으로 나누어 떨어지면 3으로 나누기
# x가 2로 나누어 떨어지면 2로 나누기
# 1을 빼기
# N의 최대값이 10^6 = 1,000,000 이고 시간제한이 0.7초라서 DP를 이용하자.

# 먼저 생각해야할 것이 dp 테이블의 크기 결정, 생성, 초기화이다.
# 크기는 N+1만큼 할당 후 초기화를 -1로 두고 시드값 1을 0으로 삽입.

if __name__ == "__main__":
    x = int(input())
    dp = [-1]*(x+1)
    dp[1] = 0
    for i in range(1, x+1):
        if dp[i] != -1:
            if i + 1 <= x: dp[i + 1] = dp[i] + 1 if dp[i + 1] == -1 else min(dp[i+1], dp[i]+1)
            if i * 2 <= x: dp[i * 2] = dp[i] + 1 if dp[i * 2] == -1 else min(dp[i*2], dp[i]+1)
            if i * 3 <= x: dp[i * 3] = dp[i] + 1 if dp[i * 3] == -1 else min(dp[i*3], dp[i]+1)
    print(dp[x])
