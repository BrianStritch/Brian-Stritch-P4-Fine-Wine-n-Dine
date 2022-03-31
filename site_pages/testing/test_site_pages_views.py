from django.test import TestCase
from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.models import User
import unittest

# 1
class TestEditProfileView(TestCase):
    """
    A class for testing edit_profile page views
    """
    def test_get_edit_profile_page(self):
        """
        This test checks that the edit_profile page
        is displayed
        """
        response = self.client.get('/edit_profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nannys_alternative/edit_profile.html', 'base.html')

# 2
class TestHomePageViews(TestCase):
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
        self.assertTemplateUsed(response, 'index.html', 'base.html')

# 3
class TestOpeningHoursView(TestCase):
    """
    A class for testing opening hours page views
    """
    def test_get_openingHours_page(self):
        """
        This test checks that the opening hours page
        is displayed
        """
        response = self.client.get('/opening_hours/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nannys_alternative/opening-times.html', 'base.html')

# 4
class TestMenuViews(TestCase):
    """
    A class for testing menu views
    """
    def test_get_menu_page(self):
        """
        This test checks that the menu page
        is displayed
        """
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nannys_alternative/menu.html', 'base.html')




# 5
class TestUserprofileViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            id=1,
            email='test@test.com',
            username='test_username',
            password='testpassword',
            first_name='test_first',
            last_name='test_last'
        )

    """
    A class for testing user profile views
    """
    def test_get_profile_page(self):
        """
        This test checks that the profile page
        is displayed
        ****************************************************************************************************************
        THis test workss just needs a user to be logged in 
        """
                
        self.client.login(username='test_username', password='testpassword')
        user = User.objects.get(id=1)
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nannys_alternative/profile.html', 'base.html')

# 6
class TestSignUpView(TestCase):
    """
    A class for testing sign up page views
    """
    def test_sign_up_page(self):
        """
        This test checks that the sign up page
        is displayed correctly
        """
        response = self.client.get('/sign_up_now/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nannys_alternative/sign_up.html', 'base.html')

# 7
class Test_test_test(TestCase):

    def test_done_defaults_to_True(self):
            user = User()
            user.email='testUser@test.com',
            user.username='testuser',
            user.password='testpassword',
            user.first_name='test_first',
            user.last_name='test_last'
            
            user.save()
            self.assertTrue(user.save)










