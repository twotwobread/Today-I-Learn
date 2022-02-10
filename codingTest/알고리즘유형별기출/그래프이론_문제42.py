# file name: 그래프이론_문제42.py
# 탑승구
# 공항에는 G개의 탑승구가 있음. 1 - G번까지의 번호로 구분
# P개의 비행기가 차례대로 도착할 예정이고 i번째 비행기를 1번부터 gi번째(1<=gi<=G) 탑승구 중 하나에 영구적으로 도킹해야함.
# 이때, 다른 비행기가 도킹하지 않은 탑승구에만 도킹할 수 있음
# 또한 P개의 비행기를 순서대로 도킹하다가 만약 어떤 탑승구에도 도킹할 수 없는 비행기가 나오는 경우, 그 시점에서 공항 운행 중지
# 공항의 관리자는 최대한 많은 비행기를 공항에 도킹하고자 함. 최대 몇 대 도킹할 수 있는지를 출력하시오
# 1 <= G <= 100,000, 탑승구 수
# 1 <= P <= 100,000, 비행기 수
# P개의 줄 - 1 <= gi <= G , 각 비행기가 도킹할 수 있는 탑승구의 정보.
# 이는 i번째 비행기가 1번부터 gi번째 탑승구 중 하나에 도킹할 수 있다는 의미.
# 풀이시간 : 50분, 시간제한 : 1초, 메모리 제한 128MB
# author : Lee Suyoung(2022-02-10)

# 해당 문제는 서로소 집합을 이용하여 풀 수 있음.
# 일단 탑승구 정보를 받을 때 4라는 값이 들어오면 1~4까지 도킹 가능한 탑승구이다.
# 그럼 가장 높은 번호의 탑승구를 먼저 들어가게 만든다. 모든 비행기에서  
# 그리고 탑승구에 들어가면 그보다 번호 하나 낮은 탑승구랑 union을 해주는 것이다.
# 맨 처음에는 항상 부모가 자기 자신이라서 말을 안적었는데 다음 노드부터는 꼭 필요한 부분이다.
# 젤 처음에 부모 노드가 뭔지를 확인한다. 부모노드가 만약 0이 된다면 이건 내가 도킹가능한 탑승구가 존재하지 않는것이다.
# 왼쪽으로 계속 union을 하면서 부모노드를 계속 옮겼다. 그게 이제 0에 union이 되면 그냥 아예 존재하지 않는 것이다 들어갈 곳이
# 와 지렸다.


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
# g 입력 , 탑승구의 개수
g = int(input())
# p 입력, 비행기 수
p = int(input())
parent = [0] * (g+1)

for i in range(g+1):
    parent[i] = i

# 비행기에서 도킹 가능한 탑승구 정보
entrance = []
for _ in range(p):
    entrance.append(int(input()))

result = 0
for e in entrance:
    parent_data = find_parent(parent, e)
    if parent_data != 0:
        result += 1
        union_parent(parent, parent_data, parent_data-1)
    else:
        break
print(result)
