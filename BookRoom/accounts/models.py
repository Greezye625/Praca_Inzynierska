from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.CharField(max_length=256, null=True)


    def get_absolute_url(self):
        return reverse('accounts:login')

    def __str__(self):
        return f'@{self.user.username}'
