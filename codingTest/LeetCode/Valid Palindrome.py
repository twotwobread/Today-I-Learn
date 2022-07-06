# 문제 유형 : 문자열 처리
# <아이디어>
# - 먼저 스트링의 최대 길이가 200,000 이다. 그렇기 때문에 처음부터 끝까지 처리하고 뒤에서 처음까지 처리해도 괜찮다.
# - 하지만 시간을 절약하기 위해서 Two Pointer를 사용했다. 맨처음부터 출발하는 포인터와 맨 뒤에서부터 출발하는 포인터를 이용한다.
# - 알파벳이거나 숫자면 포인터가 멈춰있다가 둘다 알파벳이거나 숫자면 두개를 비교한다. 대문자면 소문자로 바꾸고 비교한다.
# - 같으면 계속하고 다르면 False를 반환한다.
# - " " 과 같이 숫자나 알파벳이 없는 문자열일 경우 True를 반환한다. "" 는 그대로랑 뒤집은거랑 같기 때문이다.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isRight(s):
            if '0'<=s<='9' or 'a'<=s<='z' or 'A'<=s<='Z':
                return True
            else:
                return False
        
        left = 0
        right = len(s)-1
        while left <= right:
            if isRight(s[left]) and isRight(s[right]):
                l = s[left]; r = s[right]
                if 'A'<=l<='Z':
                    l = str(s[left]).lower()
                if 'A'<=r<='Z':
                    r = str(s[right]).lower()
                if l != r:
                    return False
                left += 1; right -= 1
            elif isRight(s[left]):
                right -= 1
            elif isRight(s[right]):
                left += 1
            else:
                right -= 1; left += 1
        return True
            
        
