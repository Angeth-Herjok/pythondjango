# Generated by Django 4.2.2 on 2023-07-14 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
        ('order', '0002_order_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customers',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.customers'),
        ),
    ]
