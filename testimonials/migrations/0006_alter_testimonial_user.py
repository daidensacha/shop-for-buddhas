# Generated by Django 3.2.8 on 2021-11-27 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testimonials', '0005_alter_testimonial_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]