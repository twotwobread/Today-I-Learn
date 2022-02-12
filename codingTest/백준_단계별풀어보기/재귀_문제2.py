# file name : 재귀_문제2.py
# 10870번 피보나치 수 5
# Fn = Fn-1 + Fn-2
# n이 주어진 경우, n번째 피보나치 수를 구하여라
# 0 <= n <= 20
# author : Lee Suyoung(2022-02-12)

array = [-1] * 21
def fibonachi(n):
    if n == 1 or n == 0:
        return array[n]
    if array[n] != -1:
        return array[n]
    array[n] = fibonachi(n-1) + fibonachi(n-2)
    return array[n]

array[0] = 0
array[1] = 1
n = int(input())

print(fibonachi(n))
