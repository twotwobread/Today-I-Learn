# file name : 3120_리모컨.py
# author : Lee Suyoung(2022-04-05)
# 1) 온도를 1도 올리는 버튼
# 2) 온도를 1도 내리는 버튼
# 3) 온도를 5도 올리는 버튼
# 4) 온도를 5도 내리는 버튼
# 5) 온도를 10도 올리는 버튼
# 6) 온도를 10도 내리는 버튼
#
# 현재 온도 a 와 목표 온도 b가 입력 ( 0<=a,b<=40 )
#
# 최소한의 버튼 사용으로 목표온도가 되는 버튼의 횟수 출력
# 시간 제한 : 1sec, 메모리 제한 : 128MB

# 문제의 크기는 온도
# p[i] = min(p[i-1], p[i+1], p[i-5], p[i+5], p[i-10], p[i+10]) + 1
BUTTON = [1, -1, 5, -5, 10, -10] # 온도를 위한 마더 퍼커

def solution(a, b):
    if a > b:
        a, b = b, a
    temper = [int(1e9) for i in range(51)]
    temper[a] = 0
    for i in range(a, 51):
        for j in range(len(BUTTON)):
            if 0<=i+BUTTON[j]<=50:
                temper[i+BUTTON[j]] = min(temper[i+BUTTON[j]], temper[i] + 1)
                if BUTTON[j] == -1:
                    for a in range(2, 5):
                        if 0<=i+(BUTTON[j]*a)<=40:
                            temper[i+(BUTTON[j]*a)] = min(temper[i+(BUTTON[j]*a)], temper[i]+a)
    return temper[b]

if __name__ == "__main__":
    # a, b 입력
    a,b = map(int, input().split(" "))
    print(solution(a,b))
