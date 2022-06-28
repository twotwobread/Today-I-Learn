# 문제 유형 : 서로소 집합
# 자료 구조 : 1차원 리스트 - 루트 정보
# [ 아이디어 ]
# - 2 이렇게 값이 들어오면 1, 2 번 탑승구에 도킹이 가능하다는 의미이다.
# - 그렇다면 무조건 왼쪽으로 가면서 확인해야하니까 노드를 왼쪽이랑 연결을 한다.
# - 만약 연결할 수 없으면 루트가 0이 되는것!
def find(rt, x):
    if rt[x] != x:
        rt[x] = find(rt, rt[x])
    return rt[x]
def union(rt, a, b):
    pA = find(rt, a)
    pB = find(rt, b)
    if pA > pB:
        rt[pA] = pB
    else:
        rt[pB] = pA

if __name__ == "__main__":
    G = int(input())
    P = int(input())
    exit = list(map(int, range(G+1)))
    maxNum = 0
    docking = [int(input()) for i in range(P)]
    for d in docking:
        rt = find(exit, d)
        if rt == 0:
            print(maxNum)
            break
        union(exit, rt, rt-1)
        maxNum += 1
    else:
        print(maxNum)
