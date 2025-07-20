from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(blank=True, max_length=20, null=True)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="photos/", blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.title}'