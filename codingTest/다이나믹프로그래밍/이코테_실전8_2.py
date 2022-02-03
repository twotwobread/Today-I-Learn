# file name : 이코테_실전8_2.py
# 1로 만들기
# 1. X가 5로 나누어떨어지면, 5로 나눔
# 2. X가 3으로 나누어떨어지면, 3으로 나눔
# 3. X가 2로 나누어 떨어지면, 2로 나눔
# 4. X에서 1을 뺀다.
# 연산을 사용하는 최솟값을 출력
# 1 <= X <= 30,000
# author : Lee Suyoung(2022-02-03)
'''
일단 다이나믹을 써야하는 이유는 큰 문제를 작은 문제로 나눌 수 있다. 큰 문제에서도 작은 문제에서도 4개의 연산을 진행한다.
작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다. 역시 4개의 연산은 언제나 동일하다.

최솟값이기 때문에 기록을 하고 비교를 해야함.
재귀를 이용해보자.
'''
def minFind(num, cnt):
    # 근데 이게 다이나믹 프로그래밍을 이용한게 아닌 것 같은데,,,
    # 그리고 recurision depth 문제 때문에 재귀를 자제하자.
    if num == 1:
        return cnt
    cnt+=1
    cnt_array = []
    if(num%5==0):
        cnt_array.append(minFind(num/5, cnt))
    if(num%3==0):
        cnt_array.append(minFind(num/3, cnt))
    if(num%2==0):
        cnt_array.append(minFind(num/2, cnt))
    cnt_array.append(minFind(num-1, cnt))
    cnt = min(cnt_array)
    return cnt

# X값 입력받기
x = int(input())

# 재귀를 이용한 최소값 찾기.
count = minFind(x, 0)
# 최솟값 출력하기
print(count)

### [ 제시된 답안 ] ###
# 먼저 점화식으로 표현을 하면 
# Ai = min(Ai-1, Ai/2, Ai/3, Ai/5) + 1 // +1을 하는 이유는 횟수를 위해서 그렇다.
# 점화식을 이용하여 코드를 짜보자.
x = int(input())

d = [0] * 30001 # 계산된 결과를 저장하기 위한 DP 테이블

#바텀업을 이용하여 다이나믹 프로그래밍 진행
for i in range(2, x+1):
    d[i] = d[i-1] + 1 # -1을 하는 경우
    if i % 2 == 0: # 2로 나눠지는 경우
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0: # 3으로 나눠지는 경우
        d[i] = min(d[i], d[i//3]+1)
    if i % 5 == 0: # 5로 나눠지는 경우
        d[i] = min(d[i], d[i//5]+1)

print(d[x])
