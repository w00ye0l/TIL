### 1. playlist_track 테이블에 `A`라는 별칭을 부여하고 데이터를 출력하세요.
| 단, 모든 컬럼을 `PlaylistId` 기준으로 내림차순으로 5개만 출력하세요.

```sql
SELECT *
FROM playlist_track AS A
ORDER BY PlaylistId DESC
LIMIT 5;
```

```
PlaylistId  TrackId
----------  -------
18          597
17          3290
17          2096
17          2095
17          2094
```

### 2. tracks 테이블에 `B`라는 별칭을 부여하고 데이터를 출력하세요.
| 단, 모든 컬럼을 `TrackId` 기준으로 오름차순으로 5개만 출력하세요.

```sql
SELECT *
FROM tracks AS B
ORDER BY TrackId ASC
LIMIT 5;
```

```
TrackId  Name                                     AlbumId  MediaTypeId  GenreId  
Composer                                                      Milliseconds  Bytes     UnitPrice
-------  ---------------------------------------  -------  -----------  -------  
------------------------------------------------------------  ------------  --------  ---------
1        For Those About To Rock (We Salute You)  1        1            1        
Angus Young, Malcolm Young, Brian Johnson                     343719        11170334  0.99

2        Balls to the Wall                        2        2            1        
                                                              342562        5510424   0.99

3        Fast As a Shark                          3        2            1        
F. Baltes, S. Kaufman, U. Dirkscneider & W. Hoffman           230619        3990994   0.99

4        Restless and Wild                        3        2            1        
F. Baltes, R.A. Smith-Diesel, S. Kaufman, U. Dirkscneider &   252051        4331779   0.99

W. Hoffman


5        Princess of the Dawn                     3        2            1        
Deaffy & R.A. Smith-Diesel                                    375418        6290521   0.99
```

### 3. 각 playlist_track 해당하는 track 데이터를 함께 출력하세요.
| 단, PlaylistId, Name 컬럼을 `PlaylistId` 기준으로 내림차순으로 10개만 출력하세요. 
```sql
SELECT 
    P.PlaylistId,
    T.Name
FROM playlist_track AS P INNER JOIN tracks AS T
    ON P.TrackId = T.TrackId
ORDER BY P.PlaylistId DESC
LIMIT 10;
```

```
PlaylistId  Name
----------  -----------------------
18          Now's The Time
17          The Zoo
17          Flying High Again
17          Crazy Train
17          I Don't Know
17          Looks That Kill
17          Live To Win
17          Ace Of Spades
17          Creeping Death
17          For Whom The Bell Tolls
```

### 4. `PlaylistId`가 `10`인 track 데이터를 함께 출력하세요. 
| 단, PlaylistId, Name 컬럼을 `Name` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT
    P.PlaylistId,
    T.Name
FROM playlist_track AS P INNER JOIN tracks AS T
    ON P.TrackId = T.TrackId
WHERE P.PlaylistId = 10
ORDER BY T.Name DESC
LIMIT 5;
```

```
PlaylistId  Name
----------  ------------------------
10          Women's Appreciation
10          White Rabbit
10          Whatever the Case May Be
10          What Kate Did
10          War of the Gods, Pt. 2
```

### 5. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `INNER JOIN`해서 데이터를 출력하세요.
| 단, 행의 개수만 출력하세요.
```sql
SELECT COUNT(*)
FROM tracks AS T INNER JOIN artists AS A
    ON T.Composer = A.Name;
```

```
COUNT(*)
--------
402
```

### 6. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `LEFT JOIN`해서 데이터를 출력하세요.
| 단, 행의 개수만 출력하세요.
```sql
SELECT COUNT(*)
FROM tracks AS T LEFT OUTER JOIN artists AS A
    ON T.Composer = A.Name;
```

```
COUNT(*)
--------
3503
```

### 7. `INNER JOIN` 과 `LEFT JOIN` 행의 개수가 다른 이유를 작성하세요.
```plain
INNER JOIN의 경우 테이블의 값들 중 NULL 값이 있는 레코드들이 조회되지 않음
LEFT JOIN의 경우 테이블1을 기준으로 NULL 값이 있는 레코드들도 함께 조회됨
```

### 8. invoice_items 테이블의 데이터를 출력하세요.
| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.

```sql
SELECT
    InvoiceLineId,
    InvoiceId
FROM invoice_items
ORDER BY InvoiceId ASC
LIMIT 5;
```

```
InvoiceLineId  InvoiceId
-------------  ---------
1              1
2              1
3              2
4              2
5              2
```

### 9. invoices 테이블의 데이터를 출력하세요.
| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT
    InvoiceId,
    CustomerId
FROM invoices
ORDER BY InvoiceId ASC
LIMIT 5;
```

```
InvoiceId  CustomerId
---------  ----------
1          2
2          4
3          8
4          14
5          23
```

### 10. 각 invoices_item에 해당하는 invoice 데이터를 함께 출력하세요.
| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT
    invoice_items.InvoiceLineId,
    invoices.InvoiceId
FROM invoice_items INNER JOIN invoices
    ON invoice_items.InvoiceId = invoices.InvoiceId
ORDER BY invoices.InvoiceId DESC
LIMIT 5;
```

```
InvoiceLineId  InvoiceId
-------------  ---------
2240           412
2226           411
2227           411
2228           411
2229           411
```


### 11. 각 invoice에 해당하는 customer 데이터를 함께 출력하세요.
| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT
    I.InvoiceId,
    C.CustomerId
FROM invoices AS I INNER JOIN customers AS C
    ON I.CustomerId = C.CustomerId
ORDER BY I.InvoiceId DESC
LIMIT 5;
```

```
InvoiceId  CustomerId
---------  ----------
412        58
411        44
410        35
409        29
408        25
```

### 12. 각 invoices_item(상품)을 포함하는 invoice(송장)와 해당 invoice를 받을 customer(고객) 데이터를 모두 함께 출력하세요.
| 단, InvoiceLineId, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
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
```

```
InvoiceLineId  InvoiceId  CustomerId
-------------  ---------  ----------
2240           412        58
2226           411        44
2227           411        44
2228           411        44
2229           411        44
```

### 13. 각 customer가 주문한 invoice_items의 개수를 출력하세요.
| 단, CustomerId와 개수 컬럼을 `CustomerId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
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
```

```
CustomerId  개수
----------  --
1           38
2           38
3           38
4           38
5           38
```

### 14. 각 customer가 주문한 invoices의 개수, CustomerId 기준 내림차순, 5개

```sql
SELECT 
    CustomerId,
    COUNT(*) AS "개수"
FROM invoices
GROUP BY CustomerId
ORDER BY CustomerId DESC
LIMIT 5;
```

```
CustomerId  개수
----------  --
59          6
58          7
57          7
56          7
55          7
```

### 15. 각 Artist가 낸 tracks의 수, 트랙 수 기준 내림차순, 10개

```sql
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
```

```
ArtistId  Name             트랙 수
--------  ---------------  ----
90        Iron Maiden      213
150       U2               135
22        Led Zeppelin     114
50        Metallica        112
58        Deep Purple      92
149       Lost             92
118       Pearl Jam        67
100       Lenny Kravitz    57
21        Various Artists  56
156       The Office       53
```





