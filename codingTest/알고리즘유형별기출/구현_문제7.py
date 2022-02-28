# file name : 구현_문제7.py
# 럭키 스트레이트
# 현재 캐릭터의 점수를 N이라 할 때 자릿수를 기준으로 점수 N을 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 자릿수의 합을
# 더한 값이 동일한 상황을 의미
# 128,420 -> 11 != 6 , 자릿수는 항상 짝수 형태로만 주어짐.
# 10<= N <= 99,999,999
# 풀이 시간 : 20분, 시간 제한 : 1초, 메모리 제한 : 256MB
# author : Lee Suyoung (2022-02-28)

# n 입력
n = input()
# 반나눠서 왼쪽 오른쪽 더하기
leftSum = 0
rightSum = 0
for i in range(len(n)):
    if i >= (len(n)//2):
        rightSum += int(n[i])
    else:
        leftSum += int(n[i])

if leftSum == rightSum:
    print("LUCKY")
else:
    print("READY")
