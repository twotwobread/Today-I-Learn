# 문제 유형 : DP
# 바닥 타일깔기랑 유사.
# 2가지 경우가 있음 내 이전꺼에서 타일하나짜리깔기랑
# 내 이전 이전꺼에서 타일 두개짜리 깔기
# 0 - 하나, []- 두개짜리 타일
# 3 에서 생각해보면
# 1 - 0 이게 끝이고 2 - 00, [ ] 이렇게 가 존재하는데
# 3에서는 00에 0, [ ]에 0, 그리고 0에 [ ]을 붙이는 경우가 존재함.
# 이걸 떠올려야함.
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        result = [0]*(n+1)
        result[1], result[2] = 1, 2
        for i in range(3, n+1):
            result[i] = (result[i-1]+result[i-2])
        return result[n]
