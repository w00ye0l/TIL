# SQLite Aggregate Functions

## Aggregate Functions (집계함수)

> 값 집합에 대한 계산을 수행하고 단일 값을 반환
>
> 여러 행으로부터 하나의 결과값을 반환하는 함수
>
> SELECT 구문에서만 사용됨

<br/>

| 함수명 | 의미                                  |
| ------ | ------------------------------------- |
| COUNT  | 그룹의 항목 수를 가져옴               |
| AVG    | 모든 값의 평균을 계산                 |
| MAX    | 그룹에 있는 모든 값의 최댓값을 가져옴 |
| MIN    | 그룹에 있는 모든 값의 최솟값을 가져옴 |
| SUM    | 모든 값의 합을 계산                   |

<br/>

```sql
-- 이씨 중에 가장 작은 나이
SELECT MIN(age), first_name FROM users WHERE last_name = '이';
```

<br/>

# LIKE

- "query data based on pattern matching"
- 패턴 일치를 기반으로 데이터를 조회하는 방법
- SQLite는 패턴 구성을 위한 2개의 wild cards를 제공
  - `%` (percent sign)
    - 0개 이상의 문자
  - `_` (underscore)
    - 임의의 단일 문자

<br/>

## wildcards

- wildcards 사용 예시

| 와일드카드 패턴 | 의미                           |
| --------------- | ------------------------------ |
| `2%`            | 2로 시작하는 값                |
| `%2`            | 2로 끝나는 값                  |
| `%2%`           | 2가 들어가는 값                |
| `_2%`           | 두 번째가 2로 시작하는 값      |
| `1___`          | 1로 시작하고 총 4자리인 값     |
| `2_%_`, `2__%`  | 2로 시작하고 적어도 3자리인 값 |

<br/>

```sql
-- 중간 핸드폰 번호가 '5114'인 사람의 수
SELECT COUNT(*) FROM users WHERE phone LIKE '%-5114-%';
```

<br/>

# ORDER BY

- "sort a result set of a query"
- 조회 결과 집합을 정렬
- SELECT 문에 추가하여 사용
- 정렬 순서를 위한 2개의 keyword 제공
  - `ASC` - 오름차순 (default)
  - `DESC` - 내림차순

```sql
-- 계좌 잔액을 내림차순으로 정렬, 성을 오름차순으로 정렬, 10개 뽑기
SELECT last_name, first_name, balance FROM users ORDER BY balance DESC, last_name ASC LIMIT 10;
```

