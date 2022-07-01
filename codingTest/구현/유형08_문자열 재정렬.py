# 문제 유형 : 구현
# [ 아이디어 ]
# - 아스키 코드값을 이용해서 정렬을 하고
# - 앞에서부터 숫자인부분을 찾아서 그대로 뒤에 붙이기.
if __name__ == "__main__":
    s = list(input())
    s.sort(key=lambda x : ord(x))
    temp = 0
    for i in range(len(s)):
        if s[i] > '9':
            temp = (i-1)
            break
    s = s[temp+1:] + s[:temp+1]
    print("".join(s))
