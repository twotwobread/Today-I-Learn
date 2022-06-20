def solution():
    for i in range(n):
        dp[i*m] = gold[i*m]
    for i in range(1, m):
        for j in range(n):
            row, col = j, i - 1
            dp[j*m + i] = max(dp[j*m + i], dp[row*m + col] + gold[j*m + i])
            u_row = row - 1
            if u_row >= 0:
                dp[j*m + i] = max(dp[j*m + i], dp[u_row * m + col] + gold[j*m + i])
            l_row = row + 1
            if l_row < n:
                dp[j*m + i] = max(dp[j*m + i], dp[l_row * m + col] + gold[j*m + i])
    print(max([dp[m*i - 1] for i in range(1, n+1)]))

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        n, m = map(int, input().split())
        gold = list(map(int, input().split()))
        dp = [0]*(n*m)
        solution()
