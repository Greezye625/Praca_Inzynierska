# Generated by Django 3.1.2 on 2020-10-25 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201021_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.CharField(default='default', max_length=256, null=True),
        ),
    ]
