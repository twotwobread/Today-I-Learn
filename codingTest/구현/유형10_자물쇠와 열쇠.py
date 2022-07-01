# 문제 유형: 규현
# [ 아이디어 ]
# - 원하는 것처럼 시계방향으로 회전해서 4개 의 키 방향이 나온다.
# - 컴비에서 패딩한 것 처럼 2차원 배열의 크기를 M+N - 1 까지 확장시키고 그 후에 스캐닝 하듯이
# - 키를 이용해서 lock을 쭉 훑으면서 덧셈연산을 한다. lock 위치의 값들이 전부 1이면 성공.

def check(graph, start, end):
    for a in range(start, end):
        for b in range(start, end):
            if graph[a][b] != 1:
                return False
    return True
def solution(key, lock):
    k = len(key)
    l = len(lock)

    eastKey = list(map(list, zip(*reversed(key))))
    southKey = list(map(list, zip(*reversed(eastKey))))
    westKey = list(map(list, zip(*reversed(southKey))))
    keyList = [key, eastKey, southKey, westKey]

    mapExpand = [[0] * (l + (k-1)*2) for _ in range(l + (k-1)*2)]  # 1681
    for i in range(l):
        for j in range(l):
            mapExpand[i + (k - 1)][j + (k - 1)] = lock[i][j]

    for key in keyList:
        for a in range(l + (k-1)):
            for b in range(l + (k-1)):
                temp = [mapExpand[x].copy() for x in range(l + (k-1)*2)]
                for i in range(k):
                    for j in range(k):
                        temp[i + a][j + b] += key[i][j]
                if check(temp, k - 1, l + (k-1)):
                    return True
    return False

if __name__ == "__main__":
    key = [[0,0,0], [1,0,0], [0,1,1]]
    lock = [[1,1,1], [1,1,0], [1,0,1]]
    print(solution(key, lock))
