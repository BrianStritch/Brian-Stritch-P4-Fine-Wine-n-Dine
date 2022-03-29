from django.test import TestCase
from django.shortcuts import render, get_object_or_404, reverse
from reviews.models import Review, Comment

# class TestCommentModel(TestCase):   

    # def test_comment_model_string(self): 
    #     queryset = Review.objects.filter(id=141)

    #     test_comment = Comment.objects.create(body='testing django comment model', name='django')
    #     self.assertEqual(
    #         str(f"Comment {self.body} by {self.name}"), 
    #         'Comment testing django comment model by django'
    #         )

