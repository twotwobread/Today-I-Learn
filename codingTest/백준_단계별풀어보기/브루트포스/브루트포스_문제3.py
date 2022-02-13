# file name : 브루트포스_문제3.py
# 덩치
# 키와 몸무게 둘다 큰 사람이 덩치가 큰것, 둘 중 하나라도 더 크지 않으면 안 큼
# 2 <= N <= 50
# 10<=x,y<=200
# author: Lee Suyoung (2022-02-13)

# n 입력 사람 수
n = int(input())
# 덩치 리스트 (몸무게, 키) 입력
size=[]
for i in range(n):
    length, kg = map(int, input().split())
    size.append((length, kg))
# for문을 이용해서 경우의수를 다 구하는데 순서 x, 반복 x
place = [1] * n
for i in range(n):
    i_length, i_kg = size[i]
    for j in range(n):
        j_length, j_kg = size[j]
        if i_length < j_length and i_kg < j_kg:
            place[i] += 1
print(*place)

 
