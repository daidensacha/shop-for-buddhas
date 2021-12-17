"""
Create custom signup form for multiple user types.
"""
from allauth.account.forms import SignupForm
from django import forms
# from .models import Profile


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
    first_name = forms.CharField(
        label=False,
        widget=forms.TextInput(attrs={'class': 'form-control-sm rounded-3','placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        label=False,
        widget=forms.TextInput(attrs={'class': 'form-control-sm rounded-3','placeholder': 'Last Name'})
    )
    # email = forms.EmailField(
    #     label=False,
    #     widget=forms.TextInput(attrs={'class': 'form-control-sm rounded-3','placeholder': 'Email Address'})
    # )
    user_type = forms.ChoiceField(
        choices=user_type,
        label='Register as a customer or vendor?',
        # label=False,
        required=True)
        

    def save(self, request):
        user = super(CustomSignup, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.user_type = self.cleaned_data['user_type']
        user.save()
        return user
        # profile = user.profile
        # profile.save()
