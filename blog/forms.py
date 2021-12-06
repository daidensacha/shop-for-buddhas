from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """Model view for the blog post comment form"""

    class Meta:
        """Define the blog comment form with labels"""

        model = Comment
        fields = ['name', 'email', 'body']
        labels = {
            "body": "Comment"
        }
