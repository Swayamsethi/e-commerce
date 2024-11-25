# Generated by Django 5.1.3 on 2024-11-19 07:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_products_price_alter_products_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
