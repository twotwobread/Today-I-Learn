# target 숫자가 주어졌을때, candidates 안에 존재하는 숫자들을 더해서 target 숫자를 만들 수 있는 조합을 반환하라.
# 해당 문제에서 원하는 것은 candidates 요소들로 만들 수 있는 모든 경우들 중에서 순서를 고려하지 않고 더했을 때, target을 만들 수 있는 경우들을 반환하라는 것이다.
# 그렇다면 순서를 고려하지 않은 모든 경우의 수는 어떻게 구할 수 있을까? 조합, 백트래킹, dp 등을 이용하여 구할 수 있다.
# 조합은 candidates의 길이가 30이기때문에 O(2^30)의 복잡도를 가질 것이고 백트래킹은 가지치기에 따라 성능이 많이 달라지지만 최악을 생각한다면 조합과 비슷할 것 이다. 
# 그래서 dp를 이용해서 문제를 해결해볼 것이다. dp는 작은 부분문제들이 중복되는 것을 이용하여 시간을 줄여주는 알고리즘이다. dp에는 memorization을 이용하는 탑다운 방식과 tabulation을 이용하는 바텀업 방식이 존재한다. memorization 방식은 큰 문제부터 작은 문제로 가면서 연산의 결과를 저장하고 후에 중복되는 연산을 요구할 때 이를 이용하여 시간을 줄여주는 방식이고 tabulation은 작은 문제에서 큰 문제로 가면서 이전에 계산했던 문제의 결과를 후의 연산에서 사용하는 개념이다.
# 필자는 tabulation이 더 편하기 때문에 이를 이용하겠다. 그렇다면 작은 문제에서 큰 문제로 커져가야하는데 해당문제에서 작은 부분문제란 뭘까? 해당 문제에선 target과 candidates가 주어진다. 이 둘다 문제에 영향을 미칠 것이다. 예를 들어서, candidates의 길이가 0이라면 항상 반환값은 [] 빈 리스트일 것이다. 그렇다면 target의 크기가 0이라면? 이 또한 반환값이 항상 []일 것이다.
# 해당 값들을 seed값으로 넣을 생각을 하고 table을 초기화 해야하는데 table의 크기는 target의 크기로 할당하겠다. 원하는 값이 target이지 그 이상이 아니기 때문에 그 이상으로 갈 필요가 없다. 그리고 초기화는 [] 빈 리스트로 하겠다. 원하는 반환값이 []이기 때문이다.
# seed 값을 이용해서 target = 0일때 -> [[]] 로 할당을 해줄 것이다. 그 이유는 조합의 갯수가 여러개가 될 수 있기 때문이다.
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target+1)]
        dp[0].append([])
        
        for i in range(target+1):
            if len(dp[i]) != 0:
                for c in candidates:
                    if i + c <= target:
                        temp = []
                        for index in dp[i]:
                            if len(index) > 0:
                                if index[-1] <= c:
                                    temp.append(index.copy() + [c])
                            else:
                                temp.append(index.copy() + [c])
                        dp[i+c] = temp if len(dp[i+c]) == 0 else temp + dp[i+c]
        return dp[target]
