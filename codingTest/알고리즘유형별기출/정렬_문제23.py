# file name : 정렬_문제23.py
# 국영수
# N명의 이름과 국어, 영어, 수학 점수가 주어짐
# 해당 조건으로 성적을 정렬
# 1. 국어 점수가 감소하는 순으로
# 2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
# 3. 국어 영어 점수가 같으면 수학 점수가 감소하는 순서로
# 4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (대문자가 소문자보다 작으니까 사전 순 앞으로)
# 1 <= N <= 100,000
# 이름, 국어, 영어, 수학 공백으로 구분, 점수는 1이상 100이하
# 이름은 알파벳 대소문자로만 구성, 10자리이하
# author : Lee Suyoung (2022-02-07)

# n 입력 (학생수)

n = int(input())

# 이름, 국어, 영어, 수학 공백으로 구분
student = []
for i in range(n):
    name, korean, english, math =  map(str, input().split())
    student.append((name, int(korean), int(english), int(math)))
# 겁나 간단하게 sort를 이용해서 국어로 정리한번하고 영어로 정리한번하고 수학으로 정리한번하고 그다음 이름으로 정리하고 이러면 안되나?
# 생각해보니까 안되겠네 계속 다르게 정렬되니까 우리가 생각한건 이제 같은 애만 그렇게 정렬하는거니까

def newPivot(array, start, end, pivot):
    new_pivot = start
    pivot_data = array[pivot]
    array[end], array[pivot] = array[pivot], array[end]
    for i in range(start, end):
        if pivot_data[1] < array[i][1]:
            array[new_pivot], array[i] = array[i], array[new_pivot]
            new_pivot+=1
        elif pivot_data[1] == array[i][1]:
            if pivot_data[2] > array[i][2]:
                array[new_pivot], array[i] = array[i], array[new_pivot]
                new_pivot+=1
            elif pivot_data[2] == array[i][2]:
                if pivot_data[3] < array[i][3]:
                    array[new_pivot], array[i] = array[i], array[new_pivot]
                    new_pivot+=1
                elif pivot_data[3] == array[i][3]:
                    if pivot_data[0] > array[i][0]:
                        array[new_pivot], array[i] = array[i], array[new_pivot]
                        new_pivot+=1
    array[new_pivot], array[end] = array[end], array[new_pivot]
    return new_pivot

def quickSort(array, start, end):
    if start>=end:
        return
    pivot = (start+end)//2
    new_pivot = newPivot(array, start, end, pivot)

    quickSort(array, start, new_pivot-1)
    quickSort(array, new_pivot+1, end)
    return array

student = quickSort(student, 0, len(student)-1)
for i in range(len(student)):
    print(student[i][0])

# 최대 100,000개라서 선택정렬이나 삽입정렬로는 못풀고
# sort()를 이용하기엔 조건이 많아서 퀵정렬이용해서 조건을 걸어줌.
