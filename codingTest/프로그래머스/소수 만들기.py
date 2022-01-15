# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 
# 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, 
# nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# - nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
# - nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.


from itertools import combinations, product
def solution(nums):
    answer = 0
    s= list(map(sum, combinations(nums, 3)))
    for l in s:
        check = 0
        for i in range(2, l):
            if l % i == 0:
                check = 1
        if check == 0:
            answer += 1
    return answer

# 하나의 리스트에서 중복되지 않는 수의 조합을 계산하기 위해서 combinations을 이용하였고 그것들의 합이 소수가 되어야하기 때문에
# map을 이용해서 sum을 구했고 그것을 소수임을 확인하기 위한 반복문에 넣었다.
