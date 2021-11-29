# Generated by Django 3.2.8 on 2021-11-29 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0009_alter_testimonial_user_testimonial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='user_rating',
            field=models.CharField(choices=[('1', '1/5 stars'), ('2', '2/5 stars'), ('3', '3/5 stars'), ('4', '4/5 stars'), ('5', '5/5 stars')], max_length=150),
        ),
    ]
