# Generated by Django 3.2.12 on 2023-08-19 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vender',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='vendor_images/'),
        ),
    ]