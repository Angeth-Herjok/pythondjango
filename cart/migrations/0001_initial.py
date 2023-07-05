# Generated by Django 4.2.2 on 2023-06-30 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('product_name', models.CharField(max_length=32)),
                ('product_price', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField()),
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='')),
                ('date_added', models.DateField()),
            ],
        ),
    ]
