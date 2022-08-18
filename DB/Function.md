# 기본 함수와 연산

## 문자열 함수

- `SUBSTR(문자열, start, length)` : 문자열 자르기
  - 시작 인덱스는 1, 마지막 인덱스는 -1
- `TRIM(문자열)`, `LTRIM(문자열)`, `RTRIM(문자열)` : 문자열 공백 제거
- `LENGTH(문자열)` : 문자열 길이
- `REPLACE(문자열, 패턴, 변경값)` : 패턴에 일치하는 부분을 변경
- `UPPER(문자열)`, `LOWER(문자열)` : 대소문자 변경
- `||` : 문자열 합치기(concatenation)

<br/>

## 숫자 함수

- `ABS(숫자)` : 절댓값
- `SIGN(숫자)` : 부호 (양수 1, 음수 -1, 0 0)
- `MOD(숫자1, 숫자2)` : 숫자1을 숫자2로 나눈 나머지
- `CEIL(숫자)`, `FLOOR(숫자)`, `ROUND(숫자, 자리)` : 올림, 내림, 반올림
- `POWER(숫자1, 숫자2)` : 숫자1의 숫자2 제곱
- `SQRT(숫자)` : 제곱근

<br/>

## 산술 연산

- `+, -, *, /`와 같은 산술 연산자와 우선 순위를 지정하는 () 기호를 연산에 활용할 수 있음

<br/>

# GROUP BY

- "make a set of summary rows from a set of rows"
- SELECT 문의 optional 절
- 행 집합에서 요약 행 집합을 만듦
- 선택된 행 그룹을 하나 이상의 열 값으로 요약 행으로 만듦
- **문장에 WHERE 절이 포함된 경우 반드시 WHERE 절 뒤에 작성해야 함**
- 지정된 컬럼의 값이 같은 행들로 묶음
- **집계함수와 활용하였을 때 의미가 있음**
- 그룹화 된 각각의 그룹이 하나의 집합으로 집계함수의 인수로 넘겨짐

```sql
-- GROUP BY에 사용한 컬럼명도 같이 작성해주어야 함
-- GROUP BY에서 활용하는 컬럼을 제외하고는 집계함수를 씀
-- 정렬이 된 것처럼 보이지만 ORDER BY를 써야 함

-- users에서 각 성(last_name)씨가 몇 명씩 있는지 조회한다면?
SELECT last_name, COUNT(*)
FROM users
GROUP BY last_name;
```

<br/>

## HAVING

- 집계함수는 WHERE 절의 조건식에서는 사용할 수 없음(실행 순서에 의해)
  - WHERE로 처리하는 것이 GROUP BY 그룹화보다 순서상 앞에 있기 때문
- 집계 결과에서 조건에 맞는 값을 따로 활용하기 위해서 HAVING을 활용

```sql
-- 100번 이상 등장한 성을 출력
SELECT last_name, COUNT(last_name)
FROM users
GROUP BY last_name
HAVING COUNT(last_name) > 100;
```

<br/>

## SELECT 문장 실행 순서

```sql
SELECT 칼럼명
FROM 테이블명
WHERE 조건식
GROUP BY 칼럼 혹은 표현식
HAVING 그룹조건식
ORDER BY 칼럼 혹은 표현식
LIMIT 숫자 OFFSET 숫자;
```

- `FROM` => `WHERE` => `GROUP BY` => `HAVING` => `SELECT` => `ORDER BY`
  - `FROM` 테이블을 대상으로
  - `WHERE` 제약조건에 맞춰서 뽑아
  - `GROUP BY` 그룹화한 뒤
  - `HAVING` 그룹 중에서 조건에 맞는 것을
  - `SELECT` 조회하고
  - `ORDER BY` 정렬하여
  - `LIMIT / OFFSET` 특정 위치의 값을 가져온다

<br/>

# ALTER TABLE

1. 테이블 이름 변경

   ```sql
   ALTER TABLE table_name
   RENAME TO new_name;
   ```

2. 새로운 column 추가

   ```sql
   ALTER TABLE table_name
   ADD COLUMN column_definition;
   ```

3. column 이름 수정

   ```sql
   ALTER TABLE table_name
   RENAME COLUMN current_name TO new_name;
   ```

4. column 삭제

   ```sql
   ALTER TABLE table_name
   DROP COLUMN column_name;
   ```

<br/>

## 실습

```sql
-- title과 content라는 컬럼을 가진 articles라는 이름의 table 생성
CREATE TABLE articles (
	title TEXT NOT NULL,
    content TEXT NOT NULL
);

-- articles 테이블에 값 추가 (title은 '1번제목', content는 '1번내용')
INSERT INTO articles VALUES ('1번제목', '1번내용');

-- 방금 만든 테이블 이름 변경
ALTER TABLE articles RENAME TO news;

-- 새로운 컬럼 추가
ALTER TABLE news ADD COLUMN created_at TEXT NOT NULL;
-- 에러 발생
```

```sql
-- 에러 발생 이유
-- 테이블에 있던 기존 레코드들에는 새로 추가할 필드에 대한 정보가 없음
-- NOT NULL 형태의 컬럼 추가 불가능!

-- 에러 해결 방법
-- 1. NOT NULL 설정 없이 추가
ALTER TABLE news ADD COLUMN created_at TEXT;

-- 2. 기본 값(DEFAULT) 설정
ALTER TABLE news ADD COLUMN created_at TEXT NOT NULL DEFAULT '소제목';
```

