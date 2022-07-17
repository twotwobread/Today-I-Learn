# gridTraveler(m, n) - 왼쪽 꼭짓점에서 출발해서 오른쪽 꼭짓점까지의 갈수있는 길의 경우의 수
# gridTraveler(1,1) -> 1
# 이 경우엔 하나 밖에 없다. 경우가.
# gridTraveler(3,3) -> ?
def gridTraveler(m, n):
    if (m == 1 and n == 1): return 1
    if (m==0 or n==0): return 0
    return gridTraveler(m-1, n) + gridTraveler(m, n-1) # 아래로 간 경우 3x3에서 2x3의 경우를 구하는 문제가 됨. 오른쪽으로 간 경우 3x3에서 3x2의 경우를 구하는 문제가 됨.
# 이 경우는 너무 느리다. 같은 값이 계속 계산되기 때문이다 -> 피보나치처럼
# 메모제이션을 생각해보자.
def gridTraveler_memo(dp, m, n):
    if (m == 1 and n == 1): return 1
    if (m==0 or n==0): return 0
    if dp[m][n] != -1:
        return dp[m][n]
    dp[m][n] = gridTraveler(dp, m-1, n) + gridTraveler(dp, m, n-1)
    dp[n][m] = dp[m][n]
    return dp[m][n]

# canSum(goal, numbers) - 목표 값을 만들 수 있으면 True
# canSum(7, [5,3,4,7]) -> true
# canSum(7, [2,4]) -> false
def canSum(goal, numbers):
    if goal == 0: return True
    if goal < 0: return False
    for n in numbers:
        if canSum(goal-n, numbers):
            return True
    return False
def canSum(dp, goal, numbers):
    if dp[goal] != -1: return dp[goal]
    if goal == 0: return True
    if goal < 0: return False

    for n in numbers:
        if canSum(dp, goal-n, numbers):
            dp[goal] = True
            return True
    dp[goal] = False
    return False

# howSum(goal, numbers) - 목표 값을 만드는게 가능하면 아무 조합이나 반환
# howSum(7, [2,3]) -> [3,2,2]
def howSum(goal, numbers):
    if goal == 0: return []
    if goal < 0: return None

    for n in numbers:
        result = howSum(goal - n, numbers)
        if result != None:
            return result.append(n)
    return None
def howSum(dp, goal, numbers):
    if dp[goal] != -1: return dp[goal]
    if goal == 0: return []
    if goal < 0: return None

    for n in numbers:
        result = howSum(dp, goal-n, numbers)
        if result != None:
            dp[goal] = result.append(n)
            return dp[goal]
    dp[goal] = None
    return dp[goal]

# bestSum(goal, numbers) - 가장 짧은 조합 반환
# bestSum(8, [2, 3, 5]) -> [3, 5]
def bestSum(goal, numbers):
    if goal == 0: return []
    if goal < 0: return None

    shortest = None
    for n in numbers:
        result = bestSum(goal - n, numbers)
        if result != None:
            result.append(n)
            if shortest == None or len(shortest) > len(result):
                shortest = result
    return shortest

def bestSum(dp, goal, numbers):
    if dp[goal] != -1: return dp[goal]
    if goal == 0: return []
    if goal < 0: return None

    shortest = None
    for n in numbers:
        result = bestSum(dp, goal - n, numbers)
        if result != None:
            result.append(n)
            if shortest == None or len(shortest) > len(result):
                shortest = result
    dp[goal] = shortest
    return dp[goal]
# canSum -> 가능한가 불가능한가? - Decision Problem ( 의견 문제 )
# howSum -> 어떻게 할 것인가? - Combinatoric Problem ( 조합 문제 )
# bestSum -> 할 수 있는 방법 중 최적의 경우는? - Optimization Problem ( 최적화 문제 )
# => 이것들은 전부 DP의 범주에 속한다.

# canConstruct(goal, wordBank) - wordBank에 있는 문자열로 goal 문자열을 만들수있는지?
# canConstruct(abcdef, [ab, abc, cd, def, abcd]) -> True
# 이거 문제의 핵심 아이디어는 prefix 부터 없애나간다는 것이다. 결국은 모든 문제에서 답이 나올려면
# 접두사에 해당하는 문자열이 존재해야 없어질 수 있다. 그리고 그것들은 항상 붙어있어야한다.
# 그렇기 때문에 모든 재귀에서 접두사만 생각해서 goal을 줄여나가면 문제를 풀수있다.
def canConstruct(dp, goal, wordBank):
    if goal in dp: return dp[goal]
    if goal == '': return True

    for word in wordBank:
        if goal.index(word) == 0:
            if canConstruct(dp, goal[len(word):], wordBank):
                dp[goal] = True
                return True
    dp[goal] = False
    return False

# countConstruct(goal, wordBank) - goal을 만들 수 있는 방법의 개수
# countConstruct(abcdef, [ab, abc, cd, def, abcd]) -> 1
def countConstruct(dp, goal, wordBank):
    if goal in dp: return dp[goal]
    if goal == '': return 1

    sumValue = 0
    for word in wordBank:
        if goal.index(word) == 0:
            sumValue += countConstruct(dp, goal[len(word):], wordBank)
    dp[goal] = sumValue
    return sumValue

# allConstruct(goal, wordBank) - goal을 만들 수 있는 방법의 조합
# allContruct(abcdef, [ab, abc, cd, def, abcd, ef, c]) -> [ [ab, cd, ef], [ab, c, def], [abc, def], [abcd, ef] ]
# 여기서의 핵심아이디어는 goal이 '' 일때 2차원 배열을 반환한다는 것이고 2차원 배열끼리 덧셈 연산을 하면 [[1]] + [[2]] => [[1], [2]] 이란 것이다.
# 재귀로 구성되다 보니까 반대 순서로 요소들이 저장되는 것을 알아놓자.
def allConstruct(goal, wordBank):
    if goal == '': return [[]]

    all = []
    for word in wordBank:
        if goal.index(word) == 0:
            result = allConstruct(goal[len(word):], wordBank)
            if len(result) != 0:
                for r in result:
                    r.append(word)
                all += result
    return all

# 지금까지 예제로 봤던 모든 문제에서 중요했던 것은 가장 쉽게 구할 수 있는 작은 부분에 대해서 생각했던 것이고
# 거기에 도달했을때 유의미한 값을 반환했다. 탑다운 방식이다 보니까 마지막엔 가장 작은 부분이 남는데 그 부분이 유의미한지를
# 생각해서 유의미한 작은 부분을 결정하고 푸는 것이 탑다운 방식에서 키 포인트인 것 같다.


#### 이제는 tabulation - 테이블 만들기라는 뜻
# 재귀적이지 않다는 것이 큰 차이점 -> 반복으로 풀어나갈 것.

# gridTraveler(m, n) - 왼쪽 꼭짓점에서 출발해서 오른쪽 꼭짓점까지의 갈수있는 길의 경우의 수
# gridTraveler(1,1) -> 1
# 이 경우엔 하나 밖에 없다. 경우가.
# gridTraveler(3,3) -> ?
# 재귀는 큰 것에서 작은 것을 향해서 갔었다. 테이블은 반대로 작은 것부터 큰 것으로 가기 때문에 얘도 작은 걸 먼저 생각해보자.
# 진짜 작게 보면 (1,1)은 1이다. 방법의 개수는 무조건 하나가 되니까 그렇다면 (1, 2)는? 이것도 1일 것이다.
# 그럼 (2,2)는 2가 된다. (1,2), (2,1)이 모여서 2가 되는 것이다. 이걸 쭉 진행하면 (3,3)은 6이 된다.
def girdTraveler(n, m):
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[1][1] = 1
    for i in range(n+1):
        for j in range(m+1):
            if j+1 <= m: dp[i][j+1] += dp[i][j]
            if i+1 <= n: dp[i+1][j] += dp[i][j]
    return dp[n][m]
# 테뷸레이션 레시피
# 1. 테이블로 문제를 시각화한다.
# 2. 입력값들로 부터 기초된 테이블의 크기
# 3. 디폴트 값들로 테이블 초기화
# 4. 테이블에서 작은 답을 심는다. ex) gridTraveler(1,1) = 1, {fib(0)=0, fib(1)=1}
# 5. 테이블을 반복해서 읽는다. -> 그러면서 다음을 디자인해야함.
# 6. 현재 위치에서 다음 포지션들을 채운다.

# canSum(goal, numbers) - 목표 값을 만들 수 있으면 True
# canSum(7, [5,3,4]) -> true
# canSum(7, [2,4]) -> false
# 이 문제의 목표는 결국 goal에 도달하는 것이고 dp의 관점에서는 현재 위치에서 이전의 값들을 재사용하는 것이기에
# 목표를 향해 증가하면서 포지션들을 유의미하게 채워나가야함.
# 목표 금액의 크기로 배열을 만들자. 어떤 데이터를 배열에 넣는 것이 맞을까?
# 여기서 요구하는 데이터 타입이 boolean 이기 때문에 boolean을 채워넣는것이 맞다.
# 그럼 초기화를 False로 채워넣고 시드값을 채워야하는데
# 테뷸레이션은 제일 작은 값에서 커져나가는 것이다. 제일 작은 값이 뭐가 될 수 있을까? 목표값이 1이라 생각하면 1이 되지 못하는 경우가 있을까?
# 있다. 그렇다면 목표값이 0이라면?? 무조건 True가 될 것이다. 그럼 시드값으로 0에 True를 채운다.
def canSum(goal, numbers):
    dp = [False]*(goal+1) # 시각화, 크기에 맞는 배열 생성 및 초기화 ( 1~3 )
    dp[0] = True # seed 값 ( 4 )
    for i in range(goal+1): # 반복해서 읽는다 ( 5 )
        if dp[i] == True:
            for index, n in enumerate(numbers): # ( 5 )
                if n + i <= goal: dp[n+i] = True # 다음 포지션 채우기 ( 6 )
    return dp[goal]

# howSum(goal, numbers) - 목표 값을 만드는게 가능하면 아무 조합이나 반환
# howSum(7, [2,3]) -> [3,2,2]
# 이 문제의 목표는 목표 값을 만드는 조합을 구하는 것이다.
# 위와 마찬가지로 목표 값의 크기에 맞는 배열을 만든다.
# 하지만 배열에 들어가는 초기값을 다를 것이다. 불린이 아니기 때문에.
# 반환되어야 하는 값이 리스트이기 때문에 None 값으로 초기화를 하자.
# 그럼 시드는?? 제일 작은 부분을 살펴보면 목표가 0인 경우일 것이고 그 경우 무조건 생성가능하기에 빈 리스트를 반환하면 된다.
def howSum(goal, numbers):
    dp = [None]*(goal + 1)# 초기화 및 배열 생성
    dp[0] = []# seed 값 삽입

    for i in range(goal + 1):
        if dp[i] != None:
            for index, n in enumerate(numbers):
                if n + i <= goal:
                    dp[n+i] = [*dp[i], n]
    return dp[goal]

# bestSum(goal, numbers) - 가장 짧은 조합 반환
# bestSum(8, [2, 3, 5]) -> [3, 5]
# 이 문제의 목표는 가장 짧은 조합을 반환하는 것이다.
# 위와 마찬가지로 목표의 크기로 배열을 생성하고 아직 해당 값에서 배열을 생성할 수 있을지를 모르기에 None으로 초기화한다.
# 그럼 시트는?? 조합을 반환해야 하기 때문에 dp[0]에 빈 리스트를 삽입하자.
# 반복하면서 None 인경우엔 빈 리스트에 해당 값을 삽입하여 넣고 None이 아니면 비교해서 더 길이가 짧은 경우에만 넣는다.
# 예를 들면 5는 [5]일 수도 있지만 [2,3]일 수도 있다. 그렇다면 [5]가 먼저 삽입될 것이다. 왜냐면 하나의 원소로도 만들 수 있기 때문이다.
# 그래서 더 짧은 경우에만 삽입한다.
def bestSum(goal, numbers):
    dp = [None]*(goal+1)# 초기화
    dp[0] = []# 시드

    for i in range(goal+1):
        if dp[i] != None:
            for index, n in enumerate(numbers):
                if n + i <= goal:
                    if dp[n+i] == None:
                        dp[n+i] = dp[i] + [n]
                    else:
                        dp[n+i] = dp[n+i] if len(dp[n+i]) <= len(dp[i]+[n]) else dp[i]+[n]
    return dp[goal]

# canConstruct(goal, wordBank) - wordBank에 있는 문자열로 goal 문자열을 만들수있는지?
# canConstruct(abcdef, [ab, abc, cd, def, abcd]) -> True
# 이 문제의 목표는 문자열을 만들 수 있는지 없는지의 decision problem이다.
# 먼저 배열의 크기를 설정해야한다. 크기는 goal의 길이의 크기만큼으로 설정하면 된다.
# 그 이유는 뭘까? 앞서서 재귀적으로 해당 문제를 풀었을때 접근했던 방법이 접두사를 이용해서 푸는 방법이었다.
# 즉, 스트링의 맨앞의 인덱스부터 차근차근 이동하면서 풀었던 것이다. 그렇기 때문에 여기서도 마찬가지로 접두사부터 끝까지 이동하는 것이다.
# 만약, a로 시작하는 접두사의 길이 다음 인덱스에 True를 표시할 수 있을 것이다. 그렇게 하다가 만약 길이의 마지막 인덱스에 True가 생기면 만들 수 있겠고
# 아닌 경우 만들 수 없는 경우이다. 즉, True가 들어간 값부터의 접두사를 찾아서 비교해나가 보자.
# 시드는 dp[0] = True 이다.
def camConstruct(goal, numbers):
    dp = [False]*(goal+1)
    dp[0] = True
    for i in range(len(goal)+1):
        if dp[i] == True:
            for n in numbers:
                if goal[i:i+len(n)] == n:
                    dp[i+len(n)] = True
    print(dp[len(goal)])

# countConstruct(goal, wordBank) - goal을 만들 수 있는 방법의 개수
# countConstruct(abcdef, [ab, abc, cd, def, abcd]) -> 1
# 이 문제의 목표는 방법의 개수를 찾는 것이다.
# 위와 마찬가지로 목표 문자열의 길이만큼 배열을 할당하고 여기서도 제일 작은 부분을 찾으면 '' 빈 문자열일 경우 1이다 어떤 배열이 들어오든 무조건 1개의 방법이 있다.
# 초기화를 dp[0] = 1로 설정, 나머지를 0으로 초기화한다. 방법의 개수를 찾기 때문이다.
def countConstruct(goal, wordBank):
    dp = [0]*(len(goal)+1)
    dp[0] = 1
    for i in range(len(goal)+1):
        for word in wordBank:
            if goal[i, i+len(word)] == word:
                dp[i+len(word)] += dp[i]
    print(dp[len(goal)])


# allConstruct(goal, wordBank) - goal을 만들 수 있는 방법의 조합
# allContruct(abcdef, [ab, abc, cd, def, abcd, ef, c]) -> [ [ab, cd, ef], [ab, c, def], [abc, def], [abcd, ef] ]
# 이 문제의 목표는 만들 수 있는 모든 방법의 조합을 반환하는 것이다.
# 앞에서 배웠듯이 모든 방법의 조합을 반환하기 위해서 2차원 리스트를 사용하는게 적합할 것 같다.
# 그리고 위와 마찬가지로 목표 문자열의 길이만큼의 크기로 dp 테이블을 만들고 ''인 경우가 [[]] 를 반환하고 나머지는 []로 초기화를 하면 좋을 것 같다.
# 그리고 돌아가면서 이전에 있던 리스트들에 전부 해당 문자열을 삽입하면서 만약 다음 칸에 리스트가 존재하면 하나로 합치는 작업을 거치면 될 것 같다.

def allConstruct4(goal, wordBank):
    dp = [[] for _ in range(len(goal)+1)]
    dp[0].append([])
    for i in range(len(goal)+1):
        for word in wordBank:
            if goal[i:i+len(word)] == word:
                temp = []
                for j in range(len(dp[i])): temp.append(dp[i][j]+[word])
                dp[i+len(word)] += temp
    print(dp[len(goal)])
allConstruct4('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c'])
allConstruct4('aaaaa', ['b'])

# 다이나믹 프로그래밍 생각할 부분
# 1. 잠시 시간을 내서 겹치는 부분을 생각하자 -> 어떤 겹치는 하위문제들이 있는지 확인하기
# 2. 가장 작은 입력이 뭔지를 생각하자 -> 작은 것으로부터 크게 만들어 가는 과정이니까 이걸 알아야 시작할 수 있다 ( seed 값을 위해서 )
# 3. 메모이제이션을 사용한 재귀, 테뷸레이션을 이용한 반복 둘 다 생각해보자.
# 4. 전략을 먼저 그리자 -> 자료구조 나 알고리즘을 어떻게 구현할지를 생각하기 위해선 프로세스를 그리면서 모든 에지 시나리오를 인식할 수 있다. ( 여기서 배울때 본것 처럼 )
