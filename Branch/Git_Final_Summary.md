# 주요 전체 흐름



## 0. 폴더를 만들기

- 폴더를 `vs code`로 연 뒤 경로를 확인하여 `(master)`가 붙어있는지 확인한다.



## 1. git 저장소로 버전 관리 시작

- `git init` 코드를 작성하여 저장소로 만든다.



## 2. 파일을 생성

- `1.txt`, `2.txt`, `3.txt` 등 여러 파일을 생성한다.
  - `$ touch 1.txt 2.txt 3.txt`



## 3. 파일을 커밋

- `1.txt`, `2.txt` 를 1차로 커밋하고
  - `$ git add 1.txt 2.txt`
  - `$ git commit -m 'First'`
- `3.txt`를 2차로 커밋하면
  - `$ git add 3.txt`
  - `$ git commit -m 'Second'`
- 각각의 커밋 메시지로 버전을 관리하게 된다.



## 4. 원격 저장소 경로 설정

- `$ git remote add origin https://github.com/w00ye0l/TIL.git`
  - `origin`이란 저장소를 만든다.
  - **처음 한번만 설정!!!!**
- `$ git push origin master`
  - `origin`이란 저장소의 변경 사항을 올린다.
- `$ git pull origin master`
  - `origin`이란 저장소에 원격 저장소의 변경 사항을 받아온다.
- `$ git clone https://github.com/w00ye0l/TIL.git`
  - 원격 저장소의 버전을 복제해온다.
  - `$ git pull origin master`로 새로운 버전을 받아온다.



## 주요 문제

### 0. Commit

- 파일 수정, 삭제 등을 한 후 `commit`하면 이전 버전에서도 확인 가능하다.



### 1. 이미지 경로

- 파일이 옮겨지거나 이름이 수정되었을 때 경로를 **꼭 수정해야 한다.**



### 2. Clone 주의

- 원격 저장소 이름의 폴더가 생성된다.