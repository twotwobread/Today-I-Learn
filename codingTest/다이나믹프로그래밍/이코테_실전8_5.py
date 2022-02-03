# file name : 이코테_실전8_5.py
# 효율적인 화폐 구성
# N가지 종류의 화폐가 있다. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려 한다.
# 이때 각 화폐는 몇 개라도 사용할 수 있고, 사용한 화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 구분한다.
# 불가능할 경우 -1을 출력한다.
# ex ) 15원을 만들기 위해서 2,3원만 사용한다. 3원을 5개 사용하는 것이 가장 최소한의 화폐 개수이다.
# 1 <= N <= 100, 1 <= M <= 10,000
# author : Lee Suyoung ( 2022-02-03 )
'''
그냥 이건 사실 생각할 것이 중복 생각도 필요없고 그냥 개수만 시아리면 된다.
dp table index 15에서 값를 보면 끝임.
'''

# N 입력 ( 화폐 가치 개수 ), M 입력 ( 화폐 가치 합 )
n, m = map(int, input().split())

# dp table 초기화
d = [0] * 10001

# array ( 화폐 가치들 입력 )
array = []
for i in range(n):
    temp = int(input())
    array.append(temp)
    d[temp] = 1
#print(d)
array.sort()
#print("array : ", array)
for i in range(array[0]+1, m+1): # 화폐 가치보다 더 큰 수부터 합계 값 까지 반복
    #print(str(i)+"에 대한 for loop 시작")
    #d[i] = d[i-array[0]] + 1
    for j in range(0, len(array)): # 모든 화폐 가치 for 문을 이용하기 위해
        #print("    화폐 가치 : "+str(array[j]))
        if d[i-array[j]] >= 1: # 화폐가치로 만들 수 있는 수라면
            if d[i] == 0:
                d[i] = d[i-array[j]] + 1 # 0인 경우 처음 온 인덱스라서 값을 넣음
                #print("        0인 경우 값을 넣음 : ", d[i])
            else: # 반복문을 통해 이전에 값을 넣은 경우
                #print("        0이 아닌 경우 : 원래 d값 = "+str(d[i])+ ", 비교하는 값 = "+str(d[i-array[j]]+1))
                d[i] = min(d[i], d[i-array[j]]+1)

if d[m] == 0:
    print("-1")
else:
    print(d[m])
#print(d)

### [ 제시된 답안 ] ###
# dp table을 10001로 초기화를 시킴으로써 
# for a
n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m+1)

d[0] = 0
for i in range(n): # 각 array에 있는 값마다 다 따로 반복문을 진행해주는 모습
    for j in range(array[i], m+1): # 각 화폐 가치마다 합계까지 반복문을 실행한다.
        # 나는 화폐가치 배열을 정렬해서 가장 작은 값부터 합계까지 돌리면서 그 안에서 각각 화폐가치 배열의 포문을 다시 돌렸는데
        # 그렇게 하면 일단 정렬에서 시간을 좀 잡아먹고 최대 10000 * 100 = 1,000,000 번의 반복문이 실행되고
        # 이렇게 하면 100 * 10000 으로 같다. 그런데 정렬이 없어서 이 방법이 훨씬 간결하다.
        if d[j - array[i]] != 10001: # 그리고 10001으로 초기화를 함으로써 min을 쓰기가 굉장히 쉬워졌다.
            # 나는 0으로 초기화를 해서 0인 경우를 따로 넣어줬다. 그리고 화폐 가치로 들어간 애들은 따로 1의 값을 넣어주는 불편한 상황이 나온다.
            # 만약 10001로 했다면 그런 상황이 연출되지 않았을 것이다. 그냥 for문 돌려도 0,1 이상,10001 전부 구별이 되기 때문이다.
            # 근데 나의 코드는 0으로 초기화해서 d[0] 과 초기화된 값들이 구분되지 않는다.
            d[j] = min(d[j], d[j-array[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
