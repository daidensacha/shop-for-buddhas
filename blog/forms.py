from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """Model view for the blog post comment form"""

    class Meta:
        """Define the blog comment form with labels"""

        model = Comment
        fields = ['name', 'body']

    def __init__(self, *args, **kwargs):
        # add placeholders and classes
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'body': 'Comment',
        }
        self.fields['name'].widget.attrs['autofocus'] = False
        self.fields['body'].widget.attrs['rows'] = 3
        for field in self.fields:

            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = \
                'stripe-style-input rounded-3 form-control-sm'
            self.fields[field].label = False
