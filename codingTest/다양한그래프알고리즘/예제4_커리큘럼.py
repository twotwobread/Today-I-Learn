# 문제 유형 : 위상 정렬, 메모라이제이션
# 자료 구조 : 2차원 리스트 - 과목 별로 선수과목을 표시하기 위함.
#           1차원 배열 - 과목 별로 선수과목 갯수, 진입차수를 위함.
#           deque - 진입차수가 0인 과목을 이용.
# [ 아이디어 ]
# - 자기 시간 더하기 선수과목 중 가장 큰 시간을 소요하는 과목만 더하면 끝.

# 이 경우는 무조건 진입차수가 0인 정보부터 들어온다는 가정하에 가능.
# if __name__=="__main__":
#     n = int(input())
#     result = [0] * (n+1)
#     for i in range(1, n+1):
#         temp = list(map(int, input().split()))
#         time = temp[0]
#         result[i] = time
#         for t in temp[1:]:
#             if t == -1:
#                 break
#             result[i] = max(result[i], time + result[t])
#         print(result[i])

# 위상 정렬이용.
from collections import deque
def solution():
    q = deque()
    result = time.copy()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        node = q.popleft()
        for adj in graph[node]:
            indegree[adj] -= 1
            result[adj] = max(result[adj], result[node]+time[adj])
            if indegree[adj] == 0:
                q.append(adj)
    for i in range(1, n+1):
        print(result[i])

if __name__ == "__main__":
    n = int(input())
    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    time = [0] * (n+1)
    for i in range(1, n+1):
        temp = list(map(int, input().split()))
        time[i] = temp[0]
        for t in temp[1:-1]:
            graph[t].append(i)
            indegree[i] += 1
    solution()

