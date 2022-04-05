from django.test import TestCase
from django.contrib.auth.models import User


class TestReviewsViews(TestCase):

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
        """
              
        self.client.login(username='test_username', password='testpassword')
        user = User.objects.get(id=1)
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nannys_alternative/profile.html', 'base.html')
   
    def test_sign_up_page(self):

        """
        This test checks that the sign up page
        is displayed correctly
        """

        response = self.client.get('/sign_up_now/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nannys_alternative/sign_up.html', 'base.html')


    def test_get_edit_profile_page(self):

        """
        This test checks that the edit_profile page
        is displayed
        """

        response = self.client.get('/edit_profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nannys_alternative/edit_profile.html', 'base.html')


