# file name : 재귀_문제4.py
# 11729번 하나이 탑 이동 순서
# 1 <= n <= 20
# author : Lee Suyoung (2022-02-12)

def hanoi(n, start, end, temp, sum):
    if n == 1:
        return [(start, end)], sum
    left, l_sum=hanoi(n-1, start, temp, end, sum+1) 
    mid = [(start, end)] # 
    right, r_sum=hanoi(n-1, temp, end, start, l_sum+1)# 처음 들어오는 값이 0이 아니라 1이라서 l_sum에서 -1하고 mid값을 +1을 하면 l_sum 그대로기 때문에 +1로 그대로 넣는다.
    return left+mid+right, r_sum


# n 입력 ( 첫번째 장대에 쌓인 판의 개수)
n = int(input())

result, sum=hanoi(n, 1,3,2,1)
print(sum)
for i in result:
    print(str(i[0])+" "+str(i[1]))

