# Generated by Django 3.2.8 on 2021-12-12 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0010_alter_testimonial_user_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='posted_at',
            field=models.DateField(null=True),
        ),
    ]
