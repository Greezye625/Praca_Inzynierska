from django.db import models
from accounts.models import UserProfile


# Create your models here.

class Conversation(models.Model):
    subject = models.CharField(max_length=256)

    initiator = models.ForeignKey(UserProfile,
                                  related_name='initiator',
                                  on_delete=models.SET_NULL,
                                  null=True)

    recipent = models.ForeignKey(UserProfile,
                                 related_name='recipent',
                                 on_delete=models.SET_NULL,
                                 null=True)

    def __str__(self):
        return f'{self.initiator.user.username} & {self.recipent.user.username} - {self.subject}'


class Message(models.Model):
    coversation = models.ForeignKey(Conversation,
                                    related_name='conversation',
                                    on_delete=models.CASCADE)

    sender = models.ForeignKey(UserProfile,
                               related_name='sender',
                               on_delete=models.SET_NULL,
                               null=True)

    receiver = models.ForeignKey(UserProfile,
                                 related_name='receiver',
                                 on_delete=models.SET_NULL,
                                 null=True)

    date_time_sent = models.DateTimeField(auto_now_add=True)

    content = models.TextField()
