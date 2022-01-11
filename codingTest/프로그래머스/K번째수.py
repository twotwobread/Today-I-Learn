def solution(array, commands):
    answer=[]
    for i in commands:
        tmp = sorted(array[i[0]-1:i[1]])
        answer.append(tmp[i[2]-1])
    return answer

#####[남이 푼 가장 짧은 코드]#####
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

# map이 commands를 하나의 리스트씩 넣어줄 수 있고, 그걸 이용해서 lambda에서 하나의 리스트씩 x로 바꾸어 리스트의 0번째, 1번째 인덱스 값만큼 슬라이싱 한 후 리스트의 2번째 요소에서의 값들을 
# 리스트로 만들어 반환한다.
