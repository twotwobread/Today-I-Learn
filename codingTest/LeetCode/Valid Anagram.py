# 둘다 최대 50,000 길이 이기때문에
# 모든 조합을 볼 순 없음.
# 그래서 hash table -> dict() 이용해서
# 갯수를 세는 방식 이용
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        result = dict()
        for i in s:
            if result.get(i, 0):
                result[i] += 1
            else:
                result[i] = 1
        for i in t:
            if result.get(i, 0):
                result[i] -= 1
            else:
                return False
        return True
