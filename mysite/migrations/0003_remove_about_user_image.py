# Generated by Django 3.2.6 on 2021-08-31 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20210831_1833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='user_image',
        ),
    ]