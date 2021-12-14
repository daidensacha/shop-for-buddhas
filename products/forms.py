from django.forms import ModelForm
from .models  import Product

class CreateProduct(ModelForm):
    class Meta:
        model = Product
        exclude = ["created_by"]