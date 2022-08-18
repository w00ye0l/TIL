-- SQLite
-- 1. 흡연 여부(smoking)로 구분한 각 그룹의 컬렴명과 그룹의 사람의 수를 출력하시오.
SELECT 
    smoking,
    COUNT(*) AS 사람수
FROM healthcare
WHERE smoking != ""
GROUP BY smoking;

-- 2. 음주 여부(is_drinking)로 구분한 각 그룹의 컬럼명과 그룹의 사람의 수를 출력하시오.
SELECT
    is_drinking,
    COUNT(*) AS 사람수
FROM healthcare
WHERE is_drinking != ""
GROUP BY is_drinking;

-- 3. 음주 여부로 구분한 각 그룹에서 혈압(blood_pressure)이 200이상인 사람의 수를 출력하시오.
SELECT
    is_drinking,
    COUNT(*) AS 사람수
FROM healthcare
WHERE blood_pressure >= 200
GROUP BY is_drinking;

-- 4. 시도(sido)에 사는 사람의 수가 50000명 이상인 시도의 코드와 그 시도에 사는 사람의 수를 출력하시오.
SELECT
    sido,
    COUNT(*) AS 사람수
FROM healthcare
GROUP BY sido
HAVING 사람수 >= 50000;

-- 5. 키(height)를 기준으로 구분하고, 각 키와 사람의 수를 출력하시오.
SELECT
    height,
    COUNT(*) AS 사람수
FROM healthcare
GROUP BY height
ORDER BY 사람수 DESC
LIMIT 5;

-- 6. 키(height)와 몸무게(weight)를 기준으로 구분하고, 몸무게와, 키, 해당 그룹의 사람의 수를 출력하시오. 
SELECT
    weight,
    height,
    COUNT(*) AS 사람수
FROM healthcare
GROUP BY height, weight
ORDER BY 사람수 DESC
LIMIT 5;

-- 7. 음주여부에 따라 평균 허리둘레(waist)와 사람의 수를 출력하시오.
SELECT 
    is_drinking,
    AVG(waist) AS "평균 허리둘레",
    COUNT(*) AS 사람수
FROM healthcare
WHERE is_drinking != ""
GROUP BY is_drinking;

-- 8. 각 성별(gender)의 평균 왼쪽 시력(va_left)과 평균 오른쪽 시력(va_right)를 출력하시오.
SELECT
    gender,
    ROUND(AVG(va_left), 2) AS "평균 왼쪽 시력",
    ROUND(AVG(va_right), 2) AS "평균 오른쪽 시력"
FROM healthcare
GROUP BY gender;

-- 9. 각 나이대(age)의 평균 키와 평균 몸무게를 출력하시오.
SELECT
    age,
    AVG(height) AS "평균 키",
    AVG(weight) AS "평균 몸무게"
FROM healthcare
GROUP BY age
HAVING "평균 키" >= 160 AND "평균 몸무게" >= 60;

-- 10. 음주 여부(is_drinking)와 흡연 여부(smoking)에 따른 평균 BMI를 출력하시오.
SELECT
    is_drinking AS "음주 여부",
    smoking AS "흡연 여부",
    AVG(weight*10000/(height*height)) AS "평균 BMI"
FROM healthcare
WHERE is_drinking != "" AND smoking != ""
GROUP BY is_drinking, smoking;