from django.forms import ModelForm
from .models import Product


class CreateProduct(ModelForm):
    class Meta:
        model = Product
        exclude = ["created_by"]
        # Testing
        fields = ('category', 'sku', 'name', 
                  'description', 'size', 'color',
                  'price', 'rating', 'image',
                  )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'sku', 'name', 
            'description', 'size', 'color',
            'price', 'image',
        }

        # self.fields['full_name'].widget.attrs['autofocus'] = False
        # for field in self.fields:
        #     if field != 'category':
        #         if self.fields[field].required:
        #             placeholder = f'{placeholders[field]} *'
        #         else:
        #             placeholder = placeholders[field]
        #         self.fields[field].widget.attrs['placeholder'] = placeholder
        #     self.fields[field].widget.attrs['class'] = 'stripe-style-input \
        #                                                 rounded-3 \
        #                                                 form-control-sm'
        # self.fields[field].label = False
