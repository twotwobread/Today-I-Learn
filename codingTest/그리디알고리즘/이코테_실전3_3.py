# file name : 이코테_실전3_3.py
# 숫자 카드 게임은 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임이다.
# 롤은 다음과 같다
# 1. NxM 형태로 카드가 놓여 있음. 
# 2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택
# 3. 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 함.
# 4. 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 
# 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.
# 1<= N, M <=100 , 1<= 숫자 <= 10,000
# author: Lee Suyoung (2021-01-03)

# 100 x 100 행렬이라서 행 중에 가장 낮은 놈들을 뽑아서 그 중 가장 큰 놈을 뽑으면 된다.
# 지금은 최대 10,000번 행한다. 근데 행렬이 커지면 시간 초과

# n, m 입력 받는 부분
n, m = map(int, input().split())

#data 입력받으면서 행마다 가장 작은 값을 찾아 놓는 부분
min_data = []
for i in range(n):
    temp = list(map(int, input().split()))
    min_data.append(min(temp))

# 가장 낮은 놈들 사이에서 가장 큰 놈을 찾기 위해 정렬 사용
result = max(min_data)
# 결과값 출력
print(result)

###[ 제시된 예시 답안 ]###
# 다 같은데 나는 마지막에 max를 써서 필요없는 작업을 한번 더 한다.
# n, m 입력 받는 부분
n, m = map(int, input().split())

#data 입력받으면서 행마다 가장 작은 값을 찾아 놓는 부분
result = 0
for i in range(n):
    temp = list(map(int, input().split()))
    min_data = min(temp)
    result = max(result, min_data) # 둘 중 더 큰 걸 result로 넘긴다.
# 결과값 출력
print(result)
