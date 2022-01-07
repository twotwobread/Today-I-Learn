# 일반적인 퀵소트 pivot은 중간값으로 정했음.

# def partition(arr, start, end, pivot):
#     global COUNT
#     new_pivot = start
#     p_value = arr[pivot] # 3
#     arr[end], arr[pivot] = arr[pivot], arr[end]
#     for i in range(start, end):
#         if p_value > arr[i]:
#             arr[new_pivot], arr[i] = arr[i], arr[new_pivot]
#             new_pivot+=1
#     arr[end], arr[new_pivot] = arr[new_pivot], arr[end]
#     return new_pivot

# def quickSort(arr, start, end):
#     global COUNT
#     if start>=end:
#         return
#     pivot = (start+end)//2
#     new_pivot = partition(arr, start, end, pivot)
#     quickSort(arr, start, new_pivot-1)
#     quickSort(arr, new_pivot+1, end)

## 파이썬을 이용하여 훨씬 편하고 간단하게 짠 퀵소트

def quickSortStPython(arr, start, end):
    if len(arr)<=1:
        return arr
    
    pivot = (start+end)//2
    p_value = arr[pivot]
    arr[pivot], arr[end] = arr[end], arr[pivot]

    left = [ arr[i] for i in range(start, end) if arr[i] < p_value ]
    right = [ arr[i] for i in range(start, end) if arr[i] > p_value ]
    
    return quickSortStPython(left, 0, len(left)-1) + [p_value] + quickSortStPython(right, 0, len(right)-1)
    

if __name__ == "__main__":
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    print(array)
    array = quickSortStPython(array, 0, len(array)-1)
    #quickSort(array, 0, len(array)-1)
    print(array)


############# [계수 정렬] #############
arr =[7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

count = [0]*(max(arr)+1)

for i in arr:
    count[i] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=" ")

