# Generated by Django 5.1.3 on 2024-11-19 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_user_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_img/'),
        ),
    ]
