from django.db import models

# Create your models here.
class Todo(models.Model):
    # django에서 pk(id)는 자동으로 만들어준다.
    content = models.CharField(max_length=80)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(default=3)
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateField(null=True)
