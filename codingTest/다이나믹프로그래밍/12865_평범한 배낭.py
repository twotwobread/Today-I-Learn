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
