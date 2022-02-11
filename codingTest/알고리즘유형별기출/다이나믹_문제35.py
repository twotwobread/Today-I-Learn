# file name : 문제35.py
# 못생긴 수
# 못생긴 수란 오직 2, 3, 5만을 소인수로 가지는 수를 의미한다. 다시 말해 오직 2,3,5를 약수로 가지는 합성수를 의미합니다. 
# 1은 못생긴 수라고 가정합니다. 따라서 못생기 수들은 {1,2,3,4,5,6,8,9,10,12,15,,,,,} 순으로 이어짐.
# 이때 n번째 못생긴 수를 차즌ㄴ 프로그램을 작성하세요. 예를 들어 11번째 못생긴 수는 15입니다.
# 1 <= n <= 1,000
# author : Lee Suyoung(2022-02-11)


# 흐음. 어짜피 1000개라서 시간 제한은 크게 신경 안써도 될듯

n = int(input())

array = [False]*1001
array[1] = True
array[2] = True
array[3] = True
array[5] = True

def FindUglyNumber(n, array, now): # 먼저 못생긴 수를 다 찾아준다.
    if now > 1000:
        return
    array[now] = True
    FindUglyNumber(n, array, now*2)
    FindUglyNumber(n, array, now*3)
    FindUglyNumber(n, array, now*5)

FindUglyNumber(n, array, 1) #1부터 못생긴 수를 1000까지 찾는다.
cnt = 0
for i in range(1, 1001): # n번째 못생긴 수를 출력한다.
    if array[i] == True:
        cnt += 1
        if cnt == n:
            print(i)

# 다이나믹스럽게 만들어야 하는데 그게 좀 부족한것 같다.
