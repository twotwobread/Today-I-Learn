# file name : 재귀문제1.py
# 10872번 팩토리얼
# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
# 0 <= N <= 12


facValue = [-1] * 13

def factorial(n):
    if facValue[n] != -1:
        return facValue[n]
    facValue[n] = n * factorial(n-1)
    return facValue[n]



facValue[0] = 1
facValue[1] = 1
n = int(input())

print(factorial(n))
