# n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.#
#제한사항
# -주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
# -각 숫자는 1 이상 50 이하인 자연수입니다.
# -타겟 넘버는 1 이상 1000 이하인 자연수입니다.

def dfs(numbers, target, sum):
    if len(numbers)<=0:
        if sum==target:
            return 1
        else:
            return 0
    num = numbers[0]
    return dfs(numbers[1:], target, sum-num) + dfs(numbers[1:], target, sum+num)

def solution(numbers, target):
    answer = 0
    answer = dfs(numbers, target, 0)
    return answer

# 프로그래머스에서는 하나의 함수를 던져주지만 내가 다른 함수를 만들면 된다는 것을 잊지말자.
# 위의 문제같은 경우에는 단지 target이 되는 경우의 수만 다 구하면 되기 때문에 1, 0으로 재귀 조건문을 나눠서 target이 되면 1을 반환하게 하고
# 그것들을 다 더하면 경우의 수가 나오기 때문에 return문에 선언을 함으로써 해결할 수 있다.
