from .models import UserProfile, Contact
from accounts.models import UserModel
from django.test import TestCase

import pytest
import tempfile

MEDIA_ROOT = tempfile.mkdtemp()
pytestmark = pytest.mark.django_db(transaction=True)


class ModelTests(TestCase):
    def test_userprofile(self):
        length = len(UserProfile.objects.all())
        assert length == 0

        test_user = UserModel.objects.create(
            first_name='first_user',
            last_name='last_user',
            username='first_last_username',
            email='firstlast@gmail.com',
            user_type='is_customer'
            )
        assert test_user.first_name == 'first_user'

        profile = UserProfile()
        assert test_user.profile.user == test_user
        assert test_user.profile.default_phone_number is None
        assert test_user.profile.default_street_address1 is None
        test_user.profile.default_phone_number = '125-852-9687'

        assert test_user.profile.default_phone_number == '125-852-9687'
        test_user.profile.save()

        length = len(UserProfile.objects.all())
        assert length == 1
        return UserProfile.objects.get(user=test_user)

    def test_userprofile_str_return(self):
        profile = self.test_userprofile()

        self.assertEqual(str(profile), 'first_last_username')

    def test_contact(self):
        length = len(Contact.objects.all())
        assert length == 0
        contact = Contact.objects.create(
            first_name='firstName',
            last_name='lastName',
            subject='subject',
            message='Message',
            sender='daidensacha@gmail.com'
            )
        length = len(Contact.objects.all())
        assert length == 1
        return contact

    def test_contact_str_return(self):
        contact = self.test_contact()
        self.assertEqual(str(contact), 'firstNamelastName')
