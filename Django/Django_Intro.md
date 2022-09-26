# Django 시작하기

## Framework 이해하기

- **누군가 만들어 놓은 코드를 재사용하는 것**은 이미 익숙한 개발 문화
- 웹 서비스도 누군가 개발해놓은 코드를 재사용한다면 쉽게 사용 가능
- 많은 개발자들이 수 없이 많이 개발을 해놓았기 때문에 자주 사용되는 부분을 재사용 가능하게 만들어둠
- 재사용 가능하도록 모아놓은 것을 **프레임워크(Framework)**라고 함

- `Frame(뼈대, 틀) + Work(일하다)`
  - 일정한 뼈대, 틀을 가지고 일하다
  - 제공받은 도구들과 뼈대, 규약을 가지고 무언가를 만드는 일
  - 특정 프로그램을 개발하기 위한 여러 도구들과 규약을 제공하는 것
- **"소프트웨어 프레임워크"**는 복잡한 문제를 해결하거나 서술하는데 사용되는 기본 개념 구조

- Framework를 잘 사용하면 웹 서비스 전체를 하나부터 열까지 직접 개발할 필요 없이, 원하는 로직에 집중해 개발을 할 수 있음 (소프트웨어의 생산성과 품질을 높임)

<br/>

## Django를 배워야 하는 이유

- Python으로 작성된 프레임워크
  - Python이라는 언어의 강력함과 거대한 커뮤니티
- 수많은 여러 유용한 기능들

<br/>

# 가상 환경 생성 / 실행

```bash
$ pwd
# 현재 경로 확인
# /C/Users/[User Name]

$ cd ~
# 현재 위치 Home으로 이동
# /C/Users/[User Name]

$ mkdir server
# 폴더 생성 (server라는 폴더)

$ cd server/
# 현재 위치 server 폴더로 이동

$ pip list
# 설치된 패키지 리스트 확인

$ python --version
# python 버전 확인
# Python 3.9.13

$ python -m venv server-venv
# python -m venv [가상 환경 이름] : 폴더 뒤에 -venv를 붙이는 방식을 주로 사용

$ source server-venv/Scripts/activate
# 가상 환경 실행

$ deactivate
# 가상 환경 실행 종료
```



<br/>

# Django 설치 / 실행

```bash
$ pip install django==3.2.13
# django 3.2.13 버전 설치
# django 4.0 릴리즈로 인해 3.2(LTS) 버전을 명시해 설치

$ pip --version
# pip 버전 확인

$ pip freeze > requirements.txt
# 패키지 목록 txt 파일 생성

$ django-admin startproject firstpjt .
# 프로젝스 생성
## Project 이름에는 Python이나 Django에서 사용 중인 키워드 및 '-'(하이픈) 사용 불가
## '.'(dot)을 붙이지 않을 경우 현재 디렉토리에 프로젝트 디렉토리를 새로 생성하게 됨

$ python manage.py runserver
# 서버 실행
```

<br/>

- [참고] `LTS`
  - Long Term Support (장기 지원 버전)
  - 일반적인 경우보다 장기간에 걸쳐 지원하도록 고안된 소프트웨어의 버전
  - 컴퓨터 소프트웨어의 제품 수명 주기 관리 정책
  - 배포자는 LTS 확정을 통해 장기적이고 안정적인 지원을 보장함

- 설치 후 `localhost:8000` 혹은 `127.0.0.1:8000`을 웹 브라우저에 입력 후 메인 페이지 확인