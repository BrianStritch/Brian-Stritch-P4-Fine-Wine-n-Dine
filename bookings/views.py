from django.shortcuts import render, get_object_or_404, reverse
from django.template.defaultfilters import slugify
from django.views import generic, View
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from .forms import BookingForm
from .models import Booking


class Bookings(TemplateView):   

    def get(self, request):
        bookings = Booking.objects.all()        
        template_name = 'bookings/bookings.html'
        paginate_by = 8
        return render(
            request, 
            template_name, 
            {
                'bookings': bookings,
            })       


class CreateBookings(TemplateView):
    template_name = 'bookings/create_a_booking.html'
    booking = Booking.objects.all()
    bookings_list = {
        'bookings':booking
    }

    def get(self, request):
        form = BookingForm()
        booking = Booking.objects.all()
        bookings_list = {
            'bookings':booking
        }
        return render(
            request, 
            self.template_name, 
            {
            'form': form,                
            })

    def post(self, request, *args, **kwargs):
        form = BookingForm(request.POST)
        booking = Booking.objects.all()
        
        if form.is_valid():
            form.instance.email = request.user.email
            email = form.instance.email
            form.instance.name = request.user.username
            name = form.instance.name
            form.instance.primary_guest = request.user
            primary_guest = form.instance.primary_guest
            number_of_guests = form.cleaned_data['number_of_guests']
            dietary_notes = form.cleaned_data['dietary_notes']
            Meal_time = form.cleaned_data['Meal_time']
            booking_date = form.cleaned_data['booking_date']
            additional_comments = form.cleaned_data['additional_comments']
            form.instance.slug = (f"{primary_guest}_{booking_date}_{Meal_time}")
            slug = form.instance.slug
            booked = form.save(commit=False)
            primary_guest = request.user
            booked.post = booked            
            booked.save() 
        else:
            form = BookingForm()
        return HttpResponseRedirect(reverse('bookings'))
