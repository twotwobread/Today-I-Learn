# file name : 9251_LCS.py
# LCS(Longest COmmon Subsequence, 최장 공통 부분 수열)
# 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제.
# ex) ACAYKP and CAPCAK => ACAK
#
# 첫째, 둘쨰 줄 두 문자열, 알파벳 대문자로만 이루어지고 최대 1000글자.
#
# LSC의 길이 출력
#
# 시간 제한 : 1초 | 메모리 제한 : 256MB |
# author : Lee SUyoung (2022-03-14)

# 두 알파벳 입력
A = list(input())
B = list(input())

table = [[0]*(len(B)+1) for _ in range(len(A)+1)]
for a in range(len(A)):
    for b in range(len(B)):
        if A[a] == B[b]:
            table[a+1][b+1]=table[a][b]+1
        else:
            table[a+1][b+1]=max(table[a][b+1], table[a+1][b])

print(max(table[len(A)]))

# 아래는 길이뿐만 아니라 부분수열 찾는 부분

# result = []
# row = len(A)
# col = len(B)

# def dfs(table, row, col):
#     if row == 0 or col == 0:
#        print(result[::-1])
#        print(len(result))
#        return
#     if table[row][col] == table[row][col-1]:
#         dfs(table, row, col-1)
#     elif table[row][col] == table[row-1][col]:
#         dfs(table, row-1, col)
#     else:
#         result.append(B[col-1])
#         dfs(table, row-1, col-1)
#         result.pop()
# dfs(table, row, col)
