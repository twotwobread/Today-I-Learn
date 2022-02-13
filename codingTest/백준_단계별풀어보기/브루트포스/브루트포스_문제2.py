# file name : 브루트포스_문제2.py
# 어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미
# 어 떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. 예를 들어 245의 분해합은 256(=245+2+4+5)이다.
# 245는 256의 분해합이 된다. 몰론 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.
# 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 출력해라
# 1 <= N <= 1,000,000
# 생성자가 없는 경우 0을 출력한다.
# author : Lee Suyoung (2022-02-13)

# n 입력 
n = int(input())

# start = max(0, n-len(str(n)*9)) # 범위를 구함 생성자가 될 수 있는 최소 범위
# end = max(0, n-len(str(n))) # 최대 범위 

# def findConstructor(num):
#     for i in range(1, num):
#         new = i
#         sum = 0
#         for j in range(len(str(i))):
#             sum+=new%10
#             new //= 10
#         if num == (i+sum):
#             return i
#     return 0
def findConstructor(num):
    for i in range(1, num):
        if sum(map(int, str(i)))+i == num:
            return i
    return 0

result = findConstructor(n)
print(result)
        
