from django import forms
from .widgets import CustomClearableFileInput
from .models import Testimonial


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        exclude = ['user', 'posted_at', 'approved', 'created_at']

        widgets = {
            'user_testimonial': forms.Textarea(
                                        attrs={'rows': 5, 'cols': 15}),
            'user_rating': forms.Select(
                attrs={'class': 'form-control-sm rounded-3'})
        }
    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control-sm rounded-3'
