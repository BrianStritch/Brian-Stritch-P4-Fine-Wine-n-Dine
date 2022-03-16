from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .forms import BookingForm
from .models import Booking
from django.template.defaultfilters import slugify
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, reverse

# Create your views here.

class Bookings(TemplateView):   

    def get(self, request):
        model = Booking
        booking = Booking.objects.all()
        bookings_list = {
            'bookings':booking
        }
        paginate_by = 8
        template_name = 'bookings.html'
        return render(request, template_name, bookings_list)
        


class CreateBookings(TemplateView):
    template_name = 'create_a_booking.html'
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
            self.template_name, {
                'form': form,                
                })

    def post(self, request, *args, **kwargs):
        form = BookingForm(request.POST)
        booking = Booking.objects.all()
        bookings_list = {
            'bookings':booking
        }
        if form.is_valid():
            form.instance.booking_id = request.user.id
            booking_id = form.instance.booking_id
            form.instance.email = request.user.email
            email = form.instance.email
            form.instance.name = request.user.username
            form.instance.primary_guest = request.user
            primary_guest = form.instance.primary_guest
            name = form.instance.name
            # booking = form.cleaned_data['booking']
            form.instance.slug = (f"{slugify('booking')}{name}")
            slug = form.instance.slug
            number_of_guests = form.cleaned_data['number_of_guests']
            dietary_notes = form.cleaned_data['dietary_notes']
            #form = BookingForm()


            context = {
                    'number_of_guests': number_of_guests,
                    'dietary_notes': dietary_notes,
                    'email': email,
                    'name': name,
                    'slug': slug,
                    'primary_guest':primary_guest,
                    } 
            booked = form.save(commit=False)
            primary_guest = request.user
            booked.post = booked
            
            booked.save() 
        else:
            form = BookingForm()
    
        return render(
            request, 
            'bookings.html',
            context = {
                    'number_of_guests': number_of_guests,
                    'dietary_notes': dietary_notes,
                    'email': email,
                    'name': name,
                    'slug': slug,
                    } )
