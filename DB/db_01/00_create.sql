-- 테이블 만들기
CREATE TABLE healthcare (
id PRIMARY KEY,
sido INTEGER NOT NULL,
gender INTEGER NOT NULL,
age INTEGER NOT NULL,
height INTEGER NOT NULL,
weight INTEGER NOT NULL,
waist REAL NOT NULL,
va_left REAL NOT NULL,
va_right REAL NOT NULL,
blood_pressure INTEGER NOT NULL,
smoking INTEGER NOT NULL,
is_drinking BOOLEAN NOT NULL
);

-- csv import 하기
.mode csv 
.import health.csv healthcare

-- SQLite
-- 1. 추가되어 있는 모든 데이터의 수를 출력하시오.
SELECT COUNT(*) FROM healthcare;

-- 2. 나이 그룹이 10(age)미만인 사람의 수를 출력하시오.
SELECT COUNT(*) FROM healthcare WHERE age < 10;

-- 3. 성별이 1인 사람의 수를 출력하시오.
SELECT COUNT(*) FROM healthcare WHERE gender = 1;

-- 4. 흡연 수치(smoking)가 3이면서 음주(is_drinking)가 1인 사람의 수를 출력하시오.
SELECT COUNT(*) FROM healthcare WHERE smoking = 3 AND is_drinking = 1;

-- 5. 양쪽 시력이(va_left, va_right) 모두 2.0이상인 사람의 수를 출력하시오.
SELECT COUNT(*) FROM healthcare WHERE va_left >= 2.0 and va_right >= 2.0;

-- 6. 시도(sido)를 모두 중복 없이 출력하시오.
SELECT DISTINCT sido FROM healthcare;

-- 
SELECT COUNT(*) FROM healthcare WHERE is_drinking = 1 AND height >= 170;