#수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.
#1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
#2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
#3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ..
#1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.
##
#제한 조건
# -시험은 최대 10,000 문제로 구성되어있습니다.
# -문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
# -가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요

def solution(answers):
    a=1
    answer = []
    # 1번 12345 5개
    # 2번 21232425 8개
    # 3번 3311224455 10개
    
    num_1 = [1,2,3,4,5]
    num_2 = [2,1,2,3,2,4,2,5]
    num_3 = [3,3,1,1,2,2,4,4,5,5]
    count_1 = 0; count_2 = 0; count_3 = 0
    for idx in range(len(answers)):
        if num_1[idx % len(num_1)] == answers[idx]:
            count_1+=1
        if num_2[idx % len(num_2)] == answers[idx]:
            count_2+=1
        if num_3[idx % len(num_3)] == answers[idx]:
            count_3+=1
            
    if count_1 == count_2:
        if count_1 < count_3:
            answer.append(3)
        elif count_1 == count_3:
            answer.append(1); answer.append(2); answer.append(3)
        else:
            answer.append(1); answer.append(2)
    elif count_1 > count_2:
        if count_1 < count_3:
            answer.append(3)
        elif count_1 == count_3:
            answer.append(1); answer.append(3)
        else:
            answer.append(1)
    elif count_1 < count_2:
        if count_2 < count_3:
            answer.append(3)
        elif count_2 == count_3:
            answer.append(2); answer.append(3)
        else:
            answer.append(2)
            
    return answer

## 너무 노가다식으로 풀어서 다음에 다시 풀어보는 것을 추천한다.
