
from blog.models import Post, Category
from accounts.models import UserModel
from django.test import TestCase
from django.utils import timezone
from datetime import datetime
import pytest
import tempfile

MEDIA_ROOT = tempfile.mkdtemp()
pytestmark = pytest.mark.django_db(transaction=True)


# Unit Tests: Testing Models
class ModelTests(TestCase):
    def test_category(self):
        length = len(Category.objects.all())
        assert length == 0
        category = Category()
        category.name = "test"
        category.slug = "test"
        category.save()

        length = len(Category.objects.all())
        assert length == 1

        
    def test_post(self):
        length = len(Post.objects.all())
        assert length == 0
        user = UserModel()
        user.first_name = "test"
        user.last_name = "user"
        user.username = "testuser"
        user.email = "testuser@gmail.com"
        user.user_type = 'is_customer'
        user.save()
        # Category()
        category = Category()
        category.name = "test"
        category.slug = "test"
        category.save()
        #blog
        blog = Post()
        blog.author = user
        blog.category = category
        blog.title = "test article"
        blog.slug = "test-article"
        blog.body = "Wwe are doing testing"
        blog.status = "published"
        blog.posted_at = datetime.today()
        blog.created_at = timezone.now
        blog.save() 
        length = len(Post.objects.all())
        assert length == 1
