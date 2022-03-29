from django.test import TestCase
from django.shortcuts import render, get_object_or_404, reverse


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


# class TestSignUpView(TestCase):
#     """
#     A class for testing sign up page views
#     """
#     def test_sign_up_page(self):
#         """
#         This test checks that the sign up page
#         is displayed correctly
#         """
#         response = self.client.get('/sign_up/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'nannys_alternative/sign_up.html', 'base.html')


class TestUserprofileViews(TestCase):
    """
    A class for testing user profile views
    """
    def test_get_profile_page(self):
        """
        This test checks that the profile page
        is displayed
        """
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nannys_alternative/profile.html', 'base.html')


# class Test------------View(TestCase):
#     """
#     A class for testing ----------- page views
#     """
#     def test_get_---------------_page(self):
#         """
#         This test checks that the ---------------- page
#         is displayed
#         """
#         response = self.client.get('/------------/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'nannys_alternative/------------.html', 'base.html')
# class Test------------View(TestCase):
#     """
#     A class for testing ----------- page views
#     """
#     def test_get_---------------_page(self):
#         """
#         This test checks that the ---------------- page
#         is displayed
#         """
#         response = self.client.get('/------------/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'nannys_alternative/------------.html', 'base.html')


# class Test------------View(TestCase):
#     """
#     A class for testing ----------- page views
#     """
#     def test_get_---------------_page(self):
#         """
#         This test checks that the ---------------- page
#         is displayed
#         """
#         response = self.client.get('/------------/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'nannys_alternative/------------.html', 'base.html')


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






   

   
    # path(
    #     'about/',
    #     views.About.as_view(),
    #     name='about'
    #     ),
    
  
    # path(
    #     'nannys_alternative/edit_profile/',
    #     views.Edit_profile.as_view(),
    #     name='edit_profile'
    #     ),
    # path(
    #     'nannys_alternative/delete_profile/<int:pk>/',
    #     views.DeleteProfile.as_view(),
    #     name='delete_profile'
    #     ),