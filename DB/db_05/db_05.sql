-- SQLite
-- 1. playlist_track 테이블에 `A`라는 별칭을 부여하고 데이터를 출력하세요.
SELECT *
FROM playlist_track AS A
ORDER BY PlaylistId DESC
LIMIT 5;

-- 2. tracks 테이블에 `B`라는 별칭을 부여하고 데이터를 출력하세요.
SELECT *
FROM tracks AS B
ORDER BY TrackId ASC
LIMIT 5;

-- 3. 각 playlist_track 해당하는 track 데이터를 함께 출력하세요.
SELECT 
    P.PlaylistId,
    T.Name
FROM playlist_track AS P INNER JOIN tracks AS T
    ON P.TrackId = T.TrackId
ORDER BY P.PlaylistId DESC
LIMIT 10;

-- 4. `PlaylistId`가 `10`인 track 데이터를 함께 출력하세요. 
SELECT
    P.PlaylistId,
    T.Name
FROM playlist_track AS P INNER JOIN tracks AS T
    ON P.TrackId = T.TrackId
WHERE P.PlaylistId = 10
ORDER BY T.Name DESC
LIMIT 5;

-- 5. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `INNER JOIN`해서 데이터를 출력하세요.
SELECT COUNT(*)
FROM tracks AS T INNER JOIN artists AS A
    ON T.Composer = A.Name;

-- 6. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `LEFT JOIN`해서 데이터를 출력하세요.
SELECT COUNT(*)
FROM tracks AS T LEFT OUTER JOIN artists AS A
    ON T.Composer = A.Name;

-- 7. `INNER JOIN` 과 `LEFT JOIN` 행의 개수가 다른 이유를 작성하세요.
INNER JOIN의 경우 테이블의 값들 중 NULL 값이 있는 레코드들이 조회되지 않음
LEFT JOIN의 경우 테이블1을 기준으로 NULL 값이 있는 레코드들도 함께 조회됨

-- 8. invoice_items 테이블의 데이터를 출력하세요.
SELECT
    InvoiceLineId,
    InvoiceId
FROM invoice_items
ORDER BY InvoiceId ASC
LIMIT 5;

-- 9. invoices 테이블의 데이터를 출력하세요.
SELECT
    InvoiceId,
    CustomerId
FROM invoices
ORDER BY InvoiceId ASC
LIMIT 5;

-- 10. 각 invoices_item에 해당하는 invoice 데이터를 함께 출력하세요.
SELECT
    invoice_items.InvoiceLineId,
    invoices.InvoiceId
FROM invoice_items INNER JOIN invoices
    ON invoice_items.InvoiceId = invoices.InvoiceId
ORDER BY invoices.InvoiceId DESC
LIMIT 5;

-- 11. 각 invoice에 해당하는 customer 데이터를 함께 출력하세요.
SELECT
    I.InvoiceId,
    C.CustomerId
FROM invoices AS I INNER JOIN customers AS C
    ON I.CustomerId = C.CustomerId
ORDER BY I.InvoiceId DESC
LIMIT 5;

-- 12. 각 invoices_item(상품)을 포함하는 invoice(송장)와 해당 invoice를 받을 customer(고객) 데이터를 모두 함께 출력하세요.
SELECT
    II.InvoiceLineId,
    I.InvoiceId,
    C.CustomerId
FROM invoices AS I
    INNER JOIN invoice_items AS II
        ON I.InvoiceId = II.InvoiceId
    INNER JOIN customers AS C
        ON I.CustomerId = C.CustomerId
ORDER BY I.InvoiceId DESC
LIMIT 5;

-- 13. 각 customer가 주문한 invoices_item의 개수를 출력하세요.
SELECT
    C.CustomerId,
    COUNT(*) AS "개수"
FROM invoice_items AS II 
    INNER JOIN invoices AS I
        ON II.InvoiceId = I.InvoiceId
    INNER JOIN customers AS C
        ON I.CustomerId = C.CustomerId
GROUP BY C.CustomerId
ORDER BY C.CustomerId ASC
LIMIT 5;

--
SELECT
    CC.CustomerId,
    COUNT(*) AS "개수"
FROM invoice_items AS II
    INNER JOIN (
        SELECT *
        FROM invoices AS I INNER JOIN customers AS C
            ON I.CustomerId = C.CustomerId
    ) AS CC
        ON II.InvoiceId = CC.InvoiceId
GROUP BY CC.CustomerId
ORDER BY CC.CustomerId ASC;

-- 14. 각 customer가 주문한 invoices의 개수, CustomerId 기준 내림차순, 5개
SELECT 
    CustomerId,
    COUNT(*) AS "개수"
FROM invoices
GROUP BY CustomerId
ORDER BY CustomerId DESC
LIMIT 5;

-- 15. 각 Artist가 낸 tracks의 수, 트랙 수 기준 내림차순, 10개
SELECT
    A.ArtistId,
    A.Name,
    COUNT(*) AS "트랙 수"
FROM artists AS A 
    INNER JOIN albums AS B
        ON A.ArtistId = B.ArtistId
    INNER JOIN tracks AS C
        ON B.AlbumId = C.AlbumId
GROUP BY A.ArtistId
ORDER BY "트랙 수" DESC
LIMIT 10;

--
SELECT
    A.ArtistId,
    A.Name,
    COUNT(*) AS "트랙 수"
FROM artists AS A
    INNER JOIN (
        SELECT *
        FROM albums AS B INNER JOIN tracks AS C
            ON B.AlbumId = C.AlbumId
    ) AS D
        ON A.ArtistId = D.ArtistId
GROUP BY A.ArtistId
ORDER BY "트랙 수" DESC
LIMIT 10;