# 먹어야할 음식 N개 존재 (1-N번)
# 섭취 시 일정 시간 소요, 다음과 같은 방법으로 음식을 섭취
# 1. 1번 음식부터 먹으며, 회전판은 번호가 증가하는 순서대로 음식을 가져도 놓음
# 2. 마지막 번호의 음식을 먹고 회전판에 의해 다시 1번 음식이 온다.
# 3. 음식 하나를 1초 동안 섭취한 후 남은 음식은 그대로 두고, 다음 음식을 섭취
#    다음 음식이란, 아직 남은 음식 중 다음으로 섭취해야 할 가장 가까운 번호의 음식
# 4. 회전판이 다음 음식을 가져오는데 걸리는 시간 x
# 먹방 시작 K초 후에 네트워크 장애로 방송이 중단. 무지가 다시 방송을 이어갈 때,
# 몇번 음식부터 섭취해야 하는지를 알고자 한다. 음식을 모두 먹는데 필요한 시간이 담겨 있는 배열 food_times, 네트워크 장애가 발생한 시간 K초가 매개변수로 주어질 때 몇 번 음식부터 다시 섭취하면 되는지 return하도록 완성하시오
# 더 섭취할 음식이 없다면 -1 반환
# 정확성 테스트 제한사항
# food_times - 길이는 1이상 2,000이하, 원소는 1이상 1,000이하
# K = 1 이상 2,000,000 이하
# 효율성 테스트 제한사항
# food_times - 길이는 1이상 200,000 이하
# food_times 원소는 1 이상 100,000,000 이하
# K = 1 이상 2x10^3 이하
# 1초, 128MB

# 효율성 체크를 보니까 그냥 돌면서 빼면 절대 통과할 수가 없네
# 일단 길이를 체크를 해서 그걸 이용해서 빼면 되는데 0이 되는 경우를 어떻게 처리를 해야할까.

def NowLength(food, now):
    sum = 0
    for i in range(len(food)):
        if food[i] == 0:
            continue
        sum += food[i]
        food[i] -= 1
        now -= 1
        if now == 0:
            return food, now, i, sum
    return food, now, 0, sum

def solution(food_times, k):
    nowK = k
    while nowK>0:
        food_times, nowK, index, sum = NowLength(food_times, nowK)
        if sum == 0:
            break
        if nowK == 0:
            if index == len(food_times) - 1:
                for i in range(0, len(food_times)):
                    if food_times[i] > 0:
                        return i+1
            else:
                for i in range(index+1, len(food_times)):
                    if food_times[i] > 0:
                        return i+1
                for i in range(0, index+1):
                    if food_times[i] > 0:
                        return i+1   
    return -1

# 정확성 체크는 다 통과하는데 효율성을 하나도 통과못함. 그래서 조금 더 빠르게 만들기 위해서
# 0이 아닌 인덱스를 리스트에 담고 그것만 돌려야겠다고 생각.


def NowLength(food, now, existFood):
    array = []
    sum = 0
    if len(existFood) == 0:
        for i in range(len(food)):
            food[i] -= 1
            sum += food[i]
            now -= 1
            array.append(i)
            if now == 0:
                return food, now, i, sum, existFood
    else:
        for i in existFood:
            if food[i] == 0:
                continue
            food[i] -= 1
            sum+=food[i]
            now -= 1
            array.append(i)
            if now == 0:
                return food, now, i, sum, existFood
    return food, now, i, sum, array

def solution(food_times, k):
    nowK = k
    array = []
    sum = 0
    while nowK>0:
        food_times, nowK, last_index, sum, array = NowLength(food_times, nowK, array)
        if sum == 0:
            break
        if nowK == 0:
            if len(array) == 0:
                for i in range(last_index+1, len(food_times)):
                    if food_times[i] > 0:
                        return i+1
                for i in range(0, last_index+1):
                    if food_times[i] > 0:
                        return i+1

            else:
                if last_index == len(food_times) - 1:
                    for i in array:
                        if food_times[i] > 0:
                            return i+1
                else:
                    array_index = array.index(last_index)
                    for i in array[array_index+1:-1]:
                        if food_times[i] > 0:
                            return i+1
                    for i in array[0:array_index+1]:
                        if food_times[i] > 0:
                            return i+1   
    return -1

# 그래서 위와 같이 짰는데 정확도도 틀리는 부분이 발생하고 효율성을 하나도 통과 못함.
# 빠르게 만드는 방법을 생각해봐야할 것같음.
