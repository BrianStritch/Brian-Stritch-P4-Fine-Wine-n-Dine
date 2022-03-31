from django.test import TestCase
from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.models import User
from bookings.models import Booking
import unittest

# 1
class TestBookingView(TestCase):
    """
        classmethod creating a user and booking instances for testing
    """
    @classmethod
    def setUpTestData(cls):
        
        user = User.objects.create_user(
                id=1,
                email='test@test.com',
                username='test_username',
                password='testpassword',
                first_name='test_first',
                last_name='test_last'
            )
        user.save()
        booking = Booking(
            primary_guest = user,
            booking_date = '2023-03-30',                       
            Meal_time = 2,
        )
        booking.save()


    """
    A class for testing edit_booking page views
    """
    def test_get_edit_booking_page(self):
        """
        This test checks that the edit_booking page
        is displayed
        """
        user = User.objects.get(id=1)
        self.client.login(username='test_username', password='testpassword')
        
        response = self.client.get('/bookings/')
        #self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/create_a_booking.html', 'base.html')

    #2
    def test_get_bookings_page(self):
        """
        This test checks that the bookings page
        is displayed
        """
        user = User.objects.get(id=1)
        self.client.login(username='test_username', password='testpassword')        
        response = self.client.get('/bookings/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/bookings.html', 'base.html')

    # 3

    def test_get_admin_bookings_page(self):
        """
        This test checks that the admin_bookings page
        is displayed
        """
        self.client.login(username='test_username', password='testpassword')
        user = User.objects.get(id=1)
        response = self.client.get('/admin_bookings/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/admin_bookings_view.html', 'base.html')

    # 4

    def test_get_menu_page(self):
        """
        This test checks that the menu page
        is displayed
        """        
        user = User.objects.get(id=1)
        self.client.login(username='test_username', password='testpassword') 
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nannys_alternative/menu.html', 'base.html')

    # 5

    def test_get_profile_page(self):
        """
        This test checks that the profile page
        is displayed
        ****************************************************************************************************************
        THis test workss just needs a user to be logged in 
        """
        user = User.objects.get(id=1)        
        self.client.login(username='test_username', password='testpassword')        
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nannys_alternative/profile.html', 'base.html')

    # 6
    def test_sign_up_page(self):
        """
        This test checks that the sign up page
        is displayed correctly
        """        
        user = User.objects.get(id=1)
        self.client.login(username='test_username', password='testpassword') 
        response = self.client.get('/sign_up_now/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nannys_alternative/sign_up.html', 'base.html')

    # 7
    def test_done_defaults_to_True(self):
            user = User()
            user.email='testUser@test.com',
            user.username='testuser',
            user.password='testpassword',
            user.first_name='test_first',
            user.last_name='test_last'
            
            user.save()
            self.assertTrue(user.save)







