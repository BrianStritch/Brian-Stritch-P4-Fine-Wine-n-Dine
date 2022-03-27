from django.urls import path
from . import views

urlpatterns = [    
    path(
        'bookings/', 
        views.Bookings.as_view(), 
        name='bookings'
        ),
    path(
        'bookings/<slug:slug>/',
        views.BookingDetails.as_view(),
        name='booking_details'
        ),     
    path(
        'edit_booking/<int:pk>/',
        views.EditBookings.as_view(),
        name='edit_booking'
        ),
    path(
        'delete_booking/<int:pk>/',
        views.DeleteBooking.as_view(),
        name='delete_booking'
        ),
    path(
        'create_a_booking/',
        views.CreateBookings.as_view(),
        name='create_a_booking'
        ),
    path(
        'admin_bookings_view/',
        views.AdminBookings.as_view(),
        name='admin_bookings'
        ),
]