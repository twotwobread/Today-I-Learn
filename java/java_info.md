## 자바의 태동
- 원래 임베디드에 올릴려고 만들어짐 -> 확장성을 좋게 만들어서 프로세서가 달라져도 동작할 수 있게 하기 위해 만들어짐 ( 플랫폼 독립적인 언어가 필요 )
  + ABI ( application binary interface ) = 프로그램이 만들어진 cpu와 os에 따라서 호환이 되는지 안되는지에 대한 이유.
  + CPU마다 기계어가 다르고 os마다 실행파일 형식이 다르고 api가 달라서 프로그램의 플랫폼 호환성이 없다. ( 플랫폼 = 하드웨어 + os )
- but 현재는 임베디드에 쓰이지 않음. ( 내가 추정할땐 가상머신을 만들어 이 위에서 프로그램이 실행되기에 무겁고 느려서 해당 언어를 쓰지않는다고 추정 )
- 자바가 나옴으로써 동적인 웹을 만들 수 있었음. 자바가 인기가 많아진 이유가 웹브라우저에서 실행 가능해서 웹의 발전과 함께 확산되었음.
- 자바(draw.java)는 소스코드에서 컴파일러를 거치면 바이트 코드(draw.class)가 되고 이 바이트 코드가 실행될때 해당 클래스와 바인딩되어 실행됨.
  + 바이트코드는 가상의 cpu에 맞는 중립적인 코드이다.
  + JVM은 플랫폼 종속적이고 실행전 미리 설치해야함.
- 링크 과정 없이 컴파일러가 바로 바이트 코드 생성을 하고 이것은 JVM에서만 실행 가능하고 필요한 클래스들을 프로그램 실행 중에 동적으로 로딩

## 소스 파일과 클래스
- 하나의 소스 파일에 여러 클래스 코드 작성 가능. 단, public 클래스는 파일당 최대 하나 소스파일 이름과 같아야함.

## 배열에 대해서
- c는 무조건 배열이 사각형이지만 자바는 비정방형이 있다.
- 그래서 배열을 생성하는 구문이 필요하다.
```java
int intArray[][]; // 2차원 배열을 선언하는 부분
int[][] intArray = new int[2][5]; // 2차원 배열을 생성한다. ( 2행에 5열의 크기로 생성한다. , 즉 얘는 정방형!!)
//c랑 그럼 같은가? 완전같지는 않다 그이유는 행안의 인덱스들은 주소가 연속되지만 다른 행간의 주소는 연속될 수도 있고 아닐 수도 있기 때문이다.

int[][] intArray = new int[4][]; // 이렇게도 배열을 만들수있다. 배열의 시작주소를 가르치는 레퍼런스를 만들었다.
intArray[0] = new int[0]; // 비정방형으로 만들기 위해선 각 행을 가르치는 레퍼런스도 필요하기 때문에 생성을 해주는 부분이다.
intArray[1] = new int[1];
intArray[2] = new int[2];
intArray[3] = new int[3];
```
- 같은 타입의 데이터들을 순차적으로 저장하고 연속된 메모리 공간에 할당된다.
- 배열의 인덱스가 0부터 시작하는 이유는 성능때문이다.
  + 시작주소를 만들땐 (인덱스의 시작 주소) + 0 * (바이트수)를 이용을 하는데 만약 첫 인덱스를 1로 만든다면
  + (인덱스의 시작 주소) + (1-1) * (바이트수)를 이용하여 주소를 만들게 된다. 이 경우 모든 인덱스에 접근할때마다 '빼기'라는 연산을 추가로 수행해야한다.
  + 그렇게 되면 성능이 저하될 수 밖에 없기 때문에 0부터 인덱스를 시작한다.