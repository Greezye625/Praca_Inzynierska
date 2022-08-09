from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(upload_to=user_directory_path, height_field=None, width_field=None, max_length=100, null=True)


    def get_absolute_url(self):
        return reverse('accounts:login')

    def __str__(self):
        return f'@{self.user.username}'
