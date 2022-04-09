# file name : 3710_369게임3.py
# author : Lee Suyoung(2022-04-10)
# 시작 수 a, 마지막 수 b가 입력될 시 그범위의 369 게임에서 박수의 총합 출력
# 숫자에 3,6,9가 들어가면 369 수에 해당됨.
# 그때, 3,6,9가 들어간 개수 만큼 박수를 침.
# 그외의 숫자들은 박수를 치지 않음.
# 1 <= 
# 시간 제한 : 2초, 메모리 제한 : 512MB
def solution(a, b):
    result = [0] * (b+1)
    for i in range(1, b+1):
        oneNum = i%10
        if oneNum == 3 or oneNum == 6 or oneNum == 9:
            result[i] = result[i//10] + 1
        else:
            result[i] = result[i//10]
    return sum(result[a:])

if __name__ == "__main__":
    # a, b 입력
    a, b = map(int, input().split(" "))
    print(solution(a, b))
# 시간초과 발생
