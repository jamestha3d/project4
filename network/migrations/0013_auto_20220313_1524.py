# Generated by Django 3.2.4 on 2022-03-13 15:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0012_auto_20220313_0928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='following',
        ),
        migrations.AlterField(
            model_name='posts',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 13, 15, 24, 11, 143903)),
        ),
    ]