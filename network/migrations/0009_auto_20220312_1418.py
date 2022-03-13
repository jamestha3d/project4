# Generated by Django 3.2.4 on 2022-03-12 14:18

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0008_alter_posts_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followings',
            field=models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='posts',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 12, 14, 18, 55, 288922)),
        ),
        migrations.DeleteModel(
            name='Followings',
        ),
    ]