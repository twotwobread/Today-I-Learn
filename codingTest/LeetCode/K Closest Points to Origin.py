# 문제 유형 : Heap
# 아이디어
# - 특정 값을 계산해서 정렬하는 문제를 풀어야함.
# - 그렇기에 정렬은 heapq에 맡기고 계산하는 것만 신경씀.
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minList = []
        for x, y in points:
            cmp = -(pow(x,2)+pow(y,2))
            heapq.heappush(minList, (cmp, x, y))
            if len(minList) > k:
                heapq.heappop(minList)
        return [minList[i][1:] for i in range(len(minList))]
