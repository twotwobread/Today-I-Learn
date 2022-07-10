class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result = dict()
        for n in nums:
            if result.get(n, 0):
                return True
            else:
                result[n] = 1
        return False
