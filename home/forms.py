from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'subject', 'email', 'message')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'First Name',
            'subject': 'Subject',
            'email': 'Email',
            'message': 'Message',
        }
        self.fields['name'].widget.attrs['autofocus'] = False
        for field in self.fields:

            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = \
                'form-control-sm rounded-3'
            self.fields[field].label = False
