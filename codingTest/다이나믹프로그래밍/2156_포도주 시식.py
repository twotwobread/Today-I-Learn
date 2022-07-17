# 잔 선택 -> 다마시고 원래 위치
# 연속으로 놓인 3잔 모두 마시기 불가
# 가능한 많은 양의 포도주 맛보기 -> 최적화
# 1 - n, 각 포도주 잔의 양 주어짐.
# n 최대값 = 10,000

# dp 테이블의 크기 = n + 1, 초기화 -> 총량을 구하기 때문에 0으로 초기화
# 작은 경우 생각, 잔의 개수가 1잔이면? 전부 다 마셔야함 / 잔의 개수가 2잔이면? 이것도 전부 다 마셔야함
# 잔의 개수가 3잔이면? 첫번쨰와 세번째 잔을 마시거나 첫번째, 두번쨰 잔을 마시거나 두번쨰 세번쨰 잔을 마셔야한다.

def solution():
    dp[1] = grape[1]
    if n == 1:
        return dp[1]
    dp[2] = dp[1] + grape[2]
    for i in range(3, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + grape[i], dp[i - 3] + grape[i - 1] + grape[i])
    return dp[n]
if __name__ == "__main__":
    n = int(input())
    grape = [int(input()) for _ in range(n)]
    grape = [0]+grape
    dp = [0] * (n + 1)
    print(solution())
