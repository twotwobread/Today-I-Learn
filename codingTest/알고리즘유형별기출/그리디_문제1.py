# file name : 그리디_문제1.py
# 모험가 N명 대상으로 공포도를 측정 공포도가 높은 모험가는 쉽게 공포를 느껴 대처 능력이 떨어짐. 
# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있음.
# 최대 몇 개의 모험가 그룹을 만들 수 있는지 궁금하다.
# N명의 모험가 정보가 주어졌을때, 여행을 떠날 수 있는 그룹 수의 최댓값을 구하는 프로그램 작성
# 1 <= N <= 100,000
# 둘째 줄에 공포도의 값을 N이하의 자연수, 공백으로 구분.
# author : Lee Suyoung(2022-02-17)

# 최대한 많은 그룹을 만들기 위해서는 공포도가 적은 놈들이 계속 뭉쳐야 한다.
# 만약 1이면 그냥 무조건 세아리고 아니면 count를 이용하면서 공포도 제일 높은 사람 하면될듯 
# 정렬을 해서 풀면 될듯

# n 입력
n = int(input())
# 공포도 정보 입력
fear = list(map(int, input().split()))
fear.sort()

cnt = 1
result = 0
temp = 0
for f in fear:
	if temp < f:
		temp = f	
	if cnt == temp:
		result += 1
		cnt = 1
	else:
		cnt+=1
print(result)

### [ 제시된 답안 ] ###
# 공포도를 오름차순으로 정렬을 하고 현재 그룹에 포함된 모험가의 수가 현재 확인하고 잇는 공포도보다 크거나 같다면 그룹으로 설정
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
    count += 1
    if count >=i:
        result += 1
        count = 0
print(result)
