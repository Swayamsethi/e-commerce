# Generated by Django 5.1.3 on 2024-11-26 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=39, null=True),
        ),
    ]
