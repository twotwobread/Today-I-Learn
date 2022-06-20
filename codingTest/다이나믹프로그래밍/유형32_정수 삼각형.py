def solution():
    dp[0][0] = triangle[0][0]
    for i in range(1, n): # row
        for j in range(i+1): # col
            if (j - 1) >= 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + triangle[i][j])
            if dp[i-1][j] > 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j] + triangle[i][j])
    print(max(dp[n-1]))


if __name__ == "__main__":
    n = int(input())
    triangle = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0]*n for _ in range(n)]
    solution()
