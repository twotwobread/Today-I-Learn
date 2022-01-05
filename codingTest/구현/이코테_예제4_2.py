# file name : 이코테_예제4_2.py
# n이 입력되면 N:59:59까지 3이 하나라도 포함된 모든 경우를 구하는 프로그램
# ex ) 1이 입력 -> 3이 하나라도 포함되어 있으므로 세어야하는 시각 : 00 00 03, 00 13 30
# 반면 세면 안되는 시각 : 00 02 55, 01 27 45
# 0<= N <= 23 
# author : 이수영 (2022-01-05)

# 제한이 2초가 주어졌는데 여기서 탐색의 최대 개수를 생각하면 24*60*60 아무리커도 이걸 넘을 수 없음
# 근데 86,400개이다. 그럼 완전 탐색을 써보자.

# n을 입력받는 부분
n=int(input())
h=0; m=0; s=0
cnt = 0
# 3이 있는 시간을 세는 부분
while (str(h)+str(m)+str(s)) != (str(n)+'59'+'59'):
    t=str(h)+str(m)+str(s)
    if str(3) in t:
        cnt += 1
    s += 1
    m += (s//60); s %= 60
    h += (m//60); m %= 60

# 출력 결과값
print(cnt)

### [ 제시된 예시 답안 ]###
n = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
