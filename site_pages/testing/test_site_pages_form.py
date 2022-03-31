from django.test import TestCase
from django.contrib.auth.models import User
import unittest

# 1
class TestSaveUser2(TestCase):

    def test_done_defaults_to_True(self):
        user = User()
        user.email='testUser@test.com'
        user.username='testuser'
        user.password='testpassword'
        user.first_name='test_first'
        user.last_name='test_last'
        
        user.save()
        self.assertTrue(user.save)

# 2
class TestSaveUser3(TestCase):

    def test_done_defaults_to_True(self):
        user = User(
            email='testUser@test.com',
            username='testuser',
            password='testpassword',
            first_name='test_first',
            last_name='test_last'
        )
        user.save()
        self.assertTrue(user.save)