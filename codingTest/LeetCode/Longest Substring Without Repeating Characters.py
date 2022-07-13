# 문제 유형 : 슬라이딩 윈도우
# 아이디어
# - 슬라이딩 윈도우는 매번 반복되는 요소를 버리지 않고 재사용하여 효율적인 코드를 짜는 방식.
# - 이를 이용해서 효율적으로 비교 및 저장.
# - dict안에 문자가 없으면 계속 넣어주다가 같은 문자가 있으면 현재의 dict 길이를 최대 서브스트링 길이와 비교해서 더 큰 값을 저장해준다.
# - 그리고 같은 문자가 없을때까지 시작점부터 값을 삭제해준다. 그 후 현재 값 삽입하고 다시 이어나간다.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        start = 0
        maxLength = 1
        subString = dict()
        for end, char in enumerate(s):
            if subString.get(char, 0):
                maxLength = max(maxLength, len(subString))
                for i in range(len(subString)):
                    del subString[s[start]]
                    start += 1
                    if not subString.get(char, 0):
                        subString[char] = 1
                        break
            else:
                subString[char] = 1
        maxLength = max(maxLength, len(subString))
        return maxLength
