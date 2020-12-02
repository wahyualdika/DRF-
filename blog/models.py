from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True,related_name='post')
    tags = models.ManyToManyField(Tag,related_name='tag')

    def __str__(self):
        return self.title
