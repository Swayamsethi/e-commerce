# Generated by Django 5.1.3 on 2024-11-21 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_products_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.IntegerField(choices=[(1, 'MALE'), (2, 'FEMALE'), (3, 'OTHER')], null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_role',
            field=models.IntegerField(choices=[(1, 'ADMIN'), (2, 'CUSTOMER'), (3, 'SELLER')], null=True),
        ),
    ]
