from django.db import models

# Create your models here.
class Contact(models.Model):
    """ Create a contact form model """

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    subject = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    Message = models.TextField(max_length=150)

    def __str__(self):
        return self.name