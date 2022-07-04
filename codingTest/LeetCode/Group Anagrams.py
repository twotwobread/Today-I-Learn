# Hash Table -> dict()
# 같은 문자로 이루어진 단어들을 반환하는 문제
# 100 * 10,000 정도 연산 개수가 발생하는데 이 정도면 얼마 안되는 것임.
# 근데 나는 여기서 해시 함수를 만들어서 ord()를 이용해 key를 새롭게 만들려고 했으나
# 중복되는 값이 무조건 발생함 -> collision 발생 이것을 해결하려면 또 다른 배열을 만들어 추가를 하든
# 충돌이 안발생하든 해야하는데 충돌이 없는 것은 힘듬 -> 문자열 길이가 100까지라서 너무 다양한 수가 나올 수 있음.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = dict()
        keyArray = set()
        for string in strs:
            s = str(sorted(list(string)))
            if result.get(s, 0):
                result[s].append(string)
            else:
                result[s] = [string]
            keyArray.add(s)
        return [result[k] for k in keyArray]
