"""
Create custom signup form for multiple user types.
"""
from allauth.account.forms import SignupForm
from django import forms


user_type = (
    ('is_customer', "Customer"),
    ('is_vendor', "Vendor")
)


"""
Add user_type choicefield to signup form so users can signup as
a customer or a vendor
Add fist_name and last_name fields to the user registraion form.
"""


class CustomSignup(SignupForm):
    """Add additional fields to the custom signup form"""
    first_name = forms.CharField(
        label=False,
        widget=forms.TextInput(attrs={'class': 'form-control-sm rounded-3',
                                      'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        label=False,
        widget=forms.TextInput(attrs={'class': 'form-control-sm rounded-3',
                                      'placeholder': 'Last Name'})
    )
    user_type = forms.ChoiceField(
        choices=user_type,
        label='Register as a customer or vendor?',
        required=True)

    def save(self, request):
        user = super(CustomSignup, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.user_type = self.cleaned_data['user_type']
        user.save()
        return user
