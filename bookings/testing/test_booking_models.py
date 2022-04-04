from django.test import TestCase
from bookings.models import Booking
from bookings import urls
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.test import Client


class TestBookingModel(TestCase):
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

    # 1
    def test_model_slugify(self):
        """
            tests for booking model slug
        """
        user = User.objects.get(email='test@test.com')
        booking = Booking.objects.get(booking_date = '2023-03-30')       
        self.client.login(username='test_username', password='testpassword')
        self.assertEqual(
            slugify(
                f"{booking.primary_guest}_{booking.booking_date}_{booking.Meal_time}"
                ),
                'test_username_2023-03-30_2')
       
    # 2
    def test_Create_Booking(self):
        """
            tests for create booking
        """
        user = User.objects.get(email='test@test.com')
        booking = Booking(
            primary_guest = user,
            booking_date = '2023-04-30',                       
            Meal_time = 2,
        )
        booking.save()        
        self.assertTrue(booking.save)

    # 3
    def test_Edit_booking(self):
        """
            tests for edit booking
        """
        booking = Booking.objects.get(booking_date = '2023-03-30')
        booking.Meal_time = 3
        booking.save()
        booking = Booking.objects.get(booking_date = '2023-03-30')
        self.assertEqual(booking.Meal_time, 3 )

    # 4
    def test_Delete_booking(self):
        """
            tests for delete booking
        """
        booking = Booking.objects.get(booking_date = '2023-03-30')        
        self.assertTrue(booking.delete())
    
    # 5
    def test_Edit_booking_front_end(self):
        """
            tests for front end edit booking page
        """
        booking = Booking.objects.get(booking_date = '2023-03-30')
        booking.Meal_time = 3
        booking.save()
        booking = Booking.objects.get(booking_date = '2023-03-30')
        self.assertEqual(booking.Meal_time , 3)
        response = self.client.post(
            reverse('edit_booking', kwargs={'pk': booking.id}), 
            {'booking.Meal_time': '3'})
        self.assertEqual(response.status_code, 302)
    
    # 6
    def test_delete_booking_front_end(self):
        """
            tests for front end delete booking page
        """
        booking = Booking.objects.get(booking_date = '2023-03-30')
        response = self.client.post(
            reverse(
                'delete_booking', 
                kwargs={'pk': booking.id}), 
            )
        self.assertTrue(booking.delete())
        self.assertEqual(response.status_code, 302)
    
    # 7
    def test_create_a_booking_page(self):
        """
            tests for front end create a booking page
        """
        user = User.objects.get(email='test@test.com')
        booking = Booking(
            primary_guest = user,
            booking_date = '2024-03-30',                       
            Meal_time = 5,
            )
        booking.save()
        self.assertTrue(booking.save)
        url = reverse('create_a_booking')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/create_a_booking.html')
        self.assertContains(response, 'title' )
        self.assertTrue(reverse('bookings'))
        self.assertEqual(booking.slug, f"{booking.primary_guest}_{booking.booking_date}_{booking.Meal_time}")
        
    # 8
    def test_view_all_my_bookings_page(self):
        """
            tests for front end bookings page
        """
        self.client.login(username='test_username', password='testpassword')
        user = User.objects.get(email='test@test.com')
        self.assertTrue(user.is_authenticated)
        bookings = Booking.objects.filter(primary_guest=user)
        url = reverse('bookings')
        page = self.client.get(url)
        self.assertEqual(page.status_code, 200)        
        self.assertTemplateUsed(page, 'bookings/bookings.html')
 