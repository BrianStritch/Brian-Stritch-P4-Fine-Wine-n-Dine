from django.test import TestCase
from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.models import User


class TestHomeViews(TestCase):
    """
    A class for testing home views
    """
    def test_get_home_page(self):
        """
        This test checks that the index page
        is displayed
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

class TestSaveUser(TestCase):

    def test_done_defaults_to_True(self):  
        user = User.objects.create_user(
            email='testUser@test.com',
            username='testuser',
            password='testpassword',
            first_name='test_first',
            last_name='test_last'
        )
        user.save()
        self.assertTrue(user.save)