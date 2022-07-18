# dp 문제다
# 코인의 가장 작은 개수를 원하는 최적화 문제이다.
# 그렇다면 dp 테이블의 크기는 amount의 크기로 정할 것이고 초기화 되는 값은 못만들면 -1을 반환하라 하니 -1로 초기화하겠다.
# seed를 찾아보자. 가장 작은 경우는 뭘까? amount가 0인 경우라면 output = 0이 되면서 무조건 성립할 것이다. 만약 1인 경우는 1이 없다면 만들지 못한다.

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1]*(amount+1)
        dp[0] = 0
        for i in range(amount):
            if dp[i] != -1:
                for c in coins:
                    if i + c <= amount:
                        dp[i+c] = dp[i] + 1 if dp[i+c] == -1 else min(dp[i+c],dp[i]+1)
        return dp[amount]
