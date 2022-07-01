# 문제 유형 : 구현
# 자료 구조 : 1차원 배열 - 점수 저장

if __name__ == "__main__":
    n = list(map(int, input()))
    left = sum(n[:len(n)//2])
    right = sum(n[len(n)//2:])
    if left == right:
        print("LUCKY")
    else:
        print("READY")
