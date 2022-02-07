# file name : 그리디_문제3.py
# 문자열 뒤집기
# 0과 1로만 이루어진 문자열 S를 가지고 있음.
# 이 문자열 S에 있는 모든 숫자를 전부 같게 만들려고 한다.
# 할 수 있는 행동은 S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다. ( 0->1, 1->0 )
# ex) S = 0001100
#     1. 전부 뒤집으면 1110011
#     2. 4번째 문자부터 5번째 문자까지 뒤집으면 1111111이 되어 두 번만에 같은 숫자로 만듬.
#     but, 처음부터 4번째 문자부터 5번쨰 문자까지 뒤집으면 0000000이 되어 1번만에 모두 같은 숫자로 만들 수 있음.
# 행동의 최소 횟수를 출력해라.
# S = 0과 1로만 이루어지고 1,000,000 이하의 길이
# 시간 제한: 2초, 메모리 제한: 128MB
# author : Lee Suyoung (2022-02-07)

# 중요한 것은 연속된 하나이상을 잡고 뒤집는다. 연속적으로 붙어있어야 같이 뒤집을 수 있음.
# 결국은 반대로 뒤집는 거잖아. 그럼 1로 뒤집어 보고 0으로 뒤집어 보고 두개의 경우 밖에 없지않나?
# 두개 횟수만 비교하면 될꺼 같은데?
# 0의 뭉탱이 갯수 세고 1의 뭉탱이 갯수 세고 두 개 비교하고 해보자

# s 문자열 입력 이거 
s = input()
# 반복문 돌리면서 0의 뭉탱이 세면될듯 1이랑 같이 세면 더 좋을꺼 같다.
cnt_zero=0
flag_zero=False
cnt_one=0
flag_one=False
for i in s:
    if i == "0":
        if flag_one:
            flag_one = False
        if flag_zero:
            continue
        else:
            flag_zero = True
            cnt_zero += 1
    elif i == "1":
        if flag_zero:
            flag_zero = False
        if flag_one:
            continue
        else:
            flag_one = True
            cnt_one += 1

print(min(cnt_one, cnt_zero))

# 최소 개수 출력
