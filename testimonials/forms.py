from django import forms
from .models import Testimonial


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        exclude = ['user', 'posted_at', 'approved',"created_at"]
        widgets = {
            "user_testimonial": forms.Textarea(
                                        attrs={"rows": 5, "cols": 15}),
            "user_rating": forms.Select(attrs={'class': "form-control"})
        }
