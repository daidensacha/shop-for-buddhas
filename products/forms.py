from django import forms
from django.forms import ModelForm
from .models import Product, Category


# class CreateProduct(ModelForm):
#     class Meta:
#         model = Product
#         exclude = ["created_by"]
#         # Testing
#         fields = ('category', 'sku', 'name', 
#                   'description', 'size', 'color',
#                   'price', 'rating', 'image',
#                   )

#     def __init__(self, *args, **kwargs):
#         """
#         Add placeholders and classes, remove auto-generated
#         labels and set autofocus on first field
#         """
#         super().__init__(*args, **kwargs)
#         placeholders = {
#             'sku', 'name', 
#             'description', 'size', 'color',
#             'price', 'image',
#         }

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        # exclude = ["created_by"]
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control-sm rounded-3'
