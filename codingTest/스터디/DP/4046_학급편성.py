# file name : 4046_학급편성.py
# author : Lee Suyoung(2022-04-10)
# 대학생이 3명이면 (1명 + 1명 + 1명), (2명 + 1명), (3명)으로 편성하는 세 가지 방법을 검토가능
# 수업의 품질을 고려하여 학급당 최대학생수를 통제하기로 함.
# 대상학생이 5명이고 학급당 최대 학생수가 3명이면, (1+1+1+1+1), (2+1+1+1), (2+2+1), (3+1+1), (3+2) 다섯 가지 방법이 도출
# 방법수를 123456789로 나눈 나머지를 출력하시오.
# N, M ( 1<=N<=1,300, 1<=M<=1,300 )
# 시간 제한 : 1초, 메모리 제한 : 128MB
COUNT = 0
SUM = 0
def memo(n, m, start):
    global COUNT, SUM
    for i in range(1, start+1):
        if SUM == n:
            COUNT += 1
            return
        if (n - SUM) - i >= 0:
            SUM += i
            memo(n, m, i)
            SUM -= i
        else:
            break
        
def solution(n, m):
    global SUM
    memo(n, m, m)
    return COUNT

if __name__ == "__main__":
    # n, m 입력
    n, m = map(int, input().split(" "))
    print((solution(n, m)%123456789))

# 시간 초과

# 이 dp에서 작은 걸로 큰 걸 풀 수 있는 경우를 생각하여 풀어봐야 할 
