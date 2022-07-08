# GitHub



## GitHub란

> GitHub는 원격 저장소로 로컬 저장소에서 한 작업을 네트워크 환경에 저장하는 곳
>
> Git과 함께 분산 버전 관리 시스템



## 원격 저장소(Remote Repository) 기본 흐름

1. **로컬 저장소의 버전(커밋)을 원격 저장소로 보냄**
2. **원격 저장소의 버전(커밋)을 로컬 저장소로 가져옴**



### 0. GitHub에서 원격 저장소 생성

- `New Repository`를 클릭 후 저장소를 만듦
- 저장소 이름, 저장소 설명, 공개 여부를 선택한 후 생성
- 생성된 저장소의 코드에서 `url`과 `git 명령어`를 확인
  - ex) `https://github.com/w00ye0l/TIL.git`
  - ex) `git remote add origin https://github.com/w00ye0l/TIL.git`



### 1. 원격 저장소의 경로를 설정

- 원격 저장소 정보를 로컬 저장소에 추가
- 로컬 저장소에는 한번만 설정
  - `$ git remote add origin https://github.com/w00ye0l/TIL.git`
- 원격 저장소의 정보를 확인하는 코드
  - `$ git remote -v`



### 2. 원격 저장소 활용 명령어

1. `Push`
   - `$ git push <원격 저장소 이름> <브랜치 이름>` 명령어 작성
     - ex) `$ git push origin master`
     - 원격 저장소로 로컬 저장소 변경 사항(커밋)을 올림(push)
     - 로컬 폴더의 파일/폴더가 아닌 저장소의 **버전(커밋)이 올라감**
2. `Pull`
   - `$ git pull <원격 저장소 이름> <브랜치 이름>` 명령어 작성
     - ex) `$ git pull origin master`
     - 원격 저장소로부터 변경된 내역을 받아와서 이력을 병합함
3. `Clone`
   - `$ git clone <원격 저장소 주소>`
     - ex) `$ git clone https://github.com/w00ye0l/TIL.git`
     - 원격 저장소를 복제해 모든 버전을 가져옴
     - 원격 저장소 이름의 폴더로 이동해서 활용

- Clone과 Pull의 차이점
  - Clone : 원격 저장소 복제
  - Pull : 원격 저장소 커밋 가져오기



## Git 파일 관리 심화

### 1. 버전 관리와 상관 없는 파일 관리

- 일반적인 개발 프로젝트에서 버전 관리를 별도로 하지 않는 파일/디렉토리가 발생
- Git 저장소에 `.gitignore` 파일을 생성하고 관리
  - **이름을 바꿀 수 없음**


```bash
$ mkdir .gitignore
$ git add .
$ git commit -m "ADD .gitignore"
```



- 작성 예시
  - 특정 파일 : `a.txt` (모든 a.txt), `test/a.txt` (테스트 폴더의 a.txt)
  - 특정 디렉토리 : `/my_secret`
  - 특정 확장자 : `*.exe`
  - 예외 처리 : `!b.exe`
- **주의! 이미 커밋된 파일은 반드시 삭제를 해야 .gitignore로 적용됨**
  - **미리 제외 파일을 설정해두자**



- 일반적으로 제외하는 파일
  - 개발 언어 ([https://github.com/github/gitignore](https://github.com/github/gitignore))
    - ex) 파이썬 : `venv/`, 자바스크립트 : `node_modules/`
  - 개발 환경
    - 운영체제 (windows, mac, linux)
    - 텍스트 에디터 / IDE (visual studio code 등)



## 2. 빈 폴더 관리하는 방법

- `.gitkeep`을 사용하여 빈 폴더를 관리
  - **이름을 바꿀 수 있음**

```bash
$ mkdir 디렉토리명/.gitkeep 
$ git add .
$ git commit -m "ADD empty directory"
```

