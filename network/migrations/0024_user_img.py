# Generated by Django 3.2.4 on 2022-03-31 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0023_auto_20220328_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='img',
            field=models.ImageField(blank=True, upload_to='profile_photo'),
        ),
    ]