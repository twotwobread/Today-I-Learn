# file name : 14888_연산자끼워넣기.py
# author : Lee Suyoung(2022-03-31)
# N개의 수로 이루어진 수열이 주어지고 N-1개의 연산자가 주어짐.
# 연산자는 +, -, *, / 로 이루어짐(나눗셈은 정수 나눗셈으로 몫만 취하는데 음수를 양수로 나눌 땐
# 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꿈.
#
# 첫째 줄, 수의 개수 N ( 2<=N<=11 )
# 둘째 줄, 수열의 정보 A ( 1<=Ai<=100 )
# 합이 N-1인 4개의 정수, 덧셈, 뺄셈, 곱셈, 나눗셈의 개수
#
# 첫째 줄에 만들 수 있는 식의 결과의 최댓값.
# 둘째 줄에는 최솟값을 출력력# 시간제한: 2초, 메모리 제한 : 512MB

MAX = -int(1e10 + 1)
MIN = int(1e10 + 1)
result = []
def dfs(n, A, operator, operatorChar):
    global MAX, MIN, result
    if len(result) == (n-1):
        sumValue = A[0]
        for r in range(len(result)):
            if result[r] == "+":
                sumValue += A[r + 1]
            elif result[r] == "-":
                sumValue -= A[r + 1]
            elif result[r] == "*":
                sumValue *= A[r + 1]
            else: # 나눗셈인 경우
                sumValue = (sumValue//A[r + 1]) if sumValue >=0 else -((-sumValue)//A[r + 1])
        
        if MAX < sumValue: MAX = sumValue
        if MIN > sumValue: MIN = sumValue
        return
    for i in range(len(operator)):
        if operator[i] == 0:
            continue
        result.append(operatorChar[i])
        operator[i] -= 1
        dfs(n, A, operator, operatorChar)
        result.pop()
        operator[i] += 1


def solution(n, A, operator):
    operatorChar = ["+", "-", "*", "/"]
    dfs(n, A, operator, operatorChar)
    return (MAX, MIN)

if __name__ == "__main__":
    # n 입력
    n = int(input())
    # 수열의 정보 입력
    A = list(map(int, input().split(" ")))
    # 연산자 개수의 정보 입력
    operator = list(map(int, input().split(" ")))
    mainResult = solution(n, A, operator)
    print(mainResult[0]) # 최댓값
    print(mainResult[1]) # 최솟값
