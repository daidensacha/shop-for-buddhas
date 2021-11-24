from allauth.account.forms import SignupForm
from django import forms
from .models import Profile


user_type = (
    ('is_customer', "Customer"),
    ('is_vendor', "Vendor")
)


class CustomSignup(SignupForm):
    user_type = forms.ChoiceField(choices=user_type, required = True)

    def save(self, request):
        user = super(CustomSignup, self).save(request)

        user.user_type = self.cleaned_data['user_type']
        user.save()
        return user
