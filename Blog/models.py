from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=100)
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)

    def __str__(self):
        return super().__str__()

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return super().__str__()
