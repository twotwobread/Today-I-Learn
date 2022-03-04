# 파이썬 문법 공부하기
- [lambda 함수](###lambda-함수(익명함수))
- [map 함수](###map-함수)
- [filter 함수](###filter-함수)
- [reduce 함수](###reduce-함수)  
- [zip 함수](###zip-함수)
- [join 함수](###join-함수)  

---
### lambda 함수(익명함수)
> 함수를 한 줄만으로 만들게 해줌.( 이름이 없는 함수를 만들 수 있음. )  
> 람다함수의 장점은 코드의 간결함, 메모리의 절약  
- lambda 매개변수 : 결과
- 함수를 만들 때, 매개변수를 매개변수 자리에 넣고 return 부분은 결과자리에 넣음.
```python
def plus(x, y):
  return x+y
  
 # 10 + 20
 (lambda x,y: x+y)(10,20)
 # target을 앞뒤 불필요한 공백을 제외한 문자열 길이 오름차순으로 정렬
 sorted(target, key=lambda x: len(x.strip()))
```
  
### map 함수
> 람다 함수의 장점은 map 함수와 함께 사용될 때 볼 수 있음.  
> map은 두개의 인수를 가지는 함수.
- r = map(function, iterable, ...)
- function : 함수의 이름, iterable : 한 번에 하나의 멤버를 반환할 수 있는 객체
- list, str, tuple -> function은 iterable의 모든 요소에 대해 적용.
- function에 의해 변경된 iterator를 반환.
```python
a = [1,2,3,4]
b = [17,12,11,10]
list(map(lambda x, y:x+y, a,b) 
# [18, 14, 14, 14]
```  

### filter 함수
> filter도 두 개의 인자를 가짐.
- r = filter(function, iterable)
- 인자로 사용되는 function은 처리되는 각각의 요에 대해 Boolean 값을 반환.
- True를 반환하면 그 요소는 남고 False를 반환하면 그 요소는 제거.
```python
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
list(filter(lambda x: (x%3) == 0, foo)) 
# [18, 9, 24, 12, 27]
```  

### reduce 함수
> reduce는 두 개의 필수 인자와 하나의 옵션 인자를 가지는데, function을 사용해서 iterable을 하나의 값으로 줄임.  
> initializer는 주어지면 첫 번째 인자로 추가 된다고 생각하면 됨.
- functools.reduce(function, iterable[, initializer])
- reduce(function, [1,2,3,4,5])에서 reduce(function, [function(1,2), 3, 4, 5])로 하나의 요소가 줄고 요소가 하나 남을 때까지 이를 반복함.
  
### map(), filter()는 내장 함수 | reduce()는 X
---

### zip 함수
> 여러 개의 순회 가능한(iterable) 객체를 인자로 받고, 각 객체가 담고 있는 원소를 튜플 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환.
- zip(*iterables)
```python
num = [1,2,3]
fruit = ["apple", "banana", "orange"]
color = ["red", "yellow", "orange"]

zip_list = zip(num, fruit, color)
print(zip_list, type(zip_list))
# <zip object at 0x0000020180766048> <class 'zip'> -> zip 타입으로 출력됨.

print(list(zip_list)) # list 타입으로 변환
# [(1, 'apple', 'red'), (2, 'banana', 'yellow'), (3, 'orange', 'orange')]
```
  
### join 함수
> 리스트를 문자열로 일정하게 합쳐주는 함수.
- '구분자'.join(리스트)
```python
a = ['a', 'b', 'c', 'd', '1', '2', '3']

list = "".join(a)
print(list)
# abcd123

list2 = "_".join(a)
print(list2)
# a_b_c_d_1_2_3
```


