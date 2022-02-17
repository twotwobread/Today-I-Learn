# file name : 다이나믹_문제31.py
# 금광
# n x m 크기의 금광이 있다. 금광은 1 x 1 크기로 나누어져 있으며 각 칸은 특정한 크기의 금이 들어 있다.
# 채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작한다. 처음에는 첫번째 열의 어느 행이든 출발할 수 있다.
# 이후엔 m번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽아래 3가지 중 하나의 위치로 이동해야한다. 결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성
# 1 <= T <= 1000, 테스트 케이스
# 매 테스트 케이스 첫째 줄에 n과 m이 공백으로 구분되어 입력, 1 <= n, m <= 20
# 둘째 줄에 N x M 위치에 매장된 금의 개수가 공백으로 구분 입력 ( 1<= 각 위치에 매장된 금의 개수 <= 100)
# author : Lee Suyoung(2022-02-17)

# 이거 딱 세개의 경우뿐이잖아 각 행에서 오른쪽 다음 행으로 갈 수 있네

# T 입력
T = int(input())
for t in range(T):
    # n, m 입력
    n, m = map(int, input().split())
    # 금에 대한 정보
    data = list(map(int, input().split()))
    gold = [[0]*m for i in range(n)]
    index = 0
    for i in range(n):
        for j in range(m):
            gold[i][j] = data[index]
            index += 1

    graph = [[0]*m for i in range(n)]
    for col in range(m):
        for row in range(n):
            if col != 0:
                if row == 0:
                    graph[row][col] = max(graph[row][col], graph[row][col-1]+gold[row][col], graph[row+1][col-1]+gold[row][col])
                elif row == n-1:
                    graph[row][col] = max(graph[row][col], graph[row][col-1]+gold[row][col], graph[row-1][col-1]+gold[row][col])
                else:
                    graph[row][col] = max(graph[row][col], graph[row][col-1]+gold[row][col], graph[row+1][col-1]+gold[row][col], graph[row-1][col-1]+gold[row][col])
            else:
                graph[row][col] = gold[row][col]
    print(max(max(graph, key=lambda x:x[-1])))

### [ 제시된 답안 ] ###
# dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])

#테스트 케이스 입력
for tc in range(int(input())):
    # 금광 정보 입력
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index += m
    
    for j in range(1, m): # 첫번째 열의 값을 살리기 위해서
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            # 왼쪽 아래에서 오는 경우
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            # 왼쪽에서 오는 경우
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

result = 0
for i in range(n):
    result = max(result, dp[i][m-1])
print(result)
