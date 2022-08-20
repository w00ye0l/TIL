# CASE

> 특정 상황에서 데이터를 변환하여 활용할 수 있음
>
> ELSE를 생략하는 경우 NULL 값이 지정됨

```sql
CASE
	WHEN 조건식 THEN 식
	WHEN 조건식 THEN 식
	ELSE 식
END

-- 예제: gender 1이면 남자, gender가 2면 여자
SELECT
    id,
    CASE
        WHEN gender = 1 THEN "남자"
        WHEN gender = 2 THEN "여자"
    END AS 성별
FROM users;

-- 예제: 나이에 따라서 구분
SELECT
    last_name,
    first_name
    age,
    CASE
        WHEN age <= 18 THEN "청소년"
        WHEN age <= 40 THEN "청년"
        WHEN age <= 90 THEN "중장년"
        ELSE "노년"
    END
FROM users;
```

<br/>

# 서브쿼리

> 특정한 값을 메인 쿼리에 반환하여 활용하는 것
>
> 실제 테이블에 없는 기준을 이용한 검색이 가능함
>
> 서브 쿼리는 소괄호로 감싸서 사용하며, 메인 쿼리의 칼럼을 모두 사용할 수 있음
>
> 메인 쿼리는 서브 쿼리의 칼럼을 이용할 수 없음

<br/>

- ## 단일행 서브쿼리

  - 서브쿼리의 결과가 0 또는 1개인 경우
  - 단일행 비교 연산자와 함께 사용(=, <, <=, >, >=, <>)

  ```sql
  -- 가장 나이가 작은 사람의 수
  SELECT
      age,
      COUNT(*)
  FROM users
  GROUP BY age
  ORDER BY age
  LIMIT 1;
  
  SELECT COUNT(*)
  FROM users
  WHERE age = (
      SELECT MIN(age)
      FROM users
  );
  
  -- 평균 계좌 잔고가 높은 사람 수
  SELECT
      balance,
      COUNT(*)
  FROM users
  WHERE balance > (
      SELECT AVG(balance)
      FROM users
  );
  
  -- 유은정과 같은 지역에 사는 사람의 수
  SELECT COUNT(*)
  FROM users
  WHERE country = (
      SELECT country
      FROM users
      WHERE
          last_name = "유" AND
          first_name = "은정"
  );
  
  -- 전체 인원과 평균 연봉, 평균 나이
  SELECT
      COUNT(*),
      AVG(balance),
      AVG(age)
  FROM users;
  
  SELECT
      (SELECT COUNT(*) FROM users) AS 총인원,
      (SELECT AVG(balance) FROM users) AS 평균연봉
      (SELECT AVG(age) FROM users) AS 평균나이;
      
  -- UPDATE에서 활용
  UPDATE users
  SET balance = (SELECT AVG(balance) FROM users);
  ```

<br/>

- ## 다중행 서브쿼리

  - 서브쿼리 결과가 2개 이상인 경우
  - 다중행 비교 연산자와 함께 사용(IN, EXISTS 등)

  ```sql
  -- 이름이 이은정인 사람과 같은 지역에 사는 사람 수
  SELECT COUNT(*)
  FROM users
  WHERE country IN (
      SELECT country
      FROM users
      WHERE 
          last_name = "이" AND
          first_name = "은정"
  );
  ```

<br/>

- ## 다중컬럼 서브쿼리

  ```sql
  -- 특정 성씨에서 가장 어린 사람들의 이름과 나이
  SELECT
      last_name AS 성,
      first_name AS 이름,
      age
  FROM users
  WHERE (last_name, age) IN (
      SELECT
          last_name,
      	MIN(age)
      FROM users
      GROUP BY last_name
  )
  ORDER BY last_name;
  ```

  

