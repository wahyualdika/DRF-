from django.db import models
from django.contrib.auth.models import User

class TipeBerita(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Berita(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True,related_name='news')
    tipe_berita = models.ForeignKey(TipeBerita, on_delete=models.CASCADE,null=True,related_name='tipe_berita')

    def __str__(self):
        return self.title
