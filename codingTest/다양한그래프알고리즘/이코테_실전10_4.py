# file name : 이코테_실전10_4.py
# 커리큘럼
# 선수 강의를 들어야 다음 강의를 들을 수 있다.
# 총 N개의 강의를 듣고자 하고 모든 강의는 1 ~ N번까지의 번호를 가진다. 또한 동시에 여러 개의 강의를 들을 수 있다.
# 예를 들어 N = 3일때, 3번 강의의 선수 강의로 1번과 2번강의가 있고 1,2d의 선수는 없다고 가정, 강의 시간은 30,20,40시간으로 가정
# 이 경우 전부 다듣기 위한 최소시간은 1 : 30, 2: 20, 3 : 40 으로 70 시간이다.
# N개의 강의에 대하여 수강하기 까지 걸리는 최소 시간을 출력
# 1 <= n <= 500
# 각 강의의 시간과 그 강의를 듣기 위해 먼저 들어야 하는 강의들의 번호가 주어짐.
# 각 줄은 -1로 끝남.
# author : Lee Suyoung (2022-02-06)

# 먼저 처음에는 진입차수를 이용해서 위상정렬해서 출력을 하고 싶었는데
# 이게 들어오는 정보가 하나의 index를 가르치는 선수 과목들을 주니까 진입차수를 어떻게 써야할지 감이 잡히지 않음.
# 그래서 그냥 정보를 저렇게 주니까 재귀를 이용해서 타고 들어가면서 결과를 더해서 비교를 해야겠다고 생각.
# 주의를 해야하는게 500개라서 괜찮을 것이라 생각했는데 중요한게 라인마다 선수과목을 주는데 그 갯수가 문제임.
# 갯수가 한정되어 있지 않아서 큰일날 수 있음.
# 그리고 재귀를 써서 시간적 부담이 더 크기 때문에 시간초과가 날 수 있다 생각.

def CompareBeforeLectureTime(index, result): # 선수과목들의 걸리는 시간을 비교하기 위한 함수
    result += time[index]
    if graph[index][0] == 0:
        return result
    last = -1
    for i in graph[index]:
        sum = CompareBeforeLectureTime(i, result)
        if last < sum:
            last = sum
    return last

# 강의 개수 입력
n = int(input())
# 연결된 값들을 알기 위함. 
graph = [[] for i in range(n+1)]
# 강의 당 걸리는 시간을 알기위함.
time = [0] * (n+1)

for i in range(1, n+1):
    count = 0
    lecture = list(map(int, input().split()))
    time[i] = lecture.pop(0)
    for j in lecture:
        if j != -1:
            count+=1
            graph[i].append(j) # i라는 과목을 듣기위한 선수과목들을 담음.
        if count == 0 and j == -1:
            graph[i].append(0) # 선수과목이 없는 경우 쓰이지 않는 인덱스인 0을 넣음.

for i in range(1, n+1):
    result = CompareBeforeLectureTime(i, 0)
    print(result)
    

### [ 제시된 답안 ] ###
# 이 문제는 위상 정렬 알고리즘의 응용문제이다.
# 각 노드에 대하여 인접한 노드를 확인할 때, 인접한 노드에 대하여 현재보다 강의 시간이 더 긴 경우를 찾는다면, 더 오랜 시간이 걸리는 경우의 시간 값을
# 저장하는 방식으로 결과 테이블을 갱신하여 답을 구할 수 있다. 따라서 위상 정렬을 수행하면서, 매번 간선 정보를 확인하여 결과 테이블을 갱신한다.
# 소스코드에서는 최종적으로 각 강의를 수강하기까지의 최소 시간을 result 리스트 변수에 담도록 하였고 처음엔 각 강의 시간은 time 리스트 변수에 담겨 있는데,
# 위상 정렬 함수의 초기 부분에서 deepcopy() 함수를 이용하여 time 리스트 변수의 값을 복사하여 result 리스트 변수의 값으로 설정하는 작업이 수행된다.
# 리스트의 경우, 복제시 deepcopy() 함수를 사용해야한다.

from collections import deque
import copy

# 노드의 개수 입력받기
v = int(input())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v+1)]
# 각 강의 시간을 0으로 초기화
time = [0] * (v+1)

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1 # 현재 인덱스 과목의 선수과목들이라서 i 인덱스에 증가를 시킴.
        graph[x].append(i) # 선수과목들에 현재 인덱스가 연결되어서 이렇게 append를 한다.

# 위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스트
    q = deque()

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            # 여기서 그냥 제일 처음부터 쭉 돌리면서 선수과목 시간들을 다 더해주네
            # 그러면 선수에서 가장 높은 시간이 저장이 되겠네
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    for i in range(1, v+1):
        print(result[i])
    
topology_sort()

# 진짜 생각하는 방법이 너무 다르네
# 너무 편협한 시각을 가지고 있는 것 같다. 많은 문제를 접하면서 사고의 폭을 늘리는게 시급하다.
# 일단 지금 너무 max, min 이런 함수를 이용해서 점화식으로 푸는 방법에 익숙하지 못하다.
# 다이나믹 프로그래밍이 진짜 많이 부족한 것 같다. 문제를 많이 풀자.
