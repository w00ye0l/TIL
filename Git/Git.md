# Git



## Git이란

> Git은 분산 버전 관리 시스템으로 코드의 버전을 관리하는 도구

- **분산버전관리시스템(DVCS)**
  - **중앙집중식버전관리시스템**은 중앙에서 버전을 관리하고 파일을 받아서 사용
  - **분산버전관리시스템**은 원격 저장소(remote repository)를 통하여 협업하고, 모든 히스토리를 클라이언트들이 공유

- 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율



## Git 주요 명령어

- `pwd` : 현재 디렉토리 출력

- `cd` (change directory) 디렉토리이름 : 디렉토리 이동
  - . : 현재 디렉토리, .. : 상위 디렉토리

- `ls` (list) : 목록

- `mkdir` (make directory) : 디렉토리 생성

- `touch` : 파일 생성

- `rm` (remove) 파일명: 파일 삭제하기

- `rm –r` 폴더명, `rmdir` 폴더명 : 폴더 삭제하기



## Git의 기본 흐름

- **Git은 파일을 `modified`, `staged`, `committed`로 관리**
  - modified : 파일이 수정된 상태 (add 명령어를 통하여 staging area로)
  - staged : 수정한 파일을 곧 커밋할 것이라고 표시한 상태 (commit 명령어로 저장소)
  - committed : 커밋이 된 상태


1. **작업하고**
2. **add하여 staging area에 모아**
3. **commit으로 버전 기록**



- Working Directory (`untracked`) => explorer에서 파일명 옆에 `U`로 표시됨
  - 파일의 변경사항
- Staging Area (`staged`) => explorer에서 파일명 옆에 `A`로 표시됨
  - 버전으로 기록하기 위한 파일 변경사항의 목록
- Repository (`committed`)
  - 커밋(버전)들이 기록되는 곳



### 0. Git 저장소 만들기

- `$ git init` 명령어 작성
  - 저장소 처음 만들 때
  - git bash에서 `(master)` 표기 확인



### 1. working directory 상의 변경 내용을 staging area에 추가하기 위해 사용

- `$ git add <파일명>`
  - `$ git status`로 체크



### 2. staged 상태의 파일들을 커밋을 통해 버전으로 기록

- `$ git commit -m '<커밋메시지>'`
  - `$ git log`로 체크
    - `$ git log -1` : 가장 최근의 커밋 하나를 보여줌
    - `$ git log --oneline` : 커밋된 로그들을 한 줄로 보여줌
    - `$ git log -2 --oneline` : 최근 두 개의 로그를 한 줄씩 보여줌

