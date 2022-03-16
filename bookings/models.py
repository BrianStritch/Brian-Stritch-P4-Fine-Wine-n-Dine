from django.db import models
from django import forms  # , forms
# from .widgets import DateTimePickerInput


from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField


BOOKING_STATUS = ((0, 'Pending'), (1, 'Approved'), (3, 'Completed'))
TIMESLOTS = (
    (0, 'Please choose:'),
    (1, '10:00'),
    (2, '11:00'),
    (3, '12:00'),
    (4, '13:00'),
    (5, '14:00'),
    (6, '15:00'),
    (7, '16:00'),
    (8, '17:00'),
    (9, '18:00'),    
    )
# BOOKING_DATES =(

# )


# Create your models here.

# Booking Model
class Booking(models.Model):
    primary_guest = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Booking_form') # noqa , ,default=""default=1  
    booking_status = models.IntegerField(choices=BOOKING_STATUS, default=0)
    availability = models.BooleanField(default=True)
    dietary_notes = models.TextField(max_length=200, blank=True)
    additional_comments = models.TextField(max_length=200, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    number_of_guests = models.IntegerField('Number of guests', default=1)
    number_of_tables = models.IntegerField(blank=True, default=0)
    Meal_time = models.IntegerField(choices=TIMESLOTS, default=0)
    booking_created_on = models.DateTimeField(auto_now=True)
    booking_date = models.TextField(max_length=200, blank=True)    
    
    # booking_id = models.IntegerField()
    # booking = models.CharField(max_length=200)
    # meal_time = 

    class Meta:
        ordering = ['-booking_created_on']

    # def __str__(self):
    #     return self.title

    



# Approval model
# class Booking_approval(models.Model):

#     booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='Approval')
#     name = models.CharField(max_length=80)
#     email = models.EmailField()
#     body = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     approved = models.BooleanField(default=False)

#     class Meta:
#         ordering = ['created_on']

#     def __str__(self):
#         return f"Comment {self.body} by {self.name}"


# Reviews Model
# class Booking(models.Model):
#     post = models.CharField(max_length=200)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    # slug = models.SlugField(max_length=200, unique=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts') # noqa
    #updated_on = models.DateTimeField(auto_now=True)
    # Dietary_notes = models.TextField()
    #featured_image = CloudinaryField('image', default='placeholder')
    # excerpt = models.TextField(blank=True)
    # created_on = models.DateTimeField(auto_now_add=True)
    # status = models.IntegerField(choices=BOOKING_STATUS, default=0)
    # likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    # class Meta:
    #     ordering = ['-created_on']

    # def __str__(self):
    #     return self.title

    # def number_of_likes(self):
        # return self.likes.count()
