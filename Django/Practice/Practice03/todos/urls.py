from django.urls import path
from . import views

# url namesapce
# url을 이름으로 분류하는 기능
app_name = "todos"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("update/<int:todo_pk>", views.update, name="update"),
    path("delete/<int:todo_pk>", views.delete, name="delete"),
]
