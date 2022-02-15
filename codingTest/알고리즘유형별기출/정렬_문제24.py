# file name : 정렬_문제24.py
# 안테나
# 효율성을 위해 안테나로부터 모든 집까지의 거리의 총합이 최소가 되도록 설치
# 안테나는 집이 위치한 곳에만 설치할 수 있고, 논리적으로 동일한 위치에 여러 개의 집이 존재하는 것이 가능
# 집들의 위치 값이 주어질 떄, 안테나를 설치할 위치를 선택하는 프로그램 작성
# 1 <= N <= 200,000 , 집의 수
# 1 <= 집의 위치 <= 100,000
# 풀이 시간 20분, 시간 제한 1초, 메모리 제한 256MB
# author : Lee Suyoung(2022-02-14)

# 일일이 하나하나 찾으면 무조건 시간 오바될꺼 같고 시간이 뭘 어떻게 해도 부족하다.
# 무조건 최소 값이 나오는 곳은 정중앙에서 나온다.
# 그럼 홀수일때는 정중앙이고 짝수일때는 중간 두개중에 더 작은 거를 생각하면 된다.

INF = int(1e9)
# n 입력
n = int(input())
# n개의 집의 위치 정보
home = list(map(int, input().split()))
home.sort()
# 그냥 중간 인덱스의 값을 출력하자.
print(home[(len(home)-1)//2])

