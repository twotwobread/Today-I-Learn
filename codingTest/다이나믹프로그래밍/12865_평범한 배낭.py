# 문제 유형 : DP
# 아이디어
# - 먼저 무게 낮은 순 -> 같은 경우 가치 높은 순으로 정렬해서 가치가 가장 높은 애들로만 하나의 리스트 구성.
#    -> 이렇게 했는데 틀렸음. 그래서 무게 낮은 순으로 정렬 후 골라내지 않고 바로 진행.
# - 이걸 이용해서 낮은 무게 순으로 올라오면서 내 이전에 내 무게를 뺀 무게에다가 내 무게를 더한 무게와 해당 무게에서 이전 요소에서의 무게중 더 가치가 높은거 선택
# - 이렇게 할 경우 k라는 가치를 무조건 넘지 않음.

def solution():
    result = [[0]*(k+1) for _ in range(n)]
    for i in range(n):
        weight, value = things[i]
        for w in range(k+1):
            if w - weight >= 0:
                result[i][w] = max(result[i-1][w - weight]+value,result[i-1][w])
            else:
                result[i][w] = result[i-1][w]
    #print(result)
    print(result[n-1][k])

if __name__ == "__main__":
    n, k = map(int, input().split())
    things = [list(map(int,input().split())) for _ in range(n)]
    things.sort()
    solution()

    
# N개의 물건 -> 각 물건 무게 W, 가치 V
# 최대 K만큼의 무게
# 이때 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 구하자.
# N개의 물건은 각각 무게 W, 가치 V를 가지는데 용량이 K인 배낭에 물건을 넣을때 넣을 수 있는 가치 중 최댓값은?
# 모든 경우의 수를 구하는 방법이 있겠지만 여기서 주어진 물품의 수의 최대는 100이고 배낭의 용량의 최대는 100,000이다.
# 그렇다면 최악의 경우는 100개의 물품에서 발생하는 K를 만드는 모든 경우의 수이다. 적어도 O(100 * 100,000)을 넘을 것인데 해결 할 수 없다.
# 특정 조건을 채우는 물건의 경우의 수 중 물건이 가진 가치가 가장 높은 경우를 찾기 위해선 모든 요소를 다 비교할 수 없고 더 빨라야 한다면
# 이전의 연산을 다음 연산들에 활용하여 중복되는 연산의 수를 줄이는 방식인 DP를 이용해보자.
# DP는 탑다운 방식과 바텀업 방식이 있는데 더 편한 바텀업 방식을 이용할 것이다.
# 먼저 바텀업 방식에선 작은 연산에서 큰 연산으로 커져나간다. 그렇게 하기 위해선 seed값이 있어야 문제들이 풀릴 수 있을 것 같다.
# 정말 작은 연산에 대해서 생각을 해보자.
# 작은 연산은 K = 0인 경우 -> 최댓값은 0일 것이다.
# 그리고 물건의 요소가 아예없다면?? 최댓값은 0일 것이다.
# 그래서 K와 물건의 요소를 이용할 생각이다.

def solution():
    for i in range(1, N+1):
        weight, value = things[i-1]
        for j in range(1, K+1):
            if j - weight >= 0: dp[i][j] = max(dp[i-1][j-weight]+value, dp[i][j-1], dp[i-1][j])
            else: dp[i][j] = dp[i-1][j]
    return dp[N][K]
if __name__ == "__main__":
    N, K = map(int, input().split())
    things = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0]*(K+1) for _ in range(N+1)]
    print(solution())
