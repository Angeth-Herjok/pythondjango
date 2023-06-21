from django.db import models

# Create your models here.
class Contact(models.Model):
    phone_number=models.CharField(max_length=22)
    emails=models.EmailField(max_length=32)
    social_media_links=models.URLField()
