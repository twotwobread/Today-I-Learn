# 해결못함 내일 시도할 예정.
# value, notClear = 도전중인 사람 -> 즉, 현재 스테이지 머물러 있는 사람의 수를 나타냄.
# array = 이걸로 이제 정렬을 할려고 했음, 스테이지 정보를 나타냈다.
# 그래서 array를 이용해서 정렬을 시도 비교하는 값은 value를 이용해서 도전중인 사람 / 시도한 사람 으로 했음.
# 같으면 스테이즈 숫자가 작은것이 먼저 오도록 해야함.


def quickSort(array, start, end, value):
    if start>=end:
        return array
    pivot = array[start]
    pivotValue = value[pivot] / sum(value[pivot:len(value)]) # 도전중인 사람 / 시도한 사람
    tail = array[start+1:]
    left = []
    right = []
    for i in tail:
        if pivotValue == (value[i] / sum(value[i:len(value)])):
            if pivot > i :
                left.append(i)
            else:
                right.append(i)
        elif pivotValue > (value[i] / sum(value[i:len(value)])):
            left.append(i)
        else:
            right.append(i)
    return quickSort(left, 0, len(left)-1, value) + [pivot] + quickSort(right, 0, len(right)-1, value)


    

def solution(N, stages):
    answer = []
    notClear = [0] * (N+2)
    array = [0] * (N+1)
    for i in range(N+1):
        array[i] = i
    for i in stages: # 몇개인지 다 세아렸음.
        notClear[i] += 1
    result = quickSort(array, 1, len(array)-1, notClear)
    print(result)
    return answer

n = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
result = solution(n, stages)
