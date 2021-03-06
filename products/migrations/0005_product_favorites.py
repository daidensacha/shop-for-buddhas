# Generated by Django 3.2.8 on 2021-12-18 11:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0004_product_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='favorites',
            field=models.ManyToManyField(blank=True, default=None, related_name='favorite', to=settings.AUTH_USER_MODEL),
        ),
    ]
