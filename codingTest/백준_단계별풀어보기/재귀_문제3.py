# file name: 재귀_문제3.py
# 2447번 별찍기 - 10
# 재귀적인 패턴으로 별을 찍어보자. N이 3의 거듭제곱(3,9,27 ,,,,)이라할때, 크기 N의 패턴은 NxN 정사각형 모양이다.
# 크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.
# N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)x(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다.
# N = 3의 거듭제곱 = 3^k, 1<=k<=8
# author: Lee Suyoung(2022-02-12)

# n 입력 ( 패턴의 크기 )

# 패턴 크기에 따라 별찍기.
def drawStar(n):
    if n == 1:
        return ["*"]
    
    star = drawStar(n//3)
    
    star_list = []
    for s in star:
        star_list.append(s*3)
    for s in star:
        star_list.append(s+" "*(n//3)+s)
    for s in star:
        star_list.append(s*3)
    return star_list

n = int(input())
print("\n".join(drawStar(n))) # "\n"으로 원소들 합치기
            
