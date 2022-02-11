# file name : 문제37.py
# 플루이드
# n개의 도시가 있고 한 도시에서 출발하여 다른 도시에 도착하는 m개의 버스가 있다.
# 각 버스는 한 번 사용할 때 필요한 비용이 있다. 모든 도시의 쌍(A, B)에 대해서 도시 A에서 B로 가는 데 필요한 비용의 최솟값을 구하여라.
# 1 <= n <= 100, 도시의 개수
# 1 <= m <= 100,000, 버스의 개수
# 셋째 줄부터 m개의 버스의 정보가 주어짐. 출발 도시, 도착 도시, 필요한 비용 / 비용은 100,000보다 작거나 같은 자연수.
# 풀이 시간 : 40분, 시간 제한 : 1초, 메모리 제한 : 256MB
#  author : Lee Suyoung(2022-02-11)

# 그냥 무조건 플루이드 모든 노드에서 노드로의 비용을 구하는 것도 그렇고
# 노드도 적다. 
import sys
input = sys.stdin.readline
# 일단 sys를 쓰니까 원래 5초 가까이 나오던게 893ms로 줄었다.
# 쓸 수 있으면 무조건 sys써야할 것 같다.
INF = int(1e9)
# n 입력, 도시의 개수
n = int(input())
# m 입력, 버스의 개수
m = int(input())
# m개의 버스의 정보 입력하면서 정보 저장.
distance = [[int(INF)] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    distance[a][b] = min(distance[a][b], c)
# 모든 노드에서 노드로의 최소 거리 구하기
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a==b:
                continue
            distance[a][b] = min(distance[a][b], distance[a][k]+distance[k][b])

# 이러니까 시간 초과 나오네
for i in range(1, n+1):
    for j in range(1, n+1):
        if distance[i][j] == int(INF):
            distance[i][j] = 0
for i in range(1, n+1):
    print(*distance[i][1:]) # 언패킹 이용해서 출력시간 줄이기 근데 못가는 경우를 0으로 출력을 해야해서 그냥 저렇게 출력해야할것같다.

# 지금 위에 처럼 0으로 넣고 나서 언패킹을 출력하는게 ie9를 만나면 0으로 출력하는 경우보다 76ms 가량 더 빨랐다.
# 이 부분도 알아두자.

# 지금 못가는 경우를 INF로 출력을 해서 틀린것 같음.
