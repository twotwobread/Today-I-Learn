# 문제 유형: 이분 탐색 변형 - 파라메트릭 서치
# 자료 구조 : 리스트 - 집 정보
def solution(start, end):
    while start < end:
        mid = (start + end + 1) // 2
        compare = home[0]
        index = 1
        for i in range(1, n):
            if (compare + mid) <= home[i]:
                compare = home[i]
                index += 1
        if index < c:
            end = mid - 1
        else:
            start = mid
    return start

if __name__ == "__main__":
    n, c = map(int, input().split())
    home = []
    for _ in range(n):
        home.append(int(input()))
    home.sort()
    start = home[1] - home[0]
    end = home[-1] - home[0]
    result = 0
    print(solution(start, end))
