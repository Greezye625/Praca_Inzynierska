from django.db import models
from accounts.models import UserProfile
from django.contrib.auth import get_user_model


class ThreadCategory(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Thread(models.Model):
    name = models.CharField(max_length=256)

    creator = models.ForeignKey(get_user_model(),
                                related_name='creator',
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=True)


    thread_category = models.ForeignKey(ThreadCategory,
                                        related_name='thread_category',
                                        null=True,
                                        on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class ThreadComment(models.Model):
    thread = models.ForeignKey(Thread,
                               related_name='thread',
                               on_delete=models.CASCADE)

    poster = models.ForeignKey(get_user_model(),
                               related_name='poster',
                               on_delete=models.SET_NULL,
                               null=True)

    post_datetime = models.DateTimeField(auto_now_add=True)

    text_content = models.TextField()

    def __str__(self):
        return f'{self.thread} - {self.poster} - {str(self.post_datetime)}'
