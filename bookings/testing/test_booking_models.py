from django.test import TestCase
from bookings.models import Booking
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from datetime import datetime, date
from django.shortcuts import reverse


class TestBookingModel(TestCase):

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
        
        """
        booking = Booking.objects.get(booking_date = '2023-03-30')
        booking.Meal_time = 3
        booking.save()
        booking = Booking.objects.get(booking_date = '2023-03-30')
        self.assertEqual(booking.Meal_time, 3 )

    # 4
    def test_Delete_booking(self):
        booking = Booking.objects.get(booking_date = '2023-03-30')        
        self.assertTrue(booking.delete())
    
    # 5
    def test_Edit_booking2(self):
        booking = Booking.objects.get(booking_date = '2023-03-30')
        booking.Meal_time = 3
        booking.save()
        booking = Booking.objects.get(booking_date = '2023-03-30')
        self.assertEqual(booking.Meal_time , 3)
        response = self.client.post(
            reverse('edit_booking', kwargs={'pk': booking.id}), 
            {'booking.Meal_time': '3'})
        self.assertEqual(response.status_code, 302)
 
    ################################################################################################################
    # def test_front_end(self):        
    #     user = User.objects.get(email='test@test.com')
    #     self.client.login(username='test_username', password='testpassword')
    #     review = Review.objects.get(title='test_review_for_all_tests')        
    #     args = {'review': review}
    #     page = self.client.get('/reviews/reviews/')
    #     self.assertEqual(page.status_code, 200)
    #     self.assertTrue(user.is_authenticated)
    #     self.assertTemplateUsed(page, 'reviews/reviews.html')

    # review = Review.objects.get(title='test_new_review_title')
    # self.assertEqual(review.title, 'test_new_review_title')




    # def test_update_book(self):
    #     book = Book.objects.create(title='The Catcher in the Rye')

        

    #     self.assertEqual(response.status_code, 302)

    #     book.refresh_from_db()
    #     self.assertEqual(book.author, 'J.D. Salinger')















    # def test_Edit_comment(self):
    #     comment = Comment.objects.get(name='test_comment_name_for_all_tests')
    #     comment.name = 'new_name'
    #     comment.save()
    #     comment = Comment.objects.get(name='new_name')
    #     self.assertEqual(comment.name, 'new_name')
    #     response = self.client.post(
    #         reverse('reviews_detail', kwargs={'pk': comment.id}), 
    #         {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger'})
        
        
    # def test_update_book(self):
    #     book = Book.objects.create(title='The Catcher in the Rye')

    #     response = self.client.post(
    #         reverse('book-update', kwargs={'pk': book.id}), 
    #         {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger'})

    #     self.assertEqual(response.status_code, 302)

    #     book.refresh_from_db()
    #     self.assertEqual(book.author, 'J.D. Salinger')