# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
# 문제 유형 : 이진 탐색 - 최대값 찾는 느낌으로 
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left < right:
            mid = (left + right)//2
            if isBadVersion(mid): # 같거나 크면
                right = mid
            else:
                left = mid + 1
        return right
                
        
