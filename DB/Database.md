# Database

> 데이터베이스는 체계화된 데이터의 모임
>
> 여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합
>
> 논리적으로 연관된 (하나 이상의) 자료의 모음으로 그 내용을 고도로 주고화 함으로써 검색과 갱신의 효율화를 꾀한 것
>
> 몇 개의 자료 파일을 조직적으로 통합하여 자료 항목의 중복을 없애고 자료를 구조화하여 기억시켜 놓은 자료의 집합체

<br/>

## 데이터베이스로 얻는 장점들

- 데이터 중복 최소화
- 데이터 무결성 (정확한 정보를 보장)
- 데이터 일관성
- 데이터 독립성 (물리적 / 논리적)
- 데이터 표준화
- 데이터 보안 유지

<br/>

## 관계형 데이터베이스 (RDB, Relational Database)

> 서로 관련된 데이터를 저장하고 접근할 수 있는 데이터베이스 유형
>
> 키(key)와 값(value)들의 간단한 관계(relation)를 표로

 | 용어                 | 정의                                                         |
 | -------------------- | ------------------------------------------------------------ |
 | 스키마 (Schema)      | 데이터베이스에서 자료의 구조, 표현방법, 관계 등 전반적인 명세를 기술한 것 |
 | 테이블 (Table)       | 열(컬럼/필드)과 행(레코드/값)의 모델을 사용해 조직된 데이터 요소들의 집합 |
 | 열 (Column)          | 각 열에 고유한 데이터 형식 지정                              |
 | 행 (Row)             | 실제 데이터가 저장되는 형태                                  |
 | 기본키 (Primary Key) | 각 행(레코드)의 고유값<br />반드시 설정해야 하며, 데이터베이스 관리 및 관계 설정 시 주요하게 활용됨 |

<br/>

# RDBMS

## 관계형 데이터베이스 관리 시스템 (RDBMS)

> 관계형 모델을 기반으로 하는 데이터베이스 관리 시스템을 의미

## 0 . SQLite

> 서버 형태가 아닌 파일 형식으로 응용 프로그램에 넣어서 사용하는 비교적 가벼운 데이터베이스
>
> 구글 안드로이드 운영체제에 기본적으로 탐재된 데이터베이스이며, 임베디드 소프트웨어에도 많이 활용됨
>
> 로컬에서 간단한 DB 구성을 할 수 있으며, 오픈 소스 프로젝트이기 때문에 자유롭게 사용 가능

<br/>

### 0.0. SQLite Data Type

1. NULL
2. INTEGER
   - 크기에 따라 0, 1, 2, 3, 4, 6 또는 8바이트에 저장된 부호 있는 정수
3. REAL
   - 8바이트 부동 소수점 숫자로 저장된 부동 소수점 값
4. TEXT
5. BLOB
   - 입력된 그대로 정확히 저정된 데이터 (별 다른 타입 없이 그대로 저장)

<br/>

### 0.1. Sqlite Type Affinity (1/2)

> 특정 컬럼에 저장하도록 권장하는 데이터 타입

1. INTEGER
2. TEXT
3. BLOB
4. REAL
5. NUMERIC

<br/>

# SQL (Structured Query Language)

> 관계형 데이터베이스 관리시스템의 데이터 관리를 위해 설계된 특수 목적으로 프로그래밍 언어
>
> 데이터베이스 스키마 생성 및 수정
>
> 자료의 검색 및 관리
>
> 데이터베이스 객체 접근 조정 관리

<br/>

| 분류                                                | 개념                                                         | 예시                            |
| --------------------------------------------------- | ------------------------------------------------------------ | ------------------------------- |
| DDL - 데이터 정의 언어 (Data Definition Language)   | 관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어 | CREATE, DROP, ALTER             |
| DML - 데이터 조작 언어 (Data Manipulation Language) | 데이터를 저장, 조회, 수정, 삭제 등을 하기 위한 명령어        | INSERT, SELECT, UPDATE, DELETE  |
| DCL - 데이터 제어 언어 (Data Control Language)      | 데이터베이스 사용자의 권한 제어를 위해 사용하는 명령어       | GRANT, REVOKE, COMMIT, ROLLBACK |

<br/>

## SQL Keywords - Data Manipulation Language

- INSERT : 새로운 데이터 삽입(추가)
- SELECT : 저장되어있는 데이터 조회
- UPDATE : 저장되어있는 데이터 갱신
- DELETE : 저장되어있는 데이터 삭제

<br/>

```sql
-- 데이터베이스 생성하기
.database

-- csv 파일을 table로 만들기
.mode csv
.import hellodb.csv examples
.tables

-- SELECT
SELECT * FROM examples;

-- (Optional) 터미널 view 변경하기
.headers on
.mode column
```



## 테이블 생성 및 삭제

- 테이블 생성 및 삭제 statement
  - CREATE TABLE
    - 데이터베이스에서 테이블 생성
  - DROP TABLE
    - 데이터베이스에서 테이블 제거

<br/>

```sql
-- classmates라는 이름의 테이블 생성
CREATE TABLE classmates (
    id INTEGER PRIMARY KEY,
    name TEXT
);

-- 테이블 목록 조회
.tables

-- 특정 테이블 스키마 조회
.schema classmates

-- 값 추가
INSERT INTO classmates VALUES (1, '조세호');

-- 테이블 조회
.headers on
.mode column
SELECT * FROM classmates;
SELECT rowid, * FROM classmates;
-- rowid는 SQLite에서 자동으로 제공하고 있는 PK. 값이 1씩 증가하며 자동으로 삽입됨

INSERT INTO classmates VALUES (2, '이동희');

-- 테이블 삭제
DROP TABLE classmates;
```

```sql
-- 예제
CREATE TABLE classmates (
    name TEXT,
    age INT,
    address TEXT
);
```

<br/>

### 필드 제약 조건

- NOT NULL : NULL 값 입력 금지
- UNIQUE : 중복 값 입력 금지 (NULL 값은 중복 입력 가능)
- PRIMARY KEY : 테이블에서 반드시 하나. NOT NULL + UNIQUE
- FOREIGN KEY : 외래키, 다른 테이블의 Key
- CHECK : 조건으로 설정된 값만 입력 허용
- DEFAULT : 기본 설정 값 

<br/>

# CRUD (Create, Read, Update, Delete)

## 0. CREATE

- INSERT

  - "insert a single row into a table"

  - 테이블에 단일 행 삽입

    `INSERT INTO 테이블_이름 (컬럼1, 컬럼2) VALUES (값1, 값2);`

  - 테이블에 정의된 모든 컬럼에 맞춰 순서대로 입력

    `INSERT INTO 테이블_이름 VALUES (값1, 값2, 값3);`

  - 여러 개의 데이터를 한번에 저장하기

    `INSERT INTO 테이블_이름 VALUES (값1-1, 값1-2, 값1-3), (값2-1, 값2-2, 값2-3), ... ;`

  - `rowid`는 SQLite에서 자동으로 제공하고 있는 PK. PK 값이 없는 경우 값이 1씩 증가하며 자동으로 삽입됨

<br/>

## 1. READ

- SELECT
  - "query data from a table"
  - 테이블에서 데이터를 조회
  - SELECT 문은 SQLite에서 가장 기본이 되는 문이며 다양한 절(clause)와 함께 사용
    - ORDER BY, DISTINCT, WHERE, LIMIT, GROUP BY ...

- LIMIT
  - "constrain the number of rows returned by a query"
  - 쿼리에서 반환되는 행 수를 제한
  - 특정 행부터 시작해서 조회하기 위해 `OFFSET` 키워드와 함께 사용하기도 함

- WHERE
  - "specify the search condition for rows returned by the query"
  - 쿼리에서 반환된 행에 대한 특정 검색 조건을 지정

- SELECT DISTINCT
  - "remove duplicate rows in the result set"
  - 조회 결과에서 중복 행을 제거
  - DISTINCT 절은 SELECT 키워드 바로 뒤에 작성해야 함


```sql
-- 하나의 컬럼 값을 조회
SELECT 컬럼1, 컬럼2, ... FROM 테이블이름 LIMIT 1;

-- 세 번째에 있는 하나의 컬럼 조회
SELECT 컬럼1, 컬럼2, ... FROM 테이블이름 LIMIT 1 OFFSET 2; 
```

- OFFSET
  - 처음부터 주어진 요소나 지점까지의 차이를 나타내는 정수형
  - 예시
    - 문자열 'abcdef'에서 문자 'c'는 시작점 'a'에서 2의 OFFSET을 지님
    - SELECT * FROM MY_TABLE LIMIT 10 OFFSET 5
      - "6번째 행부터 10개 행을 조회 (6번째 행부터 10개를 출력)"
      - 0부터 시작함

<br/>

## 2. UPDATE

- UPDATE

  ```sql
  UPDATE classmates SET address = '서울' WHERE rowid = 5;
  ```

<br/>

## 3. DELETE

- DELETE

  ```sql
  DELETE FROM classmates WHERE rowid = 5;
  ```

<br/>
