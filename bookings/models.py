from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.shortcuts import reverse



BOOKING_STATUS = (
    (0, 'Pending'),
    (1, 'Approved'),
    (3, 'Completed')
    )

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


# Booking Model
class Booking(models.Model):
    primary_guest = models.ForeignKey(
        User, on_delete=models.CASCADE, 
        related_name='Booking_form'
        )

    booking_status = models.IntegerField(
        choices=BOOKING_STATUS, 
        default=0
        )

    availability = models.BooleanField(default=True)

    dietary_notes = models.TextField(max_length=200, blank=True)

    additional_comments = models.TextField(max_length=200, blank=True)

    slug = models.SlugField(max_length=200, unique=True)

    number_of_guests = models.IntegerField('Number of guests', default=1)

    number_of_tables = models.IntegerField(blank=True, default=0)

    Meal_time = models.IntegerField(choices=TIMESLOTS, default=0)

    booking_created_on = models.DateTimeField(auto_now=True)

    booking_date = models.DateField( max_length=200, blank=True )
    

    class Meta:
        ordering = ['-booking_created_on']

    
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.primary_guest}_{self.booking_date}_{self.Meal_time}")
        super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('bookings')
