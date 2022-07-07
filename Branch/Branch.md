# Branch, GitHub Flow



## 협업을 위한 과정

- **Working directory** [->`add`] **Staging Area** [->`commit`] **Local Repository** [-> `push`, <- `pull`] **GitHub**



## Git Flow

> Git을 활용하여 협업하는 흐름으로 branch를 활용하는 전략을 의미



## Branch Merge

> 각 branch에서 작업을 한 후 이력(커밋)을 합치기 위해서 일반적으로 `merge` 명령어를 사용



## Branch 명령어

- `$ git branch`
  - 현재 branch 조회
- `$ git branch example`
  - branch 생성
- `$ git checkout example`
  - branch 이동
- `$ git merge example`
  - master에서 작성하며 example과 병합
- `$ git branch -d example`
  - branch 삭제
  - branch를 삭제해도 merge를 했다면 commit은 지워지지 않음
  - merge 했다면 대부분 branch는 삭제함



## 상황 예시 (조장 1, 조원 1)

### 상황 1. 혼자 작업 (Fast-foward)

1. feature/home branch 생성 및 이동

   ```bash
   (master) $ git branch feature/home
   (master) $ git checkout feature/home
   ```

2. branch 이동 후 commit

   ```bash
   (feature/home) $ touch home.txt
   (feature/home) $ git add.
   (feature/home) $ git commit -m 'Add home.txt'
   ```

3. master branch로 이동

   ```bash
   (feature/home) $ git checkout master
   (master) $ git log --oneline
   ```

4. master branch에 병합

   ```bash
   (master) $ git merge feature/home
   (master) $ git log --oneline
   ```

5. feature/home branch 삭제

   ```bash
   (master) $ git branch -d feature/home
   ```



### 상황 2. 보고서 파일 + 발표 자료 파일 (각자 커밋이 발생했는데, 다른 파일만 수정된 경우)

1. feature/about branch 생성 및 이동

   ```bash
   (master) $ git checkout -b feature/about
   (feature/about)
   ```

2. branch 이동 후 commit

   ```bash
   (feature/about) $ touch about.txt
   (feature/about) $ git add.
   (feature/about) $ git commit -m 'Add about.txt'
   ```

3. master 이동

   ```bash
   (feature/about) $ git checkout master
   (master)
   ```

4. 혼자 테스트하기 때문에 master에서 commit 하나 더 만들기

   ```bash
   (master) $ touch master.txt
   (master) $ git add.
   (master) $ git commit -m 'Add master.txt'
   ```

5. master branch에서 병합

   ```bash
   (master) $ git merge feature/about
   (master) $ git log --oneline
   ```

6. 결과 -> 자동으로 **merge commit** 발생

   > 같은 파일을 수정하지 않았기 때문에 commit이 자동으로 merge 됨

7. commit 및 그래프 확인하기

   ```bash
   (master) $ git log --oneline --graph
   ```

8. branch 삭제

   ```bash
   (master) $ git branch -d feature/about
   ```



### 상황 3. 진정한 협업 (각자 커밋이 있는데, 같은 파일이 수정됨)

1. feature/test branch 생성 및 이동

   ```bash
   (master) $ git checkout -b feature/test
   ```

2. 작업 완료 후 commit

   ```bash
   # README.md 파일 열어서 수정
   (feature/test) $ touch test.txt
   (feature/test) $ git add .
   (feature/test) $ git commit -m 'Add test.txt'
   ```

3. master 이동

   ```bash
   (feature/test) $ git checkout master
   (master)
   ```

4. master에 추가 commit 발생시키기

   - ***동일 파일 수정!!!***

   ```bash
   # README.md 파일 열어서 수정
   (master) $ git add README.md
   (master) $ git commit -m 'Update README.md'
   ```

5. master에 병합

   ```bash
   (master) $ git merge feature/test
   ```

6. 결과 -> **merge conflict** 발생

   > 충돌이 발생한 파일(동일 파일)을 직접 병합(수정)한 후 add, commit

   ```bash
   <<<<<<<< HEAD
   # 마스터에서 작업
   ========
   # 테스트에서 작업
   >>>>>>>> feature/test
   
   (master|MERGING) $ git status
   ```

7. 충돌 확인 및 해결

   ```bash
   (master|MERGING) $ git add README.me
   (master|MERGING) $ git commit
   ```

8. 커밋 및 확인하기

   ```bash
   (master) $ git log --oneline --graph
   ```

9. branch 삭제

   ```bash
   (master) $ git branch -d feature/test
   ```

   

## Branch 활용

### 1. Feature Branch Workflow

> 소유권이 있는 저장소

1. 나의 저장소에서 branch 생성 후 이동
2. `add`, `commit`한 후 `push`
3. GitHub에서 `Compare & pull request` 클릭
4. merge 방향 확인 후 `Create pull request`
5. `Merge pull request` 클릭 후 병합



### 2. Fork & Pull Request

> 소유권이 없는 저장소

1. Fork할 저장소에서 `Fork`를 클릭
2. 자신의 원격 저장소에 `Repository` 이름을 설정
3. 나의 원격 저장소에서 코드를 복사
4. `$ git clone 'url'`을 작성
5. branch 생성 후 `add`, `commit`
6. GitHub에서 `Compare & pull request` 클릭
7. merge 방향 확인 후 `Create pull request`
8. 소유권이 있는 사람이 `Merge pull request`를 클릭해주면 병합이 됨



## Git 심화

1. 원치 않는 파일이 Add 되었을 때 되돌리는 방법

   ```bash
   $ git restore --stage <파일명>
   ```

   

2. 파일 내용이 원치 않게 수정, 삭제 되었을 때 복구하기

   ```bash
   $ git restore <파일명>
   ```



## 최종 흐름

1. 로컬 저장소에서 `git push origin <branch 명>`
2. GitHub에서 `Pull & request` 후 `merge`
3. `git pull origin master`
4. 다시 `git checkout -b <branch 명>`
