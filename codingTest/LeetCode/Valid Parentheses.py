# 문제 유형 : 스트링, 스택
# 자료 구조 : 1차원 리스트 - 스택으로 활용 -> 괄호 저장
# < 아이디어 > 
# - 왼쪽 괄호가 먼저 나오기 때문에 왼쪽 괄호를 스택에 저장.
# - 그리고 오른쪽 괄호가 나왔을때, 스택 top에 있는걸 pop했을 때 짝이 맞으면 성공아니면 실패
# < 시간, 공간 >
# - 스트링의 길이가 10,000 이기 때문에 반복문으로 구현시 가능.
# - 공간도 달라지는 공간이 스택인데 O(10,000)으로 최대 10KB 정도라 예상.

class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                result.append(i)
            else:
                if len(result) <= 0:
                    return False
                compare = result.pop()
                if (ord(i) - ord(compare)) != 1 and (ord(i) - ord(compare)) != 2:
                    return False
        if len(result) > 0:
            return False
        return True
        
