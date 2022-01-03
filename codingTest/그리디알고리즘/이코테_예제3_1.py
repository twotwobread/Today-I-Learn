# file name : 이코테_예제3_1.py
# 당신은 음식점의 계산을 돕는 점원이다. 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정한다.
# 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 개수를 구하라. 단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.
# author : Lee Suyoung (2022-01-03)
# update

# 동전의 개수가 최소이기에 가장 큰 단위의 동전부터 거슬러주면서 작은 단위로 내려가자


unit = [500, 100, 50, 10]
print(260//500)
# N의 값을 입력받는 part
N = int(input())

# N을 가지고 큰 unit부터 거슬러주면서 나누어진 나머지를 이용하여 계속 진행 - 동전의 갯수를 세는 part
count = 0
while N!=0:
    if N//unit[0] > 0 :
        count += (N//unit[0])
        N %= unit[0]
        #print("500count : ", count)
    elif N//unit[1] > 0 :
        count += (N//unit[1])
        N %= unit[1]
        #print("100count : ", count)
    elif N//unit[2] > 0 :
        count += (N//unit[2])
        N %= unit[2]
        #print("50count : ", count) 
    elif N//unit[3] > 0 :
        count += (N//unit[3])
        N %= unit[3]
        #print("10count : ", count)
# // 나누어 떨어지는 연산자 잘 사용하기
# 동전의 개수를 output part
print(count)


# 애초에 갯수만 세면 되기 때문에 반복이 unit 만큼만 하면 된다.
n = int(input())
count = 0

for u in unit:
    count += (n//u)
    n %= u

print(count)
