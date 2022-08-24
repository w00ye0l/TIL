# 데이터베이스 07 - ORM

<aside>
💡 코드를 작성한 실습 파일을 압축해서 실라버스에 제출해주세요.

</aside>

### 1. `db/models.py` 파일에 아래의 모델 2개 `Director` `Genre` 를 작성하세요.

> 기본 코드
> 

```python
class Director(models.Model):
    name = models.TextField()
    debut = models.DateTimeField()
    country = models.TextField()

class Genre(models.Model):
    title = models.TextField()
```

### 2. 모델을 마이그레이트(migrate) 하세요.

```bash
# 가상환경 실행 확인 후 아래 명령어를 터미널에 입력합니다.
python manage.py makemigrations

python manage.py migrate
```

### 3. Queryset 메소드 `create` 를 활용해서  `Director` 테이블에 아래 데이터를 추가하는 코드를 작성하세요.

| name | debut | country |
| --- | --- | --- |
| 봉준호 | 1993-01-01 | KOR |
| 김한민 | 1999-01-01 | KOR |
| 최동훈 | 2004-01-01 | KOR |
| 이정재 | 2022-01-01 | KOR |
| 이경규 | 1992-01-01 | KOR |
| 한재림 | 2005-01-01 | KOR |
| Joseph Kosinski | 1999-01-01 | KOR |
| 김철수 | 2022-01-01 | KOR |

> 코드 작성
> 

```python
import datetime
Director.objects.create(name='봉준호', debut=datetime.date(1993, 1, 1), country='KOR')
Director.objects.create(name='김한민', debut=datetime.date(1999, 1, 1), country='KOR')
Director.objects.create(name='최동훈', debut=datetime.date(2004, 1, 1), country='KOR')
Director.objects.create(name='이정재', debut=datetime.date(2022, 1, 1), country='KOR')
Director.objects.create(name='이경규', debut=datetime.date(1992, 1, 1), country='KOR')
Director.objects.create(name='한재림', debut=datetime.date(2005, 1, 1), country='KOR')
Director.objects.create(name='Joseph Kosinski', debut=datetime.date(1999, 1, 1), country='KOR')
Director.objects.create(name='김철수', debut=datetime.date(2022, 1, 1), country='KOR')
```

### 4. `인스턴스 조작` 을 활용하여`Genre` 테이블에 아래 데이터를 추가하는 코드를 작성하세요.

| title |
| --- |
| 액션 |
| 드라마 |
| 사극 |
| 범죄 |
| 스릴러 |
| SF |
| 무협 |
| 첩보 |
| 재난 |

> 코드 작성
> 

```python
tit = ['액션', '드라마', '사극', '범죄', '스릴러', 'SF', '무협', '첩보', '재난']

for t in tit:
    genre = Genre()
    genre.title = t
    genre.save()
```

### 5. Queryset 메소드 `all` 을 활용해서 `Director` 테이블의 모든 데이터를 출력하는 코드를 작성하세요.

> 출력 예시
> 

```
봉준호 1993-01-01 00:00:00 KOR
김한민 1999-01-01 00:00:00 KOR
최동훈 2004-01-01 00:00:00 KOR
이정재 2022-01-01 00:00:00 KOR
이경규 1992-01-01 00:00:00 KOR
한재림 2005-01-01 00:00:00 KOR
Joseph Kosinski 1999-01-01 00:00:00 KOR
김철수 2022-01-01 00:00:00 KOR
```

> 코드 작성
> 

```python
for i in range(len(Director.objects.all())):
    temp = []
    temp.append(Director.objects.all()[i].name)
    temp.append(Director.objects.all()[i].debut)
    temp.append(Director.objects.all()[i].country)
    print(*temp)
```

### 6. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `id` 가 1인 데이터를 출력하는 코드를 작성하세요.

> 출력 예시
> 

```
봉준호 1993-01-01 00:00:00 KOR
```

> 코드 작성
> 

```python
dir_id1 = Director.objects.get(id=1)
print(dir_id1.name, dir_id1.debut, dir_id1.country)
```

### 7. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `country` 가 USA인 데이터를 출력하는 코드를 작성하세요.

> 코드 작성
> 

```python
Director.objects.get(country = 'USA')
```

### 8. 위 문제에서 오류가 발생합니다. 출력된 오류 메세지와 본인이 생각하는 혹은 찾은 오류가 발생한 이유를 작성하세요.

> 오류 메세지
> 

```bash
DoesNotExist: Director matching query does not exist.
```

> 이유 작성
> 

```
get 메소드는 데이터가 1개가 아닐 경우(0개 또는 2개 이상) 오류 메세지를 출력한다.
```

### 9. Queryset 메소드 `get` 과 `save` 를 활용해서 `Director` 테이블에서  `name` 이 Joseph Kosinski인 데이터를 조회해서 `country` 를 USA 로 수정하고, 출력하는 코드를 작성하세요.

> 출력 예시
> 

```
Joseph Kosinski 1999-01-01 00:00:00 USA
```

> 코드 작성
> 

```python
jk = Director.objects.get(name = 'Joseph Kosinski')
jk.country = 'USA'
jk.save()

jk = Director.objects.get(name='Joseph Kosinski')
print(jk.name, jk.debut, jk.country)
```

### 10. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `country` 가 KOR인 데이터를 출력하는 코드를 작성하세요.

> 코드 작성
> 

```python
Director.objects.get(country = 'KOR')
```

### 11. 위 문제에서 오류가 발생합니다. 출력된 오류 메세지와 본인이 생각하는 혹은 찾은 오류가 발생한 이유를 작성하세요.

> 오류 메세지
> 

```bash
MultipleObjectsReturned: get() returned more than one Director -- it returned 7!
```

> 이유 작성
> 

```
get 메소드를 사용하여 출력되는 데이터의 개수가 2개 이상이기 때문에 오류 발생
```

### 12. Queryset 메소드 `filter` 를 활용해서 `Director` 테이블에서 `country` 가 KOR인 데이터를 출력하는 코드를 작성하세요.

> 출력 예시
> 

```
봉준호 1993-01-01 00:00:00 KOR
김한민 1999-01-01 00:00:00 KOR
최동훈 2004-01-01 00:00:00 KOR
이정재 2022-01-01 00:00:00 KOR
이경규 1992-01-01 00:00:00 KOR
한재림 2005-01-01 00:00:00 KOR
김철수 2022-01-01 00:00:00 KOR
```

> 코드 작성
> 

```python
c_kr = Director.objects.filter(country = 'KOR')
for i in range(len(c_kr)):
    print(c_kr[i].name, c_kr[i].debut, c_kr[i].country)
```

### 13. 본인이 생각하는 혹은 찾은 `get` 과 `filter` 의 차이를 작성하세요.

```
get은 단 하나의 값이 존재할 경우(조건을 PK로 접근할 때) 사용하고,
filter는 값이 0개 또는 2개 이상일 경우 사용한다.
```

### 14. Queryset 메소드 `get` 과 `delete`를 활용해서  `Director` 테이블에서 `name` 이 김철수인 데이터를 삭제하는 코드를 작성하세요.

> 코드 작성
> 

```python
kcs = Director.objects.get(name = '김철수')
kcs.delete()
```

### 15. 이름이 `봉준호`인 데이터 모두 다 뽑기

```python
dic = Director.objects.filter(name='봉준호').values()[0]
for k in dic:
    print(f'{k}: {dic[k]}')
```

```
id: 1
name: 봉준호
debut: 1993-01-01 00:00:00
country: KOR
```

### 16. 전체 출력하기

```python
for obj in Director.objects.all().values():
    for o in obj:
        print(obj[o])
    print()

####
for obj in Director.objects.all().values():
    l = [*obj]
    for field in l:
        print(obj[field])
    print()
```

```
1
봉준호
1993-01-01 00:00:00
KOR

2
김한민
1999-01-01 00:00:00
KOR

3
최동훈
2004-01-01 00:00:00
KOR

4
이정재
2022-01-01 00:00:00
KOR

5
이경규
1992-01-01 00:00:00
KOR

6
한재림
2005-01-01 00:00:00
KOR

7
Joseph Kosinski
1999-01-01 00:00:00
USA
```

