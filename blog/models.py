from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=255,null=True)
    # image = 
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(max_length=255,null=True)
    tag = models.CharField(max_length=255,null=True)
    counted_view = models.IntegerField(default=0)
    published_date = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=255)

class Category(models.Model):
    name = models.CharField(max_length=255)
