from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .forms import BookingForm
from django.template.defaultfilters import slugify
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, reverse

# Create your views here.

class Bookings(TemplateView):
    template_name = 'bookings.html'


class CreateBookings(TemplateView):
    template_name = 'create_a_booking.html'

    def get(self, request):
        form = BookingForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = BookingForm(request.POST)
        if form.is_valid():
            form.instance.booking_id = request.user.id
            booking_id = form.instance.booking_id
            form.instance.email = request.user.email
            email = form.instance.email
            form.instance.name = request.user.username
            name = form.instance.name
            booking = form.cleaned_data['booking']
            form.instance.slug = slugify(booking)
            slug = form.instance.slug
            number_of_guests = form.cleaned_data['number_of_guests']
            dietary_notes = form.cleaned_data['dietary_notes']
            form = BookingForm()
            context = {
                    'booking_id': booking_id,
                    'booking': booking, 
                    'number_of_guests': number_of_guests,
                    'dietary_notes': dietary_notes,
                    'email': email,
                    'name': name,
                    'slug': slug,
                    } 
            booked = form.save(commit=False)
            #booked.user = request.user
            booked.post = booked
            
            #booked.save() 
        else:
            form = BookingForm()
    
        return render(
            request, 
            'bookings.html',
            context = {
                    'booking': booking, 
                    'number_of_guests': number_of_guests,
                    'dietary_notes': dietary_notes,
                    'email': email,
                    'name': name,
                    'slug': slug,
                    } )
