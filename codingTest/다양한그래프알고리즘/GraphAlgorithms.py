# 기본적인 서로소 집합 알고리즘 소스 코드
from itertools import cycle
import sys
input = sys.stdin.readline
INF = int(1e9)

def find_parent(parent, x):
    #루트가 아니라면 재귀적으로 호출해서 부모 찾기
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수와 간선의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v+1) # 부모 테이블 초기화

# 부모 테이블에서 부모 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

#union 연산을 각각 수행
for i in range(e):
    a,b = map(int, input().split())
    union_parent(parent, a, b)

#각 원소가 속한 집합 출력
print("각 원소가 속한 집합: ", end=" ")
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print("부모 테이블 : ", end=" ")
for i in range(1, v+1):
    print(parent[i], end=" ")


# 이렇게 구현하면 find 함수가 비효율적으로 동작한다. 최악의 경우 모든 노드를 다 확인하는 터라 시간 복잡도가 O(V)이다.
# 1,2,3,4,5 가 모두 같은 집합인 상황에서 union 연산이 순서대로 (4,5), (3,4), (2,3), (1,2)로 주어졌다고 가정하자.
# 그럼 일렬로 나열하는 형태가 된다 1 <- 2 <- 3 <- 4 <- 5
# 이러면 모든 노드의 루트는 1이 되지만 부모는 1 1 2 3 4와 같이 나온다.
# 이런 경우 O(V)의 시간이 소요된다. 그럼 V개의 노드에 M개의 union or find 연산이 있다면 O(VM)의 시간 복잡도를 가진다.
# 하지만 find 함수는 간단하게 최적화를 시킬 수 있다.
# 바로 경로 압축 기법을 적용하면 시간 복잡도를 개선시킬 수 있다. 경로 압축은 find 함수를 재귀적으로 호출한 뒤에 부모 테이블값을 갱신시키는 기법이다.
# find 함수 경로 압축으로 개선한 소스코드
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
# 근데 이렇게 되면 직접적인 부모는 모르는 거 아닌가??

# 서로소 집합은 다양한 알고리즘에 사용될 수 있다. 특히 서로소 집합은 무방향 그래프내에서의 사이클을 판별할 때 사용할 수 있다는 특징이 있다.
# 참고로 방향 그래프에서의 사이클 여부는 DFS를 이용하여 판별할 수 있다.
# 앞서 union 연산은 그래프에서의 간선으로 표현될 수 있다고 했다. 따라서 간선을 하나씩 확인하면서 두 노드가 포함되어 있는 집합을 합치는 과정을 반복하는
# 것만으로도 사이클을 판별할 수 있다.
# 알고리즘은 다음과 같다.
# 1. 각 간선을 확인하면서 두 노드의 루트 노드를 확인한다.
#   i. 루트 노드가 서로 다르다면 두 노드에 대하여 union 연산을 수행한다.
#   ii. 루트 노드가 서로 같다면 사이클이 발생한 것이다.
# 2. 그래프에 포함되어 있는 모든 간선에 대하여 1번 과정을 반복한다.


# 서로소 집합을 활용한 사이클 판별 소스코드
# 무방향 그래프에서만 적용 가능하다.
# 그래프에 포함되어 있는 간선의 개수가 E개일 때, 모든 간선을 하나씩 확인하며, 매 간선에 대하여 union 및 find 함수를 호출하는 방식으로 동작한다.

import sys
input = sys.stdin.readline
INF = int(1e9)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

# v, e 입력
v, e = map(int, input().split())
parent = [0] * (v+1)

#parent 초기화
for i in range(v+1):
    parent[i] = i

cycle = False
for _ in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클이 발생하였습니다!!")
else:
    print("사이클이 발생하지 않았습니다.")


# 크루스칼 알고리즘 소스코드
# 최소 신장 트리를 만드는데 필요한 비용을 계산하는 크루스칼 알고리즘의 소스코드는 다음과 같다.

import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, x)
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

for _ in range(v+1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a,b,c = map(int, input().split())
    edges.append((a,b,c))

edges.sort()

for i in edges:
    if find_parent(parent, i[1]) == find_parent(parent, i[2]):
        continue
    union_parent(parent, i[1], i[2])
    result+=i[0]

print(result)

# 시간 복잡도 : O(ElogE)의 시간 복잡도를 가진다.
# 왜냐하면 크루스칼 알고리즘에서 시간이 가장 오래 걸리는 부분이 간선을 정렬하는 작업이며, E개의 데이터를 정렬했을 때의 시간 복잡도는 O(ElogE)이기 때문이다.
# 크루스칼 내부에서 사용되는 서로소 집합 알고리즘의 시간 복접도는 정렬 알고리즘의 시간 복잡도보다 작으므로 무시한다.


# 위상 정렬 소스코드

from collections import deque

# 노드의 개수와 간선의 개수를 입력받기
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)
#각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for _ in range(v+1)]

# 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # A에서 B로 이동 가능
    # 진입차수를 1 증가
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque()

    # 진입차수가 0인 놈들 큐에 넣기
    for i in range(1, v+1):
        if indegree[i]==0:
            q.append(i)
    
    #큐가 빌때까지 반복
    while q:
        now = q.popleft()
        result.append(now)
        for next in graph[now]:
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)
    
    for i in result:
        print(i, end= " ")


topology_sort()

# 시간 복잡도는 O(V+E)이다. 차례대로 모든 노드를 확인하면서, 해당 노드에서 출발하는 간선을 차례대로 제거해야 한다.
# 결과적으로 노드와 간선을 모두 확인한다는 측면에서 O(V+E)의 시간이 소요되는 것이다.
