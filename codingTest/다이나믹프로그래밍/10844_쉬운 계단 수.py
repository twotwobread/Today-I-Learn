
if __name__ == "__main__":
    n = int(input())
    dp = [0]*10
    for i in range(1, 10):
        dp[i] = 1
    for i in range(2, n+1):
        new = [0]*10
        for j in range(10):
            if j-1>=0: new[j-1] += dp[j]
            if j+1<=9: new[j+1] += dp[j]
        dp = new.copy()
    print(sum(dp)%1000000000)
