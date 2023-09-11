from django.db import models

# Create your models here.
class Contact(models.Model):
    # full_name=models.CharField(max_length=30)
    phone_number=models.CharField(max_length=22)
    emails=models.EmailField(max_length=32)
    social_media_links=models.URLField()
    full_name = models.CharField(max_length=255, default="Angeth")
