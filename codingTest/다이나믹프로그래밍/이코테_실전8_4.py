# file name: 이코테_실전8_4.py
# 바닥 공사
# 가로 길이 : N, 세로 길이 : 2 인 직사각형 형태의 바닥
# 이 바닥을 1x2, 2x1, 2x2의 바닥의 덮개를 이용해 채우고자 한다.
# 모든 경우의 수를 구하시오
# ex ) 2 x 3 크기의 바닥을 채우는 경우의 수는 5가지 이다.
# 1 <= N <= 1000, 방법의 수를 796,796으로 나눈 나머지를 출력한다.
# author : Lee Suyoung (2022-02-03)

'''
경우의 수를 따져보면 1x2 두개를 꼽던가 2x2 꼽던가 2x1 두개 꼽던가 / 2x1 하나 꼽던가.
요렇게 있다.그럼 두개만 생각하면 될듯 / x가 2개 남았는지 하나 남았는지
'''

def tileNumberOfCases(num, count, max):
    if num > max:
        return count
    
    count1, count2 = 0, 0
    count1 = tileNumberOfCases(num+1, count*1, max)
    if num+1 <= max:
        count2 = tileNumberOfCases(num+2, count*2, max)
    return (count1 + count2) % 796796


# N의 길이 입력
n = int(input())

result = tileNumberOfCases(1, 1, n)
print(result)
# 이게 맞았는지 틀렸는지는 정확히 모르겠지만 이런 형식으로는 일단 테스트 케이스는 만족시킬 수 있는데
# 바텀업 형태가 너무 어렵다

### [ 제시된 답안 ] ###
# 나도 똑같이 생각했던건데 2x1이 들어가는 경우랑 2x2, 1x2가 들어가는 경우를 나눴음.
# i-1까지 길이가 덮개로 이미 채워져 있고 2x1의 덮개를 채우는 경우
# i-2까지 길이가 덮개로 이미 채워져 있고 2x2, 1x2의 덮개로 채우는 경우
# N-2 미만의 길이에 대해서는 고려할 필요가 없다. 왜냐면 사용할 수 있는 덮개의 형태가 최대 2x2라서 생각할 필요가 없다.
# 점화식 Ai = Ai-1 + Ai-2 x 2 가 된다.

n = int(input())

d = [0] * 1001

d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = (d[i-1] + d[i-2]*2) % 796796

print(d[n])
