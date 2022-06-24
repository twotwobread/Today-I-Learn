# 문제 유형 : 그리디
# 작고 큰거 합친게 n-1개면 내 등수를 알 수 있음.
# 플루이드 워셜도 생각했는데 시간복잡도가 N^3이라서 75,000,000 연산 횟수를 거쳐야한다.
# 그래서 pypy3를 지원하는경우 가능할 것 같다.
# 사실 플루이드랑 이거랑 시간복잡도는 비슷할것같다. 아니네 오히려 더 느리겠다
# extend는 O(len(a)) 이니까 전부 더 하게되면 최악의 경우엔 500개에서 500개 다 갈 수 있는 상황이 나올 것이고 그럼
# 500개에 500개의 값들을 다 들고 올테니까 500 * 500 * 500 랑 비슷할듯.
def solution():
    for i in range(1, n+1):
        temp = b_graph[i].copy()
        for b in b_graph[i]:
            temp.update(b_graph[b])
        b_graph[i] = temp
        temp = s_graph[i].copy()
        for s in s_graph[i]:
            temp.update(s_graph[s])
        s_graph[i] = temp

    count = 0
    for i in range(1, n+1):
        temp = len(b_graph[i])
        temp += len(s_graph[i])
        if temp == (n-1):
            count += 1
    print(count)

if __name__ == "__main__":
    n, m = map(int, input().split())
    s_graph = [set() for _ in range(n+1)]
    b_graph = [set() for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        s_graph[b].add(a)
        b_graph[a].add(b)
    solution()
