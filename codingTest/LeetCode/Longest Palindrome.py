# 해시 테이블 -> dict 이용할 예정
# 짝수의 문자 갯수들을 다 더하고 마지막으로 가장 큰 홀수를 더하면 무조건 회문이다.
# 위에서 가장 큰 홀수를 제외하고 나머지 홀수는 그 갯수보다 작은 가장 큰 짝수를 더하고
# 마지막으로 가장 큰 홀수를 더하면 가장 긴 회문이 된다.
class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter = dict()
        for char in s:
            if letter.get(ord(char), 0):
                letter[ord(char)] += 1
            else:
                letter[ord(char)] = 1
        result = 0
        maxKey = 0
        maxValue = 0
        for i in range(65, 91):
            if letter.get(i,0) and (letter[i] % 2) == 0:
                result += letter[i]
            elif letter.get(i,0) and (letter[i]%2) != 0:
                if maxValue < letter[i]:
                    maxKey = i
                    maxValue = letter[i]
        for i in range(97, 123):
            if letter.get(i,0) and letter[i] % 2 == 0:
                result += letter[i]
            elif letter.get(i,0) and (letter[i]%2) != 0:
                if maxValue < letter[i]:
                    maxKey = i
                    maxValue = letter[i]
        for i in range(65, 91):
            if i != maxKey and letter.get(i,0) and (letter[i] % 2) != 0:
                result += (letter[i] - 1)
        for i in range(97, 123):
            if i != maxKey and letter.get(i,0) and (letter[i] % 2) != 0:
                result += (letter[i] - 1)
        return result + maxValue
        
