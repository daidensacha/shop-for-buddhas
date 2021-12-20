from django import forms
from .widgets import CustomClearableFileInput
# from django.forms import ModelForm
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """ Product form model """
    class Meta:
        model = Product
        exclude = ['created_by', 'favorites']
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control-sm rounded-3'
