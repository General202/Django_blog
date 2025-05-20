from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)

    def __str__(self):
        return super().__str__()
    
    def published_recently(self):
        return self.published_date >= timezone.now() - timedelta.days(7)

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return super().__str__()
