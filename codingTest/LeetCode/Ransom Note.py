# Hash Table - dict() 이용해서 풀었음.
# ransomNote가 magazine에 있는 알파벳으로 만들 수 있으면 True 아니면 False 리턴하는 문제
# Hash Table에 magazine에 있는 알파벳을 다 등록하고 여러개면 숫자를 증가시켰음.
# 그리고 값이 도출되면 하나씩 숫자를 뺐고 0 = False 이기 때문에 이를 이용해서 break 시켰음.
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        result = dict()
        for m in list(magazine):
            if result.get(m, False): result[m] += 1
            else: result[m] = 1 
        for r in list(ransomNote):
            if not result.get(r, False):
                break
            result[r] -= 1
        else:
            return True
        return False
