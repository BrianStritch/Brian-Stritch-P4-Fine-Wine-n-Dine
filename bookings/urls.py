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
    path(
        'bookings/bookings_detail/<int:pk>',
        views.BookingDetails.as_view(),
        name='booking_details'
        ),    
    # path(
    #     'bookings/bookings_detail/<slug:slug>/',
    #     views.BookingDetails.as_view(),
    #     name='booking_details'
    #     ),    
    # path(
    #     'edit_booking/',
    #     views.EditBookings.as_view(),
    #     name='edit_booking'
    #     ),
]

