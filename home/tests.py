from django.test import TestCase
from profiles.models import Contact
from .forms import ContactForm
from django.urls import reverse
import pytest

pytestmark = pytest.mark.django_db(transaction=True)


class ViewsTests(TestCase):
    def test_index(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_contact(self):
        url = reverse('contact')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_contact_form(self):
        contact = Contact.objects.create(
            first_name='firstName',
            last_name='lastName',
            subject='subject',
            message='Message',
            sender='daidensacha@gmail.com'
            )
        data = {'first_name': contact.first_name,
                'last_name': contact.last_name,
                'subject': contact.subject,
                'message': contact.message,
                'sender': contact.sender
                }
        form = ContactForm(data=data)
        self.assertTrue(form.is_valid())

    def test_terms(self):
        url = reverse('terms')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_privacy(self):
        url = reverse('privacy')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
