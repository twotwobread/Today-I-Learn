def quickSorting(array, start, end):
    if start >= end:
        return
    pivot = (start+end)//2
    pivotValue = array[pivot][0]
    pivotIndex = array[pivot][1]
    array[pivot], array[end] = array[end], array[pivot]
    
    newPivot = start
    for i in range(start, end):
        if pivotValue < array[i][0]:
            array[i], array[newPivot] = array[newPivot], array[i]
            newPivot += 1
        elif pivotValue == array[i][0]:
            if pivotIndex > array[i][1]:
                array[i], array[newPivot] = array[newPivot], array[i]
                newPivot += 1
    
    array[end], array[newPivot] = array[newPivot], array[end]
    quickSorting(array, start, newPivot-1)
    quickSorting(array, newPivot+1, end)
    return array

def solution(N, stages):
    answer = []
    notClear = [0] * (N+2)
    failPercent = [[0] for _ in range(N+1)]
    # 머무르고 있는 사람의 정보
    for s in stages:
        notClear[s] += 1
    # 스테이지 돌면서 실패율 계산
    for i in range(1, N+1):
        failPercent[i][0] = notClear[i] / sum(notClear[i+1:])
        failPercent[i].append(i)
    array = quickSorting(failPercent[1:], 0, len(failPercent[1:])-1)
    for i in range(N):
        answer.append(array[i][1])
    return answer

# 문제는 런타임 에러가 발생하는 것이다.
# 나는 정렬에서 대부분 런타임 에러가 걸려서 실패하는 경우가 너무 많다.
# 이 부분을 스터디에서 질문을 해봐야할 것 같다.
