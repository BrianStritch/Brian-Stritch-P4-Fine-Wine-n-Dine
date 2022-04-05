"""
    imports  -------------Reviews forms.py----------------------
"""
# third party imports
from django import forms
# internal imports
from .models import Comment, Review


class CommentForm(forms.ModelForm):
    """
    Class based form to create new comments using the
    comments model
    """
    class Meta:
        """
        Class to indicate which model to use and to
        set the fields in the create comment model form
        """
        model = Comment
        fields = ('body',)


class CreateReviewForm(forms.ModelForm):
    """
        Class based form to set the fields in
        the Create Review model form for creating a new review
    """
    class Meta:
        """
        Class to indicate which model to use and to
        set the fields in the create review model form
        """
        model = Review
        fields = (
            'title',
            'content',
            'featured_image',
            'excerpt'
            )
