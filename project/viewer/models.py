from django.db import models
from django.contrib.auth.models import User
from writer.models import BlogModel

# Create your models here.
class CommentModel(models.Model):
    blog = models.ForeignKey(BlogModel,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
