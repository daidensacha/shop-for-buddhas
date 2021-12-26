
from blog.models import Post, Category, Comment
from accounts.models import UserModel
from django.test import TestCase
from django.utils import timezone
from datetime import datetime
from mixer.backend.django import mixer
from taggit.managers import TaggableManager
import pytest
import tempfile

MEDIA_ROOT = tempfile.mkdtemp()
pytestmark = pytest.mark.django_db(transaction=True)


# Unit Tests: Testing Models
class ModelTests(TestCase):
    # def test_category(self):
    #     length = len(Category.objects.all())
    #     assert length == 0
    #     category = Category()
    #     category.name = "test"
    #     category.slug = "test"
    #     category.save()
    #     length = len(Category.objects.all())
    #     assert length == 1

    def test_category_created(self):
        category1 = mixer.blend(Category, name="cat1", slug="cat1")
        new_category = Category.objects.last()
        assert new_category.name == "cat1"

    def test_str_return(self):
        category1 = mixer.blend(Category, name="cat1", slug="cat1")
        new_category = Category.objects.last()
        assert str(new_category) == "cat1"

    def test_user_created(self):
        user1 = mixer.blend(UserModel, first_name="user1")
        new_user = UserModel.objects.last()
        assert new_user.first_name == "user1"

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
        # blog
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

    # def test_post_created(self):
    #     # category1 = mixer.blend(Category, name="cat1", slug="cat1")
    #     # user1 = mixer.blend(UserModel, first_name="user1")
    #     post1 = mixer.blend(
    #               Post, category="cat1",
    #                     author="user1",
    #                     title="title1",
    #                     slug="title1")
    #     new_post = Post.object.last()
    #     assert new_post.title == "title1"

    def test_post_str(self):
        user = UserModel()
        user.first_name = "test"
        user.last_name = "user"
        user.username = "testuser"
        user.email = "testuser@gmail.com"
        user.user_type = 'is_customer'
        user.save()
        category = Category.objects.create(name="test", slug="test")
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

        self.assertEqual(str(blog), "test article")
        return blog

    def test_comment(self):
        post = self.test_post_str()
        comment = Comment.objects.create(
            post=post, name="good test", body="test body")
        self.assertEqual(str(comment), "good test")
