from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
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