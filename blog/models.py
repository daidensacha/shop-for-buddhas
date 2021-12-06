from datetime import datetime
from django.db import models
from taggit.managers import TaggableManager
from accounts.models import Profile


class Category(models.Model):
    """Blog category model for the blog app"""

    class Meta:
        """Plural name for Category model admin view"""

        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Post(models.Model):
    """Blog post model for the blog app"""

    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField()
    title = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)
    description = models.TextField(
                    max_length=200,
                    blank=True,
                    null=True
                    )
    body = models.TextField(
                    blank=True,
                    null=True
                    )
    posted_at = models.DateTimeField(
                    blank=True,
                    null=True
                    )
    created_at = models.DateTimeField(
                    blank=True,
                    null=True,
                    default=datetime.now
                    )
    tags = TaggableManager()

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Blog comment model for the blog app"""

    post = models.ForeignKey(
                    Post,
                    related_name='comments',
                    on_delete=models.CASCADE
                    )
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    body = models.TextField(max_length=150)
    posted_at = models.DateTimeField(
                    blank=True,
                    null=True
                    )
    created_at = models.DateTimeField(
                    blank=True,
                    null=True,
                    default=datetime.now
                    )

    def __str__(self):
        return self.name
