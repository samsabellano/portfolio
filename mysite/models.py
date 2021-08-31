from django.db import models
from django.conf import settings


class About(models.Model):
    user_first_name = models.CharField(max_length=255, null=False, blank=False, default='Samuel')
    user_last_name = models.CharField(max_length=255, null=False, blank=False, default='Sabellano')
    user_description = models.TextField(blank=True, null=True, default="I'm a backend developer and UI/UX designer.")
    user_contact_number = models.CharField(max_length=11, null=False, blank=False)
    user_address = models.CharField(max_length=255, null=False, blank=False)
    user_email = models.EmailField(max_length=255, null=False, blank=False)
    user_image = models.ImageField(blank=True, null=True, upload_to='about/images')
    user_instagram_link = models.URLField(null=True, blank=True, default='https://www.instagram.com/sam.sabellano/')
    user_github_link = models.URLField(null=True, blank=True, default='https://github.com/samsabellano')

    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return f'{self.user_first_name} - {self.user_last_name}'


class Comment(models.Model):
    comment_fullname = models.CharField(max_length=250, blank=False, null=False)
    comment_email = models.EmailField(max_length=250, blank=False, null=False)
    comment_description = models.TextField(null=False, blank=False)

    def __str__(self):
        return f'{self.comment_fullname} - {self.comment_email}'
