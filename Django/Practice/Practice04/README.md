# Django 연습 (게시판 만들기)

## 1. 가상환경 및 Django 설치

```bash
# 가상환경 설치
$ python -m venv venv

# 가상환경 실행
$ python venv/Scripts/activate

# Django 설치
$ pip install django==3.2.13

# 패키지 생성 파일(txt) 생성
$ pip freeze > requirements.txt

# .gitignore 파일을 생성하고 가상환경 폴더를 등록
$ touch .gitignore
>>> venv/
```

<br/>

## 2. 프로젝트 및 앱 생성

```bash
# 프로젝트 생성
$ django-admin startproject pjt .

# 앱 생성
$ django-admin startapp articles
```

<br/>

### 2-1. 앱 등록 (settings.py)

```python
# INSTALLED_APPS를 찾아 앱을 동록한다.

INSTALLED_APPS = [
    "articles",
    # ...
]

# 언어, 시간 설정
LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"
```

<br/>

### 2-2. urls.py

#### 2-2-1. pjt/urls.py (프로젝트 메인 urls.py)

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # include를 추가로 import하고 "[앱 이름].urls" 등록
    path("", include("articles.urls")),
]
```

<br/>

#### 2-2-2. articles/urls.py (앱 urls.py)

```python
from django.urls import path
from . import views
# 폴더 내에 있는 views를 import

# 앱 이름 등록
app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
]
```

<br/>

## 3. Model 정의 (DB 설계)

### 3-1. articles/models.py

```python
# DB 설계
class Articles(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

<br/>

### 3-2. DB 생성

```bash
# migrations 파일 생성
$ python manage.py makemigrations

# DB 반영
$ python manage.py migrate
```

<br/>

## 4. CRUD 구현

### 4-1. Create

#### 4-1-0. index.html

```html
<!-- 글 작성 페이지로 이동 링크 만들기 -->
<a href="{% url 'articles:create' %}">작성하기</a>
<!-- {% url '[app_name]:[urls.py의 path name] '%} -->
```

<br/>

#### 4-1-1. urls.py

```python
urlpatterns = [
    path("", views.index, name="index"),
    # path 추가
    path("create/", views.create, name="create"),
    # path("create/", views.[views.py의 함수명], name="create"),
]
```

<br/>

#### 4-1-2. views.py

```python
def create(request):
    return render(request, "articles/create.html")
	# render(request, "[templates/폴더명]/[html 파일명]")
```

<br/>

#### 4-1-3. templates/create.html

```html
<!-- {% url '[app_name]:[urls.py의 path name] '%} -->
<form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{ article_form.as_p }}
    <input type="submit" value="작성하기">
</form>
```

<br/>

#### 4-1-4. forms.py

```python
from django import forms
from .models import Article


# ModelForm class 생성
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
```

<br/>

#### 4-1-5. views.py

```python
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


def create(request):
    # create.html에서 작성하기 버튼을 눌렀을 때
    if request.method == "POST":
        article_form = ArticleForm(request.POST)
        
		# form의 값들이 유효하다면 (유효성 검사)
        if article_form.is_valid():
            # DB에 저장
            article_form.save()
            return redirect("articles:index")
        
    # index.html에서 작성하기 버튼을 눌렀을 때
    else:
        # 빈 form을 만듦
        article_form = ArticleForm()
	
    # form을 context에 담아 반환
    context = {
        "article_form": article_form,
    }

    return render(request, "articles/create.html", context)
```

<br/>

### 4-2. Read (index.html)

#### 4-2-1. views.py

```python
# index 함수
def index(request):
    # DB에 있는 모든 데이터를 pk 값으로 내림차순하여
    articles = Article.objects.order_by("-pk")
	
    # articles라는 변수를 통해 context에 담음
    context = {
        "articles": articles,
    }

    return render(request, "articles/index.html", context)
```

<br/>

#### 4-2-2. index.html

```html
<!-- 모든 articles 출력 -->
{% for article in articles %}
<h3>{{ article.title }}</h3>
<p>{{article.created_at}} | {{ article.updated_at }}</p>
<hr>
{% endfor %}
```

<br/>

### 4-3. Read (detail.html)

#### 4-3-0. index.html

```html
<!-- title에 링크 달기 -->
<h3><a href="{% url 'articles:detail' article.pk %}">{{ article.title }}</a></h3>
```

#### 4-3-1. urls.py

```python
urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    # pk값을 url에 포함한 path를 추가
    path("<int:pk>/", views.detail, name="detail"),
]
```

<br/>

#### 4-3-2. views.py

```python
def detail(request, pk):
    # DB에서 pk 값이 일치하는 데이터를 가져옴
    article = Article.objects.get(pk=pk)

    context = {
        "article": article,
    }

    return render(request, "articles/detail.html", context)
```

<br/>

#### 4-3-3. templates/detail.html

```html
<h1>{{ article.title }}</h1>
<h3>{{ article.pk }}번 글</h3>
<p>{{ article.created_at }} | {{ article.updated_at }}</p>
<h2>{{ article.content }}</h2>
```

<br/>

### 4-4. Update

#### 4-4-0. detail.html

```html
<!-- 수정하기 링크 달기 -->
<a href="{% url 'articles:update' article.pk %}"></a>
```

<br/>

#### 4-4-1. urls.py

```python
urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.detail, name="detail"),
    # pk값을 url에 포함한 path를 추가
    path("<int:pk>/update/", views.update, name="update"),
]
```

<br/>

#### 4-4-2. views.py

```python
def update(request, pk):
    # DB에서 pk 값이 같은 데이터를 가져옴
    article = Article.objects.get(pk=pk)
	
    # update.html에서 수정 버튼을 눌렀을 때
    if request.method == "POST":
        # instance 값을 article의 데이터로 하는 form을 생성
        article_form = ArticleForm(request.POST, instance=article)
		
        # 유효성 검사
        if article_form.is_valid():
            article_form.save()
            return redirect("articles:detail", article.pk)
    
    # detail.html에서 수정 버튼을 눌렀을 때
    else:
        article_form = ArticleForm(instance=article)

    context = {
        "article": article,
        "article_form": article_form,
    }

    return render(request, "articles/update.html", context)
```

<br/>

#### 4-4-3. update.html

```html
<h1>글 수정하기</h1>

<form action="{% url 'articles:update' article.pk %}" method="POST">
    {% csrf_token %}
    {{ article_form.as_p }}
    <input type="submit" value="수정">
</form>
```

