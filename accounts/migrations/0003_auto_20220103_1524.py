# Generated by Django 3.2.8 on 2022-01-03 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20211217_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='first_name',
            field=models.CharField(max_length=40, verbose_name='first_name'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='last_name',
            field=models.CharField(max_length=40, verbose_name='last_name'),
        ),
    ]
