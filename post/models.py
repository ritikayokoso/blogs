from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.

class Post(models.Model):
    title= models.CharField(max_length=200)
    description=models.CharField(max_length=2000)
    date = models.DateTimeField(auto_now_add=True,null = True, blank = True)
    price= models.IntegerField(blank=False)
    thumbnail= models.ImageField(upload_to= 'images/', null=True)
    likes = models.ManyToManyField(User, related_name="post_like" , default=False)
    def total_likes(self):
      return self.likes.count()
    def __str__(self):
      return self.title