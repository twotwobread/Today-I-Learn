class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = dict()
        for n in nums:
            if result.get(n, 0):
                result[n] += 1
            else:
                result[n] = 1
        return max(result.items(), key=lambda x:x[1])[0]
        
