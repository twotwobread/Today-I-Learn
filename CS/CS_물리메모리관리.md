# 01 메모리 관리의 개요
## 1 메모리 관리의 복잡성
- 메모리의 구조는 1B로 나뉘고 각 영역은 메모리 주소로 구분하는데 보통 0번지부터 시작.
- CPU는 메모리에 있는 내용을 가져오거나 작업 결과를 메모리에 저정하기 위해 MAR(Memory Address Register)를 사용.
  + MAR에 필요한 메모리 주소를 넣으면 데이터를 메모리에서 가져오거나 메모리에 데이터를 옮길 수 있음.
- 오늘날의 시분할 시스템은 OS를 포함한 모든 응용 프로그램이 메모리에 올라와 실행되어 메모리 관리가 복잡.
- 여러 작업을 동시에 처리할 때 메모리 관리( 복잡한 메모리 관리 )는 메모리 관리 시스템 (Memory Management System, MMS)가 담당.
## 2 메모리 관리의 이중성
- 프로세스 입장에서는 메모리를 독차지하려 하고, 메모리 관리자 입장에서는 되도록 관리를 효율적으로 하고 싶어 하는 것.
- 프로세스 입장에서 작업의 편리함과 관리자 입장에서 관리의 편리함이 충돌을 일으키는 것.
- 현대의 MMS는 프로세스와 메모리 관리자의 상충되는 요구 사항을 완벽하게 처리.
## 3 소스코드의 번역과 실행
### 3.1 컴파일러와 인터프린터의 동작
- 컴파일러 : 소스코드를 컴퓨터가 실행할 수 있는 기계어로 번역 후 한꺼번에 실행. ( C언어, 자바 등 )
- 인터프리터 : 소스코드를 한 행씩 번역하여 실행. ( 자바스크립트, 파이썬, 베이직 등 )
### 3.2 컴파일러의 목적
- 오류 발견
  + 컴파일러는 오류를 찾기 위해 심벌 테이블을 사용.
    - 심벌 테이블 : 변수 선언부에 명시한 각 변수의 이름과 종류를 모아놓은 테이블
  + 선언하지 않은 변수 사용, 변수에 다른 종류의 데이터 저장과 같은 오류를 잡음.
- 코드 최적화
  + 군더더기와 사용하지 않는 변수를 삭제하여 코드를 최적화시킴.
### 3.3 컴파일러와 인터프리터의 차이
- 컴파일러와 다르게 인터프리터는 한 줄씩 실행.
- 같은 일을 반복하는 경우나 필요 없는 변수를 확인 불가
- 따라서 크고 복잡한 프로그램 : 컴파일러, 간단한 프로그램 : 인터프리터 를 사용.
### 3.4 컴파일 과정
- 컴파일 : 소스코드를 목적 코드로 변환 후 라이브러리를 연결하고 최종 실행 파일을 만들어 실행하는 과정.
1. 소스코드 작성 및 컴파일
  - 컴파일 시 목적 코드 생성 -> 목적코드 : 사용자가 작성한 소스코드를 컴파일러로 일차로 번역한 코드.
2. 목적 코드와 라이브러리 연결
  - 목적 코드가 만들어지면 라이브러리에 있는 코드를 목적 코드에 삽입하여 최종 실행 파일 생성.
3. 동적 라이브러리를 포함하여 최종 실행
  - 동적 라이브러리 파일 : Dynamic Link Loader ( DLL )
  - 윈도우에서 함수의 변경이 일어난 경우, 해당 DLL 파일을 구하여 특정 폴더에 삽입하면 새로운 기능을 사용 가능.
## 4 메모리 관리자의 역할
- 메모리 관리자 : Memory Manage Unit, MMU
- 가져오기 작업
  + 프로세스와 데이터를 메모리로 가져오는 작업.
  + 사용자가 요청한 프로세스와 데이터를 메모리로 가져오는데 너무 큰 경우 일부만 가져오는 경우, 사용자의 요청없이도 필요할 것이라 예상되는 데이터를 가져오는 경우도 있음.
- 배치 작업
  + 가져온 프로세스와 데이터를 메모리의 어떤 부분에 올려놓을지 결정하는 작업.
  + 배치 작업 전 메모리를 어떤 크기로 자를 것인지가 매우 중요. -> 같은 크기로 자를 지 실행되는 프로세스의 크기에 맞게 자를지에 따라 메모리 관리의 복잡성이 달라짐.
  + 나누어진 메모리의 구역에 따라 프로세스와 데이터를 배치하는 것
- 재배치 작업
  + 꽉 차 있는 메모리에 새로운 프로세스를 가져오기 위해 오래된 프로세스를 내보내는 작업.
- 가져오기 정책
  + 프로세스가 필요로 하는 데이터를 언제 메모리로 가져올지 결정하는 정책.
  + 미리 가져오는 prefetch도 있음.
- 배치 정책
  + 가져온 프로세스를 메모리의 어떤 위치에 올려놓을지 결정하는 정책
  + 페이징(paging) : 메모리를 같은 크기로 자르는 것, 세그멘테이션(segmentation) : 프로세스의 크기에 맞게 자르는 것.
  + 이 두 방식의 장단점을 파악하여 메모리를 효율적으로 관리할 수 있도록 정책을 만드는 것.
- 재배치 정책
  + 메모리가 꽉 찼을 때 메모리 내에 있는 어떤 프로세스를 내보낼지 결정하는 정책.
  + 교체 알고리즘 : 앞으로 사용하지 않을 프로세스를 찾아서 내보내는 알고리즘.
