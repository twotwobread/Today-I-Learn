#from collections import defaultdict
# Hash table -> dictionary를 이용해서 풀었음.
# 문제에선 O(n^2)보다 더 빠른 시간 복잡도를 요구했음.
# 한 인덱스 값과 다른 인덱스의 값의 합이 target과 같은 경우를 찾는 것이라서
# 이진탐색도 별로라고 생각했음.
# 그래서 dictionary를 이용해서 합이 더 큰 경우를 도출했음.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = dict()
        for i in range(len(nums)):
            result.setdefault(nums[i], [])
            result[nums[i]].append(i)
        for k in result.keys():
            v = target - k
            if result.get(v, False) and len(result[v]) > 0:
                #print(result, v, k)
                if k == v and len(result[v]) > 1:
                    return sorted([result[k][0], result[v][1]])    
                elif result[k][0] != result[v][0]:
                    return sorted([result[k][0], result[v][0]])
