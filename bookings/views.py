from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from reviews.models import Review

# Create your views here.
class Bookings(generic.ListView):
    model = Review
    queryset = list()
    template_name = 'bookings.html'

class CreateBookings(generic.ListView):
    model = Review
    queryset = list()
    template_name = 'create_a_booking.html'
