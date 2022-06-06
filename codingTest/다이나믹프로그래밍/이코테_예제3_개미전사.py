# < 개미 전사 >
# 문제 유형 : DP
# 자료 구조 : 1차원 리스트 - DP 테이블
# [ 아이디어 ]
# - 이런 유형의 DP를 풀때는 최대값을 끌고 간다는 생각이 필요하다고 생각.
# - 떨어져있는 애들을 다 더했을때 가장 큰 값을 찾아야하니까 떨어진 놈한테도 큰 값을 끌고 와야 비교할 수 있음.

def solution():
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + room[i])
    print(dp[n-1])

if __name__ == "__main__":
    n = int(input())
    room = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = room[0]
    dp[1] = max(room[0], room[1])
    solution()
