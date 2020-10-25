# Generated by Django 3.1.2 on 2020-10-21 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='thread_type',
            field=models.CharField(choices=[('Sell', 'Sell'), ('Buy', 'Buy'), ('Exchange', 'Exchange'), ('Discussion', 'Discussion')], default='Discussion', max_length=20),
        ),
    ]
