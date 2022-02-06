# file name : 이코테_실전10_4.py
# 도시 분할 계획
# 마을은 N개 집, M개 길, 길은 어느 방향으로도 갈 수 있음. 길마다 유지비가 있음.
# 마을의 이장은 2개의 분리된 마을로 분할할 계획을 세우고 있음
# 마을을 분할할 땐 각 분리된 마을 안에 집들이 서로 연결되도록 분할해야함.
# 각 분리된 마을 안에 있는 임의의 두 집 사이에 경로가 항상 존재해야 함. 마을에는 집이 하나 이상 있어야함.
# 분리된 두 마을 사이 길들은 없앰. 유지비의 합을 최소로 하고 싶음.
# 2 <= N <= 100,000, 1 <= M <= 1,000,000
# a, b, c / a번 집과 b번 집을 연결하는 유지비가 c ( 1 <= c <= 1,000 )
# author : Lee Suyoung (2022-02-06)

# 일단 확실한 것은 최소 신장 트리를 짜야하는 것인데
# 그걸 분리 시켜야 하니까 2개를 만들어야 한다는 말이다.
# 이렇게 하자 하나의 최소 신장 트리를 만들면 어짜피 전부 다 연결되어 있다. 근데 하나 이상이니까
# 그상태에서 가장 값이 높은 길 하나를 없애면 되잖아. 이렇게 한번 짜보자.

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n+1)

edges = []
result = 0

for i in range(1, n+1):
    parent[i] = i

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

last = -1
for e in edges:
    cost, a, b = e
    if find_parent(parent, a) == find_parent(parent, b):
        continue
    else:
        union_parent(parent, a, b)
        result+=cost
        if last < cost:
            last = cost

print(result - cost)

# 제안된 답안과 같음.
# 제시된 아이디어와 나의 아이디어도 같음.
