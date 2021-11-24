"""
Create custom signup form for multiple user types.
"""
from allauth.account.forms import SignupForm
from django import forms
from .models import Profile


user_type = (
    ('is_customer', "Customer"),
    ('is_vendor', "Vendor")
)


"""
Add user type choicefield to signup form so users can signup as
a customer or a vendor
"""


class CustomSignup(SignupForm):
    """Add user_type choicefield with label to signup form"""
    user_type = forms.ChoiceField(
        choices=user_type,
        label='Register as a customer or vendor?',
        required=True)

    def save(self, request):
        user = super(CustomSignup, self).save(request)

        user.user_type = self.cleaned_data['user_type']
        user.save()
        return user
