# JOIN

> 관계형 데이터베이스의 가장 큰 장점이자 핵심적인 기능
>
> 일반적으로 데이터베이스에는 하나의 테이블에 많은 데이터를 저장하는 것이 아니라 여러 테이블로 나눠 저장하게 되며, 여러 테이블을 결합(join)하여 출력하여 활용
>
> 일반적으로 레코드는 **기본키(PK)**나 **외래키(FK)** 값의 관계에 의해 결합함

<br/>

## 대표적인 JOIN

- **INNER JOIN** : 두 테이블에 모두 일치하는 행만 반환 `(A ∩ B)`

  ```sql
  SELECT *
  FROM 테이블1 [INNER] JOIN 테이블2
  	ON 테이블1.칼럼 = 테이블2.칼럼;
  	
  -- staff(2) 사용자(users)를 역할과 함께 출력
  SELECT *
  FROM users INNER JOIN role
  	on users.role_id = role.id
  WHERE role.id = 2;
  
  -- 이름을 내림차순 정렬
  SELECT *
  FROM users INNER JOIN role
  	on users.role_id = role.id
  ORDER BY users.name DESC;
  ```

<br/>

- **OUTER JOIN** : 동일한 값이 없는 행도 반환

  - **LEFT OUTER JOIN** : `A -B`
  - **RIGHT OUTER JOIN** : `B - A`
  - **FULL OUTER JOIN** : `A ∪ B`

  ```sql
  SELECT *
  FROM 테이블1 [LEFT|RIGHT|FULL] OUTER JOIN 테이블2
  	ON 테이블1.칼럼 = 테이블2.칼럼;
  	
  -- 
  SELECT *
  FROM articles LEFT OUTER JOIN users
  	ON articles.user_id = users.id;
  ```

<br/>

- **CROSS JOIN** : 모든 데이터의 조합 `(A * B)`

  ```sql
  SELECT *
  FROM 테이블1 CROSS JOIN 테이블2;
  ```

