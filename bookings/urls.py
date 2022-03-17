from django.urls import path
from . import views

urlpatterns = [    
    path(
        'bookings/', 
        views.Bookings.as_view(), 
        name='bookings'
        ),
    path(
        'create_a_booking/',
        views.CreateBookings.as_view(),
        name='create_a_booking'
        ),
]

