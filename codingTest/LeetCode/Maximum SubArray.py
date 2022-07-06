# 연속되는거라는걸 알아야함. 그럼 나랑 전에꺼 더한거랑 나자신이랑 비교해야함.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i-1])
        return max(nums)
        
        
