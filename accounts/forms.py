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
    # username = forms.CharField(
    #     label=False,
    #     widget=forms.TextInput(attrs={'class': 'form-control-sm rounded-3','placeholder': 'Username'})
    # )
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

        user.user_type = self.cleaned_data['user_type']
        user.save()
        return user

# class TestimonialForm(forms.ModelForm):
#     class Meta:
#         model = Testimonial
#         exclude = ['user', 'posted_at', 'approved', "created_at"]
#         widgets = {
#             "user_testimonial": forms.Textarea(
#                                         attrs={"rows": 5, "cols": 15}),
#             "user_rating": forms.Select(attrs={'class': "form-control"})
#         }