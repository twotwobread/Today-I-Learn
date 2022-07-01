# 문제 유형 : 구현
# [ 아이디어 ]
# - 2부터 문자열의 절반 길이까지 순차적으로 증가하면서 자른다.
# - 문자열의 길이의 절반 이상이 되면 어짜피 똑같을 수 없다.
# - for 문을 이용해서 +i 해서 비교해간다.
# 6시 20분 - 40분
def solution(s):
    minValue = len(s)
    for i in range(1, len(s)//2 + 1): # 2부터 문자열 절반 길이까지 슬라이스
        temp = s[0:i]
        cnt = 1
        new = ""
        for j in range(i, len(s), i):
            if temp != s[j:j+i]:
                new += str(cnt) + temp if cnt > 1 else temp
                temp = s[j:j+i]
                cnt = 1
            else:
                cnt += 1
            #record = j+i
        new += str(cnt) + temp if cnt > 1 else temp
        if minValue > len(new):
            minValue = len(new)
    return minValue
if __name__ == "__main__":
    s = input()
    print(solution(s))
