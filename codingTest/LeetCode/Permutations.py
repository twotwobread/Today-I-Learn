# 문제에서 원하는 것은 순열을 구하는 것이다.
# 순열을 구하는 방법 중 백트래킹을 이용해서 구해보자.
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permutation(index):
            if len(index) == len(nums):
                result.append(index.copy())
                return
            for n in nums:
                if not n in index:
                    index.append(n)
                    permutation(index)
                    index.pop()
                    
        result = []
        index = []
        permutation(index)
        return result
            
