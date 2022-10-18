from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(blank=True)
    thumbnail = ProcessedImageField(
        upload_to="image",
        processors=[ResizeToFill(100, 50)],
        format="JPEG",
        options={"quality": 60},
    )
