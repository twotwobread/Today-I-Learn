# 문제 유형 : DP
# <아이디어>
# - 지금 이전의 값 중 가장 작은 값과 현재 값을 빼면 된다.
# - 그러기 위해서 profit 값을 변수에 저장하고 max를 이용
# - 현재 인덱스 값과 이전 인덱스 값 중 작은 것을 현재 인덱스 값에 삽입 min이용.
# 자료구조 : 변수 - profit 값 저장
#           1차원 배열 - prices 값 저장
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(1, len(prices)):
            result = max(result, prices[i]-prices[i-1])
            prices[i] = min(prices[i], prices[i-1])
        return result
