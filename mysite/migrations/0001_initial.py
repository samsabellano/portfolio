# Generated by Django 3.2.6 on 2021-08-31 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_first_name', models.CharField(default='Samuel', max_length=255)),
                ('user_last_name', models.CharField(default='Sabellano', max_length=255)),
                ('user_description', models.TextField(blank=True, default="I'm a backend developer and UI/UX designer.", null=True)),
                ('user_contact_number', models.CharField(max_length=11)),
                ('user_address', models.CharField(max_length=255)),
                ('user_email', models.EmailField(max_length=255)),
                ('user_image', models.ImageField(blank=True, null=True, upload_to='about/images')),
                ('user_instagram_link', models.URLField(blank=True, default='https://www.instagram.com/sam.sabellano/', null=True)),
                ('user_github_link', models.URLField(blank=True, default='https://github.com/samsabellano', null=True)),
            ],
            options={
                'verbose_name_plural': 'About',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_fullname', models.CharField(max_length=250)),
                ('comment_email', models.EmailField(max_length=250)),
                ('comment_description', models.TextField()),
            ],
        ),
    ]
