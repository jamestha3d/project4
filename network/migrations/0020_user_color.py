# Generated by Django 3.2.4 on 2022-03-26 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0019_alter_posts_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='color',
            field=models.CharField(default='#ddf4ff', max_length=200),
        ),
    ]