# file name : 이코테_실전6_2.py
# 내림차순 정렬
# 1<=N<=500
# author : Lee Suyoung 

# 일부러 라이브러리를 사용하지 않고 계수 정렬로 짰음.
# 익숙해지기 위해서.

# n 입력 받기
n = int(input())
# 수열 입력받기
data = []
for i in range(n):
    data.append(int(input()))

# 계수 정렬하기
count = [0]*(max(data)+1)

for i in data:
    count[i] += 1

for i in range(len(count)-1, -1, -1):
    for j in range(count[i]):
        print(i, end=" ")
