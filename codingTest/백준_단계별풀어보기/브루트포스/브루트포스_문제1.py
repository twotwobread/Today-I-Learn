# file name : 부루트포스_문제1.py
# 게임 블랙잭의 규칙은 카드의 합이 21을 넘지 않는 한도 내에서, 카드이 합을 최대한 크게 만드는 게임
# 김정인 버전의 블랙잭에서 각 카드에는 양의 정수가 쓰여 있다. 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다.
# 그런 후에 딜러는 숫자 M을 크게 외친다. 이제 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다.
# 블랙잭 변형 게임이기에 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.
# N장의 카드에 써져있는 숫자가 주어졌을때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력해라
# 3 <= N <= 100, 10<=M<=300,000
# 카드에 쓰여 있는 수 <= 100,000, 양의 정수
# 합이 M을 넘지 않는 카드 3장이 존재하는 경우만 주어짐.
# author : Lee Suyoung(2022-02-13)

# 순서 상관없이 합을 생각해야 하니까 조합을 생각하면 될꺼 같고 그럼 100 C 3을 생각해야하는데 이거 ㅈㄴ 클텐데
# 100*100*100 정도일듯 하지만 괜찮음.

from itertools import combinations
#import sys
#input = sys.stdin.readline

# n, m 입력
n, m = map(int, input().split())
# n장의 카드 정보
card = [0] * n
array = list(map(int, input().split()))
card = array
# 그중 3장 뽑기 1,000,000 최대 이정도 시간이 걸릴듯
_card = list(combinations(card, 3))
result = 0
for c in _card:
    cardSum = sum(c)
    if cardSum <= m and cardSum > result:
        result = cardSum
print(result)
