# blog/models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    date = models.DateField("Publication date")
    img = models.ImageField("Image", upload_to="image/%Y")

    def __str__(self):
        return self.title
 

class Likes(models.Model):
    ip = models.CharField("IP", max_length=50)
    post = models.ForeignKey(Post, verbose_name="post", on_delete=models.CASCADE) 