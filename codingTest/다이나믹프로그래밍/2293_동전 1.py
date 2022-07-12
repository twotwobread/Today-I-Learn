# 아이디어
# - 1 1 1 1 2 2 부터 시작하게 그니까 백트래킹 해서 나오면 같은 수를 넘겨서 그 숫자부터 가능해지게 만들면 될것 같음.
# - 근데 이게 무조건 시간초과가 날꺼야
# - 최대 10,000까지라서 1 들어가면 10,000 depth까지 들어갈텐데 그러면 끝임.
# - 그러면 DP를 생각해보자.

if __name__ == "__main__":
    n, k = map(int, input().split())
    coin = [int(input()) for _ in range(n)]

    dp = [0]*(k+1)
    dp[0] = 1
    for c in coin:
        for num in range(k+1):
            if c <= num:
                dp[num] += dp[num-c]
    print(dp[k])

