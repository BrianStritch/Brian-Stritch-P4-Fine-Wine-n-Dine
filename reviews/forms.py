from .models import Comment, Review
from django.contrib.auth.models import User
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = (
            'title',
            'content',
            'featured_image',
            'excerpt'
            )


# class EditReviewForm(forms.ModelForm):    

#     class Meta:
#         model = Review
#         fields = (
#             'content',
#             'featured_image',
#             'excerpt',
#             )




class EditReviewForm(CreateReviewForm):

    class Meta:
        model = Review
        fields = (
            'content',
            'featured_image',
            'excerpt',
            )
            
    def update(self, commit=True):        
        review = super(EditReviewForm, self).save(commit=False)
        review.content = self.cleaned_data['content']
        review.featured_image = self.cleaned_data['featured_image']
        review.excerpt = self.cleaned_data['excerpt']

        if commit:
            review.save()
        
        return review


