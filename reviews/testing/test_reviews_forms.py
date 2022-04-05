"""
    imports  -------------------------------------------------------
"""
# third party imports
from django.test import TestCase
from django.contrib.auth.models import User
# internal imports
from reviews.forms import CommentForm, CreateReviewForm


class Test_reviews_form(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User()
        user.id = 1
        user.email = 'testUser@test.com'
        user.username = 'testuser'
        user.password = 'testpassword'
        user.first_name = 'test_first'
        user.last_name = 'test_last'
        user.save()
        
    # 1
    def test_Create_Review_form(self):
        '''
        Test for testing form validation of the Create Review form
        '''

        data = {
            'title': 'test_form_title',
            'content': 'test_form_content',
            'featured_image': 'placeholder',
            'excerpt': 'test_form_excerpt',
        }

        form = CreateReviewForm(data)
        self.assertTrue(form.is_valid)

    # 2
    def test_Create_comment_form(self):
        '''
        Test for testing form validation of the Create comment form
        '''

        data = {
            'body': 'test_form_body',
        }

        form = CommentForm(data)
        self.assertTrue(form.is_valid)

