# git 기초
<img src="https://user-images.githubusercontent.com/78334910/148049038-27ffd178-55bd-4961-ac96-4c567a821ffa.PNG">
< git의 구조 >

<img src="https://user-images.githubusercontent.com/78334910/148048787-4db25212-2a55-4aaf-9ce9-d85cb35a01ab.PNG">
__git init__ 를 이용해서 원하는 디렉토리에 .git 파일을 생성하면서 로컬 저장소로 지정한다.

<img src="https://user-images.githubusercontent.com/78334910/148049546-81c5c028-e93b-43d4-9243-d1330e5c6a61.PNG">
__git status__ 를 통해서 로컬 저장소의 현재 상태를 확인한다.
만약에 빨간색으로 파일목록이 표현되면 그것은 Untracked files이다. 
- Untracked files : 준비 영역이나 로컬 저장소에 한번이라도 add되거나 commit되지 않은 파일을 말한다.

<img src="https://user-images.githubusercontent.com/78334910/148049935-1a21ea97-f4ec-4b13-9472-fba0648ce9a5.PNG">
__git clone <복사한주소> <원하는디렉토리명>__
원하는 디렉토리를 만들고 여기에 코드 내용을 다운 받는다.

<img src="https://user-images.githubusercontent.com/78334910/148052793-e0263ff1-1808-480f-b9ea-3e1564ea603a.PNG">
__git log__ 를 통해 log를 볼 수 있다. 작성자, 일시, 수행한 내용 등을 볼 수 있다.

<img src="https://user-images.githubusercontent.com/78334910/148050388-ce686633-2239-420f-a389-d1078e967cef.PNG">
__git commit <"option"> "메세지"__  
- m : vim에서 별도의 메세지를 작성할 필요없이 인라인 형식으로 바로 커밋 메세지 작성  
- a : 별도의 add 명령어를 사용하지 않고 수정된 파일에 대해 add, commit을 한번에 수행 (단, Untracked file일 경우 add를 따로 해줘야함)
- git add를 하면 작업 공간의 파일들을 준비 영역에 추가한다.
- git commit은 로컬 저장소에 최종 저장하는 단계이다.
- 이후 __git push origin <branch명>__ 를 통해서 로컬 저장소의 파일들을 원격 저장소로 올린다.
  - origin을 확인하는 방법은 __git remote -v__ 하면 어디로 연결되어 있는지를 볼 수 있음
  <img src="https://user-images.githubusercontent.com/78334910/148051174-b363539f-0f1b-4b96-9e7e-fe88a4076c3a.PNG">
  - 위 사진처럼 맨 앞에 떠있는게 원격 저장소와 연결시에 아래 사진과 같이 내가 이름을 적어주는 것
  <img src="https://user-images.githubusercontent.com/78334910/148051434-7c1142d2-2bdc-4bb7-9668-0f76ac58450f.PNG">
- __git pull origin <branch 명>__ 을 하면 브랜치에 있는 걸 그대로 끌어오는 merge를 하면서 끌어온다.

<img src="https://user-images.githubusercontent.com/78334910/148051766-c0e58735-fca6-41d6-bfb9-a719e5d7e6cd.PNG">
- __git branch <branch 명>__ 를 통해 branch를 만들어 주고 __git checkout <branch 명>__ 을 통해 현재 접속한 branch를 바꿔줄 수 있다. (branch를 만들 때 master일 경우에만 가능하다. 잘 확인해서 해줘야한다.)

<img src="https://user-images.githubusercontent.com/78334910/148052003-225f9ff1-2fec-4eb8-8c99-692f3f4f5778.PNG">
- __git branch__ 를 하면 현재 접속중인 브랜치와 모든 브랜치가 뜬다.

<img src="https://user-images.githubusercontent.com/78334910/148052435-836200e2-a7f4-4d2b-8739-5bad6582650e.PNG">
- 해당 오류가 떴던 이유는 처음 만들고 원격 저장소에 대한 기본 브랜치 설정을 안해줬기 때문이다. 브랜치를 만들고 설정을 안해줘서 그렇다.






