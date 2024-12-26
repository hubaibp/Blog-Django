from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    blog = models.TextField()
    author_name = models.CharField(max_length=100,null=True)
    date = models.DateField(auto_now_add=True)
    image=models.ImageField(upload_to='blog_images')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title