from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    
    def __str__(self):
        return self.name
    


class Post(models.Model):
    title = models.CharField(max_length=230, unique=False)
    content = models.TextField(unique=False)
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
    time = models.DateField()
    author = models.ForeignKey(User, default=1, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
