from django.db import models
from accounts.models import UserProfile
from django.contrib.auth.models import User

# Create your models here.

class ThoughtModel(models.Model):
    content = models.CharField(max_length=100)
    like = models.BooleanField(default=False)
    amount=models.IntegerField(default=0)
    date = models.DateField(auto_now=True)
    owner = models.ForeignKey(User, related_name='thoughts', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.content

    
