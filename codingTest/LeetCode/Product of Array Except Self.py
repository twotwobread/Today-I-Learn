class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [0]*len(nums)
        r_product = [0]*len(nums)
        r_nums = nums[::-1]
        for i,n in enumerate(nums):
            if i == 0:
                product[i] = n
                r_product[i] = r_nums[i]
            else:
                product[i] = product[i-1] * n
                r_product[i] = r_product[i-1] * r_nums[i]
        result = []
        for i in range(len(nums)):
            left = product[i-1] if i-1 >= 0 else 1
            right = r_product[len(nums)-i-2] if len(nums)-i-2 >=0 else 1
            result.append(left*right)
        return result
