from django.test import TestCase
from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.models import User
from bookings.models import Booking
from bookings import urls, views
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
    A class for testing create_booking page views
    """
    def test_get_create_booking_page(self):
        """
        This test checks that the edit_booking page
        is displayed
        """
        user = User.objects.get(id=1)
        self.client.login(username='test_username', password='testpassword')
        
        response = self.client.get('/bookings/create_a_booking/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/create_a_booking.html', 'base.html')

    #2
    def test_get_bookings_page(self):
        """
        This test checks that the bookings page
        is displayed
        """
        user = User.objects.get(id=1)
        self.client.login(username='test_username', password='testpassword')
        booking = Booking.objects.all()
        response = self.client.get('/bookings/bookings/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/bookings.html', 'base.html')
      
    def test_get_edit_booking_page(self):
        """
        This test checks that the edit_booking page
        is displayed
        """
        user = User.objects.get(id=1)
        self.client.login(username='test_username', password='testpassword')
        
        response = self.client.get('/bookings/edit_booking/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/edit_booking.html', 'base.html')
    
    def test_get_admin_bookings_page(self):
        """
        This test checks that the admin_bookings page
        is displayed
        """
        self.client.login(username='test_username', password='testpassword')
        user = User.objects.get(id=1)
        response = self.client.get('/bookings/admin_bookings_view/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/admin_bookings_view.html', 'base.html')

 