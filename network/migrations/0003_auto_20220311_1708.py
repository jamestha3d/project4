# Generated by Django 3.2.4 on 2022-03-11 17:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_user_info_posts_likes_follows'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likes',
            name='liked_by',
        ),
        migrations.RemoveField(
            model_name='likes',
            name='posts_liked',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='user',
        ),
        migrations.AddField(
            model_name='posts',
            name='poster',
            field=models.ManyToManyField(related_name='poster', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user_info',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]