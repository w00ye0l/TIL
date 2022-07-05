# Git 실습

## 0. 사전 설정 (PC 최초 한번)

```bash
$ git config --global user.name 'GitHub ID'
$ git config --global user.email 'GitHub Email'
```



## 1. 바탕화면에 TIL 폴더를 만든다.

- TIL 폴더를 열어서 마크다운 정리 파일을 옮긴다.
- VS Code를 연다.



## 2. TIL 폴더에 git 저장소를 만들어준다.

```bash
$ git init
Initialized empty Git repository in C:/Users/dnduf/Desktop/TIL/.git/
```

```bash
$ git add .
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   markdown_practice.assets/LWY.jpg
        new file:   markdown_practice.md
```



## 3. 커밋을 만든다.

```bash
$ git commit -m '마크다운 정리'
[master (root-commit) 6f43289] 마크다운 정리        
 2 files changed, 129 insertions(+)
 create mode 100644 markdown_practice.assets/LWY.jpg
 create mode 100644 markdown_practice.md
 
$ git log
commit 6f432896736c99def3bde99a75fbe2a331b1fc13 (HEAD -> master)
Author: lwy <dnduf158@gmail.com>
Date:   Tue Jul 5 16:18:46 2022 +0900

    마크다운 정리
    
$ git log -1
commit 6f432896736c99def3bde99a75fbe2a331b1fc13 (HEAD -> master)
Author: lwy <dnduf158@gmail.com>
Date:   Tue Jul 5 16:18:46 2022 +0900

    마크다운 정리

$ git log -1 --oneline
6f43289 (HEAD -> master) 마크다운 정리

$ git log --oneline
6f43289 (HEAD -> master) 마크다운 정리
```



## 4. 실습 정리

```bash
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        "Git \354\213\244\354\212\265.md"

nothing added to commit but untracked files present (use "git add" to 
track)
```

```bash
$ git add Git\ 실습.md 

$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)  
        new file:   "Git \354\213\244\354\212\265.md"
```

```bash
$ git commit -m 'Git 실습 정리'
[master d997b90] Git 실습 정리   
 1 file changed, 70 insertions(+)
 create mode 100644 "Git \354\213\244\354\212\265.md"
 
$ git log -1
commit d997b907317850683e9751a1c2817a2bbd1ebdcc (HEAD -> master)
Author: lwy <dnduf158@gmail.com>
Date:   Tue Jul 5 16:33:21 2022 +0900

    Git 실습 정리
```

```bash
$ git status
On branch master
nothing to commit, working tree clean
```

