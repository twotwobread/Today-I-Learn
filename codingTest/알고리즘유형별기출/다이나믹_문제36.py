# file name : 다이나믹_문제36.py
# 편집 거리
# 두개의 문자열 A, B가 주어졌을 때, A를 편집하여 B로 만들고자 한다.
# A를 편집시 다음의 세 연산 중에서 한 번에 하나씩 선택하여 이용가능하다.
# 1. 삽입 : 특정한 위치에 하나의 문자를 삽입한다.
# 2. 삭제 : 특정한 위치에 있는 하나의 문자를 삭제한다.
# 3. 교체 : 특정한 위치에 있는 하나의 문자를 다른 문자로 교체한다.
# 편집 거리는 A를 편집하여 B로 만들기 위해 사용한 연산의 수를 의미
# 최소 편집 거리를 계산하여 출력하시오
# A, B가 주어짐
# 알파벳으로만 주어지고 문자열의 길이는 1 이상 5,000 이하
# 시간 제한 : 2초, 메모리 제한 : 128MB
# author : Lee Suyoung (2022-02-07)

# n번째에서 봤을때, n-1이랑 n+1 이렇게 하냐 아니면 n->m으로 이렇게 하냐 
# 이 세가지만 생각하면 되는데 이걸 점화식으로 바꾸면 되는데 어렵네
# 일단 길이가 얼마나 다른지부터 체크하고 길이가 더 A가 더 길면 -> 삭제, 교체만 생각
# A가 더 짧다면 -> 삽입, 교체만 생각하면 될 것같다.
# 시간제한이 2초이기 때문에 40,000,000 정도까지는 여유가 있다.
# 일단 먼저 교체하지 않아도 되는 알파벳을 먼저 체크 해놓고 

def deleteReplace(num, A, B, cnt):
    if len(A) <= len(B):
        return A, cnt
    if A[num] == B[num]:
        case1, cnt1 = deleteReplace(num+1, A, B, cnt)
        if case1 == B:
            return case1, cnt1
    else:
        case2, cnt2 = deleteReplace(num, A[0:num]+A[num+1:-1], B, cnt+1) # delete
        case3, cnt3 = deleteReplace(num, A[0:num]+B[num]+A[num+1:-1], B, cnt+1) # insert
        if case2 == B:
            return case2, cnt2
        elif case3 == B:
            return case3, cnt3

def insertReplace(num, A, B, cnt):
    if len(A) >= len(B):
        return A, cnt
    if A[num] == B[num]:
        case1, cnt1 = insertReplace(num+1, A, B, cnt)
        if case1 == B:
            return case1, cnt1
    else:
        case2, cnt2 = insertReplace(num, A[0:num]+B[num]+A[num:-1], B, cnt+1) # insert
        case3, cnt3 = insertReplace(num, A[0:num]+B[num]+A[num+1:-1], B, cnt+1) # replace
        if case2 == B:
            return case2, cnt2
        elif case3 == B:
            return case3, cnt3

# A 문자열 입력
A = input()
B = input()

lenA = len(A)
lenB = len(B)

result=0
cnt = 0
if lenA > lenB : # 삭제, 교체만 생각
    A, result = deleteReplace(0, A, B, 0)
    print(A)
    print(result)

elif lenA < lenB: # 삽입, 교체만 생각
    A, result = insertReplace(0, A, B, 0)
    print(A)
    print(result)

else: # 교체만 생각
    for i in range(lenA):
        if A[i] != B[i]:
            result+=1
    print(result)

## 실패했다,,, 저렇게 재귀형식으로 짤려고 하니까 일단 재귀가 멈추는 조건이 되게 애매했다.
# count, coun을 예로 보면 A는 t가 있어서 괜찮지만 B는 out of index가 난다.
# 개수 조절이 쉽지않다. 일단 조금 더 생각해봐야할 것 같다.
