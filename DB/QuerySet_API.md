# QuerySet API

- ## gt

    ```python
    Entry.objects.filter(id__gt=4)
    # ex) add(a = 1, b = 2)처럼 키워드 호출, filter(id > 4)라는 함수 호출은 없음!
    ```

    ```sql
    SELECT ... WHERE id > 4;
    ```

- ## gte

    ```python
    Entry.objects.filter(id__gte=4)
    ```

    ```sql
    SELECT ... WHERE id >= 4;
    ```

- ## It

    ```python
    Entry.objects.filter(id__lt=4)
    ```

    ```sql
    SELECT ... WHERE id < 4;
    ```

- ## lte

    ```python
    Entry.objects.filter(id__lte=4)
    ```
    
    ```sql
    SELECT ... WHERE id <= 4;
    ```
    
- ## in

    ```python
    Entry.objects.filter(id__in = [1, 3, 4])
    Entry.objects.filter(headline__in = 'abc')
    ```

    ```sql
    SELECT ... WHERE id IN (1, 3, 4);
    SELECT ... WHERE headline IN ('a', 'b', 'c';)
    ```

- ## startswith

  ```python
  Entry.objects.filter(headline__startswith = 'Lennon')
  ```

  ```sql
  SELECT ... WHERE headline LIKE 'Lennon%';
  ```

- ## istartswith 

  > insensitive, 대소문자 구분 (X)

  ```python
  Entry.objects.filter(headline__istartswith = 'Lennon')
  ```

  ```sql
  SELECT ... WHERE headline ILIKE 'Lennon%';
  ```

- ## endswith

  ```python
  Entry.objects.filter(headline__endswith = 'Lennon')
  Entry.objects.filter(headline__iendswith = 'Lennon')
  ```

  ```sql
  SELECT ... WHERE headline LIKE '%Lennon';
  SELECT ... WHERE headline ILIKE '%Lennon';
  ```

- ## contains

  ```python
  Entry.objects.filter(headline__contains = 'Lennon')
  Entry.objects.filter(headline__icontains = 'Lennon')
  ```

  ```sql
  SELECT ... WHERE headline LIKE '%Lennon%';
  SELECT ... WHERE headline ILIKE '%Lennon%';
  ```

- ## range

  ```python
  import datetime
  start_date = datetime.date(2005, 1, 1)
  end_date = datetime.date(2005, 3, 31)
  Entry.objects.filter(pub_date__range = (start_date, end_date))
  ```

  ```sql
  SELECT ... WHERE pub_date
  BETWEEN '2005-01-01' AND '2005-03-31';
  ```

- ## 복합 활용

  ```python
  # 서브쿼리로 반환
  inner_qs = Blog.objects.filter(name__contains = 'Cheddar')
  entries = Entry.objects.filter(blog__in = inner_qs)
  ```

  ```sql
  SELECT ...
  WHERE blog.id IN (SELECT id FROM ... WHERE name LIKE '%Cheddar%');
  ```

- ## 활용

  ```python
  # 한 줄 출력
  Entry.objects.all()[0]
  ```

  ```sql
  SELECT ...
  LIMIT 1;
  ```

  <br/>

  ```python
  # ASC 정렬
  Entry.objects.order_by('id')
  ```

  ```sql
  SELECT ...
  ORDER BY id ASC;
  ```

  <br/>

  ```sql
  # DESC 정렬
  Entry.objects.order_by('-id')
  ```

  ```sql
  SELECT ...
  ORDER BY id DESC;
  ```

  

