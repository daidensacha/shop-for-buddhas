# Generated by Django 3.2.8 on 2021-12-06 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
