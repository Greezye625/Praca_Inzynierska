# Generated by Django 3.1.2 on 2020-10-21 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('threads', '0004_threadcomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='creator',
        ),
        migrations.AddField(
            model_name='thread',
            name='creator_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator_id', to='accounts.userprofile'),
        ),
        migrations.AddField(
            model_name='threadcomment',
            name='poster_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_name_for_poster', to='accounts.userprofile'),
        ),
    ]
