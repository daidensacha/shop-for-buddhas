from datetime import datetime
from django.db import models
from accounts.models import Profile


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Blog(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField()
    title = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)
    description = models.TextField(max_length=150)
    posted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(
                    blank=True,
                    null=True,
                    default=datetime.now
                    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    description = models.TextField(max_length=150)
    posted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(
                    blank=True,
                    null=True,
                    default=datetime.now
                    )

    def __str__(self):
        return self.name
