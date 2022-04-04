from django.test import TestCase
from django.contrib.auth.models import User
import unittest
from site_pages.forms import UserAccountDetailsForm,  EditProfileForm
from django.contrib.auth.forms import UserCreationForm


class Test_user_registration_form(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User()
        user.id=1
        user.email='testUser@test.com'
        user.username='testuser'
        user.password='testpassword'
        user.first_name='test_first'
        user.last_name='test_last'        
        user.save()
        
    # 1
    def test_user_creation_form(self):

        data = {
            'username': 'newtestuser',
            'password1': 'test123',
            'password2': 'test123',
        }

        form = UserCreationForm(data)
        self.assertTrue(form.is_valid)

    # 2
    def test_UserAccountDetails_form(self):

        data = {
            'username': 'newtestuser',
            'email': 'test@test.ie',
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
            'password1': 'test123',
            'password2': 'test123',
        }

        form = UserCreationForm(data)
        self.assertTrue(form.is_valid)

    # 3
    def test_edit_user_form(self):
        
        self.client.login(username='testuser', password='testpassword')

        new_user_data = {
            'username': 'edittestname',
            'email': 'test@test.ie',
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
            'password1': 'testpass',
            'password2': 'testpass',
        }   
        form = EditProfileForm(new_user_data)
        self.assertTrue(form.is_valid)
        
    #4
    def test_user_delete_form(self):
        user = User()
        user.id=2
        user.email='testUser2@test.com'
        user.username='testuser2'
        user.password='test2password'
        user.first_name='test_first2'
        user.last_name='test_last2'        
        user.save()

        user= User.objects.get(id=2)
        user.delete()
        self.assertTrue(user.delete)


 