# nums라는 오름차순으로 정렬된 배열을 일정 칸만큼 로테이션한 배열에서 target의 인덱스는 어디인가?
# 배열은 무엇일까? 하나의 자료형의 여려 데이터들을 저장한 자료구조이다.
# target의 인덱스를 찾기 위해선 어떻게 해야할까? 해당 배열을 탐색하면 된다.
# 대표적으로 배열을 탐색하기 위한 알고리즘은 완전 탐색이 있고 정렬이 된 상태라면 이진 탐색을 사용할 수 있을 것이다.
# 해당 문제에서 요구하는 시간 복잡도가 O(log n)이기 때문에 이진 탐색을 사용해야한다.
# 하지만 해당 배열을 rotate 되어서 정렬된 상태가 아니다. 그렇기 때문에 먼저 얼만큼 rotate 되었는지를 보면 좋을 것 같다.
# 어떻게 확인할 수 있을까? 알고리즘의 복잡도는 무조건 O(log n)이 되어야한다. 정렬을 하면 O(nlogn)의 복잡도이고 인덱스를 찾을 수도 없을 것이다. 
# 경우를 생각해보자.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(arr, target, start, end):
            while start <= end:
                mid = (start + end)//2
                if arr[mid] == target: return mid
                
                if arr[mid] >= arr[start]:
                    if target > arr[mid] or target < arr[start]:
                        start = mid + 1
                    else:
                        end = mid - 1
                else:
                    if target < arr[mid] or target >= arr[start]:
                        end = mid - 1
                    else:
                        start = mid + 1
            return -1
        return binarySearch(nums, target, 0, len(nums)-1)
    #print("start = {}, end = {}".format(start, end))
